grammar D96;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

// program: EOF;

// program: mptype 'main' LB RB LP body? RP EOF;

// mptype: INTTYPE | VOIDTYPE;

// body: funcall SEMI;

// exp: funcall | DEC;

// funcall: ID LB exp? RB;

// -----------start to code---------------

program: classdecls EOF;
classdecls: classdecl classdecls | classdecl;
classdecl: CLASS ID (superclass | ) LP (memberlist | ) RP;

superclass: COLON ID;

memberlist: member memberlist | member;
member: attr | method;

attr: attrtype idlist COLON typ (EQUAL exprlist | ) SEMI;
attrtype: VAL | VAR;

idlist: (STATIC | ID) COMMA idlist | (STATIC | ID);
typ: BOOLEAN | INTTYPE | FLOATTYPE | STRING | arrdecl | ID;

exprlist: expr COMMA exprlist | expr;
expr: exp1 (CONCAT | COMPARSTR) exp1 | exp1;
exp1: exp2 (COMPAR | NOTEQUAL | NOTSMALLER | NOTLARGER | LARGER | SMALLER) exp2 | exp2;
exp2: exp2 (AND | OR) exp3 | exp3;
exp3: exp3 (ADD | MINUS) exp4 | exp4;
exp4: exp4 (MULTI | DIV | PERCENT) exp5 | exp5;
exp5: NOT exp5 | exp6;
exp6: MINUS exp6 | exp7;
exp7: exp7 (LS | RS) | exp8; // này bị lỗi arr[x]
exp8: exp8 INSTANT exp9 | exp9;
exp9: exp9 STATICATTR exp9 | exp10;
exp10: NEW ID exp10 | exp11; // có $ không?
exp11: LB (expr | ) RB | NULL | INT | FLOAT | TRUE | FALSE | STR | ID | STATIC | multiarr | indexedarr | call | objcreate | SELF 
	 | imethodi | smethodi | instance | staatr | eleexp;

call: ID LB (exprlist | ) RB;

method: (CONSTRUCTOR | DESTRUCTOR | STATIC | ID) LB (paramlist | ) RB blockstate;

paramlist: param SEMI paramlist | param;
param: idlist COLON typ;

// idenlist: ID COMMA idenlist | ID;

blockstate: LP (statements | ) RP;
statements: sta statements | sta;
sta: attr | lhs | ifsta | forsta | breaksta | continuesta | returnsta | methodsta;
lhs: (eleexp | instance | staatr | ID | STATIC) EQUAL expr SEMI;

ifsta: IF LB expr RB blockstate (eliflist | ) (ELSE blockstate | );
eliflist: ELSEIF LB expr RB blockstate eliflist | ;

forsta: FOREACH LB (ID | STATIC) IN INT '..' INT ( BY INT | ) RB blockstate;

breaksta: BREAK SEMI;
continuesta: CONTINUE SEMI;
returnsta: RETURN expr SEMI;
methodsta: (smethodi | imethodi) SEMI;

indexedarr: ARRAY LB literals RB;
literals: lit COMMA literals | lit;
lit: INT | FLOAT | TRUE | FALSE | STR;

multiarr: ARRAY LB arrlist RB;
arrlist: arr COMMA arrlist | arr;
arr: multiarr | indexedarr;

arrdecl: ARRAY LS element COMMA size RS;
element: INTTYPE | FLOATTYPE | BOOLEAN | arrdecl | STRING;
size: INT; // > 1 chỉ là DEC thôi hay là tất cả?

eleexp: ID indexop;
indexop: LS expr RS | LS expr RS indexop;

instance: ID INSTANT ID;
staatr: ID STATICATTR STATIC;// nguy hiểm
imethodi: ID INSTANT ID LB (exprlist | ) RB;
smethodi: ID STATICATTR STATIC LB (exprlist | ) RB; // STATIC ?

objcreate: NEW ID LB (exprlist | ) RB;

// -----------end to code-----------------

