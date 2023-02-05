grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}
// EBNF: + * ?
// program: (vardecl | funcdecl)+ EOF;

// ----------------------

// vardecl: typ (ID (CM ID)*) SM;
// typ: INT | FLOAT;

// funcdecl: typ ID parameter body;

// -----------------------
// BNF
program: decls EOF;
decls: decl decls | decl;
decl: vardecl | funcdecl;


// vardecl: 'vardecl' ;
vardecl: typ idlist SM;
typ: (INT | FLOAT);
idlist : ID CM idlist | ID;
// funcdecl: 'funcdecl' ;
funcdecl: typ ID LB paramlist RB LC body RC;
paramlist: parameter | ;
parameter: param SM parameter | param;
param: typ idlist;

body: main body | main | ;
main: vardecl | statement SM;
statement: assign | call | returnSta;
assign: ID EQUAL expr;
call: ID LB (exprlist | ) RB;
exprlist: expr CM exprlist | expr;
returnSta: RETURN expr;

expr: operand operator expr | operand;
operand: INTLIT | FLOATLIT | ID | call | subexp;
subexp: RB expr LB;
operator: ADD | MINUS | MULTI | DIV;

RETURN: 'return';
EQUAL: '=';
ADD: '+';
MINUS: '-';
MULTI: '*';
DIV: '/';
fragment NAT: [1-9] [0-9]* | '0';
fragment FRAC: '.' [0-9]+;
FLOATLIT: NAT FRAC;
INTLIT: NAT;
LC: '{'; RC: '}';
INT: 'int';
FLOAT: 'float';
LB: '('; RB: ')';
ID: [a-zA-Z]+;
SM: ';';
CM: ',';
WS: [ \t\r\n] -> skip;

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;