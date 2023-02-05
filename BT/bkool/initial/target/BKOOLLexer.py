# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\27")
        buf.write("}\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3")
        buf.write("\6\3\7\3\7\3\b\3\b\7\bE\n\b\f\b\16\bH\13\b\3\b\5\bK\n")
        buf.write("\b\3\t\3\t\6\tO\n\t\r\t\16\tP\3\n\3\n\3\n\3\13\3\13\3")
        buf.write("\f\3\f\3\r\3\r\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\21\3\21\3\22\6\22k\n\22\r\22\16")
        buf.write("\22l\3\23\3\23\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\30\3\30\2\2\31\3\3\5\4\7\5\t\6\13\7")
        buf.write("\r\b\17\2\21\2\23\t\25\n\27\13\31\f\33\r\35\16\37\17!")
        buf.write("\20#\21%\22\'\23)\24+\25-\26/\27\3\2\6\3\2\63;\3\2\62")
        buf.write(";\4\2C\\c|\5\2\13\f\17\17\"\"\2~\2\3\3\2\2\2\2\5\3\2\2")
        buf.write("\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2")
        buf.write("\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33")
        buf.write("\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2")
        buf.write("\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2")
        buf.write("\2\2\2/\3\2\2\2\3\61\3\2\2\2\58\3\2\2\2\7:\3\2\2\2\t<")
        buf.write("\3\2\2\2\13>\3\2\2\2\r@\3\2\2\2\17J\3\2\2\2\21L\3\2\2")
        buf.write("\2\23R\3\2\2\2\25U\3\2\2\2\27W\3\2\2\2\31Y\3\2\2\2\33")
        buf.write("[\3\2\2\2\35_\3\2\2\2\37e\3\2\2\2!g\3\2\2\2#j\3\2\2\2")
        buf.write("%n\3\2\2\2\'p\3\2\2\2)r\3\2\2\2+v\3\2\2\2-y\3\2\2\2/{")
        buf.write("\3\2\2\2\61\62\7t\2\2\62\63\7g\2\2\63\64\7v\2\2\64\65")
        buf.write("\7w\2\2\65\66\7t\2\2\66\67\7p\2\2\67\4\3\2\2\289\7?\2")
        buf.write("\29\6\3\2\2\2:;\7-\2\2;\b\3\2\2\2<=\7/\2\2=\n\3\2\2\2")
        buf.write(">?\7,\2\2?\f\3\2\2\2@A\7\61\2\2A\16\3\2\2\2BF\t\2\2\2")
        buf.write("CE\t\3\2\2DC\3\2\2\2EH\3\2\2\2FD\3\2\2\2FG\3\2\2\2GK\3")
        buf.write("\2\2\2HF\3\2\2\2IK\7\62\2\2JB\3\2\2\2JI\3\2\2\2K\20\3")
        buf.write("\2\2\2LN\7\60\2\2MO\t\3\2\2NM\3\2\2\2OP\3\2\2\2PN\3\2")
        buf.write("\2\2PQ\3\2\2\2Q\22\3\2\2\2RS\5\17\b\2ST\5\21\t\2T\24\3")
        buf.write("\2\2\2UV\5\17\b\2V\26\3\2\2\2WX\7}\2\2X\30\3\2\2\2YZ\7")
        buf.write("\177\2\2Z\32\3\2\2\2[\\\7k\2\2\\]\7p\2\2]^\7v\2\2^\34")
        buf.write("\3\2\2\2_`\7h\2\2`a\7n\2\2ab\7q\2\2bc\7c\2\2cd\7v\2\2")
        buf.write("d\36\3\2\2\2ef\7*\2\2f \3\2\2\2gh\7+\2\2h\"\3\2\2\2ik")
        buf.write("\t\4\2\2ji\3\2\2\2kl\3\2\2\2lj\3\2\2\2lm\3\2\2\2m$\3\2")
        buf.write("\2\2no\7=\2\2o&\3\2\2\2pq\7.\2\2q(\3\2\2\2rs\t\5\2\2s")
        buf.write("t\3\2\2\2tu\b\25\2\2u*\3\2\2\2vw\13\2\2\2wx\b\26\3\2x")
        buf.write(",\3\2\2\2yz\13\2\2\2z.\3\2\2\2{|\13\2\2\2|\60\3\2\2\2")
        buf.write("\7\2FJPl\4\b\2\2\3\26\2")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    RETURN = 1
    EQUAL = 2
    ADD = 3
    MINUS = 4
    MULTI = 5
    DIV = 6
    FLOATLIT = 7
    INTLIT = 8
    LC = 9
    RC = 10
    INT = 11
    FLOAT = 12
    LB = 13
    RB = 14
    ID = 15
    SM = 16
    CM = 17
    WS = 18
    ERROR_CHAR = 19
    UNCLOSE_STRING = 20
    ILLEGAL_ESCAPE = 21

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'return'", "'='", "'+'", "'-'", "'*'", "'/'", "'{'", "'}'", 
            "'int'", "'float'", "'('", "')'", "';'", "','" ]

    symbolicNames = [ "<INVALID>",
            "RETURN", "EQUAL", "ADD", "MINUS", "MULTI", "DIV", "FLOATLIT", 
            "INTLIT", "LC", "RC", "INT", "FLOAT", "LB", "RB", "ID", "SM", 
            "CM", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "RETURN", "EQUAL", "ADD", "MINUS", "MULTI", "DIV", "NAT", 
                  "FRAC", "FLOATLIT", "INTLIT", "LC", "RC", "INT", "FLOAT", 
                  "LB", "RB", "ID", "SM", "CM", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[20] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


