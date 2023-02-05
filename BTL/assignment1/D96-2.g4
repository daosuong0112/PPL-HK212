grammar D96;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

// program: mptype 'main' LB RB LP body? RP EOF; mptype: INTTYPE | VOIDTYPE; body: funcall SEMI;
// exp: funcall | INTLIT; funcall: ID LB exp? RB; INTTYPE: 'int'; VOIDTYPE: 'void'; ID: [a-zA-Z]+;
// INTLIT: [0-9]+; LB: '('; RB: ')'; LP: '{'; RP: '}'; SEMI: ';';

// program = classdecls (nhieu khai bao class) + programclass (class program)


program: classdecls EOF;
classdecls
	: classdecl classdecls
	| classdecl;


// // // xoabegin  ====================================================
// program: programunits EOF;
// programunits
// 	: programunit programunits
// 	| programunit ;
// programunit
// 	: classdecl
// 	// |COMMENT
// 	;
// // // xoaend==========================================================

// classdecl
// 	: CLASS CLASSNAME (COLON CLASSNAME)? LB classbody  RB;

classdecl: CLASS IDENTIFIER parentclassname LB classbody RB;

parentclassname: (COLON IDENTIFIER)| ;


classbody: classelements| ;

classelements: classelement classelements| classelement;

// class element = vardecl or functiondecl
// classelement: attributedecl|methoddecl;
classelement: attributedecl|norm_methoddecl;

// khai báo hàm
//funcname:STATIC_IDENTIFIER|IDENTIFIER;
// methoddecl:norm_methoddecl|constructor_methoddecl|destructor_methoddecl;
norm_methoddecl
	:(STATIC_IDENTIFIER|IDENTIFIER) LP paramlist RP LB normal_functionbody RB;
// constructor_methoddecl:CONSTRUCTOR_KEY LP paramlist RP LB con_des_functionbody RB;
// destructor_methoddecl:DESTRUCTOR_KEY LP RP LB con_des_functionbody RB;

normal_functionbody: normbodystmts| ;
normbodystmts
	:normbodystmt normbodystmts
	|normbodystmt;

// normbodystmt: funcvardecl
// 	|assign_stmt
// 	| if_stmt
// 	| for_stmt
// 	| expr SM
// 	| COMMENT
// 	| block_stmts
// 	| return_stmt;
normbodystmt
	:vardecl_in_function_stmt
	|assign_stmt
	;

vardecl_in_function_stmt: var_key_dec var_list COLON var_typ_and_inital SM;
// con_des_functionbody: stmts| ;
stmts: stmt stmts| stmt;
stmt: funcvardecl
	|assign_stmt
	| if_stmt
	| for_stmt
	| expr SM
	| COMMENT
	| block_stmts
	;



paramlist: paramlsts| ;
paramlsts:paralst SM paramlsts| paralst;
paralst: IDENTIFIER( CM IDENTIFIER)* COLON paramtyp;
paramtyp:primityp|arrtyp|IDENTIFIER;	//
primityp
	:'Boolean'
	|'Int'
	|'Float'
	|'String';
arrtyp
	:index_arr_typ
	|multi_dimension_arr_typ;
// functionbody :'functionbody'| ;

// khai báo bien
// attributedecl: var_key_dec attribute_list COLON var_typ_and_inital SM;

attributedecl
	: var_key_dec attribute_list COLON var_typ SM
	| var_key_dec attribute_eq_value SM
	;
attribute_eq_value	
	: attibute_name COLON var_typ EQUALSIGN attribute_inital_value
	|   attibute_name  CM attribute_eq_value CM attribute_inital_value
	;
attribute_inital_value
	:integer_literal
	|FLOAT_LITERAL
	|BOOLEAN_LITERAL
	| STRING_LITERAL
	|IDENTIFIER
	|STATIC_IDENTIFIER
	|expr
	|index_array_int_literal
	|index_array_bool_literal
	|index_array_float_literal
	|index_array_string_literal
	|multi_dimension_array_literal
	|expr10
	;
var_typ
	:primityp
	|index_arr_typ
	|multi_dimension_arr_typ
	|IDENTIFIER
	;


















funcvardecl: var_key_dec var_list COLON var_typ_and_inital SM;



var_key_dec
	: VAR
	| VAL;

attribute_list: attibute_name CM attribute_list| attibute_name;
var_list:IDENTIFIER CM var_list| IDENTIFIER;
attibute_name: IDENTIFIER|STATIC_IDENTIFIER;

