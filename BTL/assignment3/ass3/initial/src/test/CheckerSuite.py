import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test400(self):
        input = """
        int main1(){}
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test401(self):
        input = """
        int main1(){}
        int main2(){}
        int main3(){}
        int main4(){}
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test402(self):
        input = """
        int a;
        boolean a;
        void main(){}
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,402))
    
    def test403(self):
        input = """
        int a;
        boolean b;
        string c;
        float d;
        float a;
        void main(){}
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test404(self):
        input = """
        int main(){return 1;}
        void main(){}
        """
        expect = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(input,expect,404))

    def test405(self):
        input = """
        void main1(){}
        void main2(){}
        int main3(){return 1;}
        int main(){return 0;}
        boolean main1(){return true;}
        """
        expect = "Redeclared Function: main1"
        self.assertTrue(TestChecker.test(input,expect,405))

    def test406(self):
        input = """
        void main(int a, boolean a){}
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,406))

    def test407(self):
        input = """
        void main(int a, boolean b){}
        int main2(int a, string b, float a){
            return a;
        }
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,407))

    def test408(self):
        input = """void main(){
            a = a + 1;
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,408))

    def test409(self):
        input = """
        int a;
        void main(){
            a = a + 1;
            a = a - b;
        }
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,409))

    def test410(self):
        input = """
        void main(){
            float a;
            int b;
            a = a + 1;
            a = a - b;
            a = a / c;
        }
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input,expect,410))

    def test411(self):
        input = """
        void main(){
            print("Hello");
        }
        """
        expect = "Undeclared Function: print"
        self.assertTrue(TestChecker.test(input,expect,411))

    def test412(self):
        input = """
        void main(){
            int num;
            putInt(num);
            print(getInt());
        }
        """
        expect = "Undeclared Function: print"
        self.assertTrue(TestChecker.test(input,expect,412))

    def test413(self):
        input = """
        int main(){
            int a;
            int b;
            a = sum(a, b);
            a = sub(a, b);
            return a;
        }
        int sum(int a, int b){
            return a + b;
        }
        """
        expect = "Undeclared Function: sub"
        self.assertTrue(TestChecker.test(input,expect,413))

    def test414(self):
        input = """
        void main(){
            if (print()){}
        }
        void print(){}
        """
        expect = "Type Mismatch In Statement: If(CallExpr(Id(print),[]),Block([]))"
        self.assertTrue(TestChecker.test(input,expect,414))

    def test415(self):
        input = """
        void main(){
            int a;
            if (getNum(a)){}
        }
        int getNum(int num){
            return num;
        }
        """
        expect = "Type Mismatch In Statement: If(CallExpr(Id(getNum),[Id(a)]),Block([]))"
        self.assertTrue(TestChecker.test(input,expect,415))

    def test416(self):
        input = """
        void main(){
            string a;
            a = "Hello";
            if (getString(a)){}
            else {}
        }
        string getString(string a){
            return a;
        }
        """
        expect = "Type Mismatch In Statement: If(CallExpr(Id(getString),[Id(a)]),Block([]),Block([]))"
        self.assertTrue(TestChecker.test(input,expect,416))

    def test417(self):
        input = """
        void main(){
            int a;
            a = 1;
            int b;
            b = 5;
            if (div(a, b)){}
            else {}
        }
        float div(int a, int b){
            float rlt;
            rlt = a / b;
            return rlt;
        }
        """
        expect = "Type Mismatch In Statement: If(CallExpr(Id(div),[Id(a),Id(b)]),Block([]),Block([]))"
        self.assertTrue(TestChecker.test(input,expect,417))

    # TODO: error
    def test418(self):
        input = """
        void main(){
            float a[25];
            if (div(a)){}
            else{}
        }
        float[] div(float a[]){
            int i;
            for (i = 0; i < 5; i = i+1){
                a[i] = 1;
            }
            return a;
        }
        """
        expect = "Type Mismatch In Statement: If(CallExpr(Id(div),[Id(a)]),Block([]),Block([]))"
        self.assertTrue(TestChecker.test(input,expect,418))

    def test419(self):
        input = """
        void main(){
            do {} while(1);
        }
        """
        expect = "Type Mismatch In Statement: Dowhile([Block([])],IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,419))

    def test420(self):
        input = """
        void main(){
            int a;
            do {} while(getFloatingPoint(a));
        }
        float getFloatingPoint(int a){
            return a * 1.0;
        }
        """
        expect = "Type Mismatch In Statement: Dowhile([Block([])],CallExpr(Id(getFloatingPoint),[Id(a)]))"
        self.assertTrue(TestChecker.test(input,expect,420))

    def test421(self):
        input = """
        void main(){
            string str;
            do {} while(getStr(str));
        }
        string getStr(string str){
            return str;
        }
        """
        expect = "Type Mismatch In Statement: Dowhile([Block([])],CallExpr(Id(getStr),[Id(str)]))"
        self.assertTrue(TestChecker.test(input,expect,421))

    def test422(self):
        input = """
        void main(){
            int a;
            do {} while(putInt(a));
        }
        """
        expect = "Type Mismatch In Statement: Dowhile([Block([])],CallExpr(Id(putInt),[Id(a)]))"
        self.assertTrue(TestChecker.test(input,expect,422))

    def test423(self):
        input = """
        void main(){
            int a[25];
            do {} while(a);
        }
        """
        expect = "Type Mismatch In Statement: Dowhile([Block([])],Id(a))"
        self.assertTrue(TestChecker.test(input,expect,423))

    def test424(self):
        input = """
        void main(){
            int i;
            for (i = 1; i + 1; i = i + 1){}
        }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(+,Id(i),IntLiteral(1));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([]))"
        self.assertTrue(TestChecker.test(input,expect,424))

    def test425(self):
        input = """
        void main(){
            int i;
            for (i = 1; i + getFloat(); i = i + 1){}
        }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(+,Id(i),CallExpr(Id(getFloat),[]));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([]))"
        self.assertTrue(TestChecker.test(input,expect,425))

    def test426(self):
        input = """
        void main(){
            int i;
            for (i = 1; putLn(); i = i + 1){}
        }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(i),IntLiteral(1));CallExpr(Id(putLn),[]);BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([]))"
        self.assertTrue(TestChecker.test(input,expect,426))

    def test427(self):
        input = """
        void main(){
            int i;
            string a;
            for (i = 1; a; i = i + 1){}
        }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(i),IntLiteral(1));Id(a);BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([]))"
        self.assertTrue(TestChecker.test(input,expect,427))

    def test428(self):
        input = """
        void main(){
            int i;
            string a[25];
            for (i = 1; a; i = i + 1){}
        }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(i),IntLiteral(1));Id(a);BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([]))"
        self.assertTrue(TestChecker.test(input,expect,428))

    def test429(self):
        input = """
        void main(){
            int i;
            int a;
            int b;
            for (i = 1; add(a, b) / sub(a, b); i = i + 1){}
        }
        int add(int a, int b){
            return a + b;
        }
        int sub(int a, int b){
            return a - b;
        }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(/,CallExpr(Id(add),[Id(a),Id(b)]),CallExpr(Id(sub),[Id(a),Id(b)]));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([]))"
        self.assertTrue(TestChecker.test(input,expect,429))

    def test430(self):
        input = """
        void main(){
            float i;
            for (i = 1; i < 10; i = i + 1){
                if (i == 10)
                    return;
            }
        }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(<,Id(i),IntLiteral(10));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([If(BinaryOp(==,Id(i),IntLiteral(10)),Return())]))"
        self.assertTrue(TestChecker.test(input,expect,430))

    def test431(self):
        input = """
        void main(){
            int i;
            string a;
            for (a = ""; i < 10; i = i + 1){
                if (i == 10)
                    return;
            }
        }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(a),StringLiteral());BinaryOp(<,Id(i),IntLiteral(10));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([If(BinaryOp(==,Id(i),IntLiteral(10)),Return())]))"
        self.assertTrue(TestChecker.test(input,expect,431))

    def test432(self):
        input = """
        void main(){
            int i;
            for (i = 0; i < 10; putLn()){
                if (i == 10)
                    return;
            }
        }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),IntLiteral(10));CallExpr(Id(putLn),[]);Block([If(BinaryOp(==,Id(i),IntLiteral(10)),Return())]))"
        self.assertTrue(TestChecker.test(input,expect,432))

    def test433(self):
        input = """
        void main(){
            int i;
            int arr[10];
            for (i = 0; i < 10; arr){
                arr[i] = 1;
            }
        }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),IntLiteral(10));Id(arr);Block([BinaryOp(=,ArrayCell(Id(arr),Id(i)),IntLiteral(1))]))"
        self.assertTrue(TestChecker.test(input,expect,433))

    

    def test434(self):
        input = """
        int main(){
            return;
        }
        """
        expect = "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input,expect,434))

    def test435(self):
        input = """
        void main(){
            return 1;
        }
        """
        expect = "Type Mismatch In Statement: Return(IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,435))

    def test436(self):
        input = """
        int main(){
            return 1.0;
        }
        """
        expect = "Type Mismatch In Statement: Return(FloatLiteral(1.0))"
        self.assertTrue(TestChecker.test(input,expect,436))

    def test437(self):
        input = """
        int main(){
            int arr[10];
            if (arr[5] >= 1)
                return 1;
            return arr;
        }
        """
        expect = "Type Mismatch In Statement: Return(Id(arr))"
        self.assertTrue(TestChecker.test(input,expect,437))

    def test438(self):
        input = """
        void main(){
            int arr[10];
            if (arr[5] >= 1)
                return;
            else
                return arr;
        }
        """
        expect = "Type Mismatch In Statement: Return(Id(arr))"
        self.assertTrue(TestChecker.test(input,expect,438))

    def test439(self):
        input = """
        void main(){
            int a;
            a = 1 + true;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,IntLiteral(1),BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input,expect,439))
    
    def test440(self):
        input = """
        void main(){
            int i;
            boolean is_num;
            is_num = false;
            float a[10];
            for (i = 0; i < 10; i=i+1){
                a[i] = a[i] * is_num;
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(*,ArrayCell(Id(a),Id(i)),Id(is_num))"
        self.assertTrue(TestChecker.test(input,expect,440))

    def test441(self):
        input = """
        void main(){
            int i;
            float f;
            i = f * f + f; 
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(i),BinaryOp(+,BinaryOp(*,Id(f),Id(f)),Id(f)))"
        self.assertTrue(TestChecker.test(input,expect,441))

    def test442(self):
        input = """
        void main(){
            int i;
            boolean a[10];
            for (i = 0; i < 10; i=i+1){
                a[i] = i;
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,ArrayCell(Id(a),Id(i)),Id(i))"
        self.assertTrue(TestChecker.test(input,expect,442))

    def test443(self):
        input = """
        void main(){
            boolean a[10];
            a = print("abc");
        }
        void print(string str){
            return;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),CallExpr(Id(print),[StringLiteral(abc)]))"
        self.assertTrue(TestChecker.test(input,expect,443))
    
    def test444(self):
        input = """
        void main(){
            boolean a;
            a = !4.5e10000;
        }
        """
        expect = "Type Mismatch In Expression: UnaryOp(!,FloatLiteral(inf))"
        self.assertTrue(TestChecker.test(input,expect,444))

    def test445(self):
        input = """
        void main(){
            boolean a;
            int b;
            b = -a;
        }
        """
        expect = "Type Mismatch In Expression: UnaryOp(-,Id(a))"
        self.assertTrue(TestChecker.test(input,expect,445))

    def test446(self):
        input = """
        void main(){
            float a;
            int b;
            a = 1;
            b = 1.000;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(b),FloatLiteral(1.0))"
        self.assertTrue(TestChecker.test(input,expect,446))

    def test447(self):
        input = """
        void main(){
            float a;
            int b;
            a = 1;
            b = a;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(b),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,447))
    
    def test448(self):
        input = """
        void main(){
            float a;
            boolean b;
            a + b;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,448))
    
    def test449(self):
        input = """
        void main(){
            float a;
            a % 2;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(%,Id(a),IntLiteral(2))"
        self.assertTrue(TestChecker.test(input,expect,449))
    
    def test450(self):
        """ Mismatch Expression With Binary Op """
        input = """
        void main(){
            boolean a;
            int b;
            b % a;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(%,Id(b),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,450))

    def test451(self):
        """ Mismatch Expression With Binary Op """
        input = """
        void main(){
            boolean is_true;
            is_true = 14 == 14.0;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,IntLiteral(14),FloatLiteral(14.0))"
        self.assertTrue(TestChecker.test(input,expect,451))
    
    def test452(self):
        """ Mismatch Expression With Binary Op """
        input = """
        void main(){
            boolean is_true;
            boolean a;
            is_true = a > 14.0;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(>,Id(a),FloatLiteral(14.0))"
        self.assertTrue(TestChecker.test(input,expect,452))
    
    def test453(self):
        """ Mismatch Expression With Binary Op """
        input = """
        void main(){
            int a;
            int b;
            a && b;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(&&,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,453))
    
    def test454(self):
        """ Mismatch Expression With Binary Op """
        input = """
        void main(){
            boolean a;
            boolean b;
            int c;
            c = a || b;
            
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(c),BinaryOp(||,Id(a),Id(b)))"
        self.assertTrue(TestChecker.test(input,expect,454))
    
    def test455(self):
        """ Mismatch Expression With Binary Op """
        input = """
        void main(){
            int a;
            int b;
            int c;
            a = 5;
            c = 1.0 + a + b;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(c),BinaryOp(+,BinaryOp(+,FloatLiteral(1.0),Id(a)),Id(b)))"
        self.assertTrue(TestChecker.test(input,expect,455))

    def test456(self):
        """ Function Not Return """
        input = """
        int main(){
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,456))
    
    def test457(self):
        """ Function Not Return """
        input = """
        int main(){
            int a;
            int b;
            int c;
            a = 5;
            c = 1 + a + b;
            if (true)
                return 0;
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,457))
    
    def test458(self):
        """ Function Not Return Inside If Statement """
        input = """
        int main(){
            if (true)
                return 1;
            else{
                int a;
                a = a + 1;
            }
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,458))

    def test459(self):
        """ Function Not Return Inside If Statement """
        input = """
        int main(){
            if (true){
                int a;
                a = a + 1;
            }
            else
                return 1;
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,459))
    
    def test460(self):
        """ Function Not Return Inside If Statement """
        input = """
        int main(int a){
            if(a==1){
                return 1;
            }
            else{
                
            }
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,460))

    def test461(self):
        """ Function Not Return Inside For Statement """
        input = """
        int main(){
            int i;
            int a;
            for (i=1;i<10;i=i+1)
                a = a + 1;
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,461))

    def test462(self):
        """ Function Not Return Inside Dowhile Statement """
        input = """
        int main(){
            int i;
            int a;
            do a = a + 1; while (true);
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,462))

    def test463(self):
        """ Break Not In Loop """
        input = """
        void main(){
            break;
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,463))

    def test464(self):
        """ Break Not In Loop """
        input = """
        void main(){
            if (true){
                int a;
                a = a + 1;
            }
            else {
                break;
            }
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,464))

    def test465(self):
        """ Continue Not In Loop """
        input = """
        void main(){
            continue;
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,465))

    def test466(self):
        """ Continue Not In Loop """
        input = """
        void main(){
            if (true){
                int a;
                a = a + 1;
            }
            else {
                continue;
            }
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,466))

    def test467(self):
        """ Unreachale Function """
        input = """
        void main(){}
        int add(int a, int b){
            return a + b;
        }
        """
        expect = "Unreachable Function: add"
        self.assertTrue(TestChecker.test(input,expect,467))

    def test468(self):
        """ Unreachale Function """
        input = """
        void main(){
            int a;
            int b;
            a = add(a, b);
        }
        int add(int a, int b){
            return a + b;
        }
        int sub(int a, int b){
            return a - b;
        }
        """
        expect = "Unreachable Function: sub"
        self.assertTrue(TestChecker.test(input,expect,468))

    def test469(self):
        """ Unreachale Function Recursive """
        input = """
        void main(){
            int a;
            int b;
        }
        int add(int a, int b){
            if (a > 100)
                return 1;
            return 1 * add(a, b);
        }
        """
        expect = "Unreachable Function: add"
        self.assertTrue(TestChecker.test(input,expect,469))

    def test470(self):
        """ Not Left Value With IntLiteral """
        input = """
        void main(){
            5 = 5;
        }
        """
        expect = "Not Left Value: IntLiteral(5)"
        self.assertTrue(TestChecker.test(input,expect,470))

    def test471(self):
        """ Not Left Value With CallExpr """
        input = """
        void main(){
            int a;
            int b;
            add(a, b) = 2;
        }
        int add(int a, int b){
            return a + b;
        }
        """
        expect = "Not Left Value: CallExpr(Id(add),[Id(a),Id(b)])"
        self.assertTrue(TestChecker.test(input,expect,471))

    def test472(self):
        """ Function Is Hidden By Variable """
        input = """
        int foo() { return 1; }
        int main(){
            int foo;
            foo();
            return 0;
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[])"
        self.assertTrue(TestChecker.test(input,expect,472))

    def test473(self):
        """ Redeclare Build-in Function """
        input = """
        int main(){
            int a;
            a = putInt();
            return 0;
        }
        int putInt(){
            return 1;
        }
        """
        expect = "Redeclared Function: putInt"
        self.assertTrue(TestChecker.test(input,expect,473))

    def test474(self):
        """ Primitive Type Parameter Passing Into CallExpr """
        input = """
                int func(int a, float b, string c) {
                    return 1;
                }
               void main(){
                    float a, b, c, x, y, z;
                    a = 9;
                    b = 12;
                    c = 3;
                    x = a - b / 3 + c * 2 - 1;
                    y = a - b / (3 + c) * (2 - 1);
                    z = a - ( b / (3 + c) * 2) - 1;
                    putFloat(x);
                    putFloat(y);
                    putFloat(z);
                    func(2, 2, 2.3);
                    return;
                }
                """
        expect = "Type Mismatch In Expression: CallExpr(Id(func),[IntLiteral(2),IntLiteral(2),FloatLiteral(2.3)])"
        self.assertTrue(TestChecker.test(input,expect,474))

    def test475(self):
        """ Type Mismatch In Expression With CallExpr """
        input = """
        int foo() {
            return 1;
        }

        void main() {
            foo[5]; 
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(foo),IntLiteral(5))"
        self.assertTrue(TestChecker.test(input,expect,475))

    def test476(self):
        """ Function Not Return With For Nested Dowhile """
        input = """
        float main(int a){
            do{
                for(a = 0;a >= 10; a = a*5){
                    int b;
                    float c;
                    c = (b + 5 - 10/50)/5;
                    return c;
                }
                
            }while(a == 5);
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,476))

    def test477(self):
        """ Multiple Assignment """
        input = """
        void main(){
            boolean a;
            int b;
            int c;
            a = b = c;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),BinaryOp(=,Id(b),Id(c)))"
        self.assertTrue(TestChecker.test(input,expect,477))

    def test478(self):
        """ Multiple Assignment """
        input = """
        void main(){
            int a;
            int b;
            int c;
            int d;
            int e;
            a = b = c = d = e;
            if (true){
                boolean a;
                a = true;
            }
            else{
                string a;
                a = b;
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,478))

    def test479(self):
        """ VarDecl In Block """
        input = """
        int a;
        float b;
        boolean main(){
            {
                boolean a;
            }
            {
                boolean b;
            }
            if (true)
                return a;
        }
        """
        expect = "Type Mismatch In Statement: Return(Id(a))"
        self.assertTrue(TestChecker.test(input,expect,479))

    def test480(self):
        """ VarDecl In Block """
        input = """
        int a;
        float b;
        void main(){
            boolean a;
            a = true;
            {
                string a;
                a = "Hello";
                {
                    string b;
                    b = "Bye";
                }
            }
            {
                int c;
            }
            b = b + c;
        }
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input,expect,480))

    def test481(self):
        """ VarDecl In Block """
        input = """
        int a;
        int main(){
            float a;
            {{{{{{{{{{
                boolean a;
            }}}}}}}}}}
            return a;
        }
        """
        expect = "Type Mismatch In Statement: Return(Id(a))"
        self.assertTrue(TestChecker.test(input,expect,481))

    def test482(self):
        """ VarDecl In Block """
        input = """
        int a;
        int main(){
            int a;
            if (true){
                float a;
                {{{{{
                    if (true){
                        int a;
                        return a;
                    }
                }}}}}
                
            }

        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,482))

    def test483(self):
        """ Return In Block """
        input = """
        int main(){
            {{{{{{{return 1;}}}}}}}
            int a;
            a = 1.0;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),FloatLiteral(1.0))"
        self.assertTrue(TestChecker.test(input,expect,483))

    def test484(self):
        """ Return In Block """
        input = """
        int main(){
            {{{{{{{return 1;}}}}}}}
            {{{{{{{return 1.0;}}}}}}}
        }
        """
        expect = "Type Mismatch In Statement: Return(FloatLiteral(1.0))"
        self.assertTrue(TestChecker.test(input,expect,484))

    def test485(self):
        """ Multiple Assignment """
        input = """
        int a,b,c;
        void main(){
            boolean result;
            result = a = b = c = (10+3)/4 + 5*9 - 2;
        }   
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(result),BinaryOp(=,Id(a),BinaryOp(=,Id(b),BinaryOp(=,Id(c),BinaryOp(-,BinaryOp(+,BinaryOp(/,BinaryOp(+,IntLiteral(10),IntLiteral(3)),IntLiteral(4)),BinaryOp(*,IntLiteral(5),IntLiteral(9))),IntLiteral(2))))))"
        self.assertTrue(TestChecker.test(input,expect,485))

    def test486(self):
        """ Multiple Assignment """
        input = """
        int a,b,c;
        void main(){
            boolean d,e,f;
            a = b = c = (10+3)/4 + 5*9 - 2;
            d = e = f = true;
            return 0;
        }   
        """
        expect = "Type Mismatch In Statement: Return(IntLiteral(0))"
        self.assertTrue(TestChecker.test(input,expect,486))

    def test487(self):
        """ Multiple Assignment """
        input = """
        int a,b,c;
        void main(){
            boolean d,e,f;
            a = b = c = (10+3)/4 + 5*9 - 2;
            d = e = f = true;
            int i;
            int arr[10];
            for (i = 0; i < 10; i=i+1){
                if (arr[i] > 10)
                    break;
                else{
                    d = e = f = false;
                }
            }
            return true;
        }   
        """
        expect = "Type Mismatch In Statement: Return(BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input,expect,487))

    def test488(self):
        """ Nested Statement """
        input = """
        void main(){
            if (true){
                int i;
                float arr[10];
                for (i = 0; i < 10; i=i+1)
                    arr[i] = 1;
                {
                    if (true)
                        return;
                }
                int a;
                do {
                    a = a + 1;
                    a = a * 10;
                    a = a + getInt();  
                }while(true);
            }
            else{
                print(a);
            }
        }   
        void print(int a){}
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,488))

    def test489(self):
        """ Nested Statement """
        input = """
        int a;
        void main(){
            if (true){
                int i;
                float arr[10];
                for (i = 0; i < 10; i=i+1)
                    arr[i] = 1;
                {
                    if (true)
                        return;
                }
                int a;
                do {
                    {{{
                        a = a + 1;
                        a = a * 10;
                        a = a + getInt();
                    }}}
                }while(true);
            }
            print(a);
            print(i);
        }   
        void print(int a){}
        """
        expect = "Undeclared Identifier: i"
        self.assertTrue(TestChecker.test(input,expect,489))

    def test490(self):
        """ Type Mismatch Index In Array Cell """
        input = """
        void main(){
            int a[5];
            float b;
            a[1.2] = b;
        }   
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),FloatLiteral(1.2))"
        self.assertTrue(TestChecker.test(input,expect,490))
    
    def test491(self):
        """ Type Mismatch Index In Array Cell """
        input = """
        void main(){
            int a[5];
            float b;
            a["1.2"] = b;
        }   
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),StringLiteral(1.2))"
        self.assertTrue(TestChecker.test(input,expect,491))

    def test492(self):
        """ Actual Program """
        input = """
        void main()
        {
            int year;
            printf("Enter a year: ");
            if(year%4 == 0)
            {
                if( year%100 == 0)
                {
                    // year is divisible by 400, hence the year is a leap year
                    if ( year%400 == 0)
                        print(year);
                    else
                        print(year);
                }
                else
                    print(year);
            }
            else
                print(year);
            
            return 0;
        }
        void print(int a){}
        void printf(string a){}
        
        """
        expect = "Type Mismatch In Statement: Return(IntLiteral(0))"
        self.assertTrue(TestChecker.test(input,expect,492))

    def test493(self):
        """ Actual Program """
        input = """
        int main()
        {
            int n, i, sum;
            sum = 0;
            
            printf("Enter a positive integer: ");
            for(i=1; i <= n; i=i+1)
            {
                sum = sum + i;   // sum = sum+i;
            }
            return 0;
        }
        
        """
        expect = "Undeclared Function: printf"
        self.assertTrue(TestChecker.test(input,expect,493))

    def test494(self):
        """ Actual Program """
        input = """
        int main()
        {
            int n1, n2, rlt;
            printf("Enter two positive integers: ");
            rlt = hcf(n1,n2);
            print(rlt);
            return 0;
        }
        int hcf(int n1, int n2)
        {
            if (n2 != 0)
                return hcf(n2, n1%n2);
            else 
                return n1;
        }
        void print(int rlt){
            return;
        }
        void printf(string rlt){
            return;
        }
        void println(string rlt){
            return;
        }
        """
        expect = "Unreachable Function: println"
        self.assertTrue(TestChecker.test(input,expect,494))

    def test495(self):
        """ Actual Program """
        input = """
        int main()
        {
            int n, reversedNumber, remainder;
            reversedNumber = 0;
            printf("Enter an integer: ");
            do
            {
                remainder = n%10;
                reversedNumber = reversedNumber*10 + remainder;
                n = n / 10;
            }while(n != 0);
            printf(reversedNumber);
            return 0;
        }
        void printf(string str){
            return;
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(printf),[Id(reversedNumber)])"
        self.assertTrue(TestChecker.test(input,expect,495))

    def test496(self):
        """ Actual Program """
        input = """
        int factorial(int n) {
            //base case
            if(n == 0) {
                return 1;
            } else {
                return n * factorial(n-1);
            }
        }

        int fibbonacci(int n) {
            if(n == 0){
                return 0;
            } else if(n == 1) {
                return 1;
            } else {
                return (fibbonacci(n-1) + fibbonacci(n-2));
            }
        }

        int main() {
            int n;
            n = 5;
            int i;
                
            for(i = 0;i<n;i=i+1) {
                fibbonacci(i);
            }
            return 0;
        }
        """
        expect = "Unreachable Function: factorial"
        self.assertTrue(TestChecker.test(input,expect,496))
    
    def test497(self):
        """ Actual Program """
        input = """
        int main()
        {
            int n;
            printf("Enter a binary number: ");
            printInt(convertBinaryToDecimal(n));
            return 0;
        }
        int convertBinaryToDecimal(int n)
        {
            int decimalNumber, i, remainder;
            decimalNumber = 0;
            i = 0;
            do
            {
                remainder = n%10;
                n = n / 10;
                decimalNumber = decimalNumber + remainder*pow(2,i);
                i = i + 1;
            }while (n!=0);
            return decimalNumber;
        }
        void printf(string str){
            return;
        }

        void printInt(int num){
            return;
        }
        """
        expect = "Undeclared Function: pow"
        self.assertTrue(TestChecker.test(input,expect,497))

    def test498(self):
        """ Actual Program """
        input = """
        float calculateSD(float data[])
        {
            float sum, mean, standardDeviation;
            sum = 0.0;
            standardDeviation = 0.0;
            int i;
            for(i=0; i<10; i=i+1)
            {
                sum = sum + data[i];
            }
            mean = sum/10;
            for(i=0; i<10; i=i+1)
                standardDeviation = standardDeviation + pow(data[i] - mean, 2);
            return sqrt(standardDeviation/10);
        }
        float sqrt(float num){
            return num;
        }
        float pow(float num, int exp){
            int i;
            for (i = 1; i <= exp; i=i+1)
                num = num * num;
            return num;
        }
        void printf(string str){
            return;
        }
        void printInt(int num){
            return;
        }
        void main(){
            int i;
            float data[10];
            printf("Enter 10 elements: ");
            for(i=0; i < 10; i=i+1)
                data[i] = 1;
            printInt(calculateSD(data));
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(printInt),[CallExpr(Id(calculateSD),[Id(data)])])"
        self.assertTrue(TestChecker.test(input,expect,498))

    def test499(self):
        """ Actual Program """
        input = """
        int main()
        {
            float a, b, c, discriminant, root1, root2, realPart, imaginaryPart;
            printf("Enter coefficients a, b and c: ");
            discriminant = b*b-4*a*c;
            // condition for real and different roots
            if (discriminant > 0)
            {
            // sqrt() function returns square root
                root1 = (-b+sqrt(discriminant))/(2*a);
                root2 = (-b-sqrt(discriminant))/(2*a);
                print(root1);
            }
            //condition for real and equal roots
            else {
                if (discriminant == 0)
                {
                    root1 = root2 = -b/(2*a);
                    print(root1);
                }
                else
                {
                    realPart = -b/(2*a);
                    imaginaryPart = sqrt(-discriminant)/(2*a);
                }
            }
            return 0;
        }  
        void printf(string str){
            return;
        }
        float sqrt(float num){
            return num;
        }
        void print(float num){}
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,Id(discriminant),IntLiteral(0))"
        self.assertTrue(TestChecker.test(input,expect,499))