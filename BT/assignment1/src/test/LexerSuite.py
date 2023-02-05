import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    """TEST IDENTIFIER"""
    def test100(self):
        self.assertTrue(TestLexer.test("abc","abc,<EOF>",100))
    def test101(self):
        self.assertTrue(TestLexer.test("Break","Break,<EOF>",101))
    def test102(self):
        self.assertTrue(TestLexer.test("ab?svn","ab,Error Token ?",102))
    def test103(self):
        self.assertTrue(TestLexer.test("Return x;","Return,x,;,<EOF>",103))
    def test104(self):
        self.assertTrue(TestLexer.test("Break If","Break,If,<EOF>",104))
    def test105(self):
        self.assertTrue(TestLexer.test("==.","==.,<EOF>",105))
    def test106(self):
        self.assertTrue(TestLexer.test("$_abc","$_abc,<EOF>",106))
    def test107(self):
        self.assertTrue(TestLexer.test("$_102","$_102,<EOF>",107))
    def test108(self):
        self.assertTrue(TestLexer.test("abc Break","abc,Break,<EOF>",108))
    def test109(self):
        self.assertTrue(TestLexer.test("a==.b","a,==.,b,<EOF>",109))
    def test110(self):
        self.assertTrue(TestLexer.test("a>=b","a,>=,b,<EOF>",110))
    def test111(self):
        self.assertTrue(TestLexer.test("a!=b","a,!=,b,<EOF>",111))
    def test112(self):
        self.assertTrue(TestLexer.test("Boolean String Float Int Class Array","Boolean,String,Float,Int,Class,Array,<EOF>",112))
    def test113(self):
        self.assertTrue(TestLexer.test("a::b","a,::,b,<EOF>",113))
    def test114(self):
        self.assertTrue(TestLexer.test("-100","-,100<EOF>",114))
    def test115(self):
        self.assertTrue(TestLexer.test("Elseif Else If","Elseif,Else,If,<EOF>",115))
    def test116(self):
        self.assertTrue(TestLexer.test("===","==,=,<EOF>",116))
    def test117(self):
        self.assertTrue(TestLexer.test("!=!","!=,!,<EOF>",117))
    def test118(self):
        self.assertTrue(TestLexer.test("+..","+.,.,<EOF>",118))
    def test119(self):
        self.assertTrue(TestLexer.test(">=><=<",">=,>,<=,<,<EOF>",119))
    
    """TEST FLOAT"""
    def test120(self):
        self.assertTrue(TestLexer.test("1.234","1.234,<EOF>",120))
    def test121(self):
        self.assertTrue(TestLexer.test("1.2E+3","1.2E+3,<EOF>",121))
    def test122(self):
        self.assertTrue(TestLexer.test("1E-2","1E-2,<EOF>",122))
    def test123(self):
        self.assertTrue(TestLexer.test("1.","1.,<EOF>",123))
    def test124(self):
        self.assertTrue(TestLexer.test("1.E-10","1.E-10,<EOF>",124))
    def test125(self):
        self.assertTrue(TestLexer.test(".E-5",".E-5,<EOF>",125))
    def test126(self):
        self.assertTrue(TestLexer.test(".000e-2",".000e-2,<EOF>",127))
    def test127(self):
        self.assertTrue(TestLexer.test("1.000000000","1.000000000,<EOF>",127))
    def test128(self):
        self.assertTrue(TestLexer.test("1.2e-00001","1.2e-00001,<EOF>",128))
    def test129(self):
        self.assertTrue(TestLexer.test("1_234.567","1234.567,<EOF>",129))
    def test130(self):
        self.assertTrue(TestLexer.test("1_234.","1234.,<EOF>",130))
    def test131(self):
        self.assertTrue(TestLexer.test("1_234e-10","1234e-10,<EOF>",131))
    
    """TEST INTEGER"""
    def test132(self):
        self.assertTrue(TestLexer.test("1_234","1234,<EOF>",132))
    def test133(self):
        self.assertTrue(TestLexer.test("1_234_567","1234567,<EOF>",133))
    def test134(self):
        self.assertTrue(TestLexer.test("0123","0123,<EOF>",134))
    def test135(self):
        self.assertTrue(TestLexer.test("000123","00,0123,<EOF>",135))
    def test136(self):
        self.assertTrue(TestLexer.test("00123","00,123,<EOF>",136))
    def test137(self):
        self.assertTrue(TestLexer.test("01230","01230,<EOF>",137))
    def test138(self):
        self.assertTrue(TestLexer.test("012345678","01234567,8,<EOF>",138))
    def test139(self):
        self.assertTrue(TestLexer.test("08123","0,8123,<EOF>",139))
    def test140(self):
        self.assertTrue(TestLexer.test("0800123","0,800123,<EOF>",140))
    def test141(self):
        self.assertTrue(TestLexer.test("0x0001","0x0,00,1,<EOF>",141))
    def test142(self):
        self.assertTrue(TestLexer.test("0x1ghi","0x1,ghi,<EOF>",142))
    def test143(self):
        self.assertTrue(TestLexer.test("0x123","0x123,<EOF>",143))
    def test144(self):
        self.assertTrue(TestLexer.test("0xg","0,xg,<EOF>",144))
    def test145(self):
        self.assertTrue(TestLexer.test("0xabctr","0xabc,tr,<EOF>",145))
    def test146(self):
        self.assertTrue(TestLexer.test("0b10000","0b10000,<EOF>",146))
    def test147(self):
        self.assertTrue(TestLexer.test("0b00001","0b0,00,0,1,<EOF>",147))
    def test148(self):
        self.assertTrue(TestLexer.test("0b1000x01","0b1000,x01,<EOF>",148))
    def test149(self):
        self.assertTrue(TestLexer.test("0b1_000123abc","0b1000,123,abc,<EOF>",149))
    def test150(self):
        self.assertTrue(TestLexer.test("1230x012bg","1230,x012bg,<EOF>",150))
    
    """TEST COMMENT"""
    def test151(self):
        self.assertTrue(TestLexer.test(""" ##My comment##is ignored ""","is,ignored,<EOF>",151))
    def test152(self):
        self.assertTrue(TestLexer.test(""" ##abc def##  ""","<EOF>",152))
    def test153(self):
        self.assertTrue(TestLexer.test(""" ##abc## def##  ""","def,Error Token #",153))
    def test154(self):
        self.assertTrue(TestLexer.test(""" ##abc# def##  ""","<EOF>",154))
    def test155(self):
        self.assertTrue(TestLexer.test(""" ##abc# def## ghi## ""","ghi,Error Token #",155))
    def test156(self):
        self.assertTrue(TestLexer.test(""" ##abc# def## ghi## klm## ""","ghi,<EOF>",156))
    def test157(self):
        self.assertTrue(TestLexer.test(""" ##abc# def## ghi## klm##nopq""","ghi,nopq,<EOF>",157))
    def test158(self):
        self.assertTrue(TestLexer.test(""" ##abc# def## ghi## klm##nopq ## ""","ghi,nopq,Error Token #",158))
    def test159(self):
        self.assertTrue(TestLexer.test(""" ##abc# def## 0x## klm##abc""","0,x,abc,<EOF>",159))
    
    """TEST STRING"""
    def test160(self):
        self.assertTrue(TestLexer.test(""" "abc def"  ""","abc def,<EOF>",160))
    def test161(self):
        self.assertTrue(TestLexer.test(""" ""  """,",<EOF>",161))
    def test162(self):
        self.assertTrue(TestLexer.test(""" "Hello World## " ## ""","Hello World##,Error Token #",162))
    def test163(self):
        self.assertTrue(TestLexer.test(""" "Hello ##My## World" ""","Hello ##My## World,<EOF>",163))
    def test164(self):
        self.assertTrue(TestLexer.test(""" ##"Hello ##My## World"  ""","My,Error Token #",164))
    def test165(self):
        self.assertTrue(TestLexer.test(""" "\\nabc def"  ""","\nabc def,<EOF>",165))
    def test166(self):
        self.assertTrue(TestLexer.test(""" "abc\\n def"  ""","abc\n def,<EOF>",166))
    def test167(self):
        self.assertTrue(TestLexer.test(""" "abc def\\n"  ""","abc def\n,<EOF>",167))
    def test168(self):
        self.assertTrue(TestLexer.test(""" "abc\\h def"  ""","Illegal Escape In String: abc\h",168))
    def test169(self):
        self.assertTrue(TestLexer.test(""" "abc def ""","Unclosed String: abc def",169))
    def test170(self):
        self.assertTrue(TestLexer.test(""" "abc\n def"  ""","Unclosed String: abc",170))
    def test171(self):
        self.assertTrue(TestLexer.test(""" "\nabc def"  ""","Error Token ",171))
    def test172(self):
        self.assertTrue(TestLexer.test(""" "  ""","Unclosed String: ",172))
    def test173(self):
        self.assertTrue(TestLexer.test(""" "He asked me: '"Where is John?'""  ""","He asked me: 'Where is John?',<EOF>",173))
    def test174(self):
        self.assertTrue(TestLexer.test(""" "He asked me: '"Where's John?'"" ""","He asked me: 'Where's John?',<EOF>",174))
    def test175(self):
        self.assertTrue(TestLexer.test(""" "Linda's toy is Peter's gift" ""","Linda's toy is Peter's gift,<EOF>",175))
    def test176(self):
        self.assertTrue(TestLexer.test(""" "He asked me: '"Linda's toy is Peter's gift'""  ""","He asked me: 'Linda's toy is Peter's gift',<EOF>",176))
    def test177(self):
        self.assertTrue(TestLexer.test(""" "He asked me: '"He asked: '"Where's John?'"'"" ""","He asked me: 'He asked: 'Where's John?'',<EOF>",177))

    """TEST ALL"""
    def test178(self):
        self.assertTrue(TestLexer.test(""" ABC"Hello World## " ""","ABC,Hello World## ,<EOF>",178))
    def test179(self):
        self.assertTrue(TestLexer.test(""" 0b0001"Hello ##My## World"0abc ""","0b0,00,1,Hello ##My## World,0,abc,<EOF>",179))
    def test180(self):
        self.assertTrue(TestLexer.test(""" Array(1, 5, 7, 12)  ""","Array,(,1,,,5,,,7,,,12,),<EOF>",180))
    def test181(self):
        self.assertTrue(TestLexer.test(""" Array("Kangxi", "Yongzheng", "Qianlong") ""","Array,(,Kangxi,,,Yongzheng,,,Qianlong,),<EOF>",181))
    def test182(self):
        self.assertTrue(TestLexer.test(""" Val My1stCons, My2ndCons: Int = 1 + 5, 2; ""","Val,My1stCons,,,My2stCons,:,Int,=,1,+,5,,,2,;,<EOF>",182))
    def test183(self):
        self.assertTrue(TestLexer.test(""" Class main{} ""","Class,main,{,},<EOF>",183))
    def test184(self):
        self.assertTrue(TestLexer.test(""" Class Rectangle: Shape { getArea() { Return Self.length * Self.width; } } """,
        "Class,Rectangle,:,Shape,{,getArea,(,),{,Return,Self,.,length,*,Self,.,width,;,},},<EOF>",184))
    def test185(self):
        self.assertTrue(TestLexer.test("abc$abc","abc,$abc,<EOF>",185))
    def test186(self):
        self.assertTrue(TestLexer.test(""" abc.012 ""","abc,.,012,<EOF>",186))
    def test187(self):
        self.assertTrue(TestLexer.test(""" abc.01e10 ""","abc,.01e10,<EOF>",187))
    def test188(self):
        self.assertTrue(TestLexer.test(""" abc.e+1 ""","abc,.e+1,<EOF>",188))
    def test189(self):
        self.assertTrue(TestLexer.test("0bX1","0,bX,1,<EOF>",189))
    def test190(self):
        self.assertTrue(TestLexer.test(""" 3_123abc.0 ""","3123,abc,.,0,<EOF>",190))
    def test191(self):
        self.assertTrue(TestLexer.test(""" 001_23.0 ""","00,123.0,<EOF>",191))
    def test192(self):
        self.assertTrue(TestLexer.test(""" _numOfShape::$get() ""","_numOfShape,::,$get(),<EOF>",192))
    def test193(self):
        self.assertTrue(TestLexer.test(""" Foreach (i In 1 .. 100 By 2) { Out.printInt(i); } ""","Foreach,(,i,In,1,..,100,By,2,),{,Out,.,printInt,(,i,),;,},<EOF>",193))
    def test194(self):
        self.assertTrue(TestLexer.test(""" Foreach (x In 5 .. 2) { Out.printInt(arr[x]); } """,
        "Foreach,(,x,In,5,..,2,),{,Out,.,printInt,(,arr,[,x,],),;,},<EOF>",194))
    def test195(self):
        self.assertTrue(TestLexer.test(""" Continue; ""","Continue,;,<EOF>",195))
    def test196(self):
        self.assertTrue(TestLexer.test(""" ForeachBreakabc0123 ""","Foreach,Break,abc,0123,<EOF>",196))
    def test197(self):
        self.assertTrue(TestLexer.test("0xForeach","0xF,oreach,<EOF>",197))
    def test198(self):
        self.assertTrue(TestLexer.test(""" ## ""","Error Token #,<EOF>",198))
    def test199(self):
        self.assertTrue(TestLexer.test(""" 0_1 ""","0,_1,<EOF>",199))