var_typ_and_inital: primitive_typ_and_inital| array_typ_and_inital|class_typ_and_inital;// array_typ_and_inital;

// lenh gan gia tri
assign_stmt: assign_lhs EQUALSIGN expr SM;
assign_lhs
	:IDENTIFIER
	|STATIC_IDENTIFIER
	|expr7
	// |SELF DOT_OP IDENTIFIER
	// |IDENTIFIER DOT_OP IDENTIFIER
	// |SELF STATIC_ACCESS IDENTIFIER
	// |IDENTIFIER STATIC_ACCESS STATIC_IDENTIFIER
	// |array_element
	;

// array_element:expr7;
if_stmt: if_clause (elseif_clause)* (else_clause)?;
if_clause: IF bool_expr if_block_statment;
elseif_clause:ELSEIF bool_expr if_block_statment;
else_clause: ELSE if_block_statment;


bool_expr: LP expr RP;
if_block_statment: LB loopsmt* RB;

loops: for_stmt loops| for_stmt;
for_stmt: FOR LP assign_lhs IN integer_literal RANGE_OP integer_literal (BY integer_literal)?  RP LB loopsmt* RB;
loopsmt: stmt| BREAK SM| CONTINUE SM;

return_stmt:RETURN expr SM;

block_stmts: LB stmt* RB;
// expression:
expr
	: operand1 str_op operand1
	|expr1;
operand1
	:expr1|STRING_LITERAL
	;


expr1
	:operand2_1 (EQ_COMP_OP|DIFF_COMP_OP) operand2_1
	|operand2_2(SMALL_COMP_OP|LARGE_COMP_OP|SMALL_EQ_COMP_OP|LARGE_EQ_COMP_OP)  operand2_2
	|expr2;

operand2_1:expr2|integer_literal|BOOLEAN_LITERAL;
operand2_2:expr2|FLOAT_LITERAL|integer_literal;
expr2
	: expr2 logic_op operand3
	| BOOLEAN_LITERAL logic_op operand3
	|expr3
	;
operand3:expr3|BOOLEAN_LITERAL;

expr3
	: expr3 add_sub_op operand4_2
	| operand4_1 add_sub_op operand4_2
	|expr4;

operand4_1:integer_literal|FLOAT_LITERAL;
operand4_2:operand4_1|expr4;

expr4
	:expr4 (MUL_OP|DIV_OP) operand5_1
	|expr4 MODULO_OP operand5_2
	|operand4_1 (MUL_OP|DIV_OP) operand5_1
	|operand5_2 MODULO_OP operand5_2
	|expr5
	;
	// :expr4 mul_divs_op expr5
	// |operand4_1 (MUL_OP|DIV_OP) operand5_1
	// |integer_literal MODULO_OP operand5_2
	// |expr5;
operand5_1:operand4_1|expr5;
operand5_2:integer_literal|expr5;
expr5
	: NOT_OP expr5
	| NOT_OP BOOLEAN_LITERAL
	|expr6 ;

expr6
	: SUB_OP expr6
	| SUB_OP operand4_1
	|expr7;

expr7
	: expr7 index_op_arr
	| expr8 ;

index_op_arr
	: LSB (expr|integer_literal) RSB index_op_arr
	| LSB (expr|integer_literal) RSB
	;

expr8
	:expr8 DOT_OP expr9
	| SELF DOT_OP expr9
	|expr9;

expr9
	:class_name_ref STATIC_ACCESS STATIC_IDENTIFIER
	|class_name_ref STATIC_ACCESS call_static_function
	|expr10
	;

class_name_ref
	:IDENTIFIER
	|SELF
	;

call_static_function
	:STATIC_IDENTIFIER LP arg_list RP
	;

expr10
	: NEW_OP call_function
	|expr11
	;

expr11
	: LP expr RP
	|expr12
	;

expr12
	: operand
	;

operand
	: IDENTIFIER
	// | STATIC_IDENTIFIER
	// | integer_literal
	// | FLOAT_LITERAL
	// | BOOLEAN_LITERAL
	// |STRING_LITERAL
	| call_function
	// |SELF
	;

// call_function:(STATIC_IDENTIFIER| IDENTIFIER) LP (expr(CM expr)*)* RP;
call_function: IDENTIFIER LP arg_list RP;
arg_list:args| ;
args: arg CM args
	|arg;

arg	: expr 
	| integer_literal
	|FLOAT_LITERAL
	|BOOLEAN_LITERAL
	|STRING_LITERAL
	;



