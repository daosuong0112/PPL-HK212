class ASTGenerator(CSELVisitor):
# program: decl+ EOF;
# Visit a parse tree produced by CSELParser#program.
    def visitProgram(self, ctx:CSELParser.ProgramContext):
        res = []
        for x in ctx.decl():
            res += self.visit(x)
        return Program(res)

    # cseltype: INT | FLOAT | BOOLEAN;
    # Visit a parse tree produced by CSELParser#cseltype.
    def visitCseltype(self, ctx:CSELParser.CseltypeContext):
        if ctx.INT(): 
            return IntType()
        elif ctx.FLOAT(): 
            return FloatType()
        else: 
            return BooleanType()

    # decl: vardecl decltail | constdecl decltail | funcdecl decltail;
    # Visit a parse tree produced by CSELParser#decl.
    def visitDecl(self, ctx:CSELParser.DeclContext):
        if ctx.vardecl():
            return self.visit(ctx.vardecl())+ self.visit(ctx.decltail())
        elif ctx.constdecl():
            return self.visit(ctx.constdecl()) + self.visit(ctx.decltail())
        else: 
            return self.visit(ctx.funcdecl()) + self.visit(ctx.decltail())
    
    # decltail: vardecl decltail | constdecl decltail | funcdecl decltail | ;
    # Visit a parse tree produced by CSELParser#decltail.
    def visitDecltail(self, ctx:CSELParser.DecltailContext):
        if ctx.vardecl():
            return self.visit(ctx.vardecl())+ self.visit(ctx.decltail())
        elif ctx.constdecl():
            return self.visit(ctx.constdecl()) + self.visit(ctx.decltail())
        elif ctx.funcdecl(): 
            return self.visit(ctx.funcdecl()) + self.visit(ctx.decltail()) 
        else: return []
        
    # vardecl: LET single_vardecls SEMI;
    # Visit a parse tree produced by CSELParser#vardecl.
    def visitVardecl(self, ctx:CSELParser.VardeclContext):
        return self.visit(ctx.single_vardecls())
    
    #single_vardecls: single_vardecl single_vardecltail;
    # Visit a parse tree produced by CSELParser#single_vardecls.
    def visitSingle_vardecls(self, ctx:CSELParser.Single_vardeclsContext):
        return self.visit(ctx.single_vardecl()) + self.visit(ctx.single_vardecltail())
    
    # single_vardecl: ID COLON cseltype;
    # Visit a parse tree produced by CSELParser#single_vardecl.
    def visitSingle_vardecl(self, ctx:CSELParser.Single_vardeclContext):
        return [VarDecl(Id(ctx.ID().getText()), self.visit(ctx.cseltype()))]
    
    #single_vardecltail: COMMA single_vardecl single_vardecltail |
    # Visit a parse tree produced by CSELParser#single_vardecltail.
    def visitSingle_vardecltail(self, ctx:CSELParser.Single_vardecltailContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.single_vardecl()) + self.visit(ctx.single_vardecltail())
    
    #constdecl: CONST single_constdecl SEMI;

    # Visit a parse tree produced by CSELParser#constdecl.
    def visitConstdecl(self, ctx:CSELParser.ConstdeclContext):
        return self.visit(ctx.single_constdecl())
    
    # single_constdecl: ID COLON cseltype EQ expr;

    # Visit a parse tree produced by CSELParser#single_constdecl.
    def visitSingle_constdecl(self, ctx:CSELParser.Single_constdeclContext):
        id = ctx.ID()
        typ = self.visit(ctx.cseltype())
        val = self.visit(ctx.expr())
        return [ConstDecl(Id(id.getText()), typ, val)]
    
    # Visit a parse tree produced by CSELParser#expr.
    def visitExpr(self, ctx:CSELParser.ExprContext):
        if ctx.INTLIT():
            return IntLit(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLit(float(ctx.FLOATLIT().getText()))
        else: return BooleanLit(ctx.BOOLEANLIT().getText() == 'True')
        
    # expr: INTLIT | FLOATLIT | BOOLEANLIT;
    # funcdecl: FUNCTION ID LR paramlist RR SEMI;

    # Visit a parse tree produced by CSELParser#funcdecl.
    def visitFuncdecl(self, ctx:CSELParser.FuncdeclContext):
        return [FuncDecl(Id(ctx.ID().getText()), self.visit(ctx.paramlist()))]
        
    # Visit a parse tree produced by CSELParser#paramlist.
    def visitParamlist(self, ctx:CSELParser.ParamlistContext):
        # paramlist: single_vardecls | ;
        if ctx.single_vardecls():
            return self.visit(ctx.single_vardecls())
        return []