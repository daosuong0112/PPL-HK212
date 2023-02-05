
"""
 * @author nhphung
"""

from AST import * 
from Visitor import *
from StaticError import *

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

class StaticChecker(BaseVisitor):

    global_envi = [
    Symbol("getInt",MType([],IntType())),
    Symbol("putIntLn",MType([IntType()],VoidType()))
    ]
            
    global_env = {}

    def __init__(self,ast):
        self.ast = ast

 
    
    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)

    # Class Program: 
    #   decl: List[ClassDecl]
    def visitProgram(self,ast:Program, c): 
        c = {}
        is_main = False
        for decl in ast.decl:
            if decl.classname.name == "Program":
                for mem in decl.memlist:
                    if isinstance(mem, MethodDecl) and mem.name.name == "main":
                        is_main = True
                        break
            else:
                is_main = True
                break
        if not is_main:
            raise NoEntryPoint()
        for decl in ast.decl: 
            self.visit(decl, c)
            self.global_env.update(c)

    # class ClassDecl(Decl):
    #   classname: Id
    #   memlist: List[MemDecl]
    #   parentname: Id = None  # None if there is no parent
    def visitClassDecl(self, ast:ClassDecl, c):
        # --- CLASS/STATIC METHOD DECLARE WITH THE SAME NAME ---
        if ast.classname.name in list(c.keys()):
            raise Redeclared(Class(), ast.classname.name)
        memdecls = {}
        if ast.parentname:
            # if this class is a child, update its memlist by its parent memlist
            if ast.parentname.name in list(c.keys()):
                memdecls = dict(c[ast.parentname.name][1], **memdecls)
            else:
                raise Undeclared(Class(), ast.parentname.name)
        for mem in ast.memlist: self.visit(mem, memdecls)
        if ast.parentname: c[ast.classname.name] = (ast.parentname.name, memdecls)
        else: c[ast.classname.name] = ("", memdecls)

    # class MethodDecl(MemDecl): # only INSTANCE
    #   kind: SIKind
    #   name: Id
    #   param: List[VarDecl]
    #   body: Block
    def visitMethodDecl(self, ast: MethodDecl, c):
        # ------------------------PROBLEM----------------------------------
        # --- METHOD and CLASS and ATTRIBUTE DECLARE WITH THE SAME NAME ---
        # -----------------------------------------------------------------
        if ast.name.name in list(c.keys()):
            raise Redeclared(Method(), ast.name.name)
        param = {}
        for para in ast.param: 
            if para.variable in list(param.keys()):
                raise Redeclared(Parameter(), para.variable.name)
            else:
                self.visit(para, param)
        retType = VoidType
        in_loop = False
        body = c
        body["local"] = param
        self.visit(ast.body, (body, in_loop, retType))
        c[ast.name.name] = (param, retType)

    # class AttributeDecl(MemDecl):
    #   kind: SIKind  # Instance or Static
    #   decl: StoreDecl  # VarDecl for mutable or ConstDecl for immutable
    def visitAttributeDecl(self, ast: AttributeDecl, c):
        if isinstance(ast.decl, VarDecl) and ast.decl.variable.name in list(c.keys()):
            raise Redeclared(Attribute(), ast.decl.variable.name)
        if isinstance(ast.decl, ConstDecl) and ast.decl.constant.name in list(c.keys()):
            raise Redeclared(Attribute(), ast.decl.constant.name)
        self.visit(ast.decl, c)

    # class VarDecl(StoreDecl):
    #   variable: Id
    #   varType: Type
    #   varInit: Expr = None  # None if there is no initial
    def visitVarDecl(self, ast: VarDecl, c):
        if isinstance(c, Tuple) and "local" in list(c[0].keys()) and ast.variable.name in list(c[0]["local"].keys()):
            raise Redeclared(Variable(), ast.variable.name)
        varType = self.visit(ast.varType, c)
        varInit = self.visit(ast.varInit, c)
        if isinstance(varType, type(varInit)):
            if isinstance(varType, IntType) and isinstance(varInit, FloatType):
                raise TypeMismatchInStatement(Assign(ast.variable, ast.varInit))
            else:
                varInit = varType
        if isinstance(c, Tuple) and "local" in list(c[0].keys()):
            c[0]["local"][ast.variable.name] = ("Var", varType)
        else:
            c[ast.variable.name] = ("Var", varType)

    # class ConstDecl(StoreDecl):
    #   constant: Id
    #   constType: Type
    #   value: Expr = None # None if there is no initial
    def visitConstDecl(self, ast: ConstDecl, c):
        
        if isinstance(c, Tuple) and "local" in list(c[0].keys()) and ast.constant.name in list(c[0]["local"].keys()):
            raise Redeclared(Variable(), ast.constant.name)
        if not ast.value:
            raise IllegalConstantExpression(None)
        constType = self.visit(ast.constType, c)
        value = self.visit(ast.value, c)
        if isinstance(constType, type(value)):
            if isinstance(constType, IntType) and isinstance(constType, FloatType):
                raise TypeMismatchInConstant(Assign(ast.constant, ast.value))
            else:
                value = constType      
        if isinstance(c, Tuple) and "local" in list(c[0].keys()):
            c[0]["local"][ast.constant.name] = ("Const", constType)
        else:
            c[ast.constant.name] = ("Const", constType)

    # class Block(Stmt):    # only INSTANCE
    #   inst: List[Inst]
    def visitBlock(self, ast: Block, c):
        is_return = False
        for inst in ast.inst: 
            if self.visit(inst, c):
                is_return = True
        return is_return

    # class Assign(Stmt):
    #   lhs: Expr
    #   exp: Expr
    def visitAssign(self, ast: Assign, c):
        lhs = self.visit(ast.lhs, c[0])
        if isinstance(lhs, Id):
            if c[0][lhs][0] == "Const" or c[0]["local"][lhs][0] == "Const":
                raise CannotAssignToConstant(ast)
        if isinstance(lhs, VoidType):
            raise TypeMismatchInStatement(ast)
        exp = self.visit(ast.exp, c[0])   
        if isinstance(lhs, ArrayType):
            if not isinstance(exp, ArrayType):
                raise TypeMismatchInStatement(ast)
            else:
                if lhs.size != exp.size:
                    raise TypeMismatchInStatement(ast)
                elif lhs.eleType != exp.eleType:
                    if not isinstance(lhs.eleType, FloatType) and not isinstance(exp.eleType, IntType):
                        raise TypeMismatchInStatement(ast)
        elif not isinstance(lhs, type(exp)):
            if isinstance(lhs, FloatType) and isinstance(exp, IntType):
                exp = lhs
                if isinstance(ast.exp, Id):
                    if ast.exp.name in list(c.keys()):
                        c[0][ast.exp.name][1] = lhs
                    else:
                        c[0]["local"][ast.exp.name][1] = lhs
            else:
                raise TypeMismatchInStatement(ast)
            

    # class If(Stmt):
    #   expr: Expr
    #   thenStmt: Stmt
    #   elseStmt: Stmt = None  # None if there is no else branch
    def visitIf(self, ast: If, c):
        expr = self.visit(ast.expr, c[0])
        if not isinstance(expr, BoolType):
            raise TypeMismatchInStatement(ast)
        retIf = True
        retElse = True
        if isinstance(ast.thenStmt, (Return, Block, If)):
            retIf = self.visit(ast.thenStmt, c)
        else:
            if isinstance(ast.thenStmt, (For, Break, Continue, CallStmt, Assign)):
                self.visit(ast.thenStmt, c)
            else:
                self.visit(ast.thenStmt, c[0])
            retIf = False
        
        if not ast.elseStmt:
            retElse = False
        else:
            if isinstance(ast.elseStmt, (Return, Block, If)):
                retElse = self.visit(ast.elseStmt, c)
            else: 
                if isinstance(ast.elseStmt, (For, Break, Continue, CallStmt, Assign)):
                    self.visit(ast.elseStmt,  c)
                else:
                    self.visit(ast.elseStmt, c[0])
                retElse = False
        return retIf and retElse

    # class For(Stmt):
    #   id: Id
    #   expr1: Expr
    #   expr2: Expr 
    #   loop: Stmt
    #   expr3: Expr = None
    def visitFor(self, ast: For, c):
        expr1 = self.visit(ast.expr1, c[0])
        expr2 = self.visit(ast.expr2, c[0])
        expr3 = IntType()
        if ast.expr3 != None:
            expr3 = self.visit(ast.expr3, c[0])
        is_match = isinstance(expr1, IntType) and isinstance(expr2, IntType) and isinstance(expr3, IntType)
        if not is_match:
            raise TypeMismatchInStatement(ast)
        self.visit(ast.loop, c)

    # class Break(Stmt):
    def visitBreak(self, ast: Break, c):
        in_loop = c[1]
        if not in_loop:
            raise MustInLoop(ast)

    # class Continue(Stmt):
    def visitContinue(self, ast: Continue, c):
        in_loop = c[1]
        if not in_loop:
            raise MustInLoop(ast)

    # class Return(Stmt):
    #   expr: Expr = None
    def visitReturn(self, ast: Return, c):
        retType = c[2]
        if not ast.expr:
            if not isinstance(retType, VoidType):
                raise TypeMismatchInStatement(ast)
        elif isinstance(retType, VoidType):
            raise TypeMismatchInStatement(ast)
        else:
            expr = self.visit(ast.expr, c[0])
            if isinstance(expr, ArrayType):
                if not isinstance(expr.eleType, type(retType.eleType)):
                    raise TypeMismatchInStatement(ast)
            elif isinstance(retType, FloatType):
                if not isinstance(expr, (IntType, FloatType)):
                    raise TypeMismatchInStatement(ast)
            elif not isinstance(expr, type(retType)):
                raise TypeMismatchInStatement(ast)
        return True

    # class CallStmt(Stmt):
    #     obj: Expr
    #     method: Id
    #     param: List[Expr]
    def visitCallStmt(self, ast: CallStmt, c):
        if not isinstance(ast.obj, ClassType):
            raise TypeMismatchInExpression(ast)
        else:
            if ast.method.name not in list(self.global_env[ast.obj.classname.name][1].keys()):
                raise TypeMismatchInExpression(ast)
            elif len(ast.param) != len(self.global_env[ast.obj.classname.name][1][ast.method.name]):
                raise TypeMismatchInExpression(ast)
            else:
                for i in range(0, len(ast.param)):
                    param = self.visit(ast.param[i], c)
                    para = self.visit(self.global_env[ast.obj.classname.name][1][ast.method.name][0][i])
                    if isinstance(param, ArrayType):
                        if not isinstance(param.eleType, type(para[1])):
                            raise TypeMismatchInExpression(ast)
                    if isinstance(param, FloatType) and isinstance(para, IntType):
                        raise TypeMismatchInExpression(ast)

    # class BinaryOp(Expr):
    #     op: str
    #     left: Expr
    #     right: Expr
    def visitBinaryOp(self, ast: BinaryOp, c):
        left = self.visit(ast.left, c)
        right = self.visit(ast.right, c)
        
        def checkType(parType, retType=None):
            if not isinstance(left, parType) or not isinstance(right, parType):
                raise TypeMismatchInExpression(ast)
            if retType:
                return retType
            elif isinstance(left, IntType) and isinstance(right, FloatType):
                return right
            elif isinstance(left, FloatType) and isinstance(right, IntType):
                return left
            elif isinstance(left, type(right)):
                return left
            else:
                raise TypeMismatchInExpression(ast)
        
        if ast.op in ['+','-','*','/']:
            return checkType((IntType, FloatType))
        elif ast.op == '%':
            return checkType(IntType, IntType)
        elif ast.op in ['&&','||']:
            return checkType(BoolType, BoolType)
        elif ast.op == '==.':
            return checkType(StringType, BoolType)
        elif ast.op == '+.':
            return checkType(StringType, StringType)
        elif ast.op in ['==','!=']:
            return checkType((IntType, BoolType), BoolType)
        elif ast.op in ['<','>','<=','>=']:
            return checkType((IntType, FloatType), BoolType)
        

    # class UnaryOp(Expr):
    #     op: str
    #     body: Expr
    def visitUnaryOp(self, ast: UnaryOp, c):
        body = self.visit(ast.body, c)
        if ast.op == '-':
            if not isinstance(body, (IntType, FloatType)):
                raise TypeMismatchInExpression(ast)
            else:
                return body
        if ast.op == '!':
            if not isinstance(body, BoolType):
                raise TypeMismatchInExpression(ast)
            else:
                return body


    # class CallExpr(Expr):
    #     obj: Expr
    #     method: Id
    #     param: List[Expr]
    def visitCallExpr(self, ast: CallExpr, c):
        if not isinstance(ast.obj, ClassType):
            raise TypeMismatchInExpression(ast)
        else:
            if ast.method.name not in list(self.global_env[ast.obj.classname.name][1].keys()):
                raise TypeMismatchInExpression(ast)
            elif len(ast.param) != len(self.global_env[ast.obj.classname.name][1][ast.method.name]):
                raise TypeMismatchInExpression(ast)
            else:
                for i in range(0, len(ast.param)):
                    param = self.visit(ast.param[i], c)
                    para = self.visit(self.global_env[ast.obj.classname.name][1][ast.method.name][0][i])
                    if isinstance(param, ArrayType):
                        if not isinstance(param.eleType, type(para[1])):
                            raise TypeMismatchInExpression(ast)
                    if isinstance(param, FloatType) and isinstance(para, IntType):
                        raise TypeMismatchInExpression(ast)
        return self.global_env[ast.obj.classname.name][1][ast.method.name][1]  
        

    # class NewExpr(Expr):
    #     classname: Id
    #     param: List[Expr]
    def visitNewExpr(self, ast: NewExpr, c):
        if ast.classname.name not in list(self.global_env.keys()):
            raise TypeMismatchInExpression(ast)
        return ClassType(ast.classname)

    # class Id(LHS):
    #   name: str
    def visitId(self, ast: Id, c):
        # only in class
        if ast.name[0] == '$' and ast.name not in list(c.keys()):
            raise Undeclared(Attribute(), ast.name)
        if "local" in list(c.keys()):
            if ast.name not in list(c["local"].keys()):
                raise Undeclared(Identifier(), ast.name)
            else:
                return c["local"][ast.name][1]
        return c[ast.name][1]

    # class ArrayCell(LHS):
    #     arr: Expr
    #     idx: List[Expr]
    def visitArrayCell(self, ast: ArrayCell, c):
        arr = self.visit(ast.arr, c)
        if not isinstance(arr, ArrayType):
            raise TypeMismatchInExpression(ast)
        for idx in ast.idx:
            if not isinstance(idx, IntType):
                raise TypeMismatchInExpression
        return arr.eleType

    # class FieldAccess(LHS):
    #     obj: Expr
    #     fieldname: Id
    def visitFieldAccess(self, ast: FieldAccess, c):
        if not isinstance(ast.obj, ClassType):
            raise IllegalMemberAccess(ast)
        elif ast.fieldname.name not in list(self.global_env[ast.obj.classname.name].keys()):
                raise Undeclared(Attribute(), ast.fieldname.name)
        else:
            return ClassType(ast.obj.classname)


    # class IntType(Type):
    def visitIntType(self, ast: IntType, c):
        return IntType()

    # class FloatType(Type):
    def visitFloatType(self, ast: FloatType, c):
        return FloatType()

    # class BoolType(Type):
    def visitBoolType(self, ast: BoolType, c):
        return BoolType()

    # class StringType(Type):
    def visitStringType(self, ast: StringType, c):
        return StringType()

    # class ArrayType(Type):
    #     size: int
    #     eleType: Type
    def visitArrayType(self, ast: ArrayType, c):
        return ArrayType(ast.size, self.visit(ast.eleType, c))

    # class VoidType(Type):
    def visitVoidType(self, ast: VoidType, c):
        return VoidType()

    # class ClassType(Type):
    #     classname: Id
    def visitClassType(self, ast: ClassType, c):
        return ClassType(ast.classname)

    # class IntLiteral(Literal):
    #     value: int
    def visitIntLiteral(self, ast: IntLiteral, c):
        return IntType()

    # class FloatLiteral(Literal):
    #     value: float
    def visitFloatLiteral(self, ast: FloatLiteral, c):
        return FloatType()

    # class StringLiteral(Literal):
    #     value: str
    def visitStringLiteral(self, ast: StringLiteral, c):
        return StringType()

    # class BooleanLiteral(Literal):
    #     value: bool
    def visitBooleanLiteral(self, ast: BooleanLiteral, c):
        return BoolType()

    # class ArrayLiteral(Literal):
    #     value: List[Expr]
    def visitArrayLiteral(self, ast: ArrayLiteral, c):
        arr_type = self.visit(ast.value[0], c)
        for expr in ast.value: 
            if arr_type != self.visit(expr, c):
                raise IllegalArrayLiteral(ast)
        return ArrayType(len(ast.value), arr_type)

    # class NullLiteral(Literal):
    def visitNullLiteral(self, ast: NullLiteral, c):
        return ClassType(c.classname)

    # class SelfLiteral(Literal):
    def visitSelfLiteral(self, ast: SelfLiteral, c):
        return ClassType(c.classname)