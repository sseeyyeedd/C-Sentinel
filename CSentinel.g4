grammar CSentinel;

senFile: rule* EOF;

rule: RULE_KEYWORD ID LBRACE (blockRule | onRule | onAccessRule | sourceRule | sinkRule | sanitizerRule)* RBRACE;

blockRule: BLOCK_KEYWORD ID LBRACE action RBRACE;

onRule: ON_KEYWORD CALL_KEYWORD ID LPAREN (ID (COMMA ID)*)? RPAREN LBRACE (ifStmt | requireLiteralStmt | requireNullStmt | requireNoDoubleFreeStmt | requireAutoFreeUnusedStmt | action)* RBRACE;

requireLiteralStmt: REQUIRE_LITERAL_FORMAT_KEYWORD LBRACE action RBRACE;

requireNullStmt: REQUIRE_NULL_AFTER_KEYWORD LBRACE action RBRACE;

requireNoDoubleFreeStmt: REQUIRE_NO_DOUBLE_FREE_KEYWORD LBRACE action RBRACE;

requireAutoFreeUnusedStmt: REQUIRE_AUTO_FREE_UNUSED_KEYWORD LBRACE action RBRACE;

requireNotNullStmt: REQUIRE_NOT_NULL_KEYWORD LBRACE action RBRACE;

ifStmt: IF_KEYWORD expr OVERFLOWS_KEYWORD LBRACE action RBRACE;

sourceRule: SOURCE_KEYWORD ID LBRACE action RBRACE;

sinkRule: SINK_KEYWORD ID LBRACE action RBRACE;

sanitizerRule: SANITIZER_KEYWORD ID LBRACE RBRACE;

onAccessRule: ON_KEYWORD ACCESS_KEYWORD ID LBRACE requireNotNullStmt RBRACE;

expr: term ((PLUS | MINUS) term)*;

term: factor ((STAR | DIV) factor)*;

factor: LPAREN expr RPAREN | ID | NUMBER;

action: ERROR_KEYWORD STRING;

RULE_KEYWORD: 'rule';
BLOCK_KEYWORD: 'block';
ON_KEYWORD: 'on';
CALL_KEYWORD: 'call';
IF_KEYWORD: 'if';
OVERFLOWS_KEYWORD: 'overflows';
ERROR_KEYWORD: 'error';
LBRACE: '{';
RBRACE: '}';
LPAREN: '(';
RPAREN: ')';
COMMA: ',';
PLUS: '+';
MINUS: '-';
STAR: '*';
DIV: '/';
REQUIRE_LITERAL_FORMAT_KEYWORD: 'require_literal_format';
REQUIRE_NULL_AFTER_KEYWORD: 'require_null_after';
REQUIRE_NO_DOUBLE_FREE_KEYWORD: 'require_no_double_free';
REQUIRE_AUTO_FREE_UNUSED_KEYWORD: 'require_auto_free_unused';
SOURCE_KEYWORD: 'source';
SINK_KEYWORD: 'sink';
SANITIZER_KEYWORD: 'sanitizer';
ACCESS_KEYWORD: 'access';
REQUIRE_NOT_NULL_KEYWORD: 'require_not_null';
NUMBER : [0-9]+;
ID: [a-zA-Z_][a-zA-Z0-9_]*;
STRING: '"' (~["\r\n])* '"';
WS: [ \t\r\n]+ -> skip;