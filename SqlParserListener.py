# Generated from SqlParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .SqlParser import SqlParser
else:
    from SqlParser import SqlParser

# This class defines a complete listener for a parse tree produced by SqlParser.
class SqlParserListener(ParseTreeListener):

    # Enter a parse tree produced by SqlParser#SqlScript.
    def enterSqlScript(self, ctx:SqlParser.SqlScriptContext):
        pass

    # Exit a parse tree produced by SqlParser#SqlScript.
    def exitSqlScript(self, ctx:SqlParser.SqlScriptContext):
        pass


    # Enter a parse tree produced by SqlParser#StatementWrapper.
    def enterStatementWrapper(self, ctx:SqlParser.StatementWrapperContext):
        pass

    # Exit a parse tree produced by SqlParser#StatementWrapper.
    def exitStatementWrapper(self, ctx:SqlParser.StatementWrapperContext):
        pass


    # Enter a parse tree produced by SqlParser#GoWrapper.
    def enterGoWrapper(self, ctx:SqlParser.GoWrapperContext):
        pass

    # Exit a parse tree produced by SqlParser#GoWrapper.
    def exitGoWrapper(self, ctx:SqlParser.GoWrapperContext):
        pass


    # Enter a parse tree produced by SqlParser#GoStatement.
    def enterGoStatement(self, ctx:SqlParser.GoStatementContext):
        pass

    # Exit a parse tree produced by SqlParser#GoStatement.
    def exitGoStatement(self, ctx:SqlParser.GoStatementContext):
        pass


    # Enter a parse tree produced by SqlParser#DmlStatement.
    def enterDmlStatement(self, ctx:SqlParser.DmlStatementContext):
        pass

    # Exit a parse tree produced by SqlParser#DmlStatement.
    def exitDmlStatement(self, ctx:SqlParser.DmlStatementContext):
        pass


    # Enter a parse tree produced by SqlParser#DdlStatement.
    def enterDdlStatement(self, ctx:SqlParser.DdlStatementContext):
        pass

    # Exit a parse tree produced by SqlParser#DdlStatement.
    def exitDdlStatement(self, ctx:SqlParser.DdlStatementContext):
        pass


    # Enter a parse tree produced by SqlParser#CteStatement.
    def enterCteStatement(self, ctx:SqlParser.CteStatementContext):
        pass

    # Exit a parse tree produced by SqlParser#CteStatement.
    def exitCteStatement(self, ctx:SqlParser.CteStatementContext):
        pass


    # Enter a parse tree produced by SqlParser#CursorStatement.
    def enterCursorStatement(self, ctx:SqlParser.CursorStatementContext):
        pass

    # Exit a parse tree produced by SqlParser#CursorStatement.
    def exitCursorStatement(self, ctx:SqlParser.CursorStatementContext):
        pass


    # Enter a parse tree produced by SqlParser#IfStatement.
    def enterIfStatement(self, ctx:SqlParser.IfStatementContext):
        pass

    # Exit a parse tree produced by SqlParser#IfStatement.
    def exitIfStatement(self, ctx:SqlParser.IfStatementContext):
        pass


    # Enter a parse tree produced by SqlParser#IfStmt.
    def enterIfStmt(self, ctx:SqlParser.IfStmtContext):
        pass

    # Exit a parse tree produced by SqlParser#IfStmt.
    def exitIfStmt(self, ctx:SqlParser.IfStmtContext):
        pass


    # Enter a parse tree produced by SqlParser#StatementBlock.
    def enterStatementBlock(self, ctx:SqlParser.StatementBlockContext):
        pass

    # Exit a parse tree produced by SqlParser#StatementBlock.
    def exitStatementBlock(self, ctx:SqlParser.StatementBlockContext):
        pass


    # Enter a parse tree produced by SqlParser#SelectStmt.
    def enterSelectStmt(self, ctx:SqlParser.SelectStmtContext):
        pass

    # Exit a parse tree produced by SqlParser#SelectStmt.
    def exitSelectStmt(self, ctx:SqlParser.SelectStmtContext):
        pass


    # Enter a parse tree produced by SqlParser#InsertStmt.
    def enterInsertStmt(self, ctx:SqlParser.InsertStmtContext):
        pass

    # Exit a parse tree produced by SqlParser#InsertStmt.
    def exitInsertStmt(self, ctx:SqlParser.InsertStmtContext):
        pass


    # Enter a parse tree produced by SqlParser#UpdateStmt.
    def enterUpdateStmt(self, ctx:SqlParser.UpdateStmtContext):
        pass

    # Exit a parse tree produced by SqlParser#UpdateStmt.
    def exitUpdateStmt(self, ctx:SqlParser.UpdateStmtContext):
        pass


    # Enter a parse tree produced by SqlParser#DeleteStmt.
    def enterDeleteStmt(self, ctx:SqlParser.DeleteStmtContext):
        pass

    # Exit a parse tree produced by SqlParser#DeleteStmt.
    def exitDeleteStmt(self, ctx:SqlParser.DeleteStmtContext):
        pass


    # Enter a parse tree produced by SqlParser#SelectStatement.
    def enterSelectStatement(self, ctx:SqlParser.SelectStatementContext):
        pass

    # Exit a parse tree produced by SqlParser#SelectStatement.
    def exitSelectStatement(self, ctx:SqlParser.SelectStatementContext):
        pass


    # Enter a parse tree produced by SqlParser#TopClause.
    def enterTopClause(self, ctx:SqlParser.TopClauseContext):
        pass

    # Exit a parse tree produced by SqlParser#TopClause.
    def exitTopClause(self, ctx:SqlParser.TopClauseContext):
        pass


    # Enter a parse tree produced by SqlParser#SelectStarList.
    def enterSelectStarList(self, ctx:SqlParser.SelectStarListContext):
        pass

    # Exit a parse tree produced by SqlParser#SelectStarList.
    def exitSelectStarList(self, ctx:SqlParser.SelectStarListContext):
        pass


    # Enter a parse tree produced by SqlParser#SelectItemList.
    def enterSelectItemList(self, ctx:SqlParser.SelectItemListContext):
        pass

    # Exit a parse tree produced by SqlParser#SelectItemList.
    def exitSelectItemList(self, ctx:SqlParser.SelectItemListContext):
        pass


    # Enter a parse tree produced by SqlParser#SelectItem.
    def enterSelectItem(self, ctx:SqlParser.SelectItemContext):
        pass

    # Exit a parse tree produced by SqlParser#SelectItem.
    def exitSelectItem(self, ctx:SqlParser.SelectItemContext):
        pass


    # Enter a parse tree produced by SqlParser#IdentifierAlias.
    def enterIdentifierAlias(self, ctx:SqlParser.IdentifierAliasContext):
        pass

    # Exit a parse tree produced by SqlParser#IdentifierAlias.
    def exitIdentifierAlias(self, ctx:SqlParser.IdentifierAliasContext):
        pass


    # Enter a parse tree produced by SqlParser#StringAlias.
    def enterStringAlias(self, ctx:SqlParser.StringAliasContext):
        pass

    # Exit a parse tree produced by SqlParser#StringAlias.
    def exitStringAlias(self, ctx:SqlParser.StringAliasContext):
        pass


    # Enter a parse tree produced by SqlParser#FromClause.
    def enterFromClause(self, ctx:SqlParser.FromClauseContext):
        pass

    # Exit a parse tree produced by SqlParser#FromClause.
    def exitFromClause(self, ctx:SqlParser.FromClauseContext):
        pass


    # Enter a parse tree produced by SqlParser#TableSource.
    def enterTableSource(self, ctx:SqlParser.TableSourceContext):
        pass

    # Exit a parse tree produced by SqlParser#TableSource.
    def exitTableSource(self, ctx:SqlParser.TableSourceContext):
        pass


    # Enter a parse tree produced by SqlParser#SimpleTableSource.
    def enterSimpleTableSource(self, ctx:SqlParser.SimpleTableSourceContext):
        pass

    # Exit a parse tree produced by SqlParser#SimpleTableSource.
    def exitSimpleTableSource(self, ctx:SqlParser.SimpleTableSourceContext):
        pass


    # Enter a parse tree produced by SqlParser#JoinPart.
    def enterJoinPart(self, ctx:SqlParser.JoinPartContext):
        pass

    # Exit a parse tree produced by SqlParser#JoinPart.
    def exitJoinPart(self, ctx:SqlParser.JoinPartContext):
        pass


    # Enter a parse tree produced by SqlParser#CrossJoinPart.
    def enterCrossJoinPart(self, ctx:SqlParser.CrossJoinPartContext):
        pass

    # Exit a parse tree produced by SqlParser#CrossJoinPart.
    def exitCrossJoinPart(self, ctx:SqlParser.CrossJoinPartContext):
        pass


    # Enter a parse tree produced by SqlParser#NaturalJoinPart.
    def enterNaturalJoinPart(self, ctx:SqlParser.NaturalJoinPartContext):
        pass

    # Exit a parse tree produced by SqlParser#NaturalJoinPart.
    def exitNaturalJoinPart(self, ctx:SqlParser.NaturalJoinPartContext):
        pass


    # Enter a parse tree produced by SqlParser#InnerJoinType.
    def enterInnerJoinType(self, ctx:SqlParser.InnerJoinTypeContext):
        pass

    # Exit a parse tree produced by SqlParser#InnerJoinType.
    def exitInnerJoinType(self, ctx:SqlParser.InnerJoinTypeContext):
        pass


    # Enter a parse tree produced by SqlParser#LeftJoinType.
    def enterLeftJoinType(self, ctx:SqlParser.LeftJoinTypeContext):
        pass

    # Exit a parse tree produced by SqlParser#LeftJoinType.
    def exitLeftJoinType(self, ctx:SqlParser.LeftJoinTypeContext):
        pass


    # Enter a parse tree produced by SqlParser#RightJoinType.
    def enterRightJoinType(self, ctx:SqlParser.RightJoinTypeContext):
        pass

    # Exit a parse tree produced by SqlParser#RightJoinType.
    def exitRightJoinType(self, ctx:SqlParser.RightJoinTypeContext):
        pass


    # Enter a parse tree produced by SqlParser#FullJoinType.
    def enterFullJoinType(self, ctx:SqlParser.FullJoinTypeContext):
        pass

    # Exit a parse tree produced by SqlParser#FullJoinType.
    def exitFullJoinType(self, ctx:SqlParser.FullJoinTypeContext):
        pass


    # Enter a parse tree produced by SqlParser#OffsetFetchClause.
    def enterOffsetFetchClause(self, ctx:SqlParser.OffsetFetchClauseContext):
        pass

    # Exit a parse tree produced by SqlParser#OffsetFetchClause.
    def exitOffsetFetchClause(self, ctx:SqlParser.OffsetFetchClauseContext):
        pass


    # Enter a parse tree produced by SqlParser#InsertValuesStatement.
    def enterInsertValuesStatement(self, ctx:SqlParser.InsertValuesStatementContext):
        pass

    # Exit a parse tree produced by SqlParser#InsertValuesStatement.
    def exitInsertValuesStatement(self, ctx:SqlParser.InsertValuesStatementContext):
        pass


    # Enter a parse tree produced by SqlParser#InsertSelectStatement.
    def enterInsertSelectStatement(self, ctx:SqlParser.InsertSelectStatementContext):
        pass

    # Exit a parse tree produced by SqlParser#InsertSelectStatement.
    def exitInsertSelectStatement(self, ctx:SqlParser.InsertSelectStatementContext):
        pass


    # Enter a parse tree produced by SqlParser#InsertDefaultValuesStatement.
    def enterInsertDefaultValuesStatement(self, ctx:SqlParser.InsertDefaultValuesStatementContext):
        pass

    # Exit a parse tree produced by SqlParser#InsertDefaultValuesStatement.
    def exitInsertDefaultValuesStatement(self, ctx:SqlParser.InsertDefaultValuesStatementContext):
        pass


    # Enter a parse tree produced by SqlParser#TableName.
    def enterTableName(self, ctx:SqlParser.TableNameContext):
        pass

    # Exit a parse tree produced by SqlParser#TableName.
    def exitTableName(self, ctx:SqlParser.TableNameContext):
        pass


    # Enter a parse tree produced by SqlParser#ColumnNameList.
    def enterColumnNameList(self, ctx:SqlParser.ColumnNameListContext):
        pass

    # Exit a parse tree produced by SqlParser#ColumnNameList.
    def exitColumnNameList(self, ctx:SqlParser.ColumnNameListContext):
        pass


    # Enter a parse tree produced by SqlParser#ValueList.
    def enterValueList(self, ctx:SqlParser.ValueListContext):
        pass

    # Exit a parse tree produced by SqlParser#ValueList.
    def exitValueList(self, ctx:SqlParser.ValueListContext):
        pass


    # Enter a parse tree produced by SqlParser#UpdateStatement.
    def enterUpdateStatement(self, ctx:SqlParser.UpdateStatementContext):
        pass

    # Exit a parse tree produced by SqlParser#UpdateStatement.
    def exitUpdateStatement(self, ctx:SqlParser.UpdateStatementContext):
        pass


    # Enter a parse tree produced by SqlParser#AssignmentList.
    def enterAssignmentList(self, ctx:SqlParser.AssignmentListContext):
        pass

    # Exit a parse tree produced by SqlParser#AssignmentList.
    def exitAssignmentList(self, ctx:SqlParser.AssignmentListContext):
        pass


    # Enter a parse tree produced by SqlParser#ColumnAssignment.
    def enterColumnAssignment(self, ctx:SqlParser.ColumnAssignmentContext):
        pass

    # Exit a parse tree produced by SqlParser#ColumnAssignment.
    def exitColumnAssignment(self, ctx:SqlParser.ColumnAssignmentContext):
        pass


    # Enter a parse tree produced by SqlParser#DeleteStatement.
    def enterDeleteStatement(self, ctx:SqlParser.DeleteStatementContext):
        pass

    # Exit a parse tree produced by SqlParser#DeleteStatement.
    def exitDeleteStatement(self, ctx:SqlParser.DeleteStatementContext):
        pass


    # Enter a parse tree produced by SqlParser#CreateTableStmt.
    def enterCreateTableStmt(self, ctx:SqlParser.CreateTableStmtContext):
        pass

    # Exit a parse tree produced by SqlParser#CreateTableStmt.
    def exitCreateTableStmt(self, ctx:SqlParser.CreateTableStmtContext):
        pass


    # Enter a parse tree produced by SqlParser#CreateViewStmt.
    def enterCreateViewStmt(self, ctx:SqlParser.CreateViewStmtContext):
        pass

    # Exit a parse tree produced by SqlParser#CreateViewStmt.
    def exitCreateViewStmt(self, ctx:SqlParser.CreateViewStmtContext):
        pass


    # Enter a parse tree produced by SqlParser#CreateIndexStmt.
    def enterCreateIndexStmt(self, ctx:SqlParser.CreateIndexStmtContext):
        pass

    # Exit a parse tree produced by SqlParser#CreateIndexStmt.
    def exitCreateIndexStmt(self, ctx:SqlParser.CreateIndexStmtContext):
        pass


    # Enter a parse tree produced by SqlParser#CreateDatabaseStmt.
    def enterCreateDatabaseStmt(self, ctx:SqlParser.CreateDatabaseStmtContext):
        pass

    # Exit a parse tree produced by SqlParser#CreateDatabaseStmt.
    def exitCreateDatabaseStmt(self, ctx:SqlParser.CreateDatabaseStmtContext):
        pass


    # Enter a parse tree produced by SqlParser#DropTableStmt.
    def enterDropTableStmt(self, ctx:SqlParser.DropTableStmtContext):
        pass

    # Exit a parse tree produced by SqlParser#DropTableStmt.
    def exitDropTableStmt(self, ctx:SqlParser.DropTableStmtContext):
        pass


    # Enter a parse tree produced by SqlParser#DropViewStmt.
    def enterDropViewStmt(self, ctx:SqlParser.DropViewStmtContext):
        pass

    # Exit a parse tree produced by SqlParser#DropViewStmt.
    def exitDropViewStmt(self, ctx:SqlParser.DropViewStmtContext):
        pass


    # Enter a parse tree produced by SqlParser#DropIndexStmt.
    def enterDropIndexStmt(self, ctx:SqlParser.DropIndexStmtContext):
        pass

    # Exit a parse tree produced by SqlParser#DropIndexStmt.
    def exitDropIndexStmt(self, ctx:SqlParser.DropIndexStmtContext):
        pass


    # Enter a parse tree produced by SqlParser#DropDatabaseStmt.
    def enterDropDatabaseStmt(self, ctx:SqlParser.DropDatabaseStmtContext):
        pass

    # Exit a parse tree produced by SqlParser#DropDatabaseStmt.
    def exitDropDatabaseStmt(self, ctx:SqlParser.DropDatabaseStmtContext):
        pass


    # Enter a parse tree produced by SqlParser#AlterTableStmt.
    def enterAlterTableStmt(self, ctx:SqlParser.AlterTableStmtContext):
        pass

    # Exit a parse tree produced by SqlParser#AlterTableStmt.
    def exitAlterTableStmt(self, ctx:SqlParser.AlterTableStmtContext):
        pass


    # Enter a parse tree produced by SqlParser#TruncateTableStmt.
    def enterTruncateTableStmt(self, ctx:SqlParser.TruncateTableStmtContext):
        pass

    # Exit a parse tree produced by SqlParser#TruncateTableStmt.
    def exitTruncateTableStmt(self, ctx:SqlParser.TruncateTableStmtContext):
        pass


    # Enter a parse tree produced by SqlParser#UseDatabaseStmt.
    def enterUseDatabaseStmt(self, ctx:SqlParser.UseDatabaseStmtContext):
        pass

    # Exit a parse tree produced by SqlParser#UseDatabaseStmt.
    def exitUseDatabaseStmt(self, ctx:SqlParser.UseDatabaseStmtContext):
        pass


    # Enter a parse tree produced by SqlParser#CreateTableStatement.
    def enterCreateTableStatement(self, ctx:SqlParser.CreateTableStatementContext):
        pass

    # Exit a parse tree produced by SqlParser#CreateTableStatement.
    def exitCreateTableStatement(self, ctx:SqlParser.CreateTableStatementContext):
        pass


    # Enter a parse tree produced by SqlParser#ColumnDefList.
    def enterColumnDefList(self, ctx:SqlParser.ColumnDefListContext):
        pass

    # Exit a parse tree produced by SqlParser#ColumnDefList.
    def exitColumnDefList(self, ctx:SqlParser.ColumnDefListContext):
        pass


    # Enter a parse tree produced by SqlParser#ColumnDef.
    def enterColumnDef(self, ctx:SqlParser.ColumnDefContext):
        pass

    # Exit a parse tree produced by SqlParser#ColumnDef.
    def exitColumnDef(self, ctx:SqlParser.ColumnDefContext):
        pass


    # Enter a parse tree produced by SqlParser#IdentityConstraint.
    def enterIdentityConstraint(self, ctx:SqlParser.IdentityConstraintContext):
        pass

    # Exit a parse tree produced by SqlParser#IdentityConstraint.
    def exitIdentityConstraint(self, ctx:SqlParser.IdentityConstraintContext):
        pass


    # Enter a parse tree produced by SqlParser#PrimaryKeyConstraint.
    def enterPrimaryKeyConstraint(self, ctx:SqlParser.PrimaryKeyConstraintContext):
        pass

    # Exit a parse tree produced by SqlParser#PrimaryKeyConstraint.
    def exitPrimaryKeyConstraint(self, ctx:SqlParser.PrimaryKeyConstraintContext):
        pass


    # Enter a parse tree produced by SqlParser#UniqueConstraint.
    def enterUniqueConstraint(self, ctx:SqlParser.UniqueConstraintContext):
        pass

    # Exit a parse tree produced by SqlParser#UniqueConstraint.
    def exitUniqueConstraint(self, ctx:SqlParser.UniqueConstraintContext):
        pass


    # Enter a parse tree produced by SqlParser#DefaultConstraint.
    def enterDefaultConstraint(self, ctx:SqlParser.DefaultConstraintContext):
        pass

    # Exit a parse tree produced by SqlParser#DefaultConstraint.
    def exitDefaultConstraint(self, ctx:SqlParser.DefaultConstraintContext):
        pass


    # Enter a parse tree produced by SqlParser#CheckConstraint.
    def enterCheckConstraint(self, ctx:SqlParser.CheckConstraintContext):
        pass

    # Exit a parse tree produced by SqlParser#CheckConstraint.
    def exitCheckConstraint(self, ctx:SqlParser.CheckConstraintContext):
        pass


    # Enter a parse tree produced by SqlParser#ReferencesConstraint.
    def enterReferencesConstraint(self, ctx:SqlParser.ReferencesConstraintContext):
        pass

    # Exit a parse tree produced by SqlParser#ReferencesConstraint.
    def exitReferencesConstraint(self, ctx:SqlParser.ReferencesConstraintContext):
        pass


    # Enter a parse tree produced by SqlParser#NullConstraint.
    def enterNullConstraint(self, ctx:SqlParser.NullConstraintContext):
        pass

    # Exit a parse tree produced by SqlParser#NullConstraint.
    def exitNullConstraint(self, ctx:SqlParser.NullConstraintContext):
        pass


    # Enter a parse tree produced by SqlParser#NotNullConstraint.
    def enterNotNullConstraint(self, ctx:SqlParser.NotNullConstraintContext):
        pass

    # Exit a parse tree produced by SqlParser#NotNullConstraint.
    def exitNotNullConstraint(self, ctx:SqlParser.NotNullConstraintContext):
        pass


    # Enter a parse tree produced by SqlParser#TableConstraintList.
    def enterTableConstraintList(self, ctx:SqlParser.TableConstraintListContext):
        pass

    # Exit a parse tree produced by SqlParser#TableConstraintList.
    def exitTableConstraintList(self, ctx:SqlParser.TableConstraintListContext):
        pass


    # Enter a parse tree produced by SqlParser#TableConstraint.
    def enterTableConstraint(self, ctx:SqlParser.TableConstraintContext):
        pass

    # Exit a parse tree produced by SqlParser#TableConstraint.
    def exitTableConstraint(self, ctx:SqlParser.TableConstraintContext):
        pass


    # Enter a parse tree produced by SqlParser#PrimaryKeyTableConstraint.
    def enterPrimaryKeyTableConstraint(self, ctx:SqlParser.PrimaryKeyTableConstraintContext):
        pass

    # Exit a parse tree produced by SqlParser#PrimaryKeyTableConstraint.
    def exitPrimaryKeyTableConstraint(self, ctx:SqlParser.PrimaryKeyTableConstraintContext):
        pass


    # Enter a parse tree produced by SqlParser#UniqueTableConstraint.
    def enterUniqueTableConstraint(self, ctx:SqlParser.UniqueTableConstraintContext):
        pass

    # Exit a parse tree produced by SqlParser#UniqueTableConstraint.
    def exitUniqueTableConstraint(self, ctx:SqlParser.UniqueTableConstraintContext):
        pass


    # Enter a parse tree produced by SqlParser#ForeignKeyTableConstraint.
    def enterForeignKeyTableConstraint(self, ctx:SqlParser.ForeignKeyTableConstraintContext):
        pass

    # Exit a parse tree produced by SqlParser#ForeignKeyTableConstraint.
    def exitForeignKeyTableConstraint(self, ctx:SqlParser.ForeignKeyTableConstraintContext):
        pass


    # Enter a parse tree produced by SqlParser#CheckTableConstraint.
    def enterCheckTableConstraint(self, ctx:SqlParser.CheckTableConstraintContext):
        pass

    # Exit a parse tree produced by SqlParser#CheckTableConstraint.
    def exitCheckTableConstraint(self, ctx:SqlParser.CheckTableConstraintContext):
        pass


    # Enter a parse tree produced by SqlParser#DataType.
    def enterDataType(self, ctx:SqlParser.DataTypeContext):
        pass

    # Exit a parse tree produced by SqlParser#DataType.
    def exitDataType(self, ctx:SqlParser.DataTypeContext):
        pass


    # Enter a parse tree produced by SqlParser#CreateViewStatement.
    def enterCreateViewStatement(self, ctx:SqlParser.CreateViewStatementContext):
        pass

    # Exit a parse tree produced by SqlParser#CreateViewStatement.
    def exitCreateViewStatement(self, ctx:SqlParser.CreateViewStatementContext):
        pass


    # Enter a parse tree produced by SqlParser#CreateIndexStatement.
    def enterCreateIndexStatement(self, ctx:SqlParser.CreateIndexStatementContext):
        pass

    # Exit a parse tree produced by SqlParser#CreateIndexStatement.
    def exitCreateIndexStatement(self, ctx:SqlParser.CreateIndexStatementContext):
        pass


    # Enter a parse tree produced by SqlParser#CreateDatabaseStatement.
    def enterCreateDatabaseStatement(self, ctx:SqlParser.CreateDatabaseStatementContext):
        pass

    # Exit a parse tree produced by SqlParser#CreateDatabaseStatement.
    def exitCreateDatabaseStatement(self, ctx:SqlParser.CreateDatabaseStatementContext):
        pass


    # Enter a parse tree produced by SqlParser#DropTableStatement.
    def enterDropTableStatement(self, ctx:SqlParser.DropTableStatementContext):
        pass

    # Exit a parse tree produced by SqlParser#DropTableStatement.
    def exitDropTableStatement(self, ctx:SqlParser.DropTableStatementContext):
        pass


    # Enter a parse tree produced by SqlParser#DropViewStatement.
    def enterDropViewStatement(self, ctx:SqlParser.DropViewStatementContext):
        pass

    # Exit a parse tree produced by SqlParser#DropViewStatement.
    def exitDropViewStatement(self, ctx:SqlParser.DropViewStatementContext):
        pass


    # Enter a parse tree produced by SqlParser#DropIndexStatement.
    def enterDropIndexStatement(self, ctx:SqlParser.DropIndexStatementContext):
        pass

    # Exit a parse tree produced by SqlParser#DropIndexStatement.
    def exitDropIndexStatement(self, ctx:SqlParser.DropIndexStatementContext):
        pass


    # Enter a parse tree produced by SqlParser#DropDatabaseStatement.
    def enterDropDatabaseStatement(self, ctx:SqlParser.DropDatabaseStatementContext):
        pass

    # Exit a parse tree produced by SqlParser#DropDatabaseStatement.
    def exitDropDatabaseStatement(self, ctx:SqlParser.DropDatabaseStatementContext):
        pass


    # Enter a parse tree produced by SqlParser#AlterTableStatement.
    def enterAlterTableStatement(self, ctx:SqlParser.AlterTableStatementContext):
        pass

    # Exit a parse tree produced by SqlParser#AlterTableStatement.
    def exitAlterTableStatement(self, ctx:SqlParser.AlterTableStatementContext):
        pass


    # Enter a parse tree produced by SqlParser#AlterAddColumn.
    def enterAlterAddColumn(self, ctx:SqlParser.AlterAddColumnContext):
        pass

    # Exit a parse tree produced by SqlParser#AlterAddColumn.
    def exitAlterAddColumn(self, ctx:SqlParser.AlterAddColumnContext):
        pass


    # Enter a parse tree produced by SqlParser#AlterAddConstraint.
    def enterAlterAddConstraint(self, ctx:SqlParser.AlterAddConstraintContext):
        pass

    # Exit a parse tree produced by SqlParser#AlterAddConstraint.
    def exitAlterAddConstraint(self, ctx:SqlParser.AlterAddConstraintContext):
        pass


    # Enter a parse tree produced by SqlParser#AlterDropColumn.
    def enterAlterDropColumn(self, ctx:SqlParser.AlterDropColumnContext):
        pass

    # Exit a parse tree produced by SqlParser#AlterDropColumn.
    def exitAlterDropColumn(self, ctx:SqlParser.AlterDropColumnContext):
        pass


    # Enter a parse tree produced by SqlParser#AlterDropConstraint.
    def enterAlterDropConstraint(self, ctx:SqlParser.AlterDropConstraintContext):
        pass

    # Exit a parse tree produced by SqlParser#AlterDropConstraint.
    def exitAlterDropConstraint(self, ctx:SqlParser.AlterDropConstraintContext):
        pass


    # Enter a parse tree produced by SqlParser#AlterColumnType.
    def enterAlterColumnType(self, ctx:SqlParser.AlterColumnTypeContext):
        pass

    # Exit a parse tree produced by SqlParser#AlterColumnType.
    def exitAlterColumnType(self, ctx:SqlParser.AlterColumnTypeContext):
        pass


    # Enter a parse tree produced by SqlParser#AlterRenameColumn.
    def enterAlterRenameColumn(self, ctx:SqlParser.AlterRenameColumnContext):
        pass

    # Exit a parse tree produced by SqlParser#AlterRenameColumn.
    def exitAlterRenameColumn(self, ctx:SqlParser.AlterRenameColumnContext):
        pass


    # Enter a parse tree produced by SqlParser#AlterRenameTable.
    def enterAlterRenameTable(self, ctx:SqlParser.AlterRenameTableContext):
        pass

    # Exit a parse tree produced by SqlParser#AlterRenameTable.
    def exitAlterRenameTable(self, ctx:SqlParser.AlterRenameTableContext):
        pass


    # Enter a parse tree produced by SqlParser#ConstraintDef.
    def enterConstraintDef(self, ctx:SqlParser.ConstraintDefContext):
        pass

    # Exit a parse tree produced by SqlParser#ConstraintDef.
    def exitConstraintDef(self, ctx:SqlParser.ConstraintDefContext):
        pass


    # Enter a parse tree produced by SqlParser#TruncateTableStatement.
    def enterTruncateTableStatement(self, ctx:SqlParser.TruncateTableStatementContext):
        pass

    # Exit a parse tree produced by SqlParser#TruncateTableStatement.
    def exitTruncateTableStatement(self, ctx:SqlParser.TruncateTableStatementContext):
        pass


    # Enter a parse tree produced by SqlParser#UseDatabaseStatement.
    def enterUseDatabaseStatement(self, ctx:SqlParser.UseDatabaseStatementContext):
        pass

    # Exit a parse tree produced by SqlParser#UseDatabaseStatement.
    def exitUseDatabaseStatement(self, ctx:SqlParser.UseDatabaseStatementContext):
        pass


    # Enter a parse tree produced by SqlParser#CteStatementDef.
    def enterCteStatementDef(self, ctx:SqlParser.CteStatementDefContext):
        pass

    # Exit a parse tree produced by SqlParser#CteStatementDef.
    def exitCteStatementDef(self, ctx:SqlParser.CteStatementDefContext):
        pass


    # Enter a parse tree produced by SqlParser#CteDefinition.
    def enterCteDefinition(self, ctx:SqlParser.CteDefinitionContext):
        pass

    # Exit a parse tree produced by SqlParser#CteDefinition.
    def exitCteDefinition(self, ctx:SqlParser.CteDefinitionContext):
        pass


    # Enter a parse tree produced by SqlParser#DeclareCursorStmt.
    def enterDeclareCursorStmt(self, ctx:SqlParser.DeclareCursorStmtContext):
        pass

    # Exit a parse tree produced by SqlParser#DeclareCursorStmt.
    def exitDeclareCursorStmt(self, ctx:SqlParser.DeclareCursorStmtContext):
        pass


    # Enter a parse tree produced by SqlParser#OpenCursorStmt.
    def enterOpenCursorStmt(self, ctx:SqlParser.OpenCursorStmtContext):
        pass

    # Exit a parse tree produced by SqlParser#OpenCursorStmt.
    def exitOpenCursorStmt(self, ctx:SqlParser.OpenCursorStmtContext):
        pass


    # Enter a parse tree produced by SqlParser#CloseCursorStmt.
    def enterCloseCursorStmt(self, ctx:SqlParser.CloseCursorStmtContext):
        pass

    # Exit a parse tree produced by SqlParser#CloseCursorStmt.
    def exitCloseCursorStmt(self, ctx:SqlParser.CloseCursorStmtContext):
        pass


    # Enter a parse tree produced by SqlParser#DeallocateCursorStmt.
    def enterDeallocateCursorStmt(self, ctx:SqlParser.DeallocateCursorStmtContext):
        pass

    # Exit a parse tree produced by SqlParser#DeallocateCursorStmt.
    def exitDeallocateCursorStmt(self, ctx:SqlParser.DeallocateCursorStmtContext):
        pass


    # Enter a parse tree produced by SqlParser#FetchCursorStmt.
    def enterFetchCursorStmt(self, ctx:SqlParser.FetchCursorStmtContext):
        pass

    # Exit a parse tree produced by SqlParser#FetchCursorStmt.
    def exitFetchCursorStmt(self, ctx:SqlParser.FetchCursorStmtContext):
        pass


    # Enter a parse tree produced by SqlParser#DeclareCursor.
    def enterDeclareCursor(self, ctx:SqlParser.DeclareCursorContext):
        pass

    # Exit a parse tree produced by SqlParser#DeclareCursor.
    def exitDeclareCursor(self, ctx:SqlParser.DeclareCursorContext):
        pass


    # Enter a parse tree produced by SqlParser#OpenCursor.
    def enterOpenCursor(self, ctx:SqlParser.OpenCursorContext):
        pass

    # Exit a parse tree produced by SqlParser#OpenCursor.
    def exitOpenCursor(self, ctx:SqlParser.OpenCursorContext):
        pass


    # Enter a parse tree produced by SqlParser#CloseCursor.
    def enterCloseCursor(self, ctx:SqlParser.CloseCursorContext):
        pass

    # Exit a parse tree produced by SqlParser#CloseCursor.
    def exitCloseCursor(self, ctx:SqlParser.CloseCursorContext):
        pass


    # Enter a parse tree produced by SqlParser#DeallocateCursor.
    def enterDeallocateCursor(self, ctx:SqlParser.DeallocateCursorContext):
        pass

    # Exit a parse tree produced by SqlParser#DeallocateCursor.
    def exitDeallocateCursor(self, ctx:SqlParser.DeallocateCursorContext):
        pass


    # Enter a parse tree produced by SqlParser#FetchCursor.
    def enterFetchCursor(self, ctx:SqlParser.FetchCursorContext):
        pass

    # Exit a parse tree produced by SqlParser#FetchCursor.
    def exitFetchCursor(self, ctx:SqlParser.FetchCursorContext):
        pass


    # Enter a parse tree produced by SqlParser#WhereClause.
    def enterWhereClause(self, ctx:SqlParser.WhereClauseContext):
        pass

    # Exit a parse tree produced by SqlParser#WhereClause.
    def exitWhereClause(self, ctx:SqlParser.WhereClauseContext):
        pass


    # Enter a parse tree produced by SqlParser#GroupByClause.
    def enterGroupByClause(self, ctx:SqlParser.GroupByClauseContext):
        pass

    # Exit a parse tree produced by SqlParser#GroupByClause.
    def exitGroupByClause(self, ctx:SqlParser.GroupByClauseContext):
        pass


    # Enter a parse tree produced by SqlParser#HavingClause.
    def enterHavingClause(self, ctx:SqlParser.HavingClauseContext):
        pass

    # Exit a parse tree produced by SqlParser#HavingClause.
    def exitHavingClause(self, ctx:SqlParser.HavingClauseContext):
        pass


    # Enter a parse tree produced by SqlParser#OrderByClause.
    def enterOrderByClause(self, ctx:SqlParser.OrderByClauseContext):
        pass

    # Exit a parse tree produced by SqlParser#OrderByClause.
    def exitOrderByClause(self, ctx:SqlParser.OrderByClauseContext):
        pass


    # Enter a parse tree produced by SqlParser#OrderExpression.
    def enterOrderExpression(self, ctx:SqlParser.OrderExpressionContext):
        pass

    # Exit a parse tree produced by SqlParser#OrderExpression.
    def exitOrderExpression(self, ctx:SqlParser.OrderExpressionContext):
        pass


    # Enter a parse tree produced by SqlParser#ExpressionList.
    def enterExpressionList(self, ctx:SqlParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by SqlParser#ExpressionList.
    def exitExpressionList(self, ctx:SqlParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by SqlParser#SearchCondition.
    def enterSearchCondition(self, ctx:SqlParser.SearchConditionContext):
        pass

    # Exit a parse tree produced by SqlParser#SearchCondition.
    def exitSearchCondition(self, ctx:SqlParser.SearchConditionContext):
        pass


    # Enter a parse tree produced by SqlParser#ExpressionRoot.
    def enterExpressionRoot(self, ctx:SqlParser.ExpressionRootContext):
        pass

    # Exit a parse tree produced by SqlParser#ExpressionRoot.
    def exitExpressionRoot(self, ctx:SqlParser.ExpressionRootContext):
        pass


    # Enter a parse tree produced by SqlParser#OrExpression.
    def enterOrExpression(self, ctx:SqlParser.OrExpressionContext):
        pass

    # Exit a parse tree produced by SqlParser#OrExpression.
    def exitOrExpression(self, ctx:SqlParser.OrExpressionContext):
        pass


    # Enter a parse tree produced by SqlParser#AndExpression.
    def enterAndExpression(self, ctx:SqlParser.AndExpressionContext):
        pass

    # Exit a parse tree produced by SqlParser#AndExpression.
    def exitAndExpression(self, ctx:SqlParser.AndExpressionContext):
        pass


    # Enter a parse tree produced by SqlParser#NotExpression.
    def enterNotExpression(self, ctx:SqlParser.NotExpressionContext):
        pass

    # Exit a parse tree produced by SqlParser#NotExpression.
    def exitNotExpression(self, ctx:SqlParser.NotExpressionContext):
        pass


    # Enter a parse tree produced by SqlParser#PredicateExpressionWrapper.
    def enterPredicateExpressionWrapper(self, ctx:SqlParser.PredicateExpressionWrapperContext):
        pass

    # Exit a parse tree produced by SqlParser#PredicateExpressionWrapper.
    def exitPredicateExpressionWrapper(self, ctx:SqlParser.PredicateExpressionWrapperContext):
        pass


    # Enter a parse tree produced by SqlParser#ComparisonPredicate.
    def enterComparisonPredicate(self, ctx:SqlParser.ComparisonPredicateContext):
        pass

    # Exit a parse tree produced by SqlParser#ComparisonPredicate.
    def exitComparisonPredicate(self, ctx:SqlParser.ComparisonPredicateContext):
        pass


    # Enter a parse tree produced by SqlParser#BetweenPredicate.
    def enterBetweenPredicate(self, ctx:SqlParser.BetweenPredicateContext):
        pass

    # Exit a parse tree produced by SqlParser#BetweenPredicate.
    def exitBetweenPredicate(self, ctx:SqlParser.BetweenPredicateContext):
        pass


    # Enter a parse tree produced by SqlParser#InPredicate.
    def enterInPredicate(self, ctx:SqlParser.InPredicateContext):
        pass

    # Exit a parse tree produced by SqlParser#InPredicate.
    def exitInPredicate(self, ctx:SqlParser.InPredicateContext):
        pass


    # Enter a parse tree produced by SqlParser#LikePredicate.
    def enterLikePredicate(self, ctx:SqlParser.LikePredicateContext):
        pass

    # Exit a parse tree produced by SqlParser#LikePredicate.
    def exitLikePredicate(self, ctx:SqlParser.LikePredicateContext):
        pass


    # Enter a parse tree produced by SqlParser#IsNullPredicate.
    def enterIsNullPredicate(self, ctx:SqlParser.IsNullPredicateContext):
        pass

    # Exit a parse tree produced by SqlParser#IsNullPredicate.
    def exitIsNullPredicate(self, ctx:SqlParser.IsNullPredicateContext):
        pass


    # Enter a parse tree produced by SqlParser#ExistsPredicate.
    def enterExistsPredicate(self, ctx:SqlParser.ExistsPredicateContext):
        pass

    # Exit a parse tree produced by SqlParser#ExistsPredicate.
    def exitExistsPredicate(self, ctx:SqlParser.ExistsPredicateContext):
        pass


    # Enter a parse tree produced by SqlParser#ComparisonExpression.
    def enterComparisonExpression(self, ctx:SqlParser.ComparisonExpressionContext):
        pass

    # Exit a parse tree produced by SqlParser#ComparisonExpression.
    def exitComparisonExpression(self, ctx:SqlParser.ComparisonExpressionContext):
        pass


    # Enter a parse tree produced by SqlParser#BetweenExpression.
    def enterBetweenExpression(self, ctx:SqlParser.BetweenExpressionContext):
        pass

    # Exit a parse tree produced by SqlParser#BetweenExpression.
    def exitBetweenExpression(self, ctx:SqlParser.BetweenExpressionContext):
        pass


    # Enter a parse tree produced by SqlParser#InExpression.
    def enterInExpression(self, ctx:SqlParser.InExpressionContext):
        pass

    # Exit a parse tree produced by SqlParser#InExpression.
    def exitInExpression(self, ctx:SqlParser.InExpressionContext):
        pass


    # Enter a parse tree produced by SqlParser#LikeExpression.
    def enterLikeExpression(self, ctx:SqlParser.LikeExpressionContext):
        pass

    # Exit a parse tree produced by SqlParser#LikeExpression.
    def exitLikeExpression(self, ctx:SqlParser.LikeExpressionContext):
        pass


    # Enter a parse tree produced by SqlParser#NotLikeExpression.
    def enterNotLikeExpression(self, ctx:SqlParser.NotLikeExpressionContext):
        pass

    # Exit a parse tree produced by SqlParser#NotLikeExpression.
    def exitNotLikeExpression(self, ctx:SqlParser.NotLikeExpressionContext):
        pass


    # Enter a parse tree produced by SqlParser#IsNullExpression.
    def enterIsNullExpression(self, ctx:SqlParser.IsNullExpressionContext):
        pass

    # Exit a parse tree produced by SqlParser#IsNullExpression.
    def exitIsNullExpression(self, ctx:SqlParser.IsNullExpressionContext):
        pass


    # Enter a parse tree produced by SqlParser#IsNotNullExpression.
    def enterIsNotNullExpression(self, ctx:SqlParser.IsNotNullExpressionContext):
        pass

    # Exit a parse tree produced by SqlParser#IsNotNullExpression.
    def exitIsNotNullExpression(self, ctx:SqlParser.IsNotNullExpressionContext):
        pass


    # Enter a parse tree produced by SqlParser#ExistsExpression.
    def enterExistsExpression(self, ctx:SqlParser.ExistsExpressionContext):
        pass

    # Exit a parse tree produced by SqlParser#ExistsExpression.
    def exitExistsExpression(self, ctx:SqlParser.ExistsExpressionContext):
        pass


    # Enter a parse tree produced by SqlParser#AdditiveExpression.
    def enterAdditiveExpression(self, ctx:SqlParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by SqlParser#AdditiveExpression.
    def exitAdditiveExpression(self, ctx:SqlParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by SqlParser#MultiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:SqlParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by SqlParser#MultiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:SqlParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by SqlParser#UnaryMinusExpression.
    def enterUnaryMinusExpression(self, ctx:SqlParser.UnaryMinusExpressionContext):
        pass

    # Exit a parse tree produced by SqlParser#UnaryMinusExpression.
    def exitUnaryMinusExpression(self, ctx:SqlParser.UnaryMinusExpressionContext):
        pass


    # Enter a parse tree produced by SqlParser#UnaryPlusExpression.
    def enterUnaryPlusExpression(self, ctx:SqlParser.UnaryPlusExpressionContext):
        pass

    # Exit a parse tree produced by SqlParser#UnaryPlusExpression.
    def exitUnaryPlusExpression(self, ctx:SqlParser.UnaryPlusExpressionContext):
        pass


    # Enter a parse tree produced by SqlParser#PrimaryExpressionWrapper.
    def enterPrimaryExpressionWrapper(self, ctx:SqlParser.PrimaryExpressionWrapperContext):
        pass

    # Exit a parse tree produced by SqlParser#PrimaryExpressionWrapper.
    def exitPrimaryExpressionWrapper(self, ctx:SqlParser.PrimaryExpressionWrapperContext):
        pass


    # Enter a parse tree produced by SqlParser#ParenthesizedExpression.
    def enterParenthesizedExpression(self, ctx:SqlParser.ParenthesizedExpressionContext):
        pass

    # Exit a parse tree produced by SqlParser#ParenthesizedExpression.
    def exitParenthesizedExpression(self, ctx:SqlParser.ParenthesizedExpressionContext):
        pass


    # Enter a parse tree produced by SqlParser#SubqueryExpression.
    def enterSubqueryExpression(self, ctx:SqlParser.SubqueryExpressionContext):
        pass

    # Exit a parse tree produced by SqlParser#SubqueryExpression.
    def exitSubqueryExpression(self, ctx:SqlParser.SubqueryExpressionContext):
        pass


    # Enter a parse tree produced by SqlParser#FunctionCallExpression.
    def enterFunctionCallExpression(self, ctx:SqlParser.FunctionCallExpressionContext):
        pass

    # Exit a parse tree produced by SqlParser#FunctionCallExpression.
    def exitFunctionCallExpression(self, ctx:SqlParser.FunctionCallExpressionContext):
        pass


    # Enter a parse tree produced by SqlParser#CaseExpressionWrapper.
    def enterCaseExpressionWrapper(self, ctx:SqlParser.CaseExpressionWrapperContext):
        pass

    # Exit a parse tree produced by SqlParser#CaseExpressionWrapper.
    def exitCaseExpressionWrapper(self, ctx:SqlParser.CaseExpressionWrapperContext):
        pass


    # Enter a parse tree produced by SqlParser#LiteralExpression.
    def enterLiteralExpression(self, ctx:SqlParser.LiteralExpressionContext):
        pass

    # Exit a parse tree produced by SqlParser#LiteralExpression.
    def exitLiteralExpression(self, ctx:SqlParser.LiteralExpressionContext):
        pass


    # Enter a parse tree produced by SqlParser#ColumnExpression.
    def enterColumnExpression(self, ctx:SqlParser.ColumnExpressionContext):
        pass

    # Exit a parse tree produced by SqlParser#ColumnExpression.
    def exitColumnExpression(self, ctx:SqlParser.ColumnExpressionContext):
        pass


    # Enter a parse tree produced by SqlParser#CaseExpression.
    def enterCaseExpression(self, ctx:SqlParser.CaseExpressionContext):
        pass

    # Exit a parse tree produced by SqlParser#CaseExpression.
    def exitCaseExpression(self, ctx:SqlParser.CaseExpressionContext):
        pass


    # Enter a parse tree produced by SqlParser#WhenClause.
    def enterWhenClause(self, ctx:SqlParser.WhenClauseContext):
        pass

    # Exit a parse tree produced by SqlParser#WhenClause.
    def exitWhenClause(self, ctx:SqlParser.WhenClauseContext):
        pass


    # Enter a parse tree produced by SqlParser#ElseClause.
    def enterElseClause(self, ctx:SqlParser.ElseClauseContext):
        pass

    # Exit a parse tree produced by SqlParser#ElseClause.
    def exitElseClause(self, ctx:SqlParser.ElseClauseContext):
        pass


    # Enter a parse tree produced by SqlParser#FunctionCall.
    def enterFunctionCall(self, ctx:SqlParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by SqlParser#FunctionCall.
    def exitFunctionCall(self, ctx:SqlParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by SqlParser#ColumnName.
    def enterColumnName(self, ctx:SqlParser.ColumnNameContext):
        pass

    # Exit a parse tree produced by SqlParser#ColumnName.
    def exitColumnName(self, ctx:SqlParser.ColumnNameContext):
        pass


    # Enter a parse tree produced by SqlParser#StringLiteral.
    def enterStringLiteral(self, ctx:SqlParser.StringLiteralContext):
        pass

    # Exit a parse tree produced by SqlParser#StringLiteral.
    def exitStringLiteral(self, ctx:SqlParser.StringLiteralContext):
        pass


    # Enter a parse tree produced by SqlParser#IntegerLiteral.
    def enterIntegerLiteral(self, ctx:SqlParser.IntegerLiteralContext):
        pass

    # Exit a parse tree produced by SqlParser#IntegerLiteral.
    def exitIntegerLiteral(self, ctx:SqlParser.IntegerLiteralContext):
        pass


    # Enter a parse tree produced by SqlParser#FloatLiteral.
    def enterFloatLiteral(self, ctx:SqlParser.FloatLiteralContext):
        pass

    # Exit a parse tree produced by SqlParser#FloatLiteral.
    def exitFloatLiteral(self, ctx:SqlParser.FloatLiteralContext):
        pass


    # Enter a parse tree produced by SqlParser#SimpleFloatLiteral.
    def enterSimpleFloatLiteral(self, ctx:SqlParser.SimpleFloatLiteralContext):
        pass

    # Exit a parse tree produced by SqlParser#SimpleFloatLiteral.
    def exitSimpleFloatLiteral(self, ctx:SqlParser.SimpleFloatLiteralContext):
        pass


    # Enter a parse tree produced by SqlParser#NullLiteral.
    def enterNullLiteral(self, ctx:SqlParser.NullLiteralContext):
        pass

    # Exit a parse tree produced by SqlParser#NullLiteral.
    def exitNullLiteral(self, ctx:SqlParser.NullLiteralContext):
        pass



del SqlParser