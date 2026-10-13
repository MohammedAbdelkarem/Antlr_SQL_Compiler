parser grammar SqlParser;

options {
	tokenVocab = SqlLexer;
}

// root
sql_script: statement_or_go* EOF # SqlScript;

statement_or_go:
	statement SEMI?			# StatementWrapper
	| go_statement SEMI?	# GoWrapper;

go_statement: GO # GoStatement;

// high-level statements
statement:
	dml_statement		# DmlStatement
	| ddl_statement		# DdlStatement
	| cte_statement		# CteStatement
	| cursor_statement	# CursorStatement
	| if_statement		# IfStatement;

if_statement:
	IF search_condition statement_block (ELSE statement_block)? # IfStmt;

statement_block: BEGIN statement_or_go* END # StatementBlock;

// DML
dml_statement:
	select_statement	# SelectStmt
	| insert_statement	# InsertStmt
	| update_statement	# UpdateStmt
	| delete_statement	# DeleteStmt;

select_statement:
	SELECT DISTINCT? top_clause? select_list (INTO table_name)? from_clause? where_clause?
		group_by_clause? having_clause? order_by_clause? offset_fetch_clause? # SelectStatement;

top_clause:
	TOP (LPAREN expression RPAREN | UNSIGNED_INTEGER) PERCENT? # TopClause;

select_list:
	STAR								# SelectStarList
	| select_item (COMMA select_item)*	# SelectItemList;

select_item: expression (AS? column_alias)? # SelectItem;

column_alias:
	IDENTIFIER	# IdentifierAlias
	| STRING	# StringAlias;

from_clause: FROM table_source # FromClause;

table_source: simple_table_source (join_part)* # TableSource;

simple_table_source: (IDENTIFIER | BRACKET_ID) (
		AS? (IDENTIFIER | BRACKET_ID)
	)? # SimpleTableSource;

join_part:
	join_type JOIN simple_table_source ON search_condition	# JoinPart
	| CROSS JOIN simple_table_source						# CrossJoinPart
	| NATURAL JOIN simple_table_source						# NaturalJoinPart;

join_type:
	INNER?			# InnerJoinType
	| LEFT OUTER?	# LeftJoinType
	| RIGHT OUTER?	# RightJoinType
	| FULL OUTER?	# FullJoinType;

offset_fetch_clause:
	OFFSET expression ROWS (FETCH NEXT expression ROWS ONLY)? # OffsetFetchClause;

// INSERT
insert_statement:
	INSERT INTO table_name (LPAREN column_name_list RPAREN)? VALUES value_list #
		InsertValuesStatement
	| INSERT INTO table_name (LPAREN column_name_list RPAREN)? select_statement #
		InsertSelectStatement
	| INSERT INTO table_name DEFAULT VALUES # InsertDefaultValuesStatement;

table_name: (IDENTIFIER | BRACKET_ID) (
		DOT (IDENTIFIER | BRACKET_ID)
	)* # TableName;

column_name_list:
	column_name (COMMA column_name)* # ColumnNameList;

value_list:
	LPAREN expression_list RPAREN (
		COMMA LPAREN expression_list RPAREN
	)* # ValueList;

// UPDATE
update_statement:
	UPDATE table_name SET assignment_list from_clause? where_clause? # UpdateStatement;

assignment_list:
	assignment (COMMA assignment)* # AssignmentList;

//assignment: column_name EQ expression # Assignment;
assignment: column_name EQ expression # ColumnAssignment;

// DELETE
delete_statement:
	DELETE FROM table_source where_clause? # DeleteStatement;

// DDL
ddl_statement:
	create_table_statement		# CreateTableStmt
	| create_view_statement		# CreateViewStmt
	| create_index_statement	# CreateIndexStmt
	| create_database_statement	# CreateDatabaseStmt
	| drop_table_statement		# DropTableStmt
	| drop_view_statement		# DropViewStmt
	| drop_index_statement		# DropIndexStmt
	| drop_database_statement	# DropDatabaseStmt
	| alter_table_statement		# AlterTableStmt
	| truncate_table_statement	# TruncateTableStmt
	| use_database_statement	# UseDatabaseStmt;

