grammar evm;

program: statements EOF;

statements: statement+;

statement: variable_declartion | print_variable | if_statement |while_statement | for_statement | variable_assignment;

if_statement: 'if' '(' condition ')' block_statement;

while_statement: 'while' '(' condition ')' block_statement;

for_statement: 'for' '(' for_intialization ';' condition ';' for_increment ')' block_statement;

for_increment: id '++';

for_intialization: variable_declartion;


block_statement: '{' statements '}';

condition: bool | comparison_statement;

comparison_statement: (id | value) RELATIONAL_OPERATOR (id | value);

bool: 'True' | 'False';

variable_declartion: variable_type id '=' (value | expression);

variable_assignment: id '=' (value | expression);

variable_type: 'int' | 'float' | 'string';

expression: expression ('+'|'-') term | term;

term: term ('*'|'/') factor | factor;

factor: id | value | '(' expression ')';

id: ID;

print_variable: 'print' '(' (value|id) ')';

value: INT #int
 | FLOAT #float
  | STRING #string
  ;

INT: [0-9]+;

FLOAT: [0-9]* '.' [0-9]+;

STRING: '"'.*? '"';

RELATIONAL_OPERATOR: '>' | '>=' | '<' | '<=' | '==' ;
ID: ([a-zA-Z]|'_') [a-zA-Z0-9]*;

WS : [ \t] -> skip;

NEWLINE: [\n\r] ->skip;