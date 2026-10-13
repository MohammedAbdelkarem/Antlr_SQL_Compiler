import sys
import os

# Add parent directories to path to import SqlParserVisitor
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from SqlParserVisitor import SqlParserVisitor
import SqlParser

from expression.core.SqlScriptNode import SqlScriptNode
from expression.dml.SelectStatementNode import SelectStatementNode
from expression.core.ExpressionListNode import ExpressionListNode
from expression.expression.ColumnReferenceNode import ColumnReferenceNode
from expression.expression.LiteralNode import LiteralNode
from expression.leafNode.IdentifierNode import IdentifierNode


class ASTBuilderVisitor(SqlParserVisitor):
    def __init__(self):
        self.semantics_errors = []

    # Top-level script
    def visitSqlScript(self, ctx: 'SqlParser.SqlScriptContext'):
        script = SqlScriptNode()
        for stmt_or_go in ctx.statement_or_go():
            stmt = self.visit(stmt_or_go)
            if stmt:
                script.add_child(stmt)
        return script

    def visitStatementWrapper(self, ctx: 'SqlParser.StatementWrapperContext'):
        if ctx.statement():
            return self.visit(ctx.statement())
        return None

    def visitGoWrapper(self, ctx: 'SqlParser.GoWrapperContext'):
        # GO statements don't generate AST nodes, they're just separators
        return None

    # DML Statements
    def visitSelectStatement(self, ctx: 'SqlParser.SelectStatementContext'):
        select_node = SelectStatementNode()

        if ctx.DISTINCT():
            select_node.set_distinct(True)

        if ctx.select_list():
            select_list_result = self.visit(ctx.select_list())
            # select_list_result can be ExpressionListNode (from SelectItemList) 
            # or ExpressionListNode with WildcardNode (from SelectStarList)
            if isinstance(select_list_result, ExpressionListNode):
                for expr in select_list_result.expressions:
                    select_node.add_select_item(expr)

        if ctx.from_clause():
            select_node.set_from(self.visit(ctx.from_clause()))

        if ctx.where_clause():
            select_node.set_where(self.visit(ctx.where_clause()))

        if ctx.group_by_clause():
            select_node.set_group_by(self.visit(ctx.group_by_clause()))

        if ctx.having_clause():
            select_node.set_having(self.visit(ctx.having_clause()))

        if ctx.order_by_clause():
            select_node.set_order_by(self.visit(ctx.order_by_clause()))

        return select_node

    def visitSelectStmt(self, ctx: 'SqlParser.SelectStmtContext'):
        return self.visit(ctx.select_statement())

    # IF Statement
    def visitIfStatement(self, ctx: 'SqlParser.IfStatementContext'):
        if ctx.if_statement():
            return self.visit(ctx.if_statement())
        return None

    def visitIfStmt(self, ctx: 'SqlParser.IfStmtContext'):
        from expression.core.IfStatementNode import IfStatementNode
        
        # Get the condition
        condition = None
        if ctx.search_condition():
            condition = self.visit(ctx.search_condition())
        
        # Get the IF block (THEN block)
        if_block = None
        if ctx.statement_block() and len(ctx.statement_block()) > 0:
            if_block = self.visit(ctx.statement_block(0))
        
        # Get the ELSE block if it exists
        else_block = None
        if ctx.ELSE() and len(ctx.statement_block()) > 1:
            else_block = self.visit(ctx.statement_block(1))
        
        # Create and return the IF statement node
        return IfStatementNode(condition, if_block, else_block)

    # Statement Block
    def visitStatementBlock(self, ctx: 'SqlParser.StatementBlockContext'):
        from expression.core.StatementBlockNode import StatementBlockNode
        block = StatementBlockNode()
        
        for stmt_or_go in ctx.statement_or_go():
            stmt = self.visit(stmt_or_go)
            if stmt:
                block.add_statement(stmt)
        
        return block

    # DDL Statements
    def visitDdlStatement(self, ctx: 'SqlParser.DdlStatementContext'):
        if ctx.ddl_statement():
            return self.visit(ctx.ddl_statement())
        return None

    def visitCreateTableStatement(self, ctx: 'SqlParser.CreateTableStatementContext'):
        from expression.ddl.CreateTableStatementNode import CreateTableStatementNode
        from expression.ddl.ColumnDefListNode import ColumnDefListNode
        from expression.ddl.TableConstraintListNode import TableConstraintListNode
        
        table_name = ctx.table_name().getText() if ctx.table_name() else None
        
        columns = None
        if ctx.column_def_list():
            columns = self.visit(ctx.column_def_list())
        
        constraints = None
        if ctx.table_constraint_list():
            constraints = self.visit(ctx.table_constraint_list())
        
        return CreateTableStatementNode(table_name, columns, constraints)

    # INSERT Statement
    def visitInsertStmt(self, ctx: 'SqlParser.InsertStmtContext'):
        if ctx.insert_statement():
            return self.visit(ctx.insert_statement())
        return None

    def visitInsertValuesStatement(self, ctx: 'SqlParser.InsertValuesStatementContext'):
        from expression.dml.InsertValuesStatementNode import InsertValuesStatementNode
        from expression.core.ColumnNameListNode import ColumnNameListNode
        from expression.dml.ValueListNode import ValueListNode
        
        table_name = ctx.table_name().getText() if ctx.table_name() else None
        
        columns = None
        if ctx.column_name_list():
            columns = self.visit(ctx.column_name_list())
        
        values = None
        if ctx.value_list():
            values = self.visit(ctx.value_list())
        
        return InsertValuesStatementNode(table_name, columns, values)

    def visitSelectItemList(self, ctx: 'SqlParser.SelectItemListContext'):
        expr_list = ExpressionListNode()
        for item in ctx.select_item():
            expr = self.visit(item)
            if expr:
                expr_list.add_expression(expr)
        return expr_list

    def visitSelectStarList(self, ctx: 'SqlParser.SelectStarListContext'):
        # Handle SELECT * case - you may want to create a special node for this
        from expression.leafNode.WildcardNode import WildcardNode
        expr_list = ExpressionListNode()
        expr_list.add_expression(WildcardNode())
        return expr_list

    def visitSelectItem(self, ctx: 'SqlParser.SelectItemContext'):
        return self.visit(ctx.expression())

    # FROM clause
    def visitFromClause(self, ctx: 'SqlParser.FromClauseContext'):
        if ctx.table_source():
            return self.visit(ctx.table_source())
        return None

    def visitTableSource(self, ctx: 'SqlParser.TableSourceContext'):
        from expression.dml.TableSourceNode import TableSourceNode
        
        # Get the base table
        simple_source = None
        if ctx.simple_table_source():
            simple_source = self.visit(ctx.simple_table_source())
        
        if not simple_source:
            return None
        
        # Create TableSourceNode and add joins
        table_source = TableSourceNode(simple_source)
        
        # Add any join parts
        if ctx.join_part():
            for join_part_ctx in ctx.join_part():
                join_part = self.visit(join_part_ctx)
                if join_part:
                    table_source.add_join(join_part)
        
        return table_source

    def visitSimpleTableSource(self, ctx: 'SqlParser.SimpleTableSourceContext'):
        return IdentifierNode(ctx.getText())

    # WHERE clause
    def visitWhereClause(self, ctx: 'SqlParser.WhereClauseContext'):
        if ctx.search_condition():
            return self.visit(ctx.search_condition())
        return None

    def visitSearchCondition(self, ctx: 'SqlParser.SearchConditionContext'):
        if ctx.expression():
            return self.visit(ctx.expression())
        return self.visitChildren(ctx)

    # ORDER BY, GROUP BY, HAVING
    def visitOrderByClause(self, ctx: 'SqlParser.OrderByClauseContext'):
        from expression.dml.OrderByClauseNode import OrderByClauseNode
        order_by = OrderByClauseNode()
        
        if ctx.order_expression():
            for order_expr_ctx in ctx.order_expression():
                order_expr = self.visit(order_expr_ctx)
                if order_expr:
                    order_by.add_order(order_expr)
        
        return order_by

    def visitOrderExpression(self, ctx: 'SqlParser.OrderExpressionContext'):
        from expression.dml.OrderExpressionNode import OrderExpressionNode
        
        expr = None
        if ctx.expression():
            expr = self.visit(ctx.expression())
        
        direction = None
        if ctx.ASC():
            direction = "ASC"
        elif ctx.DESC():
            direction = "DESC"
        
        return OrderExpressionNode(expr, direction)

    def visitGroupByClause(self, ctx: 'SqlParser.GroupByClauseContext'):
        from expression.dml.GroupByClauseNode import GroupByClauseNode
        
        expr_list = None
        if ctx.expression_list():
            expr_list = self.visit(ctx.expression_list())
        
        return GroupByClauseNode(expr_list)

    def visitHavingClause(self, ctx: 'SqlParser.HavingClauseContext'):
        from expression.dml.HavingClauseNode import HavingClauseNode
        
        condition = None
        if ctx.search_condition():
            condition = self.visit(ctx.search_condition())
        
        return HavingClauseNode(condition)

    # Expression handling
    def visitExpressionRoot(self, ctx: 'SqlParser.ExpressionRootContext'):
        if ctx.logical_or_expression():
            return self.visit(ctx.logical_or_expression())
        return None

    def visitOrExpression(self, ctx: 'SqlParser.OrExpressionContext'):
        from expression.expression import OrExpressionNode
        if ctx.logical_and_expression():
            expressions = ctx.logical_and_expression()
            if len(expressions) == 1:
                return self.visit(expressions[0])
            
            result = self.visit(expressions[0])
            for i in range(1, len(expressions)):
                right = self.visit(expressions[i])
                result = OrExpressionNode(result, right)
            return result
        return self.visitChildren(ctx)

    def visitAndExpression(self, ctx: 'SqlParser.AndExpressionContext'):
        from expression.expression import AndExpressionNode
        if ctx.not_expression():
            expressions = ctx.not_expression()
            if len(expressions) == 1:
                return self.visit(expressions[0])
            
            result = self.visit(expressions[0])
            for i in range(1, len(expressions)):
                right = self.visit(expressions[i])
                result = AndExpressionNode(result, right)
            return result
        return self.visitChildren(ctx)

    def visitNotExpression(self, ctx: 'SqlParser.NotExpressionContext'):
        from expression.expression import NotExpressionNode
        if ctx.NOT():
            expr = self.visit(ctx.not_expression())
            return NotExpressionNode(expr)
        return self.visit(ctx.getChild(0))

    def visitPredicateExpressionWrapper(self, ctx: 'SqlParser.PredicateExpressionWrapperContext'):
        if ctx.predicate_expression():
            return self.visit(ctx.predicate_expression())
        return None

    def visitComparisonPredicate(self, ctx: 'SqlParser.ComparisonPredicateContext'):
        if ctx.comparison_expression():
            return self.visit(ctx.comparison_expression())
        return None

    def visitComparisonExpression(self, ctx: 'SqlParser.ComparisonExpressionContext'):
        if ctx.additive_expression() and len(ctx.additive_expression()) == 2:
            left = self.visit(ctx.additive_expression(0))
            right = self.visit(ctx.additive_expression(1))
            
            from expression.expression import (
                EqualsExpressionNode, NotEqualsExpressionNode,
                GreaterThanExpressionNode, LessThanExpressionNode
            )

            if ctx.EQ():
                return EqualsExpressionNode(left, right)
            elif ctx.NOT_EQUAL():
                return NotEqualsExpressionNode(left, right)
            elif ctx.GT():
                return GreaterThanExpressionNode(left, right)
            elif ctx.LT():
                return LessThanExpressionNode(left, right)
            elif ctx.GTE():
                # You may need to add GreaterThanOrEqualExpressionNode
                self.semantics_errors.append("GreaterThanOrEqual not yet supported")
                return None
            elif ctx.LTE():
                # You may need to add LessThanOrEqualExpressionNode
                self.semantics_errors.append("LessThanOrEqual not yet supported")
                return None
        
        return self.visitChildren(ctx)

    def visitAdditiveExpression(self, ctx: 'SqlParser.AdditiveExpressionContext'):
        if ctx.multiplicative_expression():
            expressions = ctx.multiplicative_expression()
            if len(expressions) == 1:
                return self.visit(expressions[0])
            
            from expression.expression import AddExpressionNode, SubtractExpressionNode
            
            result = self.visit(expressions[0])
            plus_tokens = ctx.PLUS() if ctx.PLUS() else []
            minus_tokens = ctx.MINUS() if ctx.MINUS() else []
            
            # Combine PLUS and MINUS tokens in order
            all_ops = []
            op_index = 0
            for i in range(1, len(expressions)):
                # Find the operator token between expression i-1 and i
                # This is a simplified approach - in practice, operators appear as children
                # between expressions, but the exact structure depends on ANTLR's generated code
                if op_index < len(plus_tokens) and op_index < len(minus_tokens):
                    # Would need to check actual position - simplified here
                    # For now, assume alternating or check token positions
                    pass
                
                # Simplified: check if PLUS or MINUS token exists at this position
                if plus_tokens and op_index < len(plus_tokens):
                    result = AddExpressionNode(result, self.visit(expressions[i]))
                elif minus_tokens and op_index < len(minus_tokens):
                    result = SubtractExpressionNode(result, self.visit(expressions[i]))
                else:
                    # Fallback: use default (shouldn't happen in well-formed grammar)
                    result = AddExpressionNode(result, self.visit(expressions[i]))
                op_index += 1
            
            return result
        
        return self.visitChildren(ctx)

    def visitMultiplicativeExpression(self, ctx: 'SqlParser.MultiplicativeExpressionContext'):
        if ctx.unary_expression():
            expressions = ctx.unary_expression()
            if len(expressions) == 1:
                return self.visit(expressions[0])
            
            from expression.expression import MultiplyExpressionNode, DivideExpressionNode, ModuloExpressionNode
            
            result = self.visit(expressions[0])
            star_tokens = ctx.STAR() if ctx.STAR() else []
            slash_tokens = ctx.SLASH() if ctx.SLASH() else []
            
            op_index = 0
            for i in range(1, len(expressions)):
                if star_tokens and op_index < len(star_tokens):
                    result = MultiplyExpressionNode(result, self.visit(expressions[i]))
                elif slash_tokens and op_index < len(slash_tokens):
                    result = DivideExpressionNode(result, self.visit(expressions[i]))
                else:
                    result = MultiplyExpressionNode(result, self.visit(expressions[i]))
                op_index += 1
            
            return result
        
        return self.visitChildren(ctx)

    def visitUnaryMinusExpression(self, ctx: 'SqlParser.UnaryMinusExpressionContext'):
        if ctx.MINUS() and ctx.unary_expression():
            from expression.expression import SubtractExpressionNode
            expr = self.visit(ctx.unary_expression())
            # Represent as 0 - expr
            from expression.expression.LiteralNode import LiteralNode
            zero = LiteralNode(0)
            return SubtractExpressionNode(zero, expr)
        return self.visitChildren(ctx)

    def visitUnaryPlusExpression(self, ctx: 'SqlParser.UnaryPlusExpressionContext'):
        if ctx.unary_expression():
            return self.visit(ctx.unary_expression())
        return self.visitChildren(ctx)

    def visitPrimaryExpressionWrapper(self, ctx: 'SqlParser.PrimaryExpressionWrapperContext'):
        if ctx.primary_expression():
            return self.visit(ctx.primary_expression())
        return None

    def visitParenthesizedExpression(self, ctx: 'SqlParser.ParenthesizedExpressionContext'):
        if ctx.expression():
            return self.visit(ctx.expression())
        return None

    def visitColumnExpression(self, ctx: 'SqlParser.ColumnExpressionContext'):
        return ColumnReferenceNode(ctx.getText())

    def visitLiteralExpression(self, ctx: 'SqlParser.LiteralExpressionContext'):
        if ctx.literal_value():
            return self.visit(ctx.literal_value())
        return None

    def visitStringLiteral(self, ctx: 'SqlParser.StringLiteralContext'):
        return LiteralNode(ctx.getText().strip("'"))

    def visitIntegerLiteral(self, ctx: 'SqlParser.IntegerLiteralContext'):
        return LiteralNode(int(ctx.getText()))

    def visitFloatLiteral(self, ctx: 'SqlParser.FloatLiteralContext'):
        return LiteralNode(float(ctx.getText()))

    def visitSimpleFloatLiteral(self, ctx: 'SqlParser.SimpleFloatLiteralContext'):
        return LiteralNode(float(ctx.getText()))

    def visitNullLiteral(self, ctx: 'SqlParser.NullLiteralContext'):
        return LiteralNode(None)

    # Other predicate types
    def visitBetweenPredicate(self, ctx: 'SqlParser.BetweenPredicateContext'):
        if ctx.between_expression():
            return self.visit(ctx.between_expression())
        return None

    def visitBetweenExpression(self, ctx: 'SqlParser.BetweenExpressionContext'):
        from expression.expression import BetweenExpressionNode
        if ctx.additive_expression() and len(ctx.additive_expression()) == 3:
            expr = self.visit(ctx.additive_expression(0))
            lower = self.visit(ctx.additive_expression(1))
            upper = self.visit(ctx.additive_expression(2))
            return BetweenExpressionNode(expr, lower, upper)
        return None

    def visitInPredicate(self, ctx: 'SqlParser.InPredicateContext'):
        if ctx.in_expression():
            return self.visit(ctx.in_expression())
        return None

    def visitInExpression(self, ctx: 'SqlParser.InExpressionContext'):
        from expression.expression import InExpressionNode
        if ctx.additive_expression():
            expr = self.visit(ctx.additive_expression())
            values = None
            if ctx.expression_list():
                values = self.visit(ctx.expression_list())
                # values should be ExpressionListNode
            return InExpressionNode(expr, values)
        return None

    def visitLikePredicate(self, ctx: 'SqlParser.LikePredicateContext'):
        if ctx.like_expression():
            return self.visit(ctx.like_expression())
        return None

    def visitLikeExpression(self, ctx: 'SqlParser.LikeExpressionContext'):
        # You may need to add LikeExpressionNode
        self.semantics_errors.append("LIKE expressions not yet fully supported")
        return self.visitChildren(ctx)

    def visitIsNullPredicate(self, ctx: 'SqlParser.IsNullPredicateContext'):
        if ctx.is_null_expression():
            return self.visit(ctx.is_null_expression())
        return None

    def visitIsNullExpression(self, ctx: 'SqlParser.IsNullExpressionContext'):
        # You may need to add IsNullExpressionNode
        self.semantics_errors.append("IS NULL expressions not yet fully supported")
        return self.visitChildren(ctx)

    def visitExistsPredicate(self, ctx: 'SqlParser.ExistsPredicateContext'):
        if ctx.exists_expression():
            return self.visit(ctx.exists_expression())
        return None

    def visitExistsExpression(self, ctx: 'SqlParser.ExistsExpressionContext'):
        from expression.expression import ExistsExpressionNode
        if ctx.select_statement():
            subquery = self.visit(ctx.select_statement())
            return ExistsExpressionNode(subquery)
        return None

    # Function calls
    def visitFunctionCallExpression(self, ctx: 'SqlParser.FunctionCallExpressionContext'):
        if ctx.function_call():
            return self.visit(ctx.function_call())
        return None

    def visitFunctionCall(self, ctx: 'SqlParser.FunctionCallContext'):
        from expression.expression import FunctionCallNode
        # Function name can be IDENTIFIER or a keyword like MAX, MIN, AVG, CONCAT
        func_name = None
        if ctx.IDENTIFIER():
            func_name = ctx.IDENTIFIER().getText()
        elif ctx.MAX():
            func_name = ctx.MAX().getText()
        elif ctx.MIN():
            func_name = ctx.MIN().getText()
        elif ctx.AVG():
            func_name = ctx.AVG().getText()
        elif ctx.CONCAT_KW():
            func_name = ctx.CONCAT_KW().getText()
        
        args = None
        if ctx.expression_list():
            args = self.visit(ctx.expression_list())
            # args should be ExpressionListNode
        return FunctionCallNode(func_name, args)

    # Case expressions
    def visitCaseExpressionWrapper(self, ctx: 'SqlParser.CaseExpressionWrapperContext'):
        if ctx.case_expression():
            return self.visit(ctx.case_expression())
        return None

    def visitCaseExpression(self, ctx: 'SqlParser.CaseExpressionContext'):
        from expression.expression import CaseExpressionNode, WhenThenNode
        case_expr = CaseExpressionNode()
        
        if ctx.when_clause():
            for when_clause_ctx in ctx.when_clause():
                when_then = self.visit(when_clause_ctx)
                if when_then:
                    case_expr.add_branch(when_then)
        
        if ctx.else_clause():
            else_expr = self.visit(ctx.else_clause())
            case_expr.set_else(else_expr)
        
        return case_expr

    def visitWhenClause(self, ctx: 'SqlParser.WhenClauseContext'):
        from expression.expression import WhenThenNode
        if ctx.expression() and len(ctx.expression()) == 2:
            condition = self.visit(ctx.expression(0))
            result = self.visit(ctx.expression(1))
            return WhenThenNode(condition, result)
        return None

    def visitElseClause(self, ctx: 'SqlParser.ElseClauseContext'):
        if ctx.expression():
            return self.visit(ctx.expression())
        return None

    # Expression list
    def visitExpressionList(self, ctx: 'SqlParser.ExpressionListContext'):
        expr_list = ExpressionListNode()
        for expr_ctx in ctx.expression():
            expr = self.visit(expr_ctx)
            if expr:
                expr_list.add_expression(expr)
        return expr_list

    # Subquery
    def visitSubqueryExpression(self, ctx: 'SqlParser.SubqueryExpressionContext'):
        from expression.expression import SubqueryExpressionNode
        if ctx.select_statement():
            subquery = self.visit(ctx.select_statement())
            return SubqueryExpressionNode(subquery)
        return None

    # Column name
    def visitColumnName(self, ctx: 'SqlParser.ColumnNameContext'):
        return ColumnReferenceNode(ctx.getText())

    # Table name
    def visitTableName(self, ctx: 'SqlParser.TableNameContext'):
        return IdentifierNode(ctx.getText())

    # Column Name List
    def visitColumnNameList(self, ctx: 'SqlParser.ColumnNameListContext'):
        from expression.core.ColumnNameListNode import ColumnNameListNode
        col_list = ColumnNameListNode()
        if ctx.column_name():
            for col_ctx in ctx.column_name():
                col_name = col_ctx.getText() if col_ctx else None
                if col_name:
                    col_list.add_column_name(col_name)
        return col_list

    # Value List
    def visitValueList(self, ctx: 'SqlParser.ValueListContext'):
        from expression.dml.ValueListNode import ValueListNode
        value_list = ValueListNode()
        if ctx.expression_list():
            for expr_list_ctx in ctx.expression_list():
                expr_list = self.visit(expr_list_ctx)
                if expr_list:
                    value_list.add_row(expr_list)
        return value_list

    # Column Def List
    def visitColumnDefList(self, ctx: 'SqlParser.ColumnDefListContext'):
        from expression.ddl.ColumnDefListNode import ColumnDefListNode
        col_def_list = ColumnDefListNode()
        if ctx.column_def():
            for col_def_ctx in ctx.column_def():
                col_def = self.visit(col_def_ctx)
                if col_def:
                    col_def_list.add_column_def(col_def)
        return col_def_list

    def visitColumnDef(self, ctx: 'SqlParser.ColumnDefContext'):
        from expression.ddl.ColumnDefNode import ColumnDefNode
        from expression.ddl.DataTypeNode import DataTypeNode
        
        col_name = None
        if ctx.column_name():
            col_name = ctx.column_name().getText()
        
        data_type = None
        if ctx.data_type():
            data_type = self.visit(ctx.data_type())
        
        col_def = ColumnDefNode(col_name, data_type)
        
        # Add constraints
        if ctx.column_constraint():
            for constraint_ctx in ctx.column_constraint():
                constraint = self.visit(constraint_ctx)
                if constraint:
                    col_def.add_constraint(constraint)
        
        return col_def

    def visitNullConstraint(self, ctx: 'SqlParser.NullConstraintContext'):
        return "NULL"

    def visitNotNullConstraint(self, ctx: 'SqlParser.NotNullConstraintContext'):
        return "NOT NULL"

    def visitIdentityConstraint(self, ctx: 'SqlParser.IdentityConstraintContext'):
        return "IDENTITY"

    def visitPrimaryKeyConstraint(self, ctx: 'SqlParser.PrimaryKeyConstraintContext'):
        return "PRIMARY KEY"

    def visitUniqueConstraint(self, ctx: 'SqlParser.UniqueConstraintContext'):
        return "UNIQUE"

    def visitDefaultConstraint(self, ctx: 'SqlParser.DefaultConstraintContext'):
        default_value = None
        if ctx.literal_value():
            default_value = ctx.literal_value().getText()
        return f"DEFAULT {default_value}" if default_value else "DEFAULT"

    def visitCheckConstraint(self, ctx: 'SqlParser.CheckConstraintContext'):
        # For now, just return "CHECK" - could be expanded to include the condition
        return "CHECK"

    def visitReferencesConstraint(self, ctx: 'SqlParser.ReferencesConstraintContext'):
        table_name = None
        if ctx.table_name():
            table_name = ctx.table_name().getText()
        return f"REFERENCES {table_name}" if table_name else "REFERENCES"

    def visitDataType(self, ctx: 'SqlParser.DataTypeContext'):
        from expression.ddl.DataTypeNode import DataTypeNode
        type_name = ctx.getText() if ctx else None
        return DataTypeNode(type_name) if type_name else None

    # JOIN handling
    def visitJoinPart(self, ctx: 'SqlParser.JoinPartContext'):
        from expression.dml.JoinPartNode import JoinPartNode
        
        join_type = None
        if ctx.join_type():
            join_type = self.visit(ctx.join_type())
        
        table = None
        if ctx.simple_table_source():
            table = self.visit(ctx.simple_table_source())
        
        condition = None
        if ctx.search_condition():
            condition = self.visit(ctx.search_condition())
        
        return JoinPartNode(join_type, table, condition)

    def visitInnerJoinType(self, ctx: 'SqlParser.InnerJoinTypeContext'):
        from expression.dml.JoinTypeNode import JoinTypeNode
        return JoinTypeNode("INNER")

    def visitLeftJoinType(self, ctx: 'SqlParser.LeftJoinTypeContext'):
        from expression.dml.JoinTypeNode import JoinTypeNode
        return JoinTypeNode("LEFT OUTER")

    def visitRightJoinType(self, ctx: 'SqlParser.RightJoinTypeContext'):
        from expression.dml.JoinTypeNode import JoinTypeNode
        return JoinTypeNode("RIGHT OUTER")

    def visitFullJoinType(self, ctx: 'SqlParser.FullJoinTypeContext'):
        from expression.dml.JoinTypeNode import JoinTypeNode
        return JoinTypeNode("FULL OUTER")

    def visitCrossJoinPart(self, ctx: 'SqlParser.CrossJoinPartContext'):
        from expression.dml.JoinPartNode import JoinPartNode
        from expression.dml.JoinTypeNode import JoinTypeNode
        
        join_type = JoinTypeNode("CROSS")
        table = None
        if ctx.simple_table_source():
            table = self.visit(ctx.simple_table_source())
        
        return JoinPartNode(join_type, table, None)

    def visitNaturalJoinPart(self, ctx: 'SqlParser.NaturalJoinPartContext'):
        from expression.dml.JoinPartNode import JoinPartNode
        from expression.dml.JoinTypeNode import JoinTypeNode
        
        join_type = JoinTypeNode("NATURAL")
        table = None
        if ctx.simple_table_source():
            table = self.visit(ctx.simple_table_source())
        
        return JoinPartNode(join_type, table, None)