create_table_statement:
	CREATE TABLE table_name LPAREN column_def_list (
		COMMA table_constraint_list
	)? RPAREN # CreateTableStatement;

column_def_list: column_def (COMMA column_def)* # ColumnDefList;

column_def:
	column_name data_type column_constraint* # ColumnDef;

column_constraint:
	IDENTITY												# IdentityConstraint
	| PRIMARY KEY											# PrimaryKeyConstraint
	| UNIQUE												# UniqueConstraint
	| DEFAULT literal_value									# DefaultConstraint
	| CHECK LPAREN search_condition RPAREN					# CheckConstraint
	| REFERENCES table_name (LPAREN column_name RPAREN)?	# ReferencesConstraint
	| NULL													# NullConstraint
	| NOT NULL												# NotNullConstraint;

table_constraint_list:
	table_constraint (COMMA table_constraint)* # TableConstraintList;

table_constraint:
	CONSTRAINT IDENTIFIER? table_constraint_def # TableConstraint;

table_constraint_def:
	PRIMARY KEY (CLUSTERED | NONCLUSTERED)? LPAREN column_name_list RPAREN #
		PrimaryKeyTableConstraint
	| UNIQUE (CLUSTERED | NONCLUSTERED)? LPAREN column_name_list RPAREN # UniqueTableConstraint
	| FOREIGN KEY LPAREN column_name_list RPAREN REFERENCES table_name (
		LPAREN column_name_list RPAREN
	)?										# ForeignKeyTableConstraint
	| CHECK LPAREN search_condition RPAREN	# CheckTableConstraint;

data_type: (IDENTIFIER | INT) (
		LPAREN UNSIGNED_INTEGER (COMMA UNSIGNED_INTEGER)? RPAREN
	)? # DataType;

create_view_statement:
	CREATE VIEW table_name AS select_statement # CreateViewStatement;

create_index_statement:
	CREATE INDEX IDENTIFIER ON table_name LPAREN column_name_list RPAREN # CreateIndexStatement;

create_database_statement:
	CREATE DATABASE IDENTIFIER # CreateDatabaseStatement;

drop_table_statement:
	DROP TABLE table_name # DropTableStatement;

drop_view_statement: DROP VIEW table_name # DropViewStatement;

drop_index_statement:
	DROP INDEX IDENTIFIER # DropIndexStatement;

drop_database_statement:
	DROP DATABASE IDENTIFIER # DropDatabaseStatement;

alter_table_statement:
	ALTER TABLE table_name alter_table_action # AlterTableStatement;

alter_table_action:
	ADD column_def								# AlterAddColumn
	| ADD CONSTRAINT constraint_def				# AlterAddConstraint
	| DROP COLUMN column_name					# AlterDropColumn
	| DROP CONSTRAINT IDENTIFIER				# AlterDropConstraint
	| ALTER COLUMN column_name data_type		# AlterColumnType
	| RENAME COLUMN column_name TO column_name	# AlterRenameColumn
	| RENAME TO table_name						# AlterRenameTable;

constraint_def: table_constraint_def # ConstraintDef;

truncate_table_statement:
	TRUNCATE TABLE table_name # TruncateTableStatement;

use_database_statement: USE IDENTIFIER # UseDatabaseStatement;

// CTE & cursors
cte_statement:
	WITH cte_definition (COMMA cte_definition)* select_statement # CteStatementDef;

cte_definition:
	IDENTIFIER AS LPAREN select_statement RPAREN # CteDefinition;

cursor_statement:
	declare_cursor		# DeclareCursorStmt
	| open_cursor		# OpenCursorStmt
	| close_cursor		# CloseCursorStmt
	| deallocate_cursor	# DeallocateCursorStmt
	| fetch_cursor		# FetchCursorStmt;