str_op:(STR_COMP_OP| STR_CONCAT_OP);
comp_op:(EQ_COMP_OP|DIFF_COMP_OP|SMALL_COMP_OP|LARGE_COMP_OP|SMALL_EQ_COMP_OP|LARGE_EQ_COMP_OP);
logic_op:AND_LOGIC_OP|OR_LOGIC_OP;
add_sub_op:(ADD_OP|SUB_OP);
mul_divs_op:MUL_OP|DIV_OP|MODULO_OP;
// array type and array value=================================================================
	array_typ_and_inital:arr_index_inital|arr_multi_dimension_inital;

		// array multi inital list==========================================================
			arr_multi_dimension_inital
				:multi_dimension_arr_typ arr_multi_dimension_initals;

			arr_multi_dimension_initals
				: EQUALSIGN arr_multi_dimension_initals_values| ;

			arr_multi_dimension_initals_values
				: multi_dimension_array_literal CM arr_multi_dimension_initals_values 
				| multi_dimension_array_literal;

			// arr multi dimesion typ=======================================================
				multi_dimension_arr_typ: ARRAY LSB multi_dimension_arr_elem_typ CM integer_literal RSB;
				// multi_dimension_arr_elems_typ: (multi_dimension_arr_elem_typ) multi_dimension_arr_elems_typ;
				multi_dimension_arr_elem_typ: multi_dimension_arr_typ|index_arr_typ; 
			//=============================================================================


		

		// ========================================================================


		// array index inital list
			arr_index_inital
				:arr_index_int_list_inital
				|arr_index_bool_list_inital
				|arr_index_float_list_inital
				|arr_index_string_list_inital;

			// index array==============================================================

			index_arr_typ
				:index_arr_int_typ
				|index_arr_bool_typ
				|index_arr_float_typ
				|index_arr_string_typ;

				// index arr typ=======================================
				index_arr_int_typ: ARRAY LSB INT_TYP CM integer_literal RSB;
				index_arr_bool_typ: ARRAY LSB BOOLEAN_TYP CM integer_literal RSB;
				index_arr_float_typ: ARRAY LSB FLOAT_TYP CM integer_literal RSB;
				index_arr_string_typ:ARRAY LSB STRING_TYP CM integer_literal RSB;
				//=========================================================

				// index arr int value ================================================
				arr_index_int_list_inital: index_arr_int_typ arr_index_int_initals;
				arr_index_int_initals: EQUALSIGN arr_index_int_initals_values| ;
				arr_index_int_initals_values:index_array_int_literal CM arr_index_int_initals_values| index_array_int_literal;
				// ====================================================================

			
				// index arr bool value ================================================
				arr_index_bool_list_inital: index_arr_bool_typ arr_index_bool_initals;
				arr_index_bool_initals: EQUALSIGN arr_index_bool_initals_values| ;
				arr_index_bool_initals_values:index_array_bool_literal CM arr_index_bool_initals_values| index_array_bool_literal;
				// =======================================================================

				// index arr bool value ================================================
				arr_index_float_list_inital: index_arr_float_typ arr_index_float_initals;
				arr_index_float_initals: EQUALSIGN arr_index_float_initals_values| ;
				arr_index_float_initals_values:index_array_float_literal CM arr_index_float_initals_values| index_array_float_literal;
				// ==============================================================

			
				// index arr string value ================================================
				arr_index_string_list_inital: index_arr_string_typ arr_index_string_initals;
				arr_index_string_initals: EQUALSIGN arr_index_string_initals_values| ;
				arr_index_string_initals_values:index_array_string_literal CM arr_index_string_initals_values| index_array_string_literal;
				// ======================================================================


			//================================================================================================================

// ======================================================================


class_typ_and_inital:
	IDENTIFIER class_typ_values;
class_typ_values:EQUALSIGN class_typ_inits| ;
class_typ_inits: expr10 CM class_typ_inits|expr10;

