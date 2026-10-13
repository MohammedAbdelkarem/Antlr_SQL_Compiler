# Generated from SqlParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .SqlParser import SqlParser
else:
    from SqlParser import SqlParser

# This class defines a complete generic visitor for a parse tree produced by SqlParser.

class SqlParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SqlParser#SqlScript.
    def visitSqlScript(self, ctx:SqlParser.SqlScriptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#StatementWrapper.
    def visitStatementWrapper(self, ctx:SqlParser.StatementWrapperContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#GoWrapper.
    def visitGoWrapper(self, ctx:SqlParser.GoWrapperContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#GoStatement.
    def visitGoStatement(self, ctx:SqlParser.GoStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#DmlStatement.
    def visitDmlStatement(self, ctx:SqlParser.DmlStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#DdlStatement.
    def visitDdlStatement(self, ctx:SqlParser.DdlStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#CteStatement.
    def visitCteStatement(self, ctx:SqlParser.CteStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#CursorStatement.
    def visitCursorStatement(self, ctx:SqlParser.CursorStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#IfStatement.
    def visitIfStatement(self, ctx:SqlParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#IfStmt.
    def visitIfStmt(self, ctx:SqlParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#StatementBlock.
    def visitStatementBlock(self, ctx:SqlParser.StatementBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#SelectStmt.
    def visitSelectStmt(self, ctx:SqlParser.SelectStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#InsertStmt.
    def visitInsertStmt(self, ctx:SqlParser.InsertStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#UpdateStmt.
    def visitUpdateStmt(self, ctx:SqlParser.UpdateStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#DeleteStmt.
    def visitDeleteStmt(self, ctx:SqlParser.DeleteStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#SelectStatement.
    def visitSelectStatement(self, ctx:SqlParser.SelectStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#TopClause.
    def visitTopClause(self, ctx:SqlParser.TopClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#SelectStarList.
    def visitSelectStarList(self, ctx:SqlParser.SelectStarListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#SelectItemList.
    def visitSelectItemList(self, ctx:SqlParser.SelectItemListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#SelectItem.
    def visitSelectItem(self, ctx:SqlParser.SelectItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#IdentifierAlias.
    def visitIdentifierAlias(self, ctx:SqlParser.IdentifierAliasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#StringAlias.
    def visitStringAlias(self, ctx:SqlParser.StringAliasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#FromClause.
    def visitFromClause(self, ctx:SqlParser.FromClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#TableSource.
    def visitTableSource(self, ctx:SqlParser.TableSourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#SimpleTableSource.
    def visitSimpleTableSource(self, ctx:SqlParser.SimpleTableSourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#JoinPart.
    def visitJoinPart(self, ctx:SqlParser.JoinPartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#CrossJoinPart.
    def visitCrossJoinPart(self, ctx:SqlParser.CrossJoinPartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#NaturalJoinPart.
    def visitNaturalJoinPart(self, ctx:SqlParser.NaturalJoinPartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#InnerJoinType.
    def visitInnerJoinType(self, ctx:SqlParser.InnerJoinTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#LeftJoinType.
    def visitLeftJoinType(self, ctx:SqlParser.LeftJoinTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#RightJoinType.
    def visitRightJoinType(self, ctx:SqlParser.RightJoinTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#FullJoinType.
    def visitFullJoinType(self, ctx:SqlParser.FullJoinTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#OffsetFetchClause.
    def visitOffsetFetchClause(self, ctx:SqlParser.OffsetFetchClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#InsertValuesStatement.
    def visitInsertValuesStatement(self, ctx:SqlParser.InsertValuesStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#InsertSelectStatement.
    def visitInsertSelectStatement(self, ctx:SqlParser.InsertSelectStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#InsertDefaultValuesStatement.
    def visitInsertDefaultValuesStatement(self, ctx:SqlParser.InsertDefaultValuesStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#TableName.
    def visitTableName(self, ctx:SqlParser.TableNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#ColumnNameList.
    def visitColumnNameList(self, ctx:SqlParser.ColumnNameListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#ValueList.
    def visitValueList(self, ctx:SqlParser.ValueListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#UpdateStatement.
    def visitUpdateStatement(self, ctx:SqlParser.UpdateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#AssignmentList.
    def visitAssignmentList(self, ctx:SqlParser.AssignmentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#ColumnAssignment.
    def visitColumnAssignment(self, ctx:SqlParser.ColumnAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#DeleteStatement.
    def visitDeleteStatement(self, ctx:SqlParser.DeleteStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#CreateTableStmt.
    def visitCreateTableStmt(self, ctx:SqlParser.CreateTableStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#CreateViewStmt.
    def visitCreateViewStmt(self, ctx:SqlParser.CreateViewStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#CreateIndexStmt.
    def visitCreateIndexStmt(self, ctx:SqlParser.CreateIndexStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#CreateDatabaseStmt.
    def visitCreateDatabaseStmt(self, ctx:SqlParser.CreateDatabaseStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#DropTableStmt.
    def visitDropTableStmt(self, ctx:SqlParser.DropTableStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#DropViewStmt.
    def visitDropViewStmt(self, ctx:SqlParser.DropViewStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#DropIndexStmt.
    def visitDropIndexStmt(self, ctx:SqlParser.DropIndexStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#DropDatabaseStmt.
    def visitDropDatabaseStmt(self, ctx:SqlParser.DropDatabaseStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#AlterTableStmt.
    def visitAlterTableStmt(self, ctx:SqlParser.AlterTableStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#TruncateTableStmt.
    def visitTruncateTableStmt(self, ctx:SqlParser.TruncateTableStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#UseDatabaseStmt.
    def visitUseDatabaseStmt(self, ctx:SqlParser.UseDatabaseStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#CreateTableStatement.
    def visitCreateTableStatement(self, ctx:SqlParser.CreateTableStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#ColumnDefList.
    def visitColumnDefList(self, ctx:SqlParser.ColumnDefListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#ColumnDef.
    def visitColumnDef(self, ctx:SqlParser.ColumnDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#IdentityConstraint.
    def visitIdentityConstraint(self, ctx:SqlParser.IdentityConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#PrimaryKeyConstraint.
    def visitPrimaryKeyConstraint(self, ctx:SqlParser.PrimaryKeyConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#UniqueConstraint.
    def visitUniqueConstraint(self, ctx:SqlParser.UniqueConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#DefaultConstraint.
    def visitDefaultConstraint(self, ctx:SqlParser.DefaultConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#CheckConstraint.
    def visitCheckConstraint(self, ctx:SqlParser.CheckConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#ReferencesConstraint.
    def visitReferencesConstraint(self, ctx:SqlParser.ReferencesConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#NullConstraint.
    def visitNullConstraint(self, ctx:SqlParser.NullConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#NotNullConstraint.
    def visitNotNullConstraint(self, ctx:SqlParser.NotNullConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#TableConstraintList.
    def visitTableConstraintList(self, ctx:SqlParser.TableConstraintListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#TableConstraint.
    def visitTableConstraint(self, ctx:SqlParser.TableConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#PrimaryKeyTableConstraint.
    def visitPrimaryKeyTableConstraint(self, ctx:SqlParser.PrimaryKeyTableConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#UniqueTableConstraint.
    def visitUniqueTableConstraint(self, ctx:SqlParser.UniqueTableConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#ForeignKeyTableConstraint.
    def visitForeignKeyTableConstraint(self, ctx:SqlParser.ForeignKeyTableConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#CheckTableConstraint.
    def visitCheckTableConstraint(self, ctx:SqlParser.CheckTableConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#DataType.
    def visitDataType(self, ctx:SqlParser.DataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#CreateViewStatement.
    def visitCreateViewStatement(self, ctx:SqlParser.CreateViewStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#CreateIndexStatement.
    def visitCreateIndexStatement(self, ctx:SqlParser.CreateIndexStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#CreateDatabaseStatement.
    def visitCreateDatabaseStatement(self, ctx:SqlParser.CreateDatabaseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#DropTableStatement.
    def visitDropTableStatement(self, ctx:SqlParser.DropTableStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#DropViewStatement.
    def visitDropViewStatement(self, ctx:SqlParser.DropViewStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#DropIndexStatement.
    def visitDropIndexStatement(self, ctx:SqlParser.DropIndexStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#DropDatabaseStatement.
    def visitDropDatabaseStatement(self, ctx:SqlParser.DropDatabaseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#AlterTableStatement.
    def visitAlterTableStatement(self, ctx:SqlParser.AlterTableStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#AlterAddColumn.
    def visitAlterAddColumn(self, ctx:SqlParser.AlterAddColumnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#AlterAddConstraint.
    def visitAlterAddConstraint(self, ctx:SqlParser.AlterAddConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#AlterDropColumn.
    def visitAlterDropColumn(self, ctx:SqlParser.AlterDropColumnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#AlterDropConstraint.
    def visitAlterDropConstraint(self, ctx:SqlParser.AlterDropConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#AlterColumnType.
    def visitAlterColumnType(self, ctx:SqlParser.AlterColumnTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#AlterRenameColumn.
    def visitAlterRenameColumn(self, ctx:SqlParser.AlterRenameColumnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#AlterRenameTable.
    def visitAlterRenameTable(self, ctx:SqlParser.AlterRenameTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#ConstraintDef.
    def visitConstraintDef(self, ctx:SqlParser.ConstraintDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#TruncateTableStatement.
    def visitTruncateTableStatement(self, ctx:SqlParser.TruncateTableStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#UseDatabaseStatement.
    def visitUseDatabaseStatement(self, ctx:SqlParser.UseDatabaseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#CteStatementDef.
    def visitCteStatementDef(self, ctx:SqlParser.CteStatementDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#CteDefinition.
    def visitCteDefinition(self, ctx:SqlParser.CteDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#DeclareCursorStmt.
    def visitDeclareCursorStmt(self, ctx:SqlParser.DeclareCursorStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#OpenCursorStmt.
    def visitOpenCursorStmt(self, ctx:SqlParser.OpenCursorStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#CloseCursorStmt.
    def visitCloseCursorStmt(self, ctx:SqlParser.CloseCursorStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#DeallocateCursorStmt.
    def visitDeallocateCursorStmt(self, ctx:SqlParser.DeallocateCursorStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#FetchCursorStmt.
    def visitFetchCursorStmt(self, ctx:SqlParser.FetchCursorStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#DeclareCursor.
    def visitDeclareCursor(self, ctx:SqlParser.DeclareCursorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#OpenCursor.
    def visitOpenCursor(self, ctx:SqlParser.OpenCursorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#CloseCursor.
    def visitCloseCursor(self, ctx:SqlParser.CloseCursorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#DeallocateCursor.
    def visitDeallocateCursor(self, ctx:SqlParser.DeallocateCursorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#FetchCursor.
    def visitFetchCursor(self, ctx:SqlParser.FetchCursorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#WhereClause.
    def visitWhereClause(self, ctx:SqlParser.WhereClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#GroupByClause.
    def visitGroupByClause(self, ctx:SqlParser.GroupByClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#HavingClause.
    def visitHavingClause(self, ctx:SqlParser.HavingClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#OrderByClause.
    def visitOrderByClause(self, ctx:SqlParser.OrderByClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#OrderExpression.
    def visitOrderExpression(self, ctx:SqlParser.OrderExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#ExpressionList.
    def visitExpressionList(self, ctx:SqlParser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#SearchCondition.
    def visitSearchCondition(self, ctx:SqlParser.SearchConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#ExpressionRoot.
    def visitExpressionRoot(self, ctx:SqlParser.ExpressionRootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#OrExpression.
    def visitOrExpression(self, ctx:SqlParser.OrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#AndExpression.
    def visitAndExpression(self, ctx:SqlParser.AndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#NotExpression.
    def visitNotExpression(self, ctx:SqlParser.NotExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#PredicateExpressionWrapper.
    def visitPredicateExpressionWrapper(self, ctx:SqlParser.PredicateExpressionWrapperContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#ComparisonPredicate.
    def visitComparisonPredicate(self, ctx:SqlParser.ComparisonPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#BetweenPredicate.
    def visitBetweenPredicate(self, ctx:SqlParser.BetweenPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#InPredicate.
    def visitInPredicate(self, ctx:SqlParser.InPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#LikePredicate.
    def visitLikePredicate(self, ctx:SqlParser.LikePredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#IsNullPredicate.
    def visitIsNullPredicate(self, ctx:SqlParser.IsNullPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#ExistsPredicate.
    def visitExistsPredicate(self, ctx:SqlParser.ExistsPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#ComparisonExpression.
    def visitComparisonExpression(self, ctx:SqlParser.ComparisonExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#BetweenExpression.
    def visitBetweenExpression(self, ctx:SqlParser.BetweenExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#InExpression.
    def visitInExpression(self, ctx:SqlParser.InExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#LikeExpression.
    def visitLikeExpression(self, ctx:SqlParser.LikeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#NotLikeExpression.
    def visitNotLikeExpression(self, ctx:SqlParser.NotLikeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#IsNullExpression.
    def visitIsNullExpression(self, ctx:SqlParser.IsNullExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#IsNotNullExpression.
    def visitIsNotNullExpression(self, ctx:SqlParser.IsNotNullExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#ExistsExpression.
    def visitExistsExpression(self, ctx:SqlParser.ExistsExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#AdditiveExpression.
    def visitAdditiveExpression(self, ctx:SqlParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#MultiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:SqlParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#UnaryMinusExpression.
    def visitUnaryMinusExpression(self, ctx:SqlParser.UnaryMinusExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#UnaryPlusExpression.
    def visitUnaryPlusExpression(self, ctx:SqlParser.UnaryPlusExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#PrimaryExpressionWrapper.
    def visitPrimaryExpressionWrapper(self, ctx:SqlParser.PrimaryExpressionWrapperContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#ParenthesizedExpression.
    def visitParenthesizedExpression(self, ctx:SqlParser.ParenthesizedExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#SubqueryExpression.
    def visitSubqueryExpression(self, ctx:SqlParser.SubqueryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#FunctionCallExpression.
    def visitFunctionCallExpression(self, ctx:SqlParser.FunctionCallExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#CaseExpressionWrapper.
    def visitCaseExpressionWrapper(self, ctx:SqlParser.CaseExpressionWrapperContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#LiteralExpression.
    def visitLiteralExpression(self, ctx:SqlParser.LiteralExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#ColumnExpression.
    def visitColumnExpression(self, ctx:SqlParser.ColumnExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#CaseExpression.
    def visitCaseExpression(self, ctx:SqlParser.CaseExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#WhenClause.
    def visitWhenClause(self, ctx:SqlParser.WhenClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#ElseClause.
    def visitElseClause(self, ctx:SqlParser.ElseClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#FunctionCall.
    def visitFunctionCall(self, ctx:SqlParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#ColumnName.
    def visitColumnName(self, ctx:SqlParser.ColumnNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#StringLiteral.
    def visitStringLiteral(self, ctx:SqlParser.StringLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#IntegerLiteral.
    def visitIntegerLiteral(self, ctx:SqlParser.IntegerLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#FloatLiteral.
    def visitFloatLiteral(self, ctx:SqlParser.FloatLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#SimpleFloatLiteral.
    def visitSimpleFloatLiteral(self, ctx:SqlParser.SimpleFloatLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#NullLiteral.
    def visitNullLiteral(self, ctx:SqlParser.NullLiteralContext):
        return self.visitChildren(ctx)



del SqlParser