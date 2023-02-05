import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test300(self):
        input = """ 
            Class Vehicle {
                Shape() {
                    Foreach(a::$b In 1+2 .. 100-1 By 2)
                    {
                        Foreach(arr[0] In 4/2 .. 100*2 By 4)
                        {
                            {
                                a = 2;
                                {
                                    a = 3;
                                }
                            }
                        }
                    }
                }
            }
            """
        expect = "Program([ClassDecl(Id(Vehicle),[MethodDecl(Id(Shape),Instance,[],Block([For(FieldAccess(Id(a),Id($b)),BinaryOp(+,IntLit(1),IntLit(2)),BinaryOp(-,IntLit(100),IntLit(1)),IntLit(2),Block([For(ArrayCell(Id(arr),[IntLit(0)]),BinaryOp(/,IntLit(4),IntLit(2)),BinaryOp(*,IntLit(100),IntLit(2)),IntLit(4),Block([Block([AssignStmt(Id(a),IntLit(2)),Block([AssignStmt(Id(a),IntLit(3))])])])])])])]))])])"
        self.assertTrue(TestAST.test(input,expect,300))

    def test301(self):
        input = """
        Class Program {
            testFun() {
                If (a > b) {
                    a = a + 1;
                }
                Elseif (a < b) {
                    a = a - 1;
                }
                Else {
                    a = a * 2;
                }
            }
        }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(testFun),Instance,[],Block([If(BinaryOp(>,Id(a),Id(b)),Block([AssignStmt(Id(a),BinaryOp(+,Id(a),IntLit(1)))]),If(BinaryOp(<,Id(a),Id(b)),Block([AssignStmt(Id(a),BinaryOp(-,Id(a),IntLit(1)))]),Block([AssignStmt(Id(a),BinaryOp(*,Id(a),IntLit(2)))])))]))])])"
        self.assertTrue(TestAST.test(input,expect,301))
    
    # def test_more_complex_program(self):
    #     """More complex program"""
    #     input = """int main () {
    #         putIntLn(4);
    #     }"""
    #     expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([],[CallExpr(Id("putIntLn"),[IntLiteral(4)])]))]))
    #     self.assertTrue(TestAST.test(input,expect,301))
    
    # def test_call_without_parameter(self):
    #     """More complex program"""
    #     input = """int main () {
    #         getIntLn();
    #     }"""
    #     expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([],[CallExpr(Id("getIntLn"),[])]))]))
    #     self.assertTrue(TestAST.test(input,expect,302))
   
    def test302(self):
        input = """ 
                    Class Shape { 
                        $getNumOfShape(a : Int) { 
                            Return Self.length * Self.width; 
                        } 
                    } 
                """
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id($getNumOfShape),Static,[param(Id(a),IntType)],Block([Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))]))])])"
        self.assertTrue(TestAST.test(input,expect,302))

    def test303(self):
        input = """ Class main{
                        Var a: Array[String, 3] = Array("Volvo", "33", "18");
                    } """
        expect = "Program([ClassDecl(Id(main),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(IntLit(3),StringType),[StringLit(Volvo),StringLit(33),StringLit(18)]))])])"
        self.assertTrue(TestAST.test(input,expect,303))

    def test304(self):
        input = """ Class main{
                        Var a: Array[Array[String,3], 3] = Array (
                            Array("Volvo", "33", "18"),
                            Array("Saab", "5", "3"),
                            Array("Land Rover", "17", "15")
                        ) ;
                    } """
        expect = "Program([ClassDecl(Id(main),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(IntLit(3),ArrayType(IntLit(3),StringType)),[[StringLit(Volvo),StringLit(33),StringLit(18)],[StringLit(Saab),StringLit(5),StringLit(3)],[StringLit(Land Rover),StringLit(17),StringLit(15)]]))])])"
        self.assertTrue(TestAST.test(input,expect,304))
    
    def test305(self):
        input = """ Class main{
                        Var a: Array[Array[String,3], 3] = Array (
                            Array("Volvo", "33", "18"),
                            Array("Saab", "5", "3"),
                            Array("Land Rover", "17", "15")
                        ) ;
                        getLength(a : Int) {
                            Var r, s: Int;
                            r = 3.0;
                            Var a, b: Array[Int, 5];
                            s = r * r * Self.myPI;
                            a[0] = s;
                        }
                    } """
        expect = "Program([ClassDecl(Id(main),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(IntLit(3),ArrayType(IntLit(3),StringType)),[[StringLit(Volvo),StringLit(33),StringLit(18)],[StringLit(Saab),StringLit(5),StringLit(3)],[StringLit(Land Rover),StringLit(17),StringLit(15)]])),MethodDecl(Id(getLength),Instance,[param(Id(a),IntType)],Block([AttributeDecl(Instance,VarDecl(Id(r),IntType)),AttributeDecl(Instance,VarDecl(Id(s),IntType)),AssignStmt(Id(r),FloatLit(3.0)),AttributeDecl(Instance,VarDecl(Id(a),ArrayType(IntLit(5),IntType))),AttributeDecl(Instance,VarDecl(Id(b),ArrayType(IntLit(5),IntType))),AssignStmt(Id(s),BinaryOp(*,BinaryOp(*,Id(r),Id(r)),FieldAccess(Self(),Id(myPI)))),AssignStmt(ArrayCell(Id(a),[IntLit(0)]),Id(s))]))])])"
        self.assertTrue(TestAST.test(input,expect,305))

    def test306(self):
        input = """ Class main{
                        Var a: Array[Array[String,3], 3] = Array (
                            Array("Volvo", "33", "18"),
                            Array("Saab", "5", "3"),
                            Array("Land Rover", "17", "15")
                        );
                        getLength(a : Int; b : Float) {
                            Var r, s: Int;
                            r = 3.0;
                            Var a, b: Array[Int, 5];
                            s = r * r * Self.myPI;
                            a[0] = s;
                            If (a == b) {
                                a = a + a.b;
                            }
                        }
                    } """
        expect = "Program([ClassDecl(Id(main),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(IntLit(3),ArrayType(IntLit(3),StringType)),[[StringLit(Volvo),StringLit(33),StringLit(18)],[StringLit(Saab),StringLit(5),StringLit(3)],[StringLit(Land Rover),StringLit(17),StringLit(15)]])),MethodDecl(Id(getLength),Instance,[param(Id(a),IntType),param(Id(b),FloatType)],Block([AttributeDecl(Instance,VarDecl(Id(r),IntType)),AttributeDecl(Instance,VarDecl(Id(s),IntType)),AssignStmt(Id(r),FloatLit(3.0)),AttributeDecl(Instance,VarDecl(Id(a),ArrayType(IntLit(5),IntType))),AttributeDecl(Instance,VarDecl(Id(b),ArrayType(IntLit(5),IntType))),AssignStmt(Id(s),BinaryOp(*,BinaryOp(*,Id(r),Id(r)),FieldAccess(Self(),Id(myPI)))),AssignStmt(ArrayCell(Id(a),[IntLit(0)]),Id(s)),If(BinaryOp(==,Id(a),Id(b)),Block([AssignStmt(Id(a),BinaryOp(+,Id(a),FieldAccess(Id(a),Id(b))))]))]))])])"
        self.assertTrue(TestAST.test(input,expect,306))

    def test307(self):
        input = """ Class main{
                        Var a: Array[Array[String,3], 3] = Array (
                            Array("Volvo", "33", "18"),
                            Array("Saab", "5", "3"),
                            Array("Land Rover", "17", "15")
                        ) ;
                        getLength(a,b : Int) {
                            Var r, s: Int;
                            r = 3.0;
                            Var a, b: Array[Int, 5];
                            s = r * r * Self.myPI;
                            a[0] = s;
                            If (a == b) {
                                a = New X();
                            }
                            Elseif (a != b) {
                                b = Null;
                            }
                            Elseif (a == 0) {
                                a = b + Shape::$numOfShape();
                            }
                            Else {
                                b = a - Shape.getArea() - Shape.width - Shape::$height;
                            }
                        }
                    } """
        expect = "Program([ClassDecl(Id(main),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(IntLit(3),ArrayType(IntLit(3),StringType)),[[StringLit(Volvo),StringLit(33),StringLit(18)],[StringLit(Saab),StringLit(5),StringLit(3)],[StringLit(Land Rover),StringLit(17),StringLit(15)]])),MethodDecl(Id(getLength),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AttributeDecl(Instance,VarDecl(Id(r),IntType)),AttributeDecl(Instance,VarDecl(Id(s),IntType)),AssignStmt(Id(r),FloatLit(3.0)),AttributeDecl(Instance,VarDecl(Id(a),ArrayType(IntLit(5),IntType))),AttributeDecl(Instance,VarDecl(Id(b),ArrayType(IntLit(5),IntType))),AssignStmt(Id(s),BinaryOp(*,BinaryOp(*,Id(r),Id(r)),FieldAccess(Self(),Id(myPI)))),AssignStmt(ArrayCell(Id(a),[IntLit(0)]),Id(s)),If(BinaryOp(==,Id(a),Id(b)),Block([AssignStmt(Id(a),NewExpr(Id(X),[]))]),If(BinaryOp(!=,Id(a),Id(b)),Block([AssignStmt(Id(b),NullLiteral())]),If(BinaryOp(==,Id(a),IntLit(0)),Block([AssignStmt(Id(a),BinaryOp(+,Id(b),CallExpr(Id(Shape),Id($numOfShape),[])))]),Block([AssignStmt(Id(b),BinaryOp(-,BinaryOp(-,BinaryOp(-,Id(a),CallExpr(Id(Shape),Id(getArea),[])),FieldAccess(Id(Shape),Id(width))),FieldAccess(Id(Shape),Id($height))))]))))]))])])"
        self.assertTrue(TestAST.test(input,expect,307))
    
    def test308(self):
        input = """ Class main{
                        Var a,b,c : Float = 5.0,6.0,7.1;
                        Var b : String = "abc";
                        Var c : Int = 5;
                        Var d : Boolean = True;
                    } """
        expect = "Program([ClassDecl(Id(main),[AttributeDecl(Instance,VarDecl(Id(a),FloatType,FloatLit(5.0))),AttributeDecl(Instance,VarDecl(Id(b),FloatType,FloatLit(6.0))),AttributeDecl(Instance,VarDecl(Id(c),FloatType,FloatLit(7.1))),AttributeDecl(Instance,VarDecl(Id(b),StringType,StringLit(abc))),AttributeDecl(Instance,VarDecl(Id(c),IntType,IntLit(5))),AttributeDecl(Instance,VarDecl(Id(d),BoolType,BooleanLit(True)))])])"
        self.assertTrue(TestAST.test(input,expect,308))

    def test309(self):
        input = """ Class main{
                        Var a : Float = 5.0;
                        Var b : String = "abc";
                        $getHeight() {
                            a = b + c - d * e / f % g;
                            b = !h || i && k;
                            c = a == d;
                            e = f ==. c;
                            g = t +. d;
                        }
                    } """
        expect = "Program([ClassDecl(Id(main),[AttributeDecl(Instance,VarDecl(Id(a),FloatType,FloatLit(5.0))),AttributeDecl(Instance,VarDecl(Id(b),StringType,StringLit(abc))),MethodDecl(Id($getHeight),Static,[],Block([AssignStmt(Id(a),BinaryOp(-,BinaryOp(+,Id(b),Id(c)),BinaryOp(%,BinaryOp(/,BinaryOp(*,Id(d),Id(e)),Id(f)),Id(g)))),AssignStmt(Id(b),BinaryOp(&&,BinaryOp(||,UnaryOp(!,Id(h)),Id(i)),Id(k))),AssignStmt(Id(c),BinaryOp(==,Id(a),Id(d))),AssignStmt(Id(e),BinaryOp(==.,Id(f),Id(c))),AssignStmt(Id(g),BinaryOp(+.,Id(t),Id(d)))]))])])"
        self.assertTrue(TestAST.test(input,expect,309))

    def test310(self):
        input = """ Class main{
                        Var a : Float = 5.0;
                        Var b : String = "abc";
                        $getHeight() {
                            Val a : Int = -3;
                            Val b : Float = c + Shape::$height;
                            Var a,b: Array[Array[String,3], 3] = Array (
                                Array("Volvo", "33", "18"),
                                Array("Saab", "5", "3"),
                                Array("Land Rover", "17", "15")
                            ), Array (
                                Array("Volvo", "33", "18"),
                                Array("Saab", "5", "3"),
                                Array("Land Rover", "17", "15")
                            ) ;
                        }
                    } """
        expect = "Program([ClassDecl(Id(main),[AttributeDecl(Instance,VarDecl(Id(a),FloatType,FloatLit(5.0))),AttributeDecl(Instance,VarDecl(Id(b),StringType,StringLit(abc))),MethodDecl(Id($getHeight),Static,[],Block([AttributeDecl(Instance,ConstDecl(Id(a),IntType,UnaryOp(-,IntLit(3)))),AttributeDecl(Instance,ConstDecl(Id(b),FloatType,BinaryOp(+,Id(c),FieldAccess(Id(Shape),Id($height))))),AttributeDecl(Instance,VarDecl(Id(a),ArrayType(IntLit(3),ArrayType(IntLit(3),StringType)),[[StringLit(Volvo),StringLit(33),StringLit(18)],[StringLit(Saab),StringLit(5),StringLit(3)],[StringLit(Land Rover),StringLit(17),StringLit(15)]])),AttributeDecl(Instance,VarDecl(Id(b),ArrayType(IntLit(3),ArrayType(IntLit(3),StringType)),[[StringLit(Volvo),StringLit(33),StringLit(18)],[StringLit(Saab),StringLit(5),StringLit(3)],[StringLit(Land Rover),StringLit(17),StringLit(15)]]))]))])])"
        self.assertTrue(TestAST.test(input,expect,310))
    
    def test311(self):
        input = """ Class main{
                        Var a : Float = 5.0;
                        Var b : String = "abc";
                        $getHeight() {
                            Val a : Int = -3;
                            Val b : Float = c + Shape::$height;
                            Foreach (x In 5 .. 3) {
                                Out.printInt(arr[x]);
                            }
                            If (a > b) {
                                a = b;
                                a = c;
                            }
                            If (a > c) {
                                b = c;
                                c = temp;
                            }
                        }
                    } """
        expect = "Program([ClassDecl(Id(main),[AttributeDecl(Instance,VarDecl(Id(a),FloatType,FloatLit(5.0))),AttributeDecl(Instance,VarDecl(Id(b),StringType,StringLit(abc))),MethodDecl(Id($getHeight),Static,[],Block([AttributeDecl(Instance,ConstDecl(Id(a),IntType,UnaryOp(-,IntLit(3)))),AttributeDecl(Instance,ConstDecl(Id(b),FloatType,BinaryOp(+,Id(c),FieldAccess(Id(Shape),Id($height))))),For(Id(x),IntLit(5),IntLit(3),IntLit(1),Block([Call(Id(Out),Id(printInt),[ArrayCell(Id(arr),[Id(x)])])])]),If(BinaryOp(>,Id(a),Id(b)),Block([AssignStmt(Id(a),Id(b)),AssignStmt(Id(a),Id(c))])),If(BinaryOp(>,Id(a),Id(c)),Block([AssignStmt(Id(b),Id(c)),AssignStmt(Id(c),Id(temp))]))]))])])"
        self.assertTrue(TestAST.test(input,expect,311))

    def test312(self):
        input = """ Class main{
                        Var a : Float = 5.0;
                        Var b : String = "abc";
                        $getHeight() {
                            Val a : Int = -3;
                            Val b : Float = c + Shape::$height;
                            Foreach (x In 5 .. 2 By 2) {
                                Out.printInt(arr[x]);
                            }
                            Foreach (x In 5 .. 2 By 2) {
                                Out.printInt(arr[x]);
                            }
                        }
                    } """
        expect = "Program([ClassDecl(Id(main),[AttributeDecl(Instance,VarDecl(Id(a),FloatType,FloatLit(5.0))),AttributeDecl(Instance,VarDecl(Id(b),StringType,StringLit(abc))),MethodDecl(Id($getHeight),Static,[],Block([AttributeDecl(Instance,ConstDecl(Id(a),IntType,UnaryOp(-,IntLit(3)))),AttributeDecl(Instance,ConstDecl(Id(b),FloatType,BinaryOp(+,Id(c),FieldAccess(Id(Shape),Id($height))))),For(Id(x),IntLit(5),IntLit(2),IntLit(2),Block([Call(Id(Out),Id(printInt),[ArrayCell(Id(arr),[Id(x)])])])]),For(Id(x),IntLit(5),IntLit(2),IntLit(2),Block([Call(Id(Out),Id(printInt),[ArrayCell(Id(arr),[Id(x)])])])])]))])])"
        self.assertTrue(TestAST.test(input,expect,312))

    def test313(self):
        input = """ Class main{
                        Var a : Float = 5.0;
                        Var b : String = "abc";
                        $getHeight() {
                            Val a : Int = -3;
                            Val b : Float = c + Shape::$height;
                            Foreach (x In 5 .. 3 By 8) {
                                Foreach (x In 5 .. 3 By 3) {
                                    Out.printInt(arr[x]);
                                }
                            }
                        }
                    } """
        expect = "Program([ClassDecl(Id(main),[AttributeDecl(Instance,VarDecl(Id(a),FloatType,FloatLit(5.0))),AttributeDecl(Instance,VarDecl(Id(b),StringType,StringLit(abc))),MethodDecl(Id($getHeight),Static,[],Block([AttributeDecl(Instance,ConstDecl(Id(a),IntType,UnaryOp(-,IntLit(3)))),AttributeDecl(Instance,ConstDecl(Id(b),FloatType,BinaryOp(+,Id(c),FieldAccess(Id(Shape),Id($height))))),For(Id(x),IntLit(5),IntLit(3),IntLit(8),Block([For(Id(x),IntLit(5),IntLit(3),IntLit(3),Block([Call(Id(Out),Id(printInt),[ArrayCell(Id(arr),[Id(x)])])])])])])]))])])"
        self.assertTrue(TestAST.test(input,expect,313))
    
    def test314(self):
        input = """Class Test {
            Var myVar1: Shape = New Shape();
        }
            """
        expect = "Program([ClassDecl(Id(Test),[AttributeDecl(Instance,VarDecl(Id(myVar1),ClassType(Id(Shape)),NewExpr(Id(Shape),[])))])])"
        self.assertTrue(TestAST.test(input, expect, 314))

    def test315(self):
        input = """ Class main{
                        Var a : Float = 5.0;
                        Var b : String = "abc";
                        $getHeight() {
                            Val a : Int = -3;
                            Val b : Float = c + Shape::$height;
                            Foreach (x In 5 .. 3 By 8) {
                                Foreach (x In 5 .. 3 By 3) {
                                    Out.printInt(arr[x]);
                                    Break;
                                }
                                Continue;
                                Break;
                            }
                        }
                    } """
        expect = "Program([ClassDecl(Id(main),[AttributeDecl(Instance,VarDecl(Id(a),FloatType,FloatLit(5.0))),AttributeDecl(Instance,VarDecl(Id(b),StringType,StringLit(abc))),MethodDecl(Id($getHeight),Static,[],Block([AttributeDecl(Instance,ConstDecl(Id(a),IntType,UnaryOp(-,IntLit(3)))),AttributeDecl(Instance,ConstDecl(Id(b),FloatType,BinaryOp(+,Id(c),FieldAccess(Id(Shape),Id($height))))),For(Id(x),IntLit(5),IntLit(3),IntLit(8),Block([For(Id(x),IntLit(5),IntLit(3),IntLit(3),Block([Call(Id(Out),Id(printInt),[ArrayCell(Id(arr),[Id(x)])]),Break])]),Continue,Break])])]))])])"
        self.assertTrue(TestAST.test(input,expect,315))

    def test316(self):
        input = """ Class main{
                        Var a : Float = 5.0;
                        Var b : String = "abc";
                        $getHeight() {
                            Val a : Int = -3;
                            Val b : Float = c + Shape::$height;
                            Foreach (x In 5 .. 3 By 8) {
                                If (a == 3) {
                                    b = -3;
                                }
                                Foreach (x In 5 .. 3 By 3) {
                                    Out.printInt(arr[x]);
                                    a.b = a::$b;
                                }
                            }
                        }
                    } """
        expect = "Program([ClassDecl(Id(main),[AttributeDecl(Instance,VarDecl(Id(a),FloatType,FloatLit(5.0))),AttributeDecl(Instance,VarDecl(Id(b),StringType,StringLit(abc))),MethodDecl(Id($getHeight),Static,[],Block([AttributeDecl(Instance,ConstDecl(Id(a),IntType,UnaryOp(-,IntLit(3)))),AttributeDecl(Instance,ConstDecl(Id(b),FloatType,BinaryOp(+,Id(c),FieldAccess(Id(Shape),Id($height))))),For(Id(x),IntLit(5),IntLit(3),IntLit(8),Block([If(BinaryOp(==,Id(a),IntLit(3)),Block([AssignStmt(Id(b),UnaryOp(-,IntLit(3)))])),For(Id(x),IntLit(5),IntLit(3),IntLit(3),Block([Call(Id(Out),Id(printInt),[ArrayCell(Id(arr),[Id(x)])]),AssignStmt(FieldAccess(Id(a),Id(b)),FieldAccess(Id(a),Id($b)))])])])])]))])])"
        self.assertTrue(TestAST.test(input,expect,316))
    
    def test317(self):
        input = """ Class main{
                        Var a : Float = 5.0;
                        Var b : String = "abc";
                        $getHeight() {
                            Val a : Int = -3;
                            Val b : Float = c + Shape::$height;
                            Foreach (x In 5 .. 3 By 8) {
                                If (a ==. b) {
                                    Foreach (x In 5 .. 3 By 3) {
                                        Out.printInt(arr[x]);
                                    }
                                }
                                Foreach (x In 5 .. 3 By 3) {
                                    Out.printInt(arr[x]);
                                }
                            }
                        }
                    } """
        expect = "Program([ClassDecl(Id(main),[AttributeDecl(Instance,VarDecl(Id(a),FloatType,FloatLit(5.0))),AttributeDecl(Instance,VarDecl(Id(b),StringType,StringLit(abc))),MethodDecl(Id($getHeight),Static,[],Block([AttributeDecl(Instance,ConstDecl(Id(a),IntType,UnaryOp(-,IntLit(3)))),AttributeDecl(Instance,ConstDecl(Id(b),FloatType,BinaryOp(+,Id(c),FieldAccess(Id(Shape),Id($height))))),For(Id(x),IntLit(5),IntLit(3),IntLit(8),Block([If(BinaryOp(==.,Id(a),Id(b)),Block([For(Id(x),IntLit(5),IntLit(3),IntLit(3),Block([Call(Id(Out),Id(printInt),[ArrayCell(Id(arr),[Id(x)])])])])])),For(Id(x),IntLit(5),IntLit(3),IntLit(3),Block([Call(Id(Out),Id(printInt),[ArrayCell(Id(arr),[Id(x)])])])])])])]))])])"
        self.assertTrue(TestAST.test(input,expect,317))

    def test318(self):
        input = """ Class main{
                        Var a : Float = 5.0;
                        Var b : String = "abc";
                        $getHeight() {
                            Val a : Int = -3;
                            Val b : Float = c + Shape::$height;
                            Foreach (x In 5 .. 3 By 8) {
                                If (a ==. b) {
                                    Foreach (x In 5 .. 3 By 3) {
                                        Out.printInt(arr[x]);
                                        Return arr[5];
                                    }
                                }
                                Foreach (x In 5 .. 3 By 3) {
                                    Out.printInt(arr[x]);
                                }
                            }
                        }
                    } """
        expect = "Program([ClassDecl(Id(main),[AttributeDecl(Instance,VarDecl(Id(a),FloatType,FloatLit(5.0))),AttributeDecl(Instance,VarDecl(Id(b),StringType,StringLit(abc))),MethodDecl(Id($getHeight),Static,[],Block([AttributeDecl(Instance,ConstDecl(Id(a),IntType,UnaryOp(-,IntLit(3)))),AttributeDecl(Instance,ConstDecl(Id(b),FloatType,BinaryOp(+,Id(c),FieldAccess(Id(Shape),Id($height))))),For(Id(x),IntLit(5),IntLit(3),IntLit(8),Block([If(BinaryOp(==.,Id(a),Id(b)),Block([For(Id(x),IntLit(5),IntLit(3),IntLit(3),Block([Call(Id(Out),Id(printInt),[ArrayCell(Id(arr),[Id(x)])]),Return(ArrayCell(Id(arr),[IntLit(5)]))])])])),For(Id(x),IntLit(5),IntLit(3),IntLit(3),Block([Call(Id(Out),Id(printInt),[ArrayCell(Id(arr),[Id(x)])])])])])])]))])])"
        self.assertTrue(TestAST.test(input,expect,318))

    def test319(self):
        input = """ Class Shape {
                        Val $numOfShape: Int = 0;
                        Val immutableAttribute: Int = 0;
                        Var length, width: Int;
                        ##Var a : Int = 10;##
                        $getNumOfShape() {
                            Return $numOfShape + arr[5][6][x];
                        }
                    } """
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($numOfShape),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(immutableAttribute),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(length),IntType)),AttributeDecl(Instance,VarDecl(Id(width),IntType)),MethodDecl(Id($getNumOfShape),Static,[],Block([Return(BinaryOp(+,Id($numOfShape),ArrayCell(Id(arr),[IntLit(5),IntLit(6),Id(x)])))]))])])"
        self.assertTrue(TestAST.test(input,expect,319))
    
    def test320(self):
        input = """ Class Shape {
                        Val $numOfShape: Int = 0;
                        Val immutableAttribute: Int = 0;
                        Var length, width: Int;
                        ##Var a : Int = 10;##
                        $getNumOfShape() {
                            Return $numOfShape;
                            a = b::$shape(a[0],a[1],a[2][3]);
                        }
                    } """
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($numOfShape),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(immutableAttribute),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(length),IntType)),AttributeDecl(Instance,VarDecl(Id(width),IntType)),MethodDecl(Id($getNumOfShape),Static,[],Block([Return(Id($numOfShape)),AssignStmt(Id(a),CallExpr(Id(b),Id($shape),[ArrayCell(Id(a),[IntLit(0)]),ArrayCell(Id(a),[IntLit(1)]),ArrayCell(Id(a),[IntLit(2),IntLit(3)])]))]))])])"
        self.assertTrue(TestAST.test(input,expect,320))

    def test321(self):
        input = """ Class Shape {
                        Val $numOfShape: Int = 0;
                        Val immutableAttribute: Int = 0;
                        Var length, width: Int;
                        ##Var a : Int = 10;##
                        $getNumOfShape() {
                            Return $numOfShape;
                            a = b.shape;
                            b::$shape(a[0],a[1],a[2][3],a.b);
                        }
                    } """
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($numOfShape),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(immutableAttribute),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(length),IntType)),AttributeDecl(Instance,VarDecl(Id(width),IntType)),MethodDecl(Id($getNumOfShape),Static,[],Block([Return(Id($numOfShape)),AssignStmt(Id(a),FieldAccess(Id(b),Id(shape))),Call(Id(b),Id($shape),[ArrayCell(Id(a),[IntLit(0)]),ArrayCell(Id(a),[IntLit(1)]),ArrayCell(Id(a),[IntLit(2),IntLit(3)]),FieldAccess(Id(a),Id(b))])]))])])"
        self.assertTrue(TestAST.test(input,expect,321))

    def test322(self):
        input = """ Class Shape {
                        Val $numOfShape: Int = 0;
                        Val immutableAttribute: Int = 0;
                        Var length, width: Int;
                        ##Var a : Int = 10;##
                        $getNumOfShape() {
                            Return a::$numOfShape(a[0][1][2]);
                            a = Self.shape;
                        }
                    } """
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($numOfShape),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(immutableAttribute),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(length),IntType)),AttributeDecl(Instance,VarDecl(Id(width),IntType)),MethodDecl(Id($getNumOfShape),Static,[],Block([Return(CallExpr(Id(a),Id($numOfShape),[ArrayCell(Id(a),[IntLit(0),IntLit(1),IntLit(2)])])),AssignStmt(Id(a),FieldAccess(Self(),Id(shape)))]))])])"
        self.assertTrue(TestAST.test(input,expect,322))
    
    def test323(self):
        input = """ Class Rectangle: Shape {
                        getArea() {
                            Return Self.length * Self.width;
                        }
                    }
                    Class Program {
                        main() {
                            Out.printInt(Shape::$numOfShape);
                        }
                    }"""
        expect = "Program([ClassDecl(Id(Rectangle),Id(Shape),[MethodDecl(Id(getArea),Instance,[],Block([Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(printInt),[FieldAccess(Id(Shape),Id($numOfShape))])]))])])"
        self.assertTrue(TestAST.test(input,expect,323))

    def test324(self):
        input = """ Class Rectangle: Shape {
                        getArea() {
                            Return Self.length * Self.width;
                        }
                    }
                    Class Program {
                        main() {
                            Out.printInt(Shape::$numOfShape);
                            x = Null;
                            Val x : Shape = Null;
                        }
                    }"""
        expect = "Program([ClassDecl(Id(Rectangle),Id(Shape),[MethodDecl(Id(getArea),Instance,[],Block([Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(printInt),[FieldAccess(Id(Shape),Id($numOfShape))]),AssignStmt(Id(x),NullLiteral()),AttributeDecl(Instance,ConstDecl(Id(x),ClassType(Id(Shape)),NullLiteral()))]))])])"
        self.assertTrue(TestAST.test(input,expect,324))

    def test325(self):
        input = """ Class Shape {
                        Val $numOfShape,b: Int = 0,5;
                        Val immutableAttribute,a,c: Int = 0,6,7;
                        Var length, width: Int;
                        ##Var a : Int = 10;##
                        $getNumOfShape() {
                            Return $numOfShape;
                            a = Self.shape;
                        }
                    }
                    Class Rectangle: Shape {
                        getArea() {
                            Return Self.length * Self.width;
                        }
                    }
                    Class Program {
                        main() {
                            Out.printInt(Shape::$numOfShape);
                        }
                    }"""
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($numOfShape),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(b),IntType,IntLit(5))),AttributeDecl(Instance,ConstDecl(Id(immutableAttribute),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(6))),AttributeDecl(Instance,ConstDecl(Id(c),IntType,IntLit(7))),AttributeDecl(Instance,VarDecl(Id(length),IntType)),AttributeDecl(Instance,VarDecl(Id(width),IntType)),MethodDecl(Id($getNumOfShape),Static,[],Block([Return(Id($numOfShape)),AssignStmt(Id(a),FieldAccess(Self(),Id(shape)))]))]),ClassDecl(Id(Rectangle),Id(Shape),[MethodDecl(Id(getArea),Instance,[],Block([Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(printInt),[FieldAccess(Id(Shape),Id($numOfShape))])]))])])"
        self.assertTrue(TestAST.test(input,expect,325))
    
    def test326(self):
        input = """ Class main{
                        Var a: Array[Int, 5] = Array (
                            Array("Volvo", "32", "18"),
                            Array("Saab", "5", "2"),
                            Array("Land Rover", "17", "15")
                        ) ;
                        getLength() {
                            length = 10;
                        }
                    }
                    """
        expect = "Program([ClassDecl(Id(main),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(IntLit(5),IntType),[[StringLit(Volvo),StringLit(32),StringLit(18)],[StringLit(Saab),StringLit(5),StringLit(2)],[StringLit(Land Rover),StringLit(17),StringLit(15)]])),MethodDecl(Id(getLength),Instance,[],Block([AssignStmt(Id(length),IntLit(10))]))])])"
        self.assertTrue(TestAST.test(input,expect,326))

    def test327(self):
        input = """ Class Shape {
                        Val $numOfShape: Int = 0;
                        Val immutableAttribute: Int = 0;
                        Var length, width: Int;
                        ##Var a : Int = 10;##
                        $getNumOfShape() {
                            Return $numOfShape;
                            a = Self.shape;
                        }
                    }
                    Class Rectangle: Shape {
                        getArea() {
                            Return Self.length * Self.width;
                        }
                    }
                    Class Program {
                        main() {
                            Out.printInt(Shape::$numOfShape);
                            Foreach (x In 5 .. 2 By 8) {
                                If (a ==. b) {
                                    Foreach (x In 5 .. 2 By 2) {
                                        Out.printInt(arr[x]);
                                        Return arr[5];
                                    }
                                }
                                Foreach (x In 5 .. 2) {
                                    Out.printInt(arr[x]);
                                }
                            }
                        }
                    }"""
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($numOfShape),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(immutableAttribute),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(length),IntType)),AttributeDecl(Instance,VarDecl(Id(width),IntType)),MethodDecl(Id($getNumOfShape),Static,[],Block([Return(Id($numOfShape)),AssignStmt(Id(a),FieldAccess(Self(),Id(shape)))]))]),ClassDecl(Id(Rectangle),Id(Shape),[MethodDecl(Id(getArea),Instance,[],Block([Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(printInt),[FieldAccess(Id(Shape),Id($numOfShape))]),For(Id(x),IntLit(5),IntLit(2),IntLit(8),Block([If(BinaryOp(==.,Id(a),Id(b)),Block([For(Id(x),IntLit(5),IntLit(2),IntLit(2),Block([Call(Id(Out),Id(printInt),[ArrayCell(Id(arr),[Id(x)])]),Return(ArrayCell(Id(arr),[IntLit(5)]))])])])),For(Id(x),IntLit(5),IntLit(2),IntLit(1),Block([Call(Id(Out),Id(printInt),[ArrayCell(Id(arr),[Id(x)])])])])])])]))])])"
        self.assertTrue(TestAST.test(input,expect,327))

    def test328(self):
        input = """ Class main{
                        Var a: Array[Array[String,3], 3] = Array (
                            Array("Volvo", "32", "18"),
                            Array("Saab", "5", "2"),
                            Array("Land Rover", "17", "15")
                        ) ;
                        getLength() {
                            Var r, s: Int;
                            r = 2.0;
                            Var a, b: Array[Int, 5];
                            s = r * r * Self.myPI;
                            a[0] = s;
                            If (a == b) {
                                a = New X();
                            }
                            Elseif (a != b) {
                                b = Null;
                            }
                            Elseif (a == 0) {
                                a = b + Shape::$numOfShape();
                            }
                            Else {
                                Foreach (x In 5 .. 2 By 8) {
                                    If (a ==. b) {
                                        Foreach (x In 5 .. 2 By 2) {
                                            Out.printInt(arr[x]);
                                            Return arr[5];
                                        }
                                    }
                                    Foreach (x In 5 .. 2 By 2) {
                                        Out.printInt(arr[x]);
                                    }
                                }
                                b = a - Shape.getArea() - Shape.width - Shape::$height;
                            }
                        }
                    } """
        expect = "Program([ClassDecl(Id(main),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(IntLit(3),ArrayType(IntLit(3),StringType)),[[StringLit(Volvo),StringLit(32),StringLit(18)],[StringLit(Saab),StringLit(5),StringLit(2)],[StringLit(Land Rover),StringLit(17),StringLit(15)]])),MethodDecl(Id(getLength),Instance,[],Block([AttributeDecl(Instance,VarDecl(Id(r),IntType)),AttributeDecl(Instance,VarDecl(Id(s),IntType)),AssignStmt(Id(r),FloatLit(2.0)),AttributeDecl(Instance,VarDecl(Id(a),ArrayType(IntLit(5),IntType))),AttributeDecl(Instance,VarDecl(Id(b),ArrayType(IntLit(5),IntType))),AssignStmt(Id(s),BinaryOp(*,BinaryOp(*,Id(r),Id(r)),FieldAccess(Self(),Id(myPI)))),AssignStmt(ArrayCell(Id(a),[IntLit(0)]),Id(s)),If(BinaryOp(==,Id(a),Id(b)),Block([AssignStmt(Id(a),NewExpr(Id(X),[]))]),If(BinaryOp(!=,Id(a),Id(b)),Block([AssignStmt(Id(b),NullLiteral())]),If(BinaryOp(==,Id(a),IntLit(0)),Block([AssignStmt(Id(a),BinaryOp(+,Id(b),CallExpr(Id(Shape),Id($numOfShape),[])))]),Block([For(Id(x),IntLit(5),IntLit(2),IntLit(8),Block([If(BinaryOp(==.,Id(a),Id(b)),Block([For(Id(x),IntLit(5),IntLit(2),IntLit(2),Block([Call(Id(Out),Id(printInt),[ArrayCell(Id(arr),[Id(x)])]),Return(ArrayCell(Id(arr),[IntLit(5)]))])])])),For(Id(x),IntLit(5),IntLit(2),IntLit(2),Block([Call(Id(Out),Id(printInt),[ArrayCell(Id(arr),[Id(x)])])])])])]),AssignStmt(Id(b),BinaryOp(-,BinaryOp(-,BinaryOp(-,Id(a),CallExpr(Id(Shape),Id(getArea),[])),FieldAccess(Id(Shape),Id(width))),FieldAccess(Id(Shape),Id($height))))]))))]))])])"
        self.assertTrue(TestAST.test(input,expect,328))
    
    def test329(self):
        input = """ Class Rectangle : Shape {
                        getShape(a,b : Int; c,d : Float) {
                            Out.printInt(Shape::$numOfShape);
                            Val x,y : Int = Shape::$numOfShape + x, a % b;
                        }
                    }"""
        expect = "Program([ClassDecl(Id(Rectangle),Id(Shape),[MethodDecl(Id(getShape),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),FloatType),param(Id(d),FloatType)],Block([Call(Id(Out),Id(printInt),[FieldAccess(Id(Shape),Id($numOfShape))]),AttributeDecl(Instance,ConstDecl(Id(x),IntType,BinaryOp(+,FieldAccess(Id(Shape),Id($numOfShape)),Id(x)))),AttributeDecl(Instance,ConstDecl(Id(y),IntType,BinaryOp(%,Id(a),Id(b))))]))])])"
        self.assertTrue(TestAST.test(input,expect,329))

    def test330(self):
        input = """ Class Program {
                        main() {
                            Out.printInt(Shape::$numOfShape);
                            Val x : A = New A(a,a.b,a::$b,a[0][x]);
                        }
                    }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(printInt),[FieldAccess(Id(Shape),Id($numOfShape))]),AttributeDecl(Instance,ConstDecl(Id(x),ClassType(Id(A)),NewExpr(Id(A),[Id(a),FieldAccess(Id(a),Id(b)),FieldAccess(Id(a),Id($b)),ArrayCell(Id(a),[IntLit(0),Id(x)])])))]))])])"
        self.assertTrue(TestAST.test(input,expect,330))

    def test331(self):
        input = """ Class Program {
                        main(a : Int) {
                            Out.printInt(Shape::$numOfShape);
                            Val x,y : A = New A(a,b), Null;
                        }
                    }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[param(Id(a),IntType)],Block([Call(Id(Out),Id(printInt),[FieldAccess(Id(Shape),Id($numOfShape))]),AttributeDecl(Instance,ConstDecl(Id(x),ClassType(Id(A)),NewExpr(Id(A),[Id(a),Id(b)]))),AttributeDecl(Instance,ConstDecl(Id(y),ClassType(Id(A)),NullLiteral()))]))])])"
        self.assertTrue(TestAST.test(input,expect,331))
    
    def test332(self):
        input = """ Class Program {
                        main() {
                            Out.printInt(Shape::$numOfShape);
                            Val x,z : A = New A(x), New B();
                        }
                    }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(printInt),[FieldAccess(Id(Shape),Id($numOfShape))]),AttributeDecl(Instance,ConstDecl(Id(x),ClassType(Id(A)),NewExpr(Id(A),[Id(x)]))),AttributeDecl(Instance,ConstDecl(Id(z),ClassType(Id(A)),NewExpr(Id(B),[])))]))])])"
        self.assertTrue(TestAST.test(input,expect,332))

    def test333(self):
        input = """ Class Program {
                        main() {
                            Out.printInt(Shape::$numOfShape);
                            Val x : A = New A(x);
                            Var y : Array[Array[String,3],5];
                        }
                    }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(printInt),[FieldAccess(Id(Shape),Id($numOfShape))]),AttributeDecl(Instance,ConstDecl(Id(x),ClassType(Id(A)),NewExpr(Id(A),[Id(x)]))),AttributeDecl(Instance,VarDecl(Id(y),ArrayType(IntLit(5),ArrayType(IntLit(3),StringType))))]))])])"
        self.assertTrue(TestAST.test(input,expect,333))

    def test334(self):
        input = """ Class Program {
                        main() {
                            Out.printInt(Shape::$numOfShape);
                            Val x : String = a +. b;
                            Var y : Boolean = a ==. b;
                        }
                    }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(printInt),[FieldAccess(Id(Shape),Id($numOfShape))]),AttributeDecl(Instance,ConstDecl(Id(x),StringType,BinaryOp(+.,Id(a),Id(b)))),AttributeDecl(Instance,VarDecl(Id(y),BoolType,BinaryOp(==.,Id(a),Id(b))))]))])])"
        self.assertTrue(TestAST.test(input,expect,334))
    
    def test335(self):
        input = """ Class Program {
                        main() {
                            Out.printInt(Shape::$numOfShape);
                            Val x, y, z, k : Boolean = a >= b, c < d, e != f, m == n;
                        }
                    }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(printInt),[FieldAccess(Id(Shape),Id($numOfShape))]),AttributeDecl(Instance,ConstDecl(Id(x),BoolType,BinaryOp(>=,Id(a),Id(b)))),AttributeDecl(Instance,ConstDecl(Id(y),BoolType,BinaryOp(<,Id(c),Id(d)))),AttributeDecl(Instance,ConstDecl(Id(z),BoolType,BinaryOp(!=,Id(e),Id(f)))),AttributeDecl(Instance,ConstDecl(Id(k),BoolType,BinaryOp(==,Id(m),Id(n))))]))])])"
        self.assertTrue(TestAST.test(input,expect,335))

    def test336(self):
        input = """ Class Program {
                        main() {
                            Out.printInt(Shape::$numOfShape);
                            Val x,y,z : Boolean = a || b, a && b, !c;
                        }
                    }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(printInt),[FieldAccess(Id(Shape),Id($numOfShape))]),AttributeDecl(Instance,ConstDecl(Id(x),BoolType,BinaryOp(||,Id(a),Id(b)))),AttributeDecl(Instance,ConstDecl(Id(y),BoolType,BinaryOp(&&,Id(a),Id(b)))),AttributeDecl(Instance,ConstDecl(Id(z),BoolType,UnaryOp(!,Id(c))))]))])])"
        self.assertTrue(TestAST.test(input,expect,336))

    def test337(self):
        input = """ Class Program {
                        main() {
                            Out.printInt(Shape::$numOfShape);
                            Val x,y,z : Float = a + b, a - b, a + b - c;
                        }
                    }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(printInt),[FieldAccess(Id(Shape),Id($numOfShape))]),AttributeDecl(Instance,ConstDecl(Id(x),FloatType,BinaryOp(+,Id(a),Id(b)))),AttributeDecl(Instance,ConstDecl(Id(y),FloatType,BinaryOp(-,Id(a),Id(b)))),AttributeDecl(Instance,ConstDecl(Id(z),FloatType,BinaryOp(-,BinaryOp(+,Id(a),Id(b)),Id(c))))]))])])"
        self.assertTrue(TestAST.test(input,expect,337))
    
    def test338(self):
        input = """ Class Program {
                        main() {
                            Out.printInt(Shape::$numOfShape);
                            Val x,y,z,t : Float = a * b, a / b, c % d, a * b / c % d;
                        }
                    }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(printInt),[FieldAccess(Id(Shape),Id($numOfShape))]),AttributeDecl(Instance,ConstDecl(Id(x),FloatType,BinaryOp(*,Id(a),Id(b)))),AttributeDecl(Instance,ConstDecl(Id(y),FloatType,BinaryOp(/,Id(a),Id(b)))),AttributeDecl(Instance,ConstDecl(Id(z),FloatType,BinaryOp(%,Id(c),Id(d)))),AttributeDecl(Instance,ConstDecl(Id(t),FloatType,BinaryOp(%,BinaryOp(/,BinaryOp(*,Id(a),Id(b)),Id(c)),Id(d))))]))])])"
        self.assertTrue(TestAST.test(input,expect,338))

    def test339(self):
        input = """ Class Program {
                        main() {
                            Out.printInt(Shape::$numOfShape);
                            Val x,y,z : Boolean = !a, !!b, !!!c;
                        }
                    }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(printInt),[FieldAccess(Id(Shape),Id($numOfShape))]),AttributeDecl(Instance,ConstDecl(Id(x),BoolType,UnaryOp(!,Id(a)))),AttributeDecl(Instance,ConstDecl(Id(y),BoolType,UnaryOp(!,UnaryOp(!,Id(b))))),AttributeDecl(Instance,ConstDecl(Id(z),BoolType,UnaryOp(!,UnaryOp(!,UnaryOp(!,Id(c))))))]))])])"
        self.assertTrue(TestAST.test(input,expect,339))

    def test340(self):
        input = """ Class Program {
                        main() {
                            Out.printInt(Shape::$numOfShape);
                            Val x,y,z : Float = -a, --b, ---c;
                        }
                    }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(printInt),[FieldAccess(Id(Shape),Id($numOfShape))]),AttributeDecl(Instance,ConstDecl(Id(x),FloatType,UnaryOp(-,Id(a)))),AttributeDecl(Instance,ConstDecl(Id(y),FloatType,UnaryOp(-,UnaryOp(-,Id(b))))),AttributeDecl(Instance,ConstDecl(Id(z),FloatType,UnaryOp(-,UnaryOp(-,UnaryOp(-,Id(c))))))]))])])"
        self.assertTrue(TestAST.test(input,expect,340))
    
    def test341(self):
        input = """ Class Program {
                        main() {
                            Out.printInt(Shape::$numOfShape);
                            Val x,y,z : Float = arr[1], arr[2][3], arr[x][y];
                        }
                    }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(printInt),[FieldAccess(Id(Shape),Id($numOfShape))]),AttributeDecl(Instance,ConstDecl(Id(x),FloatType,ArrayCell(Id(arr),[IntLit(1)]))),AttributeDecl(Instance,ConstDecl(Id(y),FloatType,ArrayCell(Id(arr),[IntLit(2),IntLit(3)]))),AttributeDecl(Instance,ConstDecl(Id(z),FloatType,ArrayCell(Id(arr),[Id(x),Id(y)])))]))])])"
        self.assertTrue(TestAST.test(input,expect,341))

    def test342(self):
        input = """ Class Program {
                        main() {
                            Out.printInt(Shape::$numOfShape);
                            Val x,y,z,t : Float = a.b, a::$b, a.b(), a::$b();
                        }
                    }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(printInt),[FieldAccess(Id(Shape),Id($numOfShape))]),AttributeDecl(Instance,ConstDecl(Id(x),FloatType,FieldAccess(Id(a),Id(b)))),AttributeDecl(Instance,ConstDecl(Id(y),FloatType,FieldAccess(Id(a),Id($b)))),AttributeDecl(Instance,ConstDecl(Id(z),FloatType,CallExpr(Id(a),Id(b),[]))),AttributeDecl(Instance,ConstDecl(Id(t),FloatType,CallExpr(Id(a),Id($b),[])))]))])])"
        self.assertTrue(TestAST.test(input,expect,342))

    def test343(self):
        input = """ Class Program {
                        main() {
                            Out.printInt(Shape::$numOfShape);
                            Val x : A = New A();
                            Val y : B = New B(a);
                        }
                    }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(printInt),[FieldAccess(Id(Shape),Id($numOfShape))]),AttributeDecl(Instance,ConstDecl(Id(x),ClassType(Id(A)),NewExpr(Id(A),[]))),AttributeDecl(Instance,ConstDecl(Id(y),ClassType(Id(B)),NewExpr(Id(B),[Id(a)])))]))])])"
        self.assertTrue(TestAST.test(input,expect,343))
    
    def test344(self):
        input = """ Class Program {
                        main() {
                            Out.printInt(Shape::$numOfShape);
                            Val x,y,z : Float = (a + b) * c, a - (b / c.b()), c;
                        }
                    }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(printInt),[FieldAccess(Id(Shape),Id($numOfShape))]),AttributeDecl(Instance,ConstDecl(Id(x),FloatType,BinaryOp(*,BinaryOp(+,Id(a),Id(b)),Id(c)))),AttributeDecl(Instance,ConstDecl(Id(y),FloatType,BinaryOp(-,Id(a),BinaryOp(/,Id(b),CallExpr(Id(c),Id(b),[]))))),AttributeDecl(Instance,ConstDecl(Id(z),FloatType,Id(c)))]))])])"
        self.assertTrue(TestAST.test(input,expect,344))

    def test345(self):
        input = """ Class Program {
                        main() {
                            Out.printInt(Shape::$numOfShape);
                            Val x,y,z : Boolean = True, False, True || False;
                        }
                    }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(printInt),[FieldAccess(Id(Shape),Id($numOfShape))]),AttributeDecl(Instance,ConstDecl(Id(x),BoolType,BooleanLit(True))),AttributeDecl(Instance,ConstDecl(Id(y),BoolType,BooleanLit(False))),AttributeDecl(Instance,ConstDecl(Id(z),BoolType,BinaryOp(||,BooleanLit(True),BooleanLit(False))))]))])])"
        self.assertTrue(TestAST.test(input,expect,345))

    def test346(self):
        input = """ Class Program {
                        main() {
                            Out.printInt(Shape::$numOfShape);
                            Val x,y,z : String = "She is tall", "He asked me: '"Where's John?'"", "He asked me: '"He asked: '"Where's John?'"'"";
                        }
                    }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(printInt),[FieldAccess(Id(Shape),Id($numOfShape))]),AttributeDecl(Instance,ConstDecl(Id(x),StringType,StringLit(She is tall))),AttributeDecl(Instance,ConstDecl(Id(y),StringType,StringLit(He asked me: 'Where's John?'))),AttributeDecl(Instance,ConstDecl(Id(z),StringType,StringLit(He asked me: 'He asked: 'Where's John?'')))]))])])"
        self.assertTrue(TestAST.test(input,expect,346))
    
    def test347(self):
        input = """ Class Program {
                        main() {
                            Out.printInt(Shape::$numOfShape);
                            Val x : Float = $sum;
                            Val y : A = Null;
                        }
                    }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(printInt),[FieldAccess(Id(Shape),Id($numOfShape))]),AttributeDecl(Instance,ConstDecl(Id(x),FloatType,Id($sum))),AttributeDecl(Instance,ConstDecl(Id(y),ClassType(Id(A)),NullLiteral()))]))])])"
        self.assertTrue(TestAST.test(input,expect,347))

    def test348(self):
        input = """ Class Program {
                        main() {
                            Out.printInt(Shape::$numOfShape);
                            Val x : Float = a.recursive();
                        }
                    }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(printInt),[FieldAccess(Id(Shape),Id($numOfShape))]),AttributeDecl(Instance,ConstDecl(Id(x),FloatType,CallExpr(Id(a),Id(recursive),[])))]))])])"
        self.assertTrue(TestAST.test(input,expect,348))

    def test349(self):
        input = """ Class Program {
                        main() {
                            Out.printInt(Shape::$numOfShape);
                            Val x : Float = b::$recursive(a,b);
                        }
                    }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(printInt),[FieldAccess(Id(Shape),Id($numOfShape))]),AttributeDecl(Instance,ConstDecl(Id(x),FloatType,CallExpr(Id(b),Id($recursive),[Id(a),Id(b)])))]))])])"
        self.assertTrue(TestAST.test(input,expect,349))
    
    def test350(self):
        input = """ Class Program {
                        main() {
                            Out.printInt(Shape::$numOfShape);
                            Val x : Float = $sum;
                            Val y : A = Null;
                        }
                        getHeight(a : Int; b : Array[Int, 3]) {
                            a.b(a.b);
                        }
                    }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(printInt),[FieldAccess(Id(Shape),Id($numOfShape))]),AttributeDecl(Instance,ConstDecl(Id(x),FloatType,Id($sum))),AttributeDecl(Instance,ConstDecl(Id(y),ClassType(Id(A)),NullLiteral()))])),MethodDecl(Id(getHeight),Instance,[param(Id(a),IntType),param(Id(b),ArrayType(IntLit(3),IntType))],Block([Call(Id(a),Id(b),[FieldAccess(Id(a),Id(b))])]))])])"
        self.assertTrue(TestAST.test(input,expect,350))

    def test351(self):
        input = """ Class Program {
                        main() {
                            Out.printInt(Shape::$numOfShape);
                            Val x : Float = $sum;
                            Val y : A = Null;
                        }
                        getHeight(a : Int; b : Array[Int, 3]) {
                            a = Null;
                        }
                        getWidth(a : Float; B : A) {
                            a = arr[3][4][6];
                        }
                    }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(printInt),[FieldAccess(Id(Shape),Id($numOfShape))]),AttributeDecl(Instance,ConstDecl(Id(x),FloatType,Id($sum))),AttributeDecl(Instance,ConstDecl(Id(y),ClassType(Id(A)),NullLiteral()))])),MethodDecl(Id(getHeight),Instance,[param(Id(a),IntType),param(Id(b),ArrayType(IntLit(3),IntType))],Block([AssignStmt(Id(a),NullLiteral())])),MethodDecl(Id(getWidth),Instance,[param(Id(a),FloatType),param(Id(B),ClassType(Id(A)))],Block([AssignStmt(Id(a),ArrayCell(Id(arr),[IntLit(3),IntLit(4),IntLit(6)]))]))])])"
        self.assertTrue(TestAST.test(input,expect,351))

    def test352(self):
        input = """ Class Program {
                        main() {
                            Out.printInt(Shape::$numOfShape);
                            Val x : Float = $sum;
                            Val y : A = Null;
                        }
                        getHeight(a : Int; b : Array[Int, 3]) {
                            a = New A(a);
                            b = Null;
                        }
                        getWidth(a :  Float; B : A) {
                            a = arr[3][4][6];
                        }
                    }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(printInt),[FieldAccess(Id(Shape),Id($numOfShape))]),AttributeDecl(Instance,ConstDecl(Id(x),FloatType,Id($sum))),AttributeDecl(Instance,ConstDecl(Id(y),ClassType(Id(A)),NullLiteral()))])),MethodDecl(Id(getHeight),Instance,[param(Id(a),IntType),param(Id(b),ArrayType(IntLit(3),IntType))],Block([AssignStmt(Id(a),NewExpr(Id(A),[Id(a)])),AssignStmt(Id(b),NullLiteral())])),MethodDecl(Id(getWidth),Instance,[param(Id(a),FloatType),param(Id(B),ClassType(Id(A)))],Block([AssignStmt(Id(a),ArrayCell(Id(arr),[IntLit(3),IntLit(4),IntLit(6)]))]))])])"
        self.assertTrue(TestAST.test(input,expect,352))
    
    def test353(self):
        input = """ Class Program {
                        main() {
                            Out.printInt(Shape::$numOfShape);
                            Val x : Float = $sum;
                            Val y : A = Null;
                        }
                        getHeight(a : Int; b : Array[Int, 3]) {
                            a = New A(a,b);
                            b = Null;
                        }
                        getWidth(a :  Float; B : A) {
                            If (a == b) {
                                Return a + arr[3][4][6];
                            }
                        }
                    }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(printInt),[FieldAccess(Id(Shape),Id($numOfShape))]),AttributeDecl(Instance,ConstDecl(Id(x),FloatType,Id($sum))),AttributeDecl(Instance,ConstDecl(Id(y),ClassType(Id(A)),NullLiteral()))])),MethodDecl(Id(getHeight),Instance,[param(Id(a),IntType),param(Id(b),ArrayType(IntLit(3),IntType))],Block([AssignStmt(Id(a),NewExpr(Id(A),[Id(a),Id(b)])),AssignStmt(Id(b),NullLiteral())])),MethodDecl(Id(getWidth),Instance,[param(Id(a),FloatType),param(Id(B),ClassType(Id(A)))],Block([If(BinaryOp(==,Id(a),Id(b)),Block([Return(BinaryOp(+,Id(a),ArrayCell(Id(arr),[IntLit(3),IntLit(4),IntLit(6)])))]))]))])])"
        self.assertTrue(TestAST.test(input,expect,353))

    def test354(self):
        input = """ Class Program {
                        main() {
                            Out.printInt(Shape::$numOfShape);
                            Val x : Float = $sum;
                            Val y : A = Null;
                        }
                        getHeight(a : Int; b : Array[Int, 3]) {
                            a = New A(a,b,c);
                            b = Null;
                        }
                        getWidth(a :  Float; B : A) {
                            If (a == b) {
                                Return a;
                            }
                            Elseif (a > b) {
                                Break;
                            }
                            Elseif(a < b) {
                                Continue;
                            }
                        }
                    }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(printInt),[FieldAccess(Id(Shape),Id($numOfShape))]),AttributeDecl(Instance,ConstDecl(Id(x),FloatType,Id($sum))),AttributeDecl(Instance,ConstDecl(Id(y),ClassType(Id(A)),NullLiteral()))])),MethodDecl(Id(getHeight),Instance,[param(Id(a),IntType),param(Id(b),ArrayType(IntLit(3),IntType))],Block([AssignStmt(Id(a),NewExpr(Id(A),[Id(a),Id(b),Id(c)])),AssignStmt(Id(b),NullLiteral())])),MethodDecl(Id(getWidth),Instance,[param(Id(a),FloatType),param(Id(B),ClassType(Id(A)))],Block([If(BinaryOp(==,Id(a),Id(b)),Block([Return(Id(a))]),If(BinaryOp(>,Id(a),Id(b)),Block([Break]),If(BinaryOp(<,Id(a),Id(b)),Block([Continue]))))]))])])"
        self.assertTrue(TestAST.test(input,expect,354))

    def test355(self):
        input = """ Class Program {
                        main() {
                            Out.printInt(Shape::$numOfShape);
                            Val x : Float = $sum;
                            Val y : A = Null;
                        }
                        getHeight(a : Int; b : Array[Int, 3]) {
                            a = New A(a,b);
                            b = Null;
                        }
                        getWidth(a :  Float; B : A) {
                            If (a == b) {
                                Return a;
                            }
                            Elseif (a > b) {
                                Break;
                            }
                            Elseif(a < b) {
                                Continue;
                            }
                            Else {
                                a = arr[3][4][6];
                            }
                        }
                    }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(printInt),[FieldAccess(Id(Shape),Id($numOfShape))]),AttributeDecl(Instance,ConstDecl(Id(x),FloatType,Id($sum))),AttributeDecl(Instance,ConstDecl(Id(y),ClassType(Id(A)),NullLiteral()))])),MethodDecl(Id(getHeight),Instance,[param(Id(a),IntType),param(Id(b),ArrayType(IntLit(3),IntType))],Block([AssignStmt(Id(a),NewExpr(Id(A),[Id(a),Id(b)])),AssignStmt(Id(b),NullLiteral())])),MethodDecl(Id(getWidth),Instance,[param(Id(a),FloatType),param(Id(B),ClassType(Id(A)))],Block([If(BinaryOp(==,Id(a),Id(b)),Block([Return(Id(a))]),If(BinaryOp(>,Id(a),Id(b)),Block([Break]),If(BinaryOp(<,Id(a),Id(b)),Block([Continue]),Block([AssignStmt(Id(a),ArrayCell(Id(arr),[IntLit(3),IntLit(4),IntLit(6)]))]))))]))])])"
        self.assertTrue(TestAST.test(input,expect,355))
    
    def test356(self):
        input = """ Class Program {
                        main() {
                            Out.printInt(Shape::$numOfShape);
                            Val x : Float = $sum;
                            Val y : A = Null;
                        }
                        getHeight(a : Int; b : Array[Int, 3]) {
                            a = New A(a);
                            b = Null;
                        }
                        getWidth(a :  Float; B : A) {
                            If (a == b) {
                                Return a;
                            }
                            Elseif (a > b) {
                                Break;
                            }
                            Elseif(a < b) {
                                Continue;
                            }
                            Else {
                                Val a : Int = 0;
                            }
                        }
                    }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(printInt),[FieldAccess(Id(Shape),Id($numOfShape))]),AttributeDecl(Instance,ConstDecl(Id(x),FloatType,Id($sum))),AttributeDecl(Instance,ConstDecl(Id(y),ClassType(Id(A)),NullLiteral()))])),MethodDecl(Id(getHeight),Instance,[param(Id(a),IntType),param(Id(b),ArrayType(IntLit(3),IntType))],Block([AssignStmt(Id(a),NewExpr(Id(A),[Id(a)])),AssignStmt(Id(b),NullLiteral())])),MethodDecl(Id(getWidth),Instance,[param(Id(a),FloatType),param(Id(B),ClassType(Id(A)))],Block([If(BinaryOp(==,Id(a),Id(b)),Block([Return(Id(a))]),If(BinaryOp(>,Id(a),Id(b)),Block([Break]),If(BinaryOp(<,Id(a),Id(b)),Block([Continue]),Block([AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(0)))]))))]))])])"
        self.assertTrue(TestAST.test(input,expect,356))
    def test357(self):
        input = """ Class Program {
                        main() {
                            Out.printInt(Shape::$numOfShape);
                            Val x : Float = $sum;
                            Val y : A = Null;
                        }
                        getHeight(a : Int; b : Array[Int, 3]) {
                            a = New A();
                            b = Null;
                        }
                        getWidth(a :  Float; B : A) {
                            Foreach (i In 1 .. 100 By 2) {
                                Out.printInt(i);
                            }
                        }
                    }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(printInt),[FieldAccess(Id(Shape),Id($numOfShape))]),AttributeDecl(Instance,ConstDecl(Id(x),FloatType,Id($sum))),AttributeDecl(Instance,ConstDecl(Id(y),ClassType(Id(A)),NullLiteral()))])),MethodDecl(Id(getHeight),Instance,[param(Id(a),IntType),param(Id(b),ArrayType(IntLit(3),IntType))],Block([AssignStmt(Id(a),NewExpr(Id(A),[])),AssignStmt(Id(b),NullLiteral())])),MethodDecl(Id(getWidth),Instance,[param(Id(a),FloatType),param(Id(B),ClassType(Id(A)))],Block([For(Id(i),IntLit(1),IntLit(100),IntLit(2),Block([Call(Id(Out),Id(printInt),[Id(i)])])])]))])])"
        self.assertTrue(TestAST.test(input,expect,357))

    def test358(self):
        input = """ Class Program {
                        main() {
                            Out.printInt(Shape::$numOfShape);
                            Val x : Float = $sum;
                            Val y : A = Null;
                        }
                        getHeight(a : Int; b : Array[Int, 3]) {
                            a = New A();
                            b = Null;
                        }
                        getWidth(a :  Float; B : A) {
                            Foreach (i In 1 .. 100 By 2) {
                                Out.printInt(i);
                                Foreach (i In 1 .. 100 By 2) {
                                    Out.printInt(i);
                                    Foreach (i In 1 .. 100 By 2) {
                                        Out.printInt(i);
                                    }
                                }
                            }
                        }
                    }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(printInt),[FieldAccess(Id(Shape),Id($numOfShape))]),AttributeDecl(Instance,ConstDecl(Id(x),FloatType,Id($sum))),AttributeDecl(Instance,ConstDecl(Id(y),ClassType(Id(A)),NullLiteral()))])),MethodDecl(Id(getHeight),Instance,[param(Id(a),IntType),param(Id(b),ArrayType(IntLit(3),IntType))],Block([AssignStmt(Id(a),NewExpr(Id(A),[])),AssignStmt(Id(b),NullLiteral())])),MethodDecl(Id(getWidth),Instance,[param(Id(a),FloatType),param(Id(B),ClassType(Id(A)))],Block([For(Id(i),IntLit(1),IntLit(100),IntLit(2),Block([Call(Id(Out),Id(printInt),[Id(i)]),For(Id(i),IntLit(1),IntLit(100),IntLit(2),Block([Call(Id(Out),Id(printInt),[Id(i)]),For(Id(i),IntLit(1),IntLit(100),IntLit(2),Block([Call(Id(Out),Id(printInt),[Id(i)])])])])])])])]))])])"
        self.assertTrue(TestAST.test(input,expect,358))
    
    def test359(self):
        input = """ Class Program {
                        main() {
                            Out.printInt(Shape::$numOfShape);
                            Val x : Float = $sum;
                            Val y : A = Null;
                        }
                        getHeight(a : Int; b : Array[Int, 3]) {
                            a = New A();
                            b = Null;
                        }
                        getWidth(a :  Float; B : A) {
                            If (a == b) {
                                Return a;
                                Foreach (i In 1 .. 100 By 2) {
                                    Out.printInt(i);
                                }
                            }
                        }
                    }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(printInt),[FieldAccess(Id(Shape),Id($numOfShape))]),AttributeDecl(Instance,ConstDecl(Id(x),FloatType,Id($sum))),AttributeDecl(Instance,ConstDecl(Id(y),ClassType(Id(A)),NullLiteral()))])),MethodDecl(Id(getHeight),Instance,[param(Id(a),IntType),param(Id(b),ArrayType(IntLit(3),IntType))],Block([AssignStmt(Id(a),NewExpr(Id(A),[])),AssignStmt(Id(b),NullLiteral())])),MethodDecl(Id(getWidth),Instance,[param(Id(a),FloatType),param(Id(B),ClassType(Id(A)))],Block([If(BinaryOp(==,Id(a),Id(b)),Block([Return(Id(a)),For(Id(i),IntLit(1),IntLit(100),IntLit(2),Block([Call(Id(Out),Id(printInt),[Id(i)])])])]))]))])])"
        self.assertTrue(TestAST.test(input,expect,359))
    def test360(self):
        input = """ Class Program {
                        main() {
                            Out.printInt(Shape::$numOfShape);
                            Val x : Float = $sum;
                            Val y : A = Null;
                        }
                        getHeight(a : Int; b : Array[Int, 3]) {
                            a = New A(1.0);
                            b = Null;
                        }
                        getWidth(a :  Float; B : A) {
                            If (a == b) {
                                Return a;
                                Foreach (i In 1 .. 100 By 2) {
                                    Out.printInt(i);
                                }
                            }
                            Foreach (i In 1 .. 100 By 2) {
                                Out.printInt(i);
                                If (a == b) {
                                    Return a;
                                    Foreach (i In 1 .. 100 By 2) {
                                        Out.printInt(i);
                                    }
                                }
                            }
                        }
                    }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(printInt),[FieldAccess(Id(Shape),Id($numOfShape))]),AttributeDecl(Instance,ConstDecl(Id(x),FloatType,Id($sum))),AttributeDecl(Instance,ConstDecl(Id(y),ClassType(Id(A)),NullLiteral()))])),MethodDecl(Id(getHeight),Instance,[param(Id(a),IntType),param(Id(b),ArrayType(IntLit(3),IntType))],Block([AssignStmt(Id(a),NewExpr(Id(A),[FloatLit(1.0)])),AssignStmt(Id(b),NullLiteral())])),MethodDecl(Id(getWidth),Instance,[param(Id(a),FloatType),param(Id(B),ClassType(Id(A)))],Block([If(BinaryOp(==,Id(a),Id(b)),Block([Return(Id(a)),For(Id(i),IntLit(1),IntLit(100),IntLit(2),Block([Call(Id(Out),Id(printInt),[Id(i)])])])])),For(Id(i),IntLit(1),IntLit(100),IntLit(2),Block([Call(Id(Out),Id(printInt),[Id(i)]),If(BinaryOp(==,Id(a),Id(b)),Block([Return(Id(a)),For(Id(i),IntLit(1),IntLit(100),IntLit(2),Block([Call(Id(Out),Id(printInt),[Id(i)])])])]))])])]))])])"
        self.assertTrue(TestAST.test(input,expect,360))

    def test361(self):
        input = """ Class Program {
                        main() {
                            Out.printInt(Shape::$numOfShape);
                            Val x : Float = $sum;
                            Val y : A = Null;
                        }
                        getHeight(a : Int; b : Array[Int, 3]) {
                            a = New A();
                            b = Null;
                        }
                        getWidth(a :  Float; B : A) {
                            If (a == b) {
                                Return a;
                                Foreach (i In 1 .. 100 By 2) {
                                    Out.printInt(i);
                                }
                            }
                            Elseif (a > b) {
                                Break;
                            }
                            Elseif(a < b) {
                                Continue;
                                Foreach (i In 1 .. 100 By 2) {
                                    Out.printInt(i);
                                }
                            }
                        }
                    }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(printInt),[FieldAccess(Id(Shape),Id($numOfShape))]),AttributeDecl(Instance,ConstDecl(Id(x),FloatType,Id($sum))),AttributeDecl(Instance,ConstDecl(Id(y),ClassType(Id(A)),NullLiteral()))])),MethodDecl(Id(getHeight),Instance,[param(Id(a),IntType),param(Id(b),ArrayType(IntLit(3),IntType))],Block([AssignStmt(Id(a),NewExpr(Id(A),[])),AssignStmt(Id(b),NullLiteral())])),MethodDecl(Id(getWidth),Instance,[param(Id(a),FloatType),param(Id(B),ClassType(Id(A)))],Block([If(BinaryOp(==,Id(a),Id(b)),Block([Return(Id(a)),For(Id(i),IntLit(1),IntLit(100),IntLit(2),Block([Call(Id(Out),Id(printInt),[Id(i)])])])]),If(BinaryOp(>,Id(a),Id(b)),Block([Break]),If(BinaryOp(<,Id(a),Id(b)),Block([Continue,For(Id(i),IntLit(1),IntLit(100),IntLit(2),Block([Call(Id(Out),Id(printInt),[Id(i)])])])]))))]))])])"
        self.assertTrue(TestAST.test(input,expect,361))
    
    def test362(self):
        input = """ Class Program {
                        main() {
                            Out.printInt(Shape::$numOfShape);
                            Val x : Float = $sum;
                            Val y : A = Null;
                        }
                        getHeight(a : Int; b : Array[Int, 3]) {
                            a = New A();
                            b = Null;
                        }
                        getWidth(a :  Float; B : A) {
                            If (a == b) {
                                Return a;
                                Foreach (i In 1 .. 100 By 2) {
                                    Out.printInt(i);
                                    If (a == b) {
                                        Return a;
                                    }
                                    Elseif (a > b) {
                                        Break;
                                    }
                                    Elseif(a < b) {
                                        Continue;
                                    }
                                    Else {
                                        Val a : Int = 0;
                                    }
                                }
                            }
                        }
                    }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(printInt),[FieldAccess(Id(Shape),Id($numOfShape))]),AttributeDecl(Instance,ConstDecl(Id(x),FloatType,Id($sum))),AttributeDecl(Instance,ConstDecl(Id(y),ClassType(Id(A)),NullLiteral()))])),MethodDecl(Id(getHeight),Instance,[param(Id(a),IntType),param(Id(b),ArrayType(IntLit(3),IntType))],Block([AssignStmt(Id(a),NewExpr(Id(A),[])),AssignStmt(Id(b),NullLiteral())])),MethodDecl(Id(getWidth),Instance,[param(Id(a),FloatType),param(Id(B),ClassType(Id(A)))],Block([If(BinaryOp(==,Id(a),Id(b)),Block([Return(Id(a)),For(Id(i),IntLit(1),IntLit(100),IntLit(2),Block([Call(Id(Out),Id(printInt),[Id(i)]),If(BinaryOp(==,Id(a),Id(b)),Block([Return(Id(a))]),If(BinaryOp(>,Id(a),Id(b)),Block([Break]),If(BinaryOp(<,Id(a),Id(b)),Block([Continue]),Block([AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(0)))]))))])])]))]))])])"
        self.assertTrue(TestAST.test(input,expect,362))

    def test363(self):
        input = """ Class Program {
                        main() {
                            Out.printInt(Shape::$numOfShape);
                            Val x : Float = $sum;
                            Val y : A = Null;
                        }
                        getHeight(a : Int; b : Array[Int, 3]) {
                            a = New A();
                            b = Null;
                        }
                        getWidth(a :  Float; B : A) {
                            If (a == b) {
                                Return a;
                                Foreach (i In 1 .. 100 By 2) {
                                    Out.printInt(i);
                                }
                            }
                            If (a == b) {
                                        Return a;
                                    }
                                    Elseif (a > b) {
                                        Break;
                                    }
                                    Elseif(a < b) {
                                        Continue;
                                        If (a == b) {
                                            Return a;
                                        }
                                        Elseif (a > b) {
                                            Break;
                                        }
                                        Elseif(a < b) {
                                            Continue;
                                        }
                                        Else {
                                            Val a : Int = 0;
                                        }
                                    }
                                    Else {
                                        Val a : Int = 0;
                                    }
                        }
                    }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(printInt),[FieldAccess(Id(Shape),Id($numOfShape))]),AttributeDecl(Instance,ConstDecl(Id(x),FloatType,Id($sum))),AttributeDecl(Instance,ConstDecl(Id(y),ClassType(Id(A)),NullLiteral()))])),MethodDecl(Id(getHeight),Instance,[param(Id(a),IntType),param(Id(b),ArrayType(IntLit(3),IntType))],Block([AssignStmt(Id(a),NewExpr(Id(A),[])),AssignStmt(Id(b),NullLiteral())])),MethodDecl(Id(getWidth),Instance,[param(Id(a),FloatType),param(Id(B),ClassType(Id(A)))],Block([If(BinaryOp(==,Id(a),Id(b)),Block([Return(Id(a)),For(Id(i),IntLit(1),IntLit(100),IntLit(2),Block([Call(Id(Out),Id(printInt),[Id(i)])])])])),If(BinaryOp(==,Id(a),Id(b)),Block([Return(Id(a))]),If(BinaryOp(>,Id(a),Id(b)),Block([Break]),If(BinaryOp(<,Id(a),Id(b)),Block([Continue,If(BinaryOp(==,Id(a),Id(b)),Block([Return(Id(a))]),If(BinaryOp(>,Id(a),Id(b)),Block([Break]),If(BinaryOp(<,Id(a),Id(b)),Block([Continue]),Block([AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(0)))]))))]),Block([AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(0)))]))))]))])])"
        self.assertTrue(TestAST.test(input,expect,363))

    def test364(self):
        input = """ Class main {}
                    Class Program {}
                    Class Rectangle : Shape {}"""
        expect = "Program([ClassDecl(Id(main),[]),ClassDecl(Id(Program),[]),ClassDecl(Id(Rectangle),Id(Shape),[])])"
        self.assertTrue(TestAST.test(input,expect,364))
    
    def test365(self):
        input = """ Class main {
                        getArea() {
                            Shape::$getArea(a);
                        }
                    }
                    Class Program {}
                    Class Rectangle : Shape {}"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(getArea),Instance,[],Block([Call(Id(Shape),Id($getArea),[Id(a)])]))]),ClassDecl(Id(Program),[]),ClassDecl(Id(Rectangle),Id(Shape),[])])"
        self.assertTrue(TestAST.test(input,expect,365))
    
    def test366(self):
        input = """ Class main {
                        getArea() {
                            Shape ::$getArea(a);
                        }
                    }
                    Class Program {
                        getArea() {
                            Shape.getArea(a);
                        }
                    }
                    Class Rectangle : Shape {}"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(getArea),Instance,[],Block([Call(Id(Shape),Id($getArea),[Id(a)])]))]),ClassDecl(Id(Program),[MethodDecl(Id(getArea),Instance,[],Block([Call(Id(Shape),Id(getArea),[Id(a)])]))]),ClassDecl(Id(Rectangle),Id(Shape),[])])"
        self.assertTrue(TestAST.test(input,expect,366))

    def test367(self):
        input = """ Class main {
                        getArea() {
                            Shape::$getArea(a);
                        }
                    }
                    Class Program {
                        getArea() {
                            Shape.getArea(a);
                        }
                    }
                    Class Rectangle : Shape {
                        getArea() {
                           Shape::$getArea(1_234.5);
                        }
                    }"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(getArea),Instance,[],Block([Call(Id(Shape),Id($getArea),[Id(a)])]))]),ClassDecl(Id(Program),[MethodDecl(Id(getArea),Instance,[],Block([Call(Id(Shape),Id(getArea),[Id(a)])]))]),ClassDecl(Id(Rectangle),Id(Shape),[MethodDecl(Id(getArea),Instance,[],Block([Call(Id(Shape),Id($getArea),[FloatLit(1234.5)])]))])])"
        self.assertTrue(TestAST.test(input,expect,367))
    
    def test368(self):
        input = """ Class main {
                        getArea() {
                            Shape ::$getArea(a);
                        }
                    }
                    Class Program {
                        getArea() {
                            Shape.getArea(a);
                        }
                    }
                    Class Rectangle : Shape {
                        getArea() {
                            Shape.getArea(Self.a);
                        }
                    }"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(getArea),Instance,[],Block([Call(Id(Shape),Id($getArea),[Id(a)])]))]),ClassDecl(Id(Program),[MethodDecl(Id(getArea),Instance,[],Block([Call(Id(Shape),Id(getArea),[Id(a)])]))]),ClassDecl(Id(Rectangle),Id(Shape),[MethodDecl(Id(getArea),Instance,[],Block([Call(Id(Shape),Id(getArea),[FieldAccess(Self(),Id(a))])]))])])"
        self.assertTrue(TestAST.test(input,expect,368))

    def test369(self):
        input = """ Class main {
                        getArea() {
                            Shape::$getArea(a);
                        }
                    }
                    Class Program {
                        getArea() {
                            Shape.getArea = arr[3];
                        }
                    } """
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(getArea),Instance,[],Block([Call(Id(Shape),Id($getArea),[Id(a)])]))]),ClassDecl(Id(Program),[MethodDecl(Id(getArea),Instance,[],Block([AssignStmt(FieldAccess(Id(Shape),Id(getArea)),ArrayCell(Id(arr),[IntLit(3)]))]))])])"
        self.assertTrue(TestAST.test(input,expect,369))

    def test370(self):
        input = """ Class Program {
                        getArea() {
                            Shape.getArea = arr[x];
                        }
                    } """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(getArea),Instance,[],Block([AssignStmt(FieldAccess(Id(Shape),Id(getArea)),ArrayCell(Id(arr),[Id(x)]))]))])])"
        self.assertTrue(TestAST.test(input,expect,370))
    
    def test371(self):
        input = """ Class Program {
                        getArea() {
                            Shape.getArea = arr[1] + arr[2] ;
                        }
                    } """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(getArea),Instance,[],Block([AssignStmt(FieldAccess(Id(Shape),Id(getArea)),BinaryOp(+,ArrayCell(Id(arr),[IntLit(1)]),ArrayCell(Id(arr),[IntLit(2)])))]))])])"
        self.assertTrue(TestAST.test(input,expect,371))

    def test372(self):
        input = """ Class Program {
                        getArea() {
                            Shape.getArea = arr[x] - arr[y];
                        }
                    } """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(getArea),Instance,[],Block([AssignStmt(FieldAccess(Id(Shape),Id(getArea)),BinaryOp(-,ArrayCell(Id(arr),[Id(x)]),ArrayCell(Id(arr),[Id(y)])))]))])])"
        self.assertTrue(TestAST.test(input,expect,372))

    def test373(self):
        input = """ Class Program {
                        getArea() {
                            Shape.getArea = arr[x] * arr[u] / arr[z] % (arr[a] - arr[1]);
                        }
                    } """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(getArea),Instance,[],Block([AssignStmt(FieldAccess(Id(Shape),Id(getArea)),BinaryOp(%,BinaryOp(/,BinaryOp(*,ArrayCell(Id(arr),[Id(x)]),ArrayCell(Id(arr),[Id(u)])),ArrayCell(Id(arr),[Id(z)])),BinaryOp(-,ArrayCell(Id(arr),[Id(a)]),ArrayCell(Id(arr),[IntLit(1)]))))]))])])"
        self.assertTrue(TestAST.test(input,expect,373))
    
    def test374(self):
        input = """ Class Program {
                        getArea() {
                            arr[z] = Shape.getArea();
                        }
                    } """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(getArea),Instance,[],Block([AssignStmt(ArrayCell(Id(arr),[Id(z)]),CallExpr(Id(Shape),Id(getArea),[]))]))])])"
        self.assertTrue(TestAST.test(input,expect,374))

    def test375(self):
        input = """ Class Program {
                        getArea() {
                            arr[z] = Shape.getArea() || Shape::$num;
                        }
                    } """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(getArea),Instance,[],Block([AssignStmt(ArrayCell(Id(arr),[Id(z)]),BinaryOp(||,CallExpr(Id(Shape),Id(getArea),[]),FieldAccess(Id(Shape),Id($num))))]))])])"
        self.assertTrue(TestAST.test(input,expect,375))

    def test376(self):
        input = """ Class Program {
                        getArea() {
                            arr[z] = Shape.getArea() + arr[3][4];
                        }
                    } """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(getArea),Instance,[],Block([AssignStmt(ArrayCell(Id(arr),[Id(z)]),BinaryOp(+,CallExpr(Id(Shape),Id(getArea),[]),ArrayCell(Id(arr),[IntLit(3),IntLit(4)])))]))])])"
        self.assertTrue(TestAST.test(input,expect,376))
    
    def test377(self):
        input = """ Class Program {
                        getArea() {
                            arr[z] = Shape.getArea() + arr[3][4][4];
                        }
                    } """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(getArea),Instance,[],Block([AssignStmt(ArrayCell(Id(arr),[Id(z)]),BinaryOp(+,CallExpr(Id(Shape),Id(getArea),[]),ArrayCell(Id(arr),[IntLit(3),IntLit(4),IntLit(4)])))]))])])"
        self.assertTrue(TestAST.test(input,expect,377))
    
    def test378(self):
        input = """ Class Program {
                        getArea() {
                            arr[z] = arr[3];
                        }
                    } """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(getArea),Instance,[],Block([AssignStmt(ArrayCell(Id(arr),[Id(z)]),ArrayCell(Id(arr),[IntLit(3)]))]))])])"
        self.assertTrue(TestAST.test(input,expect,378))

    def test379(self):
        input = """ Class Program {
                        getArea() {
                            Foreach (x In 5 .. 2) {
                                Out.printInt(arr[x] + arr[3]);
                            }
                        }
                    } """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(getArea),Instance,[],Block([For(Id(x),IntLit(5),IntLit(2),IntLit(1),Block([Call(Id(Out),Id(printInt),[BinaryOp(+,ArrayCell(Id(arr),[Id(x)]),ArrayCell(Id(arr),[IntLit(3)]))])])])]))])])"
        self.assertTrue(TestAST.test(input,expect,379))
    
    def test380(self):
        input = """ Class Program {
                        getArea() {
                            Foreach (x In 5 .. 2) {
                                Out.printInt(arr[x] + arr[3]);
                                If (arr[d] == b) {
                                    Return a;
                                }
                                Elseif (arr[c] > b) {
                                    Break;
                                }
                                Elseif(a < b) {
                                    Continue;
                                }
                            }
                        }
                    } """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(getArea),Instance,[],Block([For(Id(x),IntLit(5),IntLit(2),IntLit(1),Block([Call(Id(Out),Id(printInt),[BinaryOp(+,ArrayCell(Id(arr),[Id(x)]),ArrayCell(Id(arr),[IntLit(3)]))]),If(BinaryOp(==,ArrayCell(Id(arr),[Id(d)]),Id(b)),Block([Return(Id(a))]),If(BinaryOp(>,ArrayCell(Id(arr),[Id(c)]),Id(b)),Block([Break]),If(BinaryOp(<,Id(a),Id(b)),Block([Continue]))))])])]))])])"
        self.assertTrue(TestAST.test(input,expect,380))

    def test381(self):
        input = """ Class Program {
                        getArea() {
                            Foreach (x In 5 .. 2) {
                                Out.printInt(arr[x] + arr[3]);
                                If (arr[d] == b) {
                                    Return a;
                                }
                                Elseif (arr[c] > b) {
                                    Break;
                                }
                                Elseif(a < b) {
                                    Continue;
                                    Foreach (x In 5 .. 2) {
                                        Out.printInt(arr[x] + arr[3]);
                                        If (arr[d] == b) {
                                            Return a;
                                        }
                                        Elseif (arr[c] > b) {
                                            Break;
                                        }
                                        Elseif(a < b) {
                                            Continue;
                                        }
                                    }
                                }
                            }
                        }
                    } """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(getArea),Instance,[],Block([For(Id(x),IntLit(5),IntLit(2),IntLit(1),Block([Call(Id(Out),Id(printInt),[BinaryOp(+,ArrayCell(Id(arr),[Id(x)]),ArrayCell(Id(arr),[IntLit(3)]))]),If(BinaryOp(==,ArrayCell(Id(arr),[Id(d)]),Id(b)),Block([Return(Id(a))]),If(BinaryOp(>,ArrayCell(Id(arr),[Id(c)]),Id(b)),Block([Break]),If(BinaryOp(<,Id(a),Id(b)),Block([Continue,For(Id(x),IntLit(5),IntLit(2),IntLit(1),Block([Call(Id(Out),Id(printInt),[BinaryOp(+,ArrayCell(Id(arr),[Id(x)]),ArrayCell(Id(arr),[IntLit(3)]))]),If(BinaryOp(==,ArrayCell(Id(arr),[Id(d)]),Id(b)),Block([Return(Id(a))]),If(BinaryOp(>,ArrayCell(Id(arr),[Id(c)]),Id(b)),Block([Break]),If(BinaryOp(<,Id(a),Id(b)),Block([Continue]))))])])]))))])])]))])])"
        self.assertTrue(TestAST.test(input,expect,381))

    def test382(self):
        input = """ Class Program {
                        getArea() {
                            Foreach (x In 5 .. 2) {
                                Out.printInt(arr[x] + arr[3]);
                                Var r, s: Int;
                                r = 2.0;
                                Var a, b: Array[Int, 5];
                                s = r * r * Self.myPI;
                                a[0] = s;
                            }
                        }
                    } """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(getArea),Instance,[],Block([For(Id(x),IntLit(5),IntLit(2),IntLit(1),Block([Call(Id(Out),Id(printInt),[BinaryOp(+,ArrayCell(Id(arr),[Id(x)]),ArrayCell(Id(arr),[IntLit(3)]))]),AttributeDecl(Instance,VarDecl(Id(r),IntType)),AttributeDecl(Instance,VarDecl(Id(s),IntType)),AssignStmt(Id(r),FloatLit(2.0)),AttributeDecl(Instance,VarDecl(Id(a),ArrayType(IntLit(5),IntType))),AttributeDecl(Instance,VarDecl(Id(b),ArrayType(IntLit(5),IntType))),AssignStmt(Id(s),BinaryOp(*,BinaryOp(*,Id(r),Id(r)),FieldAccess(Self(),Id(myPI)))),AssignStmt(ArrayCell(Id(a),[IntLit(0)]),Id(s))])])]))])])"
        self.assertTrue(TestAST.test(input,expect,382))
    
    def test383(self):
        input = """ Class Program {
                        getArea() {
                            Foreach (x In 5 .. 2) {
                                arr[x] = x * x;
                            }
                        }
                    } """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(getArea),Instance,[],Block([For(Id(x),IntLit(5),IntLit(2),IntLit(1),Block([AssignStmt(ArrayCell(Id(arr),[Id(x)]),BinaryOp(*,Id(x),Id(x)))])])]))])])"
        self.assertTrue(TestAST.test(input,expect,383))

    def test384(self):
        input = """ Class Program {
                        getArea() {
                            Foreach (x In 5 .. 2) {
                                arr[x] = x * x;
                                arr[3] = !a || !!b;
                            }
                        }
                    } """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(getArea),Instance,[],Block([For(Id(x),IntLit(5),IntLit(2),IntLit(1),Block([AssignStmt(ArrayCell(Id(arr),[Id(x)]),BinaryOp(*,Id(x),Id(x))),AssignStmt(ArrayCell(Id(arr),[IntLit(3)]),BinaryOp(||,UnaryOp(!,Id(a)),UnaryOp(!,UnaryOp(!,Id(b)))))])])]))])])"
        self.assertTrue(TestAST.test(input,expect,384))

    def test385(self):
        input = """ Class Program {
                        getArea() {
                            Foreach (x In 5 .. 2) {
                                x = 3 * !a;
                                arr[3] = !a || !!b;
                            }
                        }
                    } """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(getArea),Instance,[],Block([For(Id(x),IntLit(5),IntLit(2),IntLit(1),Block([AssignStmt(Id(x),BinaryOp(*,IntLit(3),UnaryOp(!,Id(a)))),AssignStmt(ArrayCell(Id(arr),[IntLit(3)]),BinaryOp(||,UnaryOp(!,Id(a)),UnaryOp(!,UnaryOp(!,Id(b)))))])])]))])])"
        self.assertTrue(TestAST.test(input,expect,385))
    
    def test386(self):
        input = """ Class Program {
                        getArea() {
                            Foreach (x In 5 .. 2 By 3) {
                                x = a +. b;
                                arr[3] = !a || !!b;
                            }
                        }
                    } """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(getArea),Instance,[],Block([For(Id(x),IntLit(5),IntLit(2),IntLit(3),Block([AssignStmt(Id(x),BinaryOp(+.,Id(a),Id(b))),AssignStmt(ArrayCell(Id(arr),[IntLit(3)]),BinaryOp(||,UnaryOp(!,Id(a)),UnaryOp(!,UnaryOp(!,Id(b)))))])])]))])])"
        self.assertTrue(TestAST.test(input,expect,386))

    def test387(self):
        input = """ Class Program {
                        getArea() {
                            Foreach (x In 5 .. 2) {
                               arr[x] = arr[x] * arr[x] + Self.a;
                            }
                        }
                    } """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(getArea),Instance,[],Block([For(Id(x),IntLit(5),IntLit(2),IntLit(1),Block([AssignStmt(ArrayCell(Id(arr),[Id(x)]),BinaryOp(+,BinaryOp(*,ArrayCell(Id(arr),[Id(x)]),ArrayCell(Id(arr),[Id(x)])),FieldAccess(Self(),Id(a))))])])]))])])"
        self.assertTrue(TestAST.test(input,expect,387))

    def test388(self):
        input = """ Class Program {
                        getArea() {
                            If (a == b) {
                                Return a;
                            }
                            Elseif (a > b) {
                                Break;
                                If (a == b) {
                                    Return a;
                                }
                                Elseif (a > b) {
                                    Break;
                                }
                                Elseif(a < b) {
                                    Continue;
                                }
                                Else {
                                    Val a : Int = 0;
                                }
                            }
                            Else {
                                Val a : Int = 0;
                                If (a == b) {
                                    Return a;
                                }
                                Elseif (a > b) {
                                    Break;
                                }
                                Elseif(a < b) {
                                    Continue;
                                }
                                Else {
                                    Val a : Int = 0;
                                }
                            }
                        }
                    } """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(getArea),Instance,[],Block([If(BinaryOp(==,Id(a),Id(b)),Block([Return(Id(a))]),If(BinaryOp(>,Id(a),Id(b)),Block([Break,If(BinaryOp(==,Id(a),Id(b)),Block([Return(Id(a))]),If(BinaryOp(>,Id(a),Id(b)),Block([Break]),If(BinaryOp(<,Id(a),Id(b)),Block([Continue]),Block([AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(0)))]))))]),Block([AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(0))),If(BinaryOp(==,Id(a),Id(b)),Block([Return(Id(a))]),If(BinaryOp(>,Id(a),Id(b)),Block([Break]),If(BinaryOp(<,Id(a),Id(b)),Block([Continue]),Block([AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(0)))]))))])))]))])])"
        self.assertTrue(TestAST.test(input,expect,388))
    
    def test389(self):
        input = """ Class Program {
                        getArea() {
                            Val a,b : A = New A(a,b), New A(a,c);
                        }
                    } """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(getArea),Instance,[],Block([AttributeDecl(Instance,ConstDecl(Id(a),ClassType(Id(A)),NewExpr(Id(A),[Id(a),Id(b)]))),AttributeDecl(Instance,ConstDecl(Id(b),ClassType(Id(A)),NewExpr(Id(A),[Id(a),Id(c)])))]))])])"
        self.assertTrue(TestAST.test(input,expect,389))

    def test390(self):
        input = """ Class Rectangle {
                        Var length: Int;
                    } """           
        expect = "Program([ClassDecl(Id(Rectangle),[AttributeDecl(Instance,VarDecl(Id(length),IntType))])])"
        self.assertTrue(TestAST.test(input,expect,390))

    def test391(self):
        input = """ Class Program {
            Var a, b, c: Int = 0x1A, 0x2B ,0x3C;
            main() {
                a = a + 0x4D + 0x2E6;
                b = b * 0x5EB42 + 0x6FA2F;
                Return c + b + a;
            }
        }
        """
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(0x1a))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(0x2b))),AttributeDecl(Instance,VarDecl(Id(c),IntType,IntLit(0x3c))),MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),BinaryOp(+,BinaryOp(+,Id(a),IntLit(0x4d)),IntLit(0x2e6))),AssignStmt(Id(b),BinaryOp(+,BinaryOp(*,Id(b),IntLit(0x5eb42)),IntLit(0x6fa2f))),Return(BinaryOp(+,BinaryOp(+,Id(c),Id(b)),Id(a)))]))])])"
        self.assertTrue(TestAST.test(input,expect,391))
    
    def test392(self):
        input = """ Class Program {
                        getArea() {
                            Val a,b,c : Int = 0b1001, 0x123, 012;
                            a = b;
                        }
                    } """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(getArea),Instance,[],Block([AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(0b1001))),AttributeDecl(Instance,ConstDecl(Id(b),IntType,IntLit(0x123))),AttributeDecl(Instance,ConstDecl(Id(c),IntType,IntLit(0o12))),AssignStmt(Id(a),Id(b))]))])])"
        self.assertTrue(TestAST.test(input,expect,392))

    def test393(self):
        input = """Class Rectangle {
                    Val a : String = "mewmew";
                    Var b : Float = 1e-3;
                    
                    Shape(){
                        If (3 > 2){
                            a = 5;
                        }
                    }
        }          
                   """
        expect = "Program([ClassDecl(Id(Rectangle),[AttributeDecl(Instance,ConstDecl(Id(a),StringType,StringLit(mewmew))),AttributeDecl(Instance,VarDecl(Id(b),FloatType,FloatLit(0.001))),MethodDecl(Id(Shape),Instance,[],Block([If(BinaryOp(>,IntLit(3),IntLit(2)),Block([AssignStmt(Id(a),IntLit(5))]))]))])])"
        self.assertTrue(TestAST.test(input,expect,393))

    def test394(self):
        input = """ Class Program {
                        getArea() {
                            ##Val a,b : A = New A(a,b), New A(a,c);##
                            Val a, b: Int = 2 + 5 - 9, 3 + 2 * 0;
                        }
                    } """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(getArea),Instance,[],Block([AttributeDecl(Instance,ConstDecl(Id(a),IntType,BinaryOp(-,BinaryOp(+,IntLit(2),IntLit(5)),IntLit(9)))),AttributeDecl(Instance,ConstDecl(Id(b),IntType,BinaryOp(+,IntLit(3),BinaryOp(*,IntLit(2),IntLit(0)))))]))])])"
        self.assertTrue(TestAST.test(input,expect,394))
    
    def test395(self):
        input = """ Class Program {
                        getArea() {
                            Val a : String = "";
                        }
                    } """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(getArea),Instance,[],Block([AttributeDecl(Instance,ConstDecl(Id(a),StringType,StringLit()))]))])])"
        self.assertTrue(TestAST.test(input,expect,395))

    def test396(self):
        input = """ Class Program {
                        getArea() {
                            a = "";
                        }
                    } """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(getArea),Instance,[],Block([AssignStmt(Id(a),StringLit())]))])])"
        self.assertTrue(TestAST.test(input,expect,396))

    def test397(self):
        input = """ Class Program {
                        getArea() {
                            a = "" +. "abc";
                            b = 0;
                        }
                    } """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(getArea),Instance,[],Block([AssignStmt(Id(a),BinaryOp(+.,StringLit(),StringLit(abc))),AssignStmt(Id(b),IntLit(0))]))])])"
        self.assertTrue(TestAST.test(input,expect,397))
    
    def test398(self):
        input = """ Class Program {
                        getArea() {
                            a = "" +. c;
                        }
                    } """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(getArea),Instance,[],Block([AssignStmt(Id(a),BinaryOp(+.,StringLit(),Id(c)))]))])])"
        self.assertTrue(TestAST.test(input,expect,398))

    def test399(self):
        input = """ Class Program {
                        Constructor(a : Int) {
                            arr[1] = 2;
                        }
                    } """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(Constructor),Instance,[param(Id(a),IntType)],Block([AssignStmt(ArrayCell(Id(arr),[IntLit(1)]),IntLit(2))]))])])"
        self.assertTrue(TestAST.test(input,expect,399))