primitive_typ_and_inital
	: attribute_int_list_intial
	| attribute_bool_list_intial
	| attribute_float_list_intial
	| attribute_string_list_intial ;

		// int intial list_intial
		attribute_int_list_intial: INT_TYP int_values_inital;

		int_values_inital: EQUALSIGN int_values_init| ;

		int_values_init: int_value_init CM int_values_init | int_value_init;

		int_value_init: IDENTIFIER|STATIC_IDENTIFIER|integer_literal|expr; // insert int expresion


		// bool intial list_intial
		attribute_bool_list_intial: BOOLEAN_TYP bool_values_inital; 

		bool_values_inital: EQUALSIGN bool_values_init| ;

		bool_values_init: bool_value_init CM bool_values_init | bool_value_init;

		bool_value_init	: IDENTIFIER| STATIC_IDENTIFIER	| BOOLEAN_LITERAL|expr; // insert bool expresion

		// float intial list_intial
		attribute_float_list_intial: FLOAT_TYP float_values_inital;

		float_values_inital: EQUALSIGN float_values_init| ;

		float_values_init: float_value_init CM float_values_init | float_value_init;

		float_value_init: IDENTIFIER|STATIC_IDENTIFIER|FLOAT_LITERAL|expr; // insert float expresion


		// string intial list_intial
		attribute_string_list_intial: STRING_TYP string_values_inital;

		string_values_inital: EQUALSIGN string_values_init| ;

		string_values_init: string_value_init CM string_values_init | string_value_init;

		string_value_init: IDENTIFIER|STATIC_IDENTIFIER|STRING_LITERAL|expr; // insert string expresion


// integer literal
integer_literal
	: INTEGER_LITERAL_X10
	| INTEGER_LITERAL_X16
	| INTEGER_LITERAL_X8
	| INTEGER_LITERAL_X2
	;


// token Literals
//integer Literals
// INTEGER_LITERAL: INTEGER_LITERAL_X10 {self.text=self.text.replace("_","")}
// 	|INTEGER_LITERAL_X16 {self.text=self.text.replace("_","")}
// 	|INTEGER_LITERAL_X8 {self.text=self.text.replace("_","")}
// 	|INTEGER_LITERAL_X2 {self.text=self.text.replace("_","")};
	//base 10
INTEGER_LITERAL_X10
	: [1-9] NUMBERDIGIT* ('_'NUMBERDIGIT+)* {self.text=self.text.replace("_","")}
	|'0' ;

	//base 16
INTEGER_LITERAL_X16
	:('0x'|'0X')[1-9A-F] X16DIGIT* ('_' X16DIGIT+)* { self.text=self.text.replace("_","") }
	|('0x0'|'0X0');
	
	//base 8
INTEGER_LITERAL_X8
	:'0'[1-7] X8DIGIT* ('_'X8DIGIT+)* { self.text=self.text.replace("_","") }
	|('00');
	
	//base 2
INTEGER_LITERAL_X2
	:('0b'|'0B')'1' X2DIGIT* ('_'X2DIGIT+)* { self.text=self.text.replace("_","") }
	|('0b0'|'0B0');

fragment NUMBERDIGIT:[0-9];
fragment X16DIGIT:[0-9A-F];
fragment X8DIGIT:[0-7];
fragment X2DIGIT:[0-1];

//float Literals
FLOAT_LITERAL
	: FLOAT_INT_COMPO FLOAT_DECIMAL_COMPO { self.text=self.text.replace("_","") }
	| FLOAT_INT_COMPO FLOAT_EXPO_COMPO { self.text=self.text.replace("_","") }
	| FLOAT_DECIMAL_COMPO FLOAT_EXPO_COMPO
	| FLOAT_INT_COMPO FLOAT_DECIMAL_COMPO FLOAT_EXPO_COMPO { self.text=self.text.replace("_","") };
	
fragment FLOAT_INT_COMPO: [1-9] NUMBERDIGIT* ('_'NUMBERDIGIT+)* |'0' ;
fragment FLOAT_DECIMAL_COMPO: '.'NUMBERDIGIT*;
fragment FLOAT_EXPO_COMPO: [eE] [-+]? NUMBERDIGIT+;

COMMENT: ('##' (.)*? '##') -> skip;

//boolean Literals
BOOLEAN_LITERAL
	: 'True'
	| 'False'
	;

// string Literals
STRING_LITERAL
	: '"' CHARACTER* '"'
	{
		inputstr=str(self.text)
		self.text=inputstr[1:-1]
	}
	;

