
"""
 * @author nhphung
"""
from pydoc import classname
from AST import * 
from Visitor import *
from Utils import Utils
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

class StaticChecker(BaseVisitor,Utils):

    global_envi = [
    Symbol("getInt",MType([],IntType())),
    Symbol("putIntLn",MType([IntType()],VoidType()))
    ]
            
    
    def __init__(self,ast):
        self.ast = ast

 
    
    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)

    # Class Program: 
    #   decl: List[ClassDecl]
    def visitProgram(self,ast:Program, c): 
        c = {}
        for decl in ast.decl: self.visit(decl, c)
        classlist = list(c.keys())
        for decl in ast.decl:
            if decl.parentname.name != "":
                if decl.parentname.name == decl.classname.name:
                    raise Redeclared(Class, decl.parentname.name)
                # Maybe A{B{A{}}}: A inside A is wrong => need to check ancestor of class
                elif decl.parentname.name not in classlist:
                    raise Undeclared(Class, decl.parentname.name)
            else:
                pass


    # class ClassDecl(Decl):
    #   classname: Id
    #   memlist: List[MemDecl]
    #   parentname: Id = None  # None if there is no parent
    def visitClassDecl(self, ast:ClassDecl, c):
        if ast.classname.name in list(c.keys()):
            raise Redeclared(Class, ast.classname.name)
        memdecls = {
            "MethodDecl": {},
            "AttributeDecl": {}
        }
        for mem in ast.memlist: self.visit(mem, memdecls)
        c[ast.classname.name] = (ast.parentname.name, memdecls)

    # class MethodDecl(MemDecl):
    #   kind: SIKind
    #   name: Id
    #   param: List[VarDecl]
    #   body: Block
    def visitMethodDecl(self, ast: MethodDecl, c):
        if ast.name.name in list(c["MethodDecl"].keys()):
            raise Redeclared(Method, ast.name.name)
        if ast.name.name in list(c["AttributeDecl"]["VarDecl"].keys()):
            raise Redeclared(Method, ast.name.name)
        if ast.name.name in list(c["AttributeDecl"]["ConstDecl"].keys()):
            raise Redeclared(Method, ast.name.name)
        methoddecls = {
            "VarDecl": {}
        }
        for param in ast.param: self.visit(param, methoddecls)
        # use "=" must RETURN => ast.body must RETURN
        c["MethodDecl"][ast.name.name] = (methoddecls, self.visit(ast.body, c))

    # ------CÁI NÀY CÓ VAR VỚI CONST RỒI THÌ CẦN GÌ NỮA NHỈ? CHẮC CẦN CHO VIỆC KHÁC--------------------------------------
    # class AttributeDecl(MemDecl):
    #   kind: SIKind  # Instance or Static
    #   decl: StoreDecl  # VarDecl for mutable or ConstDecl for immutable
    def visitAttributeDecl(self, ast: AttributeDecl, c):
        attributedecls = {
            "VarDecl": {},
            "ConstDecl": {}
        }
        self.visit(ast.decl, attributedecls)
        c["AttributeDecl"] = attributedecls

    # class VarDecl(StoreDecl):
    #   variable: Id
    #   varType: Type
    #   varInit: Expr = None  # None if there is no initial
    def visitVarDecl(self, ast: VarDecl, c):
        if ast.variable.name in list(c["MethodDecl"].keys()):
            raise Redeclared(Variable, ast.variable.name)
        if ast.variable.name in list(c["AttributeDecl"]["VarDecl"].keys()):
            raise Redeclared(Variable, ast.variable.name)
        if ast.variable.name in list(c["AttributeDecl"]["ConstDecl"].keys()):
            raise Redeclared(Variable, ast.variable.name)
        c["VarDecl"][ast.variable.name] = (self.visit(ast.varType, c), self.visit(ast.varInit, c))

    # class ConstDecl(StoreDecl):
    #   constant: Id
    #   constType: Type
    #   value: Expr = None # None if there is no initial
    def visitConstDecl(self, ast: ConstDecl, c):
        if ast.constant.name in list(c["MethodDecl"].keys()):
            raise Redeclared(Constant, ast.constant.name)
        if ast.constant.name in list(c["AttributeDecl"]["VarDecl"].keys()):
            raise Redeclared(Constant, ast.constant.name)
        if ast.constant.name in list(c["AttributeDecl"]["ConstDecl"].keys()):
            raise Redeclared(Constant, ast.constant.name)
        c["AttributeDecl"]["VarDecl"][ast.constant.name] = (self.visit(ast.constType, c), self.visit(ast.value, c))


    # class Block(Stmt):
    #   inst: List[Inst]
    def visitBlock(self, ast: Block, c):
        pass

    # class Assign(Stmt):
    #   lhs: Expr
    #   exp: Expr
    def visitAssign(self, ast: Assign, c):
        pass

    # class If(Stmt):
    #   expr: Expr
    #   thenStmt: Stmt
    #   elseStmt: Stmt = None  # None if there is no else branch
    def visitIf(self, ast: If, c):
        pass

    # class For(Stmt):
    #   id: Id
    #   expr1: Expr
    #   expr2: Expr 
    #   loop: Stmt
    #   expr3: Expr = None
    def visitFor(self, ast: For, c):
        pass

    # class Return(Stmt):
    #   expr: Expr = None
    def visitReturn(self, ast: Return, c):
        pass

    # class CallStmt(Stmt):
    #     obj: Expr
    #     method: Id
    #     param: List[Expr]
    def visitCallStmt(self, ast: CallStmt, c):
        pass

    # class BinaryOp(Expr):
    #     op: str
    #     left: Expr
    #     right: Expr
    def visitBinaryOp(self, ast: BinaryOp, c):
        pass

    # class UnaryOp(Expr):
    #     op: str
    #     body: Expr
    def visitUnaryOp(self, ast: UnaryOp, c):
        pass
    
    # class CallExpr(Expr):
    #     obj: Expr
    #     method: Id
    #     param: List[Expr]
    def visitCallExpr(self, ast: CallExpr, c):
        pass

    # class NewExpr(Expr):
    #     classname: Id
    #     param: List[Expr]
    def visitNewExpr(self, ast: NewExpr, c):
        pass

    # class Id(LHS):
    #   name: str
    def visitId(self, ast: Id, c):
        return c[ast.name]

    # class ArrayCell(LHS):
    #     arr: Expr
    #     idx: List[Expr]
    def visitArrayCell(self, ast: ArrayCell, c):
        pass

    # class FieldAccess(LHS):
    #     obj: Expr
    #     fieldname: Id
    def visitFieldAccess(self, ast: FieldAccess, c):
        pass

    # class ArrayType(Type):
    #     size: int
    #     eleType: Type
    def visitArrayType(self, ast: ArrayType, c):
        pass

    # class ClassType(Type):
    #     classname: Id
    def visitClassType(self, ast: ClassType, c):
        pass

    # class IntLiteral(Literal):
    #     value: int
    def visitIntLiteral(self, ast: IntLiteral, c):
        return 1

    # class FloatLiteral(Literal):
    #     value: float
    def visitFloatLiteral(self, ast: FloatLiteral, c):
        return 2

    # class StringLiteral(Literal):
    #     value: str
    def visitStringLiteral(self, ast: StringLiteral, c):
        return 3

    # class BooleanLiteral(Literal):
    #     value: bool
    def visitBooleanLiteral(self, ast: BooleanLiteral, c):
        return 4

    # class ArrayLiteral(Literal):
    #     value: List[Expr]
    def visitArrayLiteral(self, ast: ArrayLiteral, c):
        pass






        







    
    # # classdecls: classdecl classdecls | classdecl;
    # def visitFuncDecl(self,ast, c): 
    #     return list(map(lambda x: self.visit(x,(c,True)),ast.body.stmt)) 
    

    # def visitCallExpr(self, ast, c): 
    #     at = [self.visit(x,(c[0],False)) for x in ast.param]
        
    #     res = self.lookup(ast.method.name,c[0],lambda x: x.name)
    #     if res is None or not type(res.mtype) is MType:
    #         raise Undeclared(Function(),ast.method.name)
    #     elif len(res.mtype.partype) != len(at):
    #         if c[1]:
    #             raise TypeMismatchInStatement(ast)
    #         else:
    #             raise TypeMismatchInExpression(ast)
    #     else:
    #         return res.mtype.rettype

    # def visitIntLiteral(self,ast, c): 
    #     return IntType()
    

