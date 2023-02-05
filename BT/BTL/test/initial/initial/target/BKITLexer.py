# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\b")
        buf.write("\64\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write("\7\3\2\3\2\7\2\22\n\2\f\2\16\2\25\13\2\3\2\3\2\6\2\31")
        buf.write("\n\2\r\2\16\2\32\7\2\35\n\2\f\2\16\2 \13\2\3\2\3\2\5\2")
        buf.write("$\n\2\3\3\6\3\'\n\3\r\3\16\3(\3\3\3\3\3\4\3\4\3\5\3\5")
        buf.write("\3\6\3\6\3\7\3\7\2\2\b\3\3\5\4\7\5\t\6\13\7\r\b\3\2\5")
        buf.write("\3\2\63;\3\2\62;\5\2\13\f\17\17\"\"\28\2\3\3\2\2\2\2\5")
        buf.write("\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2")
        buf.write("\2\2\3#\3\2\2\2\5&\3\2\2\2\7,\3\2\2\2\t.\3\2\2\2\13\60")
        buf.write("\3\2\2\2\r\62\3\2\2\2\17\23\t\2\2\2\20\22\t\3\2\2\21\20")
        buf.write("\3\2\2\2\22\25\3\2\2\2\23\21\3\2\2\2\23\24\3\2\2\2\24")
        buf.write("\36\3\2\2\2\25\23\3\2\2\2\26\30\7a\2\2\27\31\t\3\2\2\30")
        buf.write("\27\3\2\2\2\31\32\3\2\2\2\32\30\3\2\2\2\32\33\3\2\2\2")
        buf.write("\33\35\3\2\2\2\34\26\3\2\2\2\35 \3\2\2\2\36\34\3\2\2\2")
        buf.write("\36\37\3\2\2\2\37!\3\2\2\2 \36\3\2\2\2!$\b\2\2\2\"$\7")
        buf.write("\62\2\2#\17\3\2\2\2#\"\3\2\2\2$\4\3\2\2\2%\'\t\4\2\2&")
        buf.write("%\3\2\2\2\'(\3\2\2\2(&\3\2\2\2()\3\2\2\2)*\3\2\2\2*+\b")
        buf.write("\3\3\2+\6\3\2\2\2,-\13\2\2\2-\b\3\2\2\2./\13\2\2\2/\n")
        buf.write("\3\2\2\2\60\61\13\2\2\2\61\f\3\2\2\2\62\63\13\2\2\2\63")
        buf.write("\16\3\2\2\2\b\2\23\32\36#(\4\3\2\2\b\2\2")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INTEGER = 1
    WS = 2
    ERROR_CHAR = 3
    UNCLOSE_STRING = 4
    ILLEGAL_ESCAPE = 5
    UNTERMINATED_COMMENT = 6

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "INTEGER", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "UNTERMINATED_COMMENT" ]

    ruleNames = [ "INTEGER", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "UNTERMINATED_COMMENT" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:       
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        elif tk == self.UNTERMINATED_COMMENT:
            raise UnterminatedComment()
        else:
            return result;


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[0] = self.INTEGER_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTEGER_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace("_","")
     


