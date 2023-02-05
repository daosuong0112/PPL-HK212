import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test200(self):
        input = """ Class main{} """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,200))

    def test201(self):
        input = """ 
                    Class Rectangle: Shape {
                        getArea() { 
                            Return Self.length * Self.width; 
                        } 
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))
    
    def test202(self):
        input = """ 
                    Class Shape { 
                        $getNumOfShape( { 
                            Return Self.length * Self.width; 
                        } 
                    } 
                """
        expect = "Error on line 3 col 24: {"
        self.assertTrue(TestParser.test(input,expect,202))

    def test203(self):
        input = """ Class main{
                        Var a: Array[String, 3] = Array("Volvo", "22", "18");
                    } """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,203))

    def test204(self):
        input = """ Class main{
                        Var a: Array[Array[String,3], 3] = Array (
                            Array("Volvo", "22", "18"),
                            Array("Saab", "5", "2"),
                            Array("Land Rover", "17", "15")
                        ) ;
                    } """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,204))
    
    def test205(self):
        input = """ Class main{
                        Var a: Array[Array[String,3], 3] = Array (
                            Array("Volvo", "22", "18"),
                            Array("Saab", "5", "2"),
                            Array("Land Rover", "17", "15")
                        ) ;
                        getLength() {
                            Var r, s: Int;
                            r = 2.0;
                            Var a, b: Array[Int, 5];
                            s = r * r * Self.myPI;
                            a[0] = s;
                        }
                    } """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,205))

    def test206(self):
        input = """ Class main{
                        Var a: Array[Array[String,3], 3] = Array (
                            Array("Volvo", "22", "18"),
                            Array("Saab", "5", "2"),
                            Array("Land Rover", "17", "15")
                        ) ;
                        getLength() {
                            Var r, s: Int;
                            r = 2.0;
                            Var a, b: Array[Int, 5];
                            s = r * r * Self.myPI;
                            a[0] = s;
                            If (a == b) {}
                        }
                    } """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,206))

    def test207(self):
        input = """ Class main{
                        Var a: Array[Array[String,3], 3] = Array (
                            Array("Volvo", "22", "18"),
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
                                b = a - Shape.getArea() - Shape.width - Shape::$height;
                            }
                        }
                    } """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,207))
    
    def test208(self):
        input = """ Class main{
                        Var a : Float = 5.0;
                        Var b : String = "abc";
                        Var c : Int = 5;
                        Var d : Boolean = True;
                    } """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,208))

    def test209(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,209))

    def test210(self):
        input = """ Class main{
                        Var a : Float = 5.0;
                        Var b : String = "abc";
                        $getHeight() {
                            Val a : Int = -3;
                            Val b : Float = c + Shape::$height;
                        }
                    } """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,210))
    
    def test211(self):
        input = """ Class main{
                        Var a : Float = 5.0;
                        Var b : String = "abc";
                        $getHeight() {
                            Val a : Int = -3;
                            Val b : Float = c + Shape::$height;
                            Foreach (x In 5 .. 2) {
                                Out.printInt(arr[x]);
                            }
                        }
                    } """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,211))

    def test212(self):
        input = """ Class main{
                        Var a : Float = 5.0;
                        Var b : String = "abc";
                        $getHeight() {
                            Val a : Int = -3;
                            Val b : Float = c + Shape::$height;
                            Foreach (x In 5 .. 2 By 2) {
                                Out.printInt(arr[x]);
                            }
                        }
                    } """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,212))

    def test213(self):
        input = """ Class main{
                        Var a : Float = 5.0;
                        Var b : String = "abc";
                        $getHeight() {
                            Val a : Int = -3;
                            Val b : Float = c + Shape::$height;
                            Foreach (x In 5 .. 2 By 8) {
                                Foreach (x In 5 .. 2 By 2) {
                                    Out.printInt(arr[x]);
                                }
                            }
                        }
                    } """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,213))
    
    def test214(self):
        input = """ Class main{
                        Var a : Float = 5.0;
                        Var b : String = "abc";
                        $getHeight() {
                            Val a : Int = -3;
                            Val b : Float = c + Shape::$height;
                            Foreach (x In 5 .. 2 By 8) {
                                Foreach (x In 5 .. 2 By a) {
                                    Out.printInt(arr[x]);
                                }
                            }
                        }
                    } """
        expect = "Error on line 8 col 56: a"
        self.assertTrue(TestParser.test(input,expect,214))

    def test215(self):
        input = """ Class main{
                        Var a : Float = 5.0;
                        Var b : String = "abc";
                        $getHeight() {
                            Val a : Int = -3;
                            Val b : Float = c + Shape::$height;
                            Foreach (x In 5 .. 2 By 8) {
                                Foreach (x In 5 .. 2 By 2) {
                                    Out.printInt(arr[x]);
                                    Break;
                                }
                                Continue;
                            }
                        }
                    } """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,215))

    def test216(self):
        input = """ Class main{
                        Var a : Float = 5.0;
                        Var b : String = "abc";
                        $getHeight() {
                            Val a : Int = -3;
                            Val b : Float = c + Shape::$height;
                            Foreach (x In 5 .. 2 By 8) {
                                If (a == 2) {
                                    b = -2;
                                }
                                Foreach (x In 5 .. 2 By 2) {
                                    Out.printInt(arr[x]);
                                }
                            }
                        }
                    } """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,216))
    
    def test217(self):
        input = """ Class main{
                        Var a : Float = 5.0;
                        Var b : String = "abc";
                        $getHeight() {
                            Val a : Int = -3;
                            Val b : Float = c + Shape::$height;
                            Foreach (x In 5 .. 2 By 8) {
                                If (a ==. b) {
                                    Foreach (x In 5 .. 2 By 2) {
                                        Out.printInt(arr[x]);
                                    }
                                }
                                Foreach (x In 5 .. 2 By 2) {
                                    Out.printInt(arr[x]);
                                }
                            }
                        }
                    } """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,217))

    def test218(self):
        input = """ Class main{
                        Var a : Float = 5.0;
                        Var b : String = "abc";
                        $getHeight() {
                            Val a : Int = -3;
                            Val b : Float = c + Shape::$height;
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
                        }
                    } """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,218))

    def test219(self):
        input = """ Class Shape {
                        Val $numOfShape: Int = 0;
                        Val immutableAttribute: Int = 0;
                        Var length, width: Int;
                        ##Var a : Int = 10;##
                        $getNumOfShape() {
                            Return $numOfShape;
                        }
                    } """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,219))
    
    def test220(self):
        input = """ Class Shape {
                        Val $numOfShape: Int = 0;
                        Val immutableAttribute: Int = 0;
                        Var length, width: Int;
                        ##Var a : Int = 10;##
                        $getNumOfShape() {
                            Return $numOfShape;
                            a = b::shape;
                        }
                    } """
        expect = "Error on line 8 col 5: s"
        self.assertTrue(TestParser.test(input,expect,220))

    def test221(self):
        input = """ Class Shape {
                        Val $numOfShape: Int = 0;
                        Val immutableAttribute: Int = 0;
                        Var length, width: Int;
                        ##Var a : Int = 10;##
                        $getNumOfShape() {
                            Return $numOfShape;
                            a = b.$shape;
                        }
                    } """
        expect = "Error on line 8 col 4: $"
        self.assertTrue(TestParser.test(input,expect,221))

    def test222(self):
        input = """ Class Shape {
                        Val $numOfShape: Int = 0;
                        Val immutableAttribute: Int = 0;
                        Var length, width: Int;
                        ##Var a : Int = 10;##
                        $getNumOfShape() {
                            Return $numOfShape;
                            a = Self.shape;
                        }
                    } """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,222))
    
    def test223(self):
        input = """ CLass Rectangle: Shape {
                        getArea() {
                            Return Self.length * Self.width;
                        }
                    }
                    Class Program {
                        main() {
                            Out.printInt(Shape::$numOfShape);
                        }
                    }"""
        expect = "Error on line 1 col 1: CLass"
        self.assertTrue(TestParser.test(input,expect,223))

    def test224(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,224))

    def test225(self):
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
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,225))
    
    def test226(self):
        input = """ Class main{
                        Var a: Array[Int, 5] = Array (
                            Array("Volvo", "22", "18"),
                            Array("Saab", "5", "2"),
                            Array("Land Rover", "17", "15")
                        ) ;
                        getLength() {
                            length = 10;
                        }
                    }
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,226))

    def test227(self):
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
                                Foreach (x In 5 .. 2 By 2) {
                                    Out.printInt(arr[x]);
                                }
                            }
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,227))

    def test228(self):
        input = """ Class main{
                        Var a: Array[Array[String,3], 3] = Array (
                            Array("Volvo", "22", "18"),
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,228))
    
    def test229(self):
        input = """ Class Rectangle : Shape {
                        getShape(a,b : Int; c,d : Float) {
                            Out.printInt(Shape::$numOfShape);
                            Val x,y : Int = Shape::$numOfShape + x, a % b;
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,229))

    def test230(self):
        input = """ Class Program {
                        main() {
                            Out.printInt(Shape::$numOfShape);
                            Val x : A = New A();
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,230))

    def test231(self):
        input = """ Class Program {
                        main() {
                            Out.printInt(Shape::$numOfShape);
                            Val x : A = New A(a,b);
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,231))
    
    def test232(self):
        input = """ Class Program {
                        main() {
                            Out.printInt(Shape::$numOfShape);
                            Val x : A = New A(x);
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,232))

    def test233(self):
        input = """ Class Program {
                        main() {
                            Out.printInt(Shape::$numOfShape);
                            Val x : A = New A(x);
                            Var y : Array[Array[String,3],5];
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,233))

    def test234(self):
        input = """ Class Program {
                        main() {
                            Out.printInt(Shape::$numOfShape);
                            Val x : String = a +. b;
                            Var y : Boolean = a ==. b;
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,234))
    
    def test235(self):
        input = """ Class Program {
                        main() {
                            Out.printInt(Shape::$numOfShape);
                            Val x, y, z, k : Boolean = a >= b, c < d, e != f, m == n;
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,235))

    def test236(self):
        input = """ Class Program {
                        main() {
                            Out.printInt(Shape::$numOfShape);
                            Val x,y,z : Boolean = a || b, a && b, !c;
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,236))

    def test237(self):
        input = """ Class Program {
                        main() {
                            Out.printInt(Shape::$numOfShape);
                            Val x,y,z : Float = a + b, a - b, a + b - c;
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,237))
    
    def test238(self):
        input = """ Class Program {
                        main() {
                            Out.printInt(Shape::$numOfShape);
                            Val x,y,z,t : Float = a * b, a / b, c % d, a * b / c % d;
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,238))

    def test239(self):
        input = """ Class Program {
                        main() {
                            Out.printInt(Shape::$numOfShape);
                            Val x,y,z : Boolean = !a, !!b, !!!c;
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,239))

    def test240(self):
        input = """ Class Program {
                        main() {
                            Out.printInt(Shape::$numOfShape);
                            Val x,y,z : Float = -a, --b, ---c;
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,240))
    
    def test241(self):
        input = """ Class Program {
                        main() {
                            Out.printInt(Shape::$numOfShape);
                            Val x,y,z : Float = arr[1], arr[2][3], arr[x][y];
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,241))

    def test242(self):
        input = """ Class Program {
                        main() {
                            Out.printInt(Shape::$numOfShape);
                            Val x,y,z,t : Float = a.b, a::$b, a.b(), a::$b();
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,242))

    def test243(self):
        input = """ Class Program {
                        main() {
                            Out.printInt(Shape::$numOfShape);
                            Val x : A = New A();
                            Val y : B = New B(a);
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,243))
    
    def test244(self):
        input = """ Class Program {
                        main() {
                            Out.printInt(Shape::$numOfShape);
                            Val x,y,z : Float = (a + b) * c, a - (b / c.b());
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,244))

    def test245(self):
        input = """ Class Program {
                        main() {
                            Out.printInt(Shape::$numOfShape);
                            Val x,y,z : Boolean = True, False, True || False;
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,245))

    def test246(self):
        input = """ Class Program {
                        main() {
                            Out.printInt(Shape::$numOfShape);
                            Val x,y,z : String = "She is tall", "He asked me: '"Where's John?'"", "He asked me: '"He asked: '"Where's John?'"'"";
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,246))
    
    def test247(self):
        input = """ Class Program {
                        main() {
                            Out.printInt(Shape::$numOfShape);
                            Val x : Float = $sum;
                            Val y : A = Null;
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,247))

    def test248(self):
        input = """ Class Program {
                        main() {
                            Out.printInt(Shape::$numOfShape);
                            Val x : Float = recursive();
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,248))

    def test249(self):
        input = """ Class Program {
                        main() {
                            Out.printInt(Shape::$numOfShape);
                            Val x : Float = recursive(a,b);
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,249))
    
    def test250(self):
        input = """ Class Program {
                        main() {
                            Out.printInt(Shape::$numOfShape);
                            Val x : Float = $sum;
                            Val y : A = Null;
                        }
                        getHeight(a : Int; b : Array[Int, 3]) {}
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,250))

    def test251(self):
        input = """ Class Program {
                        main() {
                            Out.printInt(Shape::$numOfShape);
                            Val x : Float = $sum;
                            Val y : A = Null;
                        }
                        getHeight(a : Int; b : Array[Int, 3]) {}
                        getWidth(a : Float; B : A) {}
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,251))

    def test252(self):
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
                        getWidth(a :  Float; B : A) {}
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,252))
    
    def test253(self):
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
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,253))

    def test254(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,254))

    def test255(self):
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
                            Else {}
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,255))
    
    def test256(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,256))
    def test257(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,257))

    def test258(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,258))
    
    def test259(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,259))
    def test260(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,260))

    def test261(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,261))
    
    def test262(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,262))

    def test263(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,263))

    def test264(self):
        input = """ Class main {}
                    Class Program {}
                    Class Rectangle : Shape {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,264))
    
    def test265(self):
        input = """ Class main {
                        getArea() {
                            Shape::$getArea(a);
                        }
                    }
                    Class Program {}
                    Class Rectangle : Shape {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,265))
    
    def test266(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,266))

    def test267(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,267))
    
    def test268(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,268))

    def test269(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,269))

    def test270(self):
        input = """ Class Program {
                        getArea() {
                            Shape.getArea = arr[x];
                        }
                    } """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,270))
    
    def test271(self):
        input = """ Class Program {
                        getArea() {
                            Shape.getArea = arr[1] + arr[2] ;
                        }
                    } """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,271))

    def test272(self):
        input = """ Class Program {
                        getArea() {
                            Shape.getArea = arr[x] - arr[y];
                        }
                    } """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,272))

    def test273(self):
        input = """ Class Program {
                        getArea() {
                            Shape.getArea = arr[x] * arr[u] / arr[z] % (arr[a] - arr[1]);
                        }
                    } """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,273))
    
    def test274(self):
        input = """ Class Program {
                        getArea() {
                            arr[z] = Shape.getArea();
                        }
                    } """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,274))

    def test275(self):
        input = """ Class Program {
                        getArea() {
                            arr[z] = Shape.getArea() || Shape::$num;
                        }
                    } """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,275))

    def test276(self):
        input = """ Class Program {
                        getArea() {
                            arr[z] = Shape.getArea() + arr[3][4];
                        }
                    } """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,276))
    
    def test277(self):
        input = """ Class Program {
                        getArea() {
                            arr[z] = Shape.getArea() + arr[3][4][4];
                        }
                    } """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,277))
    
    def test278(self):
        input = """ Class Program {
                        getArea() {
                            arr[z] = arr[3];
                        }
                    } """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,278))

    def test279(self):
        input = """ Class Program {
                        getArea() {
                            Foreach (x In 5 .. 2) {
                                Out.printInt(arr[x] + arr[3]);
                            }
                        }
                    } """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,279))
    
    def test280(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,280))

    def test281(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,281))

    def test282(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,282))
    
    def test283(self):
        input = """ Class Program {
                        getArea() {
                            Foreach (x In 5 .. 2) {
                                arr[x] = x * x;
                            }
                        }
                    } """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,283))

    def test284(self):
        input = """ Class Program {
                        getArea() {
                            Foreach (x In 5 .. 2) {
                                arr[x] = x * x;
                                arr[3] = !a || !!b;
                            }
                        }
                    } """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,284))

    def test285(self):
        input = """ Class Program {
                        getArea() {
                            Foreach (x In 5 .. 2) {
                                x = 3 * !a;
                                arr[3] = !a || !!b;
                            }
                        }
                    } """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,285))
    
    def test286(self):
        input = """ Class Program {
                        getArea() {
                            Foreach (x In 5 .. 2 By 3) {
                                x = a +. b;
                                arr[3] = !a || !!b;
                            }
                        }
                    } """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,286))

    def test287(self):
        input = """ Class Program {
                        getArea() {
                            Foreach (x In 5 .. 2) {
                               arr[x] = arr[x] * arr[x] + Self.a;
                            }
                        }
                    } """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,287))

    def test288(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,288))
    
    def test289(self):
        input = """ Class Program {
                        getArea() {
                            Val a,b : A = New A(a,b), New A(a,c);
                        }
                    } """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,289))

    def test290(self):
        input = """ Class Program {
                        getArea() {
                            Val a,b : A = New A(a,b), Null;
                        }
                    } """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,290))

    def test291(self):
        input = """ Class Program {
                        getArea() {
                            Val a,b : Float = 1.0, 1_234e10;
                        }
                    } """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,291))
    
    def test292(self):
        input = """ Class Program {
                        getArea() {
                            Val a,b : Int = 0b1001, 0x123;
                        }
                    } """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,292))

    def test293(self):
        input = """ Class Program {
                        getArea() {
                            Val a: Boolean = True;
                        }
                    } """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,293))

    def test294(self):
        input = """ Class Program {
                        getArea() {
                            ##Val a,b : A = New A(a,b), New A(a,c);##
                        }
                    } """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,294))
    
    def test295(self):
        input = """ Class Program {
                        getArea() {
                            Val a : String = "";
                        }
                    } """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,295))

    def test296(self):
        input = """ Class Program {
                        getArea() {
                            a = "";
                        }
                    } """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,296))

    def test297(self):
        input = """ Class Program {
                        getArea() {
                            a = "" +. "abc";
                        }
                    } """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,297))
    
    def test298(self):
        input = """ Class Program {
                        getArea() {
                            a = "" +. c;
                        }
                    } """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,298))

    def test299(self):
        input = """ Class Program {
                        Constructor(a : Int) {
                            arr[1] = 2;
                        }
                    } """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,299))

    