fragment CHARACTER
	: ~[\b\f\r\n\t"'\\]|ESCAPE_CHAR|DOUBLE_QUOTE_IN_STRING
	;

fragment ESCAPE_CHAR
	: '\\' [bfrnt'\\]
	;

fragment DOUBLE_QUOTE_IN_STRING
	:'\'"'
	;

fragment ESCAPE_CHAR_ILEGAL
	: '\\' ~[bfrnt'\\] 
	| ~'\\'
	;

		

	//==========================================================================================================================================
															// STRING_LITERAL
															// 	:'"' CHARACTER* '"'
															// 	{
															// 		inputstr=str(self.text)
															// 		self.text=inputstr[1:-1]
															// 	}
															// 	;

															// fragment CHARACTER
															// :  ~[\b\t\n\f\r"'\\]
															// |ESCAPE_CHAR
															// ;
															// // fragment ESCAPE_CHAR: ('\\b'|'\\f'|'\\r'|'\\n'|'\\t'|'\\\''|'\\\\');
															
															// fragment ESCAPE_CHAR: '\\' [btnfr'\\]|'\'"' ;
															// // fragment ESCAPE_CHAR_ILEGAL: '\\'~[bfrnt"'\\]  ~'\\' ;
															// fragment ESCAPE_CHAR_ILEGAL: '\\' ~[btnfr'\\] | ~'\\' ;
															// 	// 		fragment
															// 	// ESC : '\\"' | '\\\\' ; // 2-char sequences \" and \\

	//==========================================================================================================================================

// array Literals
// index_array_literal:;
index_array_literal:index_array_int_literal| index_array_bool_literal| index_array_string_literal| index_array_float_literal;

index_array_int_literal: ARRAY LP int_values_init RP;	
index_array_bool_literal: ARRAY LP bool_values_init RP;	
index_array_string_literal: ARRAY LP string_values_init RP;	
index_array_float_literal: ARRAY LP float_values_init RP;

// multi_dimension_array_literal
multi_dimension_array_literal: ARRAY LP elements_multi_dimension_arr RP;
elements_multi_dimension_arr: elem_multi_dimension_arr CM elements_multi_dimension_arr| elem_multi_dimension_arr;
elem_multi_dimension_arr: multi_dimension_array_literal| index_array_literal;

CLASS:'Class';
ARRAY:'Array';
VAR:'Var';
VAL:'Val';
LP:'(';
RP:')';
LB:'{';
RB:'}';
LSB:'[';
RSB:']';
SM:';';
CM:',';
SELF:'Self';
IF:'If';
IN:'In';
BY:'By';
FOR:'Foreach';
ELSEIF:'Elseif';
ELSE:'Else';
BREAK:'Break';
RANGE_OP:'..';
CONTINUE:'Continue';
COLON:':';
RETURN: 'Return';
EQUALSIGN:'=';
STR_COMP_OP:'==.';
STR_CONCAT_OP:'+.';
EQ_COMP_OP:'==';
DIFF_COMP_OP:'!=';
SMALL_COMP_OP:'<';
LARGE_COMP_OP:'>';
SMALL_EQ_COMP_OP:'<=';
LARGE_EQ_COMP_OP:'>=';
AND_LOGIC_OP:'&&';
OR_LOGIC_OP:'||';
ADD_OP:'+';
SUB_OP:'-';
MUL_OP:'*';
DIV_OP:'/';
MODULO_OP:'%';
NOT_OP:'!';
DOT_OP:'.';
STATIC_ACCESS:'::';
NEW_OP:'New';
BOOLEAN_TYP:'Boolean';
INT_TYP:'Int';
FLOAT_TYP:'Float';
STRING_TYP:'String';
CONSTRUCTOR_KEY:'Constructor';
DESTRUCTOR_KEY:'Destructor';
IDENTIFIER:([A-Za-z]|'_')+ ([A-Za-z0-9]|'_')* ;
fragment DOLAR_SIGN:'$';
STATIC_IDENTIFIER: DOLAR_SIGN [A-Za-z_]+ [A-Za-z_0-9]* ;



WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines


// UNCLOSE_STRING
// 	: '"' CHARACTER* END_A_LINE_SIGN
// 	{
// 		unclose_string = str(self.text)
// 		end_sign=['\b', '\t', '\n', '\f', '\r', '"', "'", '\\']
// 		i=len(a)
// 		if unclose_string[i-1] in end_sign:
// 			raise UncloseString(unclose_string[1:-1])
// 		else:
// 			raise UncloseString(unclose_string[1:])
// 	}
// 	;
UNCLOSE_STRING
	: '"' CHARACTER* END_A_LINE_SIGN 
	{ 
		unclose_str=str(self.text)
		raise UncloseString(unclose_str[1:])
	};

fragment END_A_LINE_SIGN
	: [\b\t\n\f\r"'\\] | EOF
	;

ILLEGAL_ESCAPE
	: '"' CHARACTER* ESCAPE_CHAR_ILEGAL
	{
		ilegal = str(self.text)
		raise IllegalEscape(ilegal[1:])
	}
	;

ERROR_CHAR: .
	{
		raise ErrorToken(self.text)
	}
	;