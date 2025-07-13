grammar CSentinel;

senFile: rule* EOF;

rule: RULE_KEYWORD ID LBRACE (blockRule | onRule)* RBRACE;

blockRule: BLOCK_KEYWORD ID LBRACE action RBRACE;

onRule: ON_KEYWORD CALL_KEYWORD LPAREN ID (COMMA ID)* RPAREN LBRACE (ifStmt | action)* RBRACE;

ifStmt: IF_KEYWORD expr OVERFLOWS_KEYWORD LBRACE action RBRACE;

expr: ID PLUS ID;

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

ID: [a-zA-Z_][a-zA-Z0-9_]*;
STRING: '"' (~["\r\n])* '"';
WS: [ \t\r\n]+ -> skip;