declare_cursor:
	DECLARE IDENTIFIER CURSOR FOR select_statement # DeclareCursor;

open_cursor: OPEN IDENTIFIER # OpenCursor;

close_cursor: CLOSE IDENTIFIER # CloseCursor;

deallocate_cursor: DEALLOCATE IDENTIFIER # DeallocateCursor;

fetch_cursor: FETCH NEXT FROM IDENTIFIER # FetchCursor;

// WHERE, GROUP BY, etc.
where_clause: WHERE search_condition # WhereClause;

group_by_clause: GROUP BY expression_list # GroupByClause;

having_clause: HAVING search_condition # HavingClause;

order_by_clause:
	ORDER BY order_expression (COMMA order_expression)* # OrderByClause;

order_expression: expression (ASC | DESC)? # OrderExpression;

expression_list:
	expression (COMMA expression)* # ExpressionList;

search_condition: expression # SearchCondition;

// expressions – each alternative gets its own class
expression: logical_or_expression # ExpressionRoot;

logical_or_expression:
	logical_and_expression (OR logical_and_expression)* # OrExpression;

logical_and_expression:
	not_expression (AND not_expression)* # AndExpression;

not_expression:
	NOT not_expression		# NotExpression
	| predicate_expression	# PredicateExpressionWrapper;

predicate_expression:
	comparison_expression	# ComparisonPredicate
	| between_expression	# BetweenPredicate
	| in_expression			# InPredicate
	| like_expression		# LikePredicate
	| is_null_expression	# IsNullPredicate
	| exists_expression		# ExistsPredicate;

comparison_expression:
	additive_expression (
		(EQ | NOT_EQUAL | LT | LTE | GT | GTE) additive_expression
	)? # ComparisonExpression;

between_expression:
	additive_expression BETWEEN additive_expression AND additive_expression # BetweenExpression;

in_expression:
	additive_expression IN LPAREN expression_list RPAREN # InExpression;

like_expression:
	additive_expression LIKE additive_expression		# LikeExpression
	| additive_expression NOT LIKE additive_expression	# NotLikeExpression;

is_null_expression:
	additive_expression IS NULL			# IsNullExpression
	| additive_expression IS NOT NULL	# IsNotNullExpression;

exists_expression:
	EXISTS LPAREN select_statement RPAREN # ExistsExpression;

additive_expression:
	multiplicative_expression (
		(PLUS | MINUS) multiplicative_expression
	)* # AdditiveExpression;

multiplicative_expression:
	unary_expression ((STAR | SLASH) unary_expression)* # MultiplicativeExpression;

unary_expression:
	MINUS unary_expression	# UnaryMinusExpression
	| PLUS unary_expression	# UnaryPlusExpression
	| primary_expression	# PrimaryExpressionWrapper;

primary_expression:
	LPAREN expression RPAREN			# ParenthesizedExpression
	| LPAREN select_statement RPAREN	# SubqueryExpression
	| function_call						# FunctionCallExpression
	| case_expression					# CaseExpressionWrapper
	| literal_value						# LiteralExpression
	| column_name						# ColumnExpression;

case_expression:
	CASE expression? when_clause+ else_clause? END # CaseExpression;

when_clause: WHEN expression THEN expression # WhenClause;

else_clause: ELSE expression # ElseClause;

function_call: (IDENTIFIER | MAX | MIN | AVG | CONCAT_KW) LPAREN (
		expression_list
	)? RPAREN # FunctionCall;

column_name: (IDENTIFIER | BRACKET_ID) (
		DOT (IDENTIFIER | BRACKET_ID)
	)* # ColumnName;

literal_value:
	STRING					# StringLiteral
	| UNSIGNED_INTEGER		# IntegerLiteral
	| UNSIGNED_FLOAT		# FloatLiteral
	| UNSIGNED_FLOAT_SIMPLE	# SimpleFloatLiteral
	| NULL					# NullLiteral;