// Keyword không nhận diện được khi ở chung với nhau ví dụ: BreakIf --> BreakIf
BREAK: 'Break'; 	CONTINUE: 'Continue'; 	IF: 'If'; 			ELSEIF: 'Elseif'; 	ELSE: 'Else';
FOREACH: 'Foreach'; TRUE: 'True'; 			FALSE: 'False'; 	ARRAY: 'Array'; 	IN: 'In';
INTTYPE: 'Int'; 	FLOATTYPE: 'Float'; 	BOOLEAN: 'Boolean'; STRING: 'String'; 	RETURN: 'Return';
NULL: 'Null'; 		CLASS: 'Class'; 		VAL: 'Val'; 		VAR: 'Var';
CONSTRUCTOR: 'Constructor'; 				DESTRUCTOR: 'Destructor';
NEW: 'New'; 		BY: 'By';				SELF: 'Self';

// operator
// nên test "!=!" để xem độ nhận diện trước sau
NOTEQUAL: '!='; 	NOTLARGER: '<=';NOTSMALLER: '>='; 	LARGER: '>'; 		SMALLER: '<';
COMPARSTR: '==.'; 	CONCAT: '+.'; 	INSTANT: '.'; 		STATICATTR: '::';	INDEXOPR: '->';
ADD: '+'; 			MINUS: '-'; 	MULTI: '*'; 		DIV: '/'; 			PERCENT: '%';
NOT: '!'; 			AND: '&&'; 		OR: '||'; 			COMPAR: '=='; 		EQUAL: '=';


STR: '"' (CHAR | ('\'"' CHAR* '\'"'))* '"' {self.text = self.text.replace('"', "")};


BLOCKCOMMENT: COMMENT (~[#])* ('#' | (~[#]))*? COMMENT -> skip;


// Identify có cần khác keyword không?
STATIC: '$' IDENTIFY;
ID: IDENTIFY;
fragment IDENTIFY: [a-zA-Z_] [a-zA-Z_0-9]*;

// Literals

// FLOAT
FLOAT: (DEC DECIMAL? EXPONENT | DEC DECIMAL | DECIMAL EXPONENT) {self.text = self.text.replace("_", "")};
fragment DECIMAL: '.' [0-9]*;
fragment EXPONENT: [eE] ('-' | '+')? [0-9]+;

// INTEGER

INT: (OCT | HEX | BIN | DEC) {self.text = self.text.replace("_", "")};
fragment OCT: '0' ([1-7] [_0-7]* | '0');
fragment HEX: '0' [xX] ([1-9A-Fa-f] [_0-9A-Fa-f]* | '0');
fragment BIN: '0' [bB] ('1' [_01]* | '0');
fragment DEC: [1-9] [0-9]* ('_' [0-9]*)* | '0';

// BOOLEAN

// ARRAY

// STRING

BACKSPACE: '\b';
FORMFEED: '\f';
CARRETURN: '\r';
NEWLINE: '\n';
HORTAB: '\t';
SINGQ: '\'';
BACKSLASH: '\\';
fragment ESC: '\\' [btnrf'\\];
// CHAR -> escape |  không chấp nhận các ký tự đặc biệt như backspace,
//  form feed, carriage return, horizontal tab,... 
// các ký tự trên chỉ có thể sử dụng dưới dạng escape sequence. | chấp nhận '
fragment CHAR: ESC | ~[\\"\b\t\n\r\f] | '\'';

// COMMENT

// SEPERATORS
LS: '[';

RS: ']';

LB: '(';

RB: ')';

LP: '{';

RP: '}';

SEMI: ';';

COMMA: ',';

COLON: ':';

fragment COMMENT: '##';

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines


ERROR_CHAR: .{raise ErrorToken(self.text)};
UNCLOSE_STRING: '"' (CHAR | ('\'"' CHAR* '\'"'))* {raise UncloseString(self.text.replace('"', ""))};
// ILLEGAL -> các kí tự \b\n\r\f\t\\ | các kí tự như \a\c\d\e = '\\' ~[bntrf\\]
ILLEGAL_ESCAPE: '"' CHAR* (~[\\"\b\t\n\r\f] | '\\' ~[bntrf\\]) {raise IllegalEscape(self.text.replace('"', ""))};
