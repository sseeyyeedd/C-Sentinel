grammar CSentinel;

senFile: rule* EOF;

rule: RULE_KEYWORD ID LBRACE (blockRule | onRule | sourceRule | sinkRule | sanitizerRule)* RBRACE;

blockRule: BLOCK_KEYWORD ID LBRACE action RBRACE;

onRule: ON_KEYWORD CALL_KEYWORD ID LPAREN (ID (COMMA ID)*)? RPAREN LBRACE (ifStmt | requireLiteralStmt | requireNullStmt | requireNoDoubleFreeStmt | action)* RBRACE;

requireLiteralStmt: REQUIRE_LITERAL_FORMAT_KEYWORD LBRACE action RBRACE;

requireNullStmt: REQUIRE_NULL_AFTER_KEYWORD LBRACE action RBRACE;

requireNoDoubleFreeStmt: REQUIRE_NO_DOUBLE_FREE_KEYWORD LBRACE action RBRACE;

ifStmt: IF_KEYWORD expr OVERFLOWS_KEYWORD LBRACE action RBRACE;

sourceRule: SOURCE_KEYWORD ID LBRACE action RBRACE;

sinkRule: SINK_KEYWORD ID LBRACE action RBRACE;

sanitizerRule: SANITIZER_KEYWORD ID LBRACE RBRACE;

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
SOURCE_KEYWORD: 'source';
SINK_KEYWORD: 'sink';
SANITIZER_KEYWORD: 'sanitizer';
NUMBER : [0-9]+;
ID: [a-zA-Z_][a-zA-Z0-9_]*;
STRING: '"' (~["\r\n])* '"';
WS: [ \t\r\n]+ -> skip;