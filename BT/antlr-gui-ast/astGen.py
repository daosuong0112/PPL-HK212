class Program(ABC): pass # decl: List[Decl]

class Type(ABC): pass

class IntType(Type): pass

class FloatType(Type): pass

class BooleanType(Type): pass

class LHS(ABC): pass

class Id(LHS): pass # name: str

class Decl(ABC): pass

class VarDecl(Decl): pass # id: Id, typ: Type

class ConstDecl(Decl): pass # id: Id, typ: Type, value: Expr

class FuncDecl(Decl): pass # name: Id, param: List[VarDecl]

class Exp(ABC): pass

class IntLit(Exp): pass # value: int


class FloatLit(Exp): pass # value: float

class BooleanLit(Exp): pass # value: bool

class ASTGenerator(CSELVisitor):
    
    # Visit a parse tree produced by CSELParser#program.
    # program: decl+ EOF;
    def visitProgram(self, ctx:CSELParser.ProgramContext):
        temp = []
        for x in ctx.decl():
            temp += self.visit(x)
        return Program(temp)

    # Visit a parse tree produced by CSELParser#cseltype.
    # cseltype: INT | FLOAT | BOOLEAN;
    def visitCseltype(self, ctx:CSELParser.CseltypeContext):
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        return BooleanType()

    # Visit a parse tree produced by CSELParser#decl.
    # decl: vardecl decltail | constdecl decltail | funcdecl decltail;
    def visitDecl(self, ctx:CSELParser.DeclContext):
        if ctx.vardecl():
            return self.visit(ctx.vardecl()) + self.visit(ctx.decltail())
        elif ctx.constdecl():
            return self.visit(ctx.constdecl()) + self.visit(ctx.decltail())
        elif ctx.funcdecl():
            return self.visit(ctx.funcdecl()) + self.visit(ctx.decltail())

    # Visit a parse tree produced by CSELParser#decltail.
    # decltail: vardecl decltail | constdecl decltail | funcdecl decltail | ;
    def visitDecltail(self, ctx:CSELParser.DecltailContext):
        if ctx.vardecl():
            return self.visit(ctx.vardecl()) + self.visit(ctx.decltail())
        elif ctx.constdecl():
            return self.visit(ctx.constdecl()) + self.visit(ctx.decltail())
        elif ctx.funcdecl():
            return self.visit(ctx.funcdecl()) + self.visit(ctx.decltail())
        return []

    # Visit a parse tree produced by CSELParser#vardecl.
    # vardecl: LET single_vardecls SEMI;
    def visitVardecl(self, ctx:CSELParser.VardeclContext):
        return self.visit(ctx.single_vardecls())

    # Visit a parse tree produced by CSELParser#single_vardecls.
    # single_vardecls: single_vardecl single_vardecltail;
    def visitSingle_vardecls(self, ctx:CSELParser.Single_vardeclsContext):
        single_vardecl = self.visit(ctx.single_vardecl())
        single_vardecltail = self.visit(ctx.single_vardecltail())
        return single_vardecl + single_vardecltail

    # Visit a parse tree produced by CSELParser#single_vardecl.
    # single_vardecl: ID COLON cseltype;
    def visitSingle_vardecl(self, ctx:CSELParser.Single_vardeclContext):
        cseltype = self.visit(ctx.cseltype())
        return [VarDecl(Id(ctx.ID().getText()), cseltype)]

    # Visit a parse tree produced by CSELParser#single_vardecltail.
    # single_vardecltail: COMMA single_vardecl single_vardecltail | ;
    def visitSingle_vardecltail(self, ctx:CSELParser.Single_vardecltailContext):
        if ctx.COMMA():
            single_vardecl = self.visit(ctx.single_vardecl())
            single_vardecltail = self.visit(ctx.single_vardecltail())
            return single_vardecl + single_vardecltail
        return []

    # Visit a parse tree produced by CSELParser#constdecl.
    # constdecl: CONST single_constdecl SEMI;
    def visitConstdecl(self, ctx:CSELParser.ConstdeclContext):
        return self.visit(ctx.single_constdecl())

    # Visit a parse tree produced by CSELParser#single_constdecl.
    # single_constdecl: ID COLON cseltype EQ expr;
    def visitSingle_constdecl(self, ctx:CSELParser.Single_constdeclContext):
        cseltype = self.visit(ctx.cseltype())
        expr = self.visit(ctx.expr())
        return [ConstDecl(Id(ctx.ID().getText()), cseltype, expr)]

    # Visit a parse tree produced by CSELParser#expr.
    # expr: INTLIT | FLOATLIT | BOOLEANLIT;
    def visitExpr(self, ctx:CSELParser.ExprContext):
        if ctx.INTLIT():
            return IntLit(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLit(float(ctx.FLOATLIT().getText()))
        return BooleanLit(ctx.BOOLEANLIT().getText() == "True")

    # Visit a parse tree produced by CSELParser#funcdecl.
    # funcdecl: FUNCTION ID LR paramlist RR SEMI;
    def visitFuncdecl(self, ctx:CSELParser.FuncdeclContext):
        paramlist = self.visit(ctx.paramlist())
        return [FuncDecl(Id(ctx.ID().getText()), paramlist)]

    # Visit a parse tree produced by CSELParser#paramlist.
    # paramlist: single_vardecls | ;
    def visitParamlist(self, ctx:CSELParser.ParamlistContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.single_vardecls())