# Generated from c:\Users\PC\Downloads\HK212\PPL\BTL\assignment1\src\main\d96\parser\D96.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3H")
        buf.write("\u01f5\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\3\2\3\2\3\2\3\3\3\3\3\3")
        buf.write("\3\3\5\3v\n\3\3\4\3\4\3\4\3\4\5\4|\n\4\3\4\3\4\3\4\5\4")
        buf.write("\u0081\n\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\5\6\u008c")
        buf.write("\n\6\3\7\3\7\5\7\u0090\n\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\5\b\u0099\n\b\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\n\5\n\u00a3")
        buf.write("\n\n\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u00ab\n\13\3\f")
        buf.write("\3\f\3\f\3\f\3\f\5\f\u00b2\n\f\3\r\3\r\3\r\3\r\3\r\5\r")
        buf.write("\u00b9\n\r\3\16\3\16\3\16\3\16\3\16\5\16\u00c0\n\16\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\7\17\u00c8\n\17\f\17\16\17")
        buf.write("\u00cb\13\17\3\20\3\20\3\20\3\20\3\20\3\20\7\20\u00d3")
        buf.write("\n\20\f\20\16\20\u00d6\13\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\7\21\u00de\n\21\f\21\16\21\u00e1\13\21\3\22\3\22")
        buf.write("\3\22\5\22\u00e6\n\22\3\23\3\23\3\23\5\23\u00eb\n\23\3")
        buf.write("\24\3\24\3\24\3\24\3\24\7\24\u00f2\n\24\f\24\16\24\u00f5")
        buf.write("\13\24\3\25\3\25\3\25\3\25\3\25\3\25\7\25\u00fd\n\25\f")
        buf.write("\25\16\25\u0100\13\25\3\26\3\26\3\26\3\26\3\26\3\26\7")
        buf.write("\26\u0108\n\26\f\26\16\26\u010b\13\26\3\27\3\27\3\27\3")
        buf.write("\27\5\27\u0111\n\27\3\30\3\30\3\30\5\30\u0116\n\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\5\30")
        buf.write("\u0123\n\30\3\31\3\31\3\31\3\31\5\31\u0129\n\31\3\31\3")
        buf.write("\31\3\32\3\32\3\32\3\32\5\32\u0131\n\32\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\33\3\33\5\33\u013b\n\33\3\34\3\34\3")
        buf.write("\34\3\34\3\35\3\35\3\35\3\35\5\35\u0145\n\35\3\36\3\36")
        buf.write("\3\36\5\36\u014a\n\36\3\36\3\36\3\37\3\37\3\37\3\37\5")
        buf.write("\37\u0152\n\37\3 \3 \3 \3 \3 \3 \3 \3 \5 \u015c\n \3!")
        buf.write("\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\5\"\u016a\n\"")
        buf.write("\3\"\3\"\3\"\5\"\u016f\n\"\3#\3#\3#\3#\3#\3#\3#\3#\5#")
        buf.write("\u0179\n#\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\5$\u0186\n")
        buf.write("$\3$\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3\'\3(\3(\3(")
        buf.write("\3(\5(\u0199\n(\3(\3(\3)\3)\3)\3)\3)\3*\3*\3*\3*\3*\5")
        buf.write("*\u01a7\n*\3+\3+\3,\3,\3,\3,\3,\3-\3-\3-\3-\3-\5-\u01b5")
        buf.write("\n-\3.\3.\5.\u01b9\n.\3/\3/\3/\3/\3/\3/\3/\3\60\3\60\3")
        buf.write("\60\3\60\3\60\5\60\u01c7\n\60\3\61\3\61\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\65")
        buf.write("\3\65\3\65\3\65\3\65\3\65\5\65\u01de\n\65\3\65\3\65\3")
        buf.write("\66\3\66\3\66\3\66\3\66\3\66\5\66\u01e8\n\66\3\66\3\66")
        buf.write("\3\67\3\67\3\67\3\67\3\67\5\67\u01f1\n\67\3\67\3\67\3")
        buf.write("\67\2\b\34\36 &(*8\2\4\6\b\n\f\16\20\22\24\26\30\32\34")
        buf.write("\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjl\2")
        buf.write("\13\3\2\25\26\3\2\60\61\3\2!\"\4\2\34 ..\3\2,-\3\2&\'")
        buf.write("\3\2(*\3\2<=\5\2\n\13\62\63;;\2\u01ff\2n\3\2\2\2\4u\3")
        buf.write("\2\2\2\6w\3\2\2\2\b\u0084\3\2\2\2\n\u008b\3\2\2\2\f\u008f")
        buf.write("\3\2\2\2\16\u0091\3\2\2\2\20\u009c\3\2\2\2\22\u00a2\3")
        buf.write("\2\2\2\24\u00aa\3\2\2\2\26\u00b1\3\2\2\2\30\u00b8\3\2")
        buf.write("\2\2\32\u00bf\3\2\2\2\34\u00c1\3\2\2\2\36\u00cc\3\2\2")
        buf.write("\2 \u00d7\3\2\2\2\"\u00e5\3\2\2\2$\u00ea\3\2\2\2&\u00ec")
        buf.write("\3\2\2\2(\u00f6\3\2\2\2*\u0101\3\2\2\2,\u0110\3\2\2\2")
        buf.write(".\u0122\3\2\2\2\60\u0124\3\2\2\2\62\u012c\3\2\2\2\64\u013a")
        buf.write("\3\2\2\2\66\u013c\3\2\2\28\u0144\3\2\2\2:\u0146\3\2\2")
        buf.write("\2<\u0151\3\2\2\2>\u015b\3\2\2\2@\u015d\3\2\2\2B\u0162")
        buf.write("\3\2\2\2D\u0178\3\2\2\2F\u017a\3\2\2\2H\u018a\3\2\2\2")
        buf.write("J\u018d\3\2\2\2L\u0190\3\2\2\2N\u0198\3\2\2\2P\u019c\3")
        buf.write("\2\2\2R\u01a6\3\2\2\2T\u01a8\3\2\2\2V\u01aa\3\2\2\2X\u01b4")
        buf.write("\3\2\2\2Z\u01b8\3\2\2\2\\\u01ba\3\2\2\2^\u01c6\3\2\2\2")
        buf.write("`\u01c8\3\2\2\2b\u01ca\3\2\2\2d\u01cf\3\2\2\2f\u01d3\3")
        buf.write("\2\2\2h\u01d7\3\2\2\2j\u01e1\3\2\2\2l\u01eb\3\2\2\2no")
        buf.write("\5\4\3\2op\7\2\2\3p\3\3\2\2\2qr\5\6\4\2rs\5\4\3\2sv\3")
        buf.write("\2\2\2tv\5\6\4\2uq\3\2\2\2ut\3\2\2\2v\5\3\2\2\2wx\7\24")
        buf.write("\2\2x{\7\61\2\2y|\5\b\5\2z|\3\2\2\2{y\3\2\2\2{z\3\2\2")
        buf.write("\2|}\3\2\2\2}\u0080\7@\2\2~\u0081\5\n\6\2\177\u0081\3")
        buf.write("\2\2\2\u0080~\3\2\2\2\u0080\177\3\2\2\2\u0081\u0082\3")
        buf.write("\2\2\2\u0082\u0083\7A\2\2\u0083\7\3\2\2\2\u0084\u0085")
        buf.write("\7D\2\2\u0085\u0086\7\61\2\2\u0086\t\3\2\2\2\u0087\u0088")
        buf.write("\5\f\7\2\u0088\u0089\5\n\6\2\u0089\u008c\3\2\2\2\u008a")
        buf.write("\u008c\5\f\7\2\u008b\u0087\3\2\2\2\u008b\u008a\3\2\2\2")
        buf.write("\u008c\13\3\2\2\2\u008d\u0090\5\16\b\2\u008e\u0090\5\62")
        buf.write("\32\2\u008f\u008d\3\2\2\2\u008f\u008e\3\2\2\2\u0090\r")
        buf.write("\3\2\2\2\u0091\u0092\5\20\t\2\u0092\u0093\5\22\n\2\u0093")
        buf.write("\u0094\7D\2\2\u0094\u0098\5\24\13\2\u0095\u0096\7/\2\2")
        buf.write("\u0096\u0099\5\26\f\2\u0097\u0099\3\2\2\2\u0098\u0095")
        buf.write("\3\2\2\2\u0098\u0097\3\2\2\2\u0099\u009a\3\2\2\2\u009a")
        buf.write("\u009b\7B\2\2\u009b\17\3\2\2\2\u009c\u009d\t\2\2\2\u009d")
        buf.write("\21\3\2\2\2\u009e\u009f\t\3\2\2\u009f\u00a0\7C\2\2\u00a0")
        buf.write("\u00a3\5\22\n\2\u00a1\u00a3\t\3\2\2\u00a2\u009e\3\2\2")
        buf.write("\2\u00a2\u00a1\3\2\2\2\u00a3\23\3\2\2\2\u00a4\u00ab\7")
        buf.write("\20\2\2\u00a5\u00ab\7\16\2\2\u00a6\u00ab\7\17\2\2\u00a7")
        buf.write("\u00ab\7\21\2\2\u00a8\u00ab\5\\/\2\u00a9\u00ab\7\24\2")
        buf.write("\2\u00aa\u00a4\3\2\2\2\u00aa\u00a5\3\2\2\2\u00aa\u00a6")
        buf.write("\3\2\2\2\u00aa\u00a7\3\2\2\2\u00aa\u00a8\3\2\2\2\u00aa")
        buf.write("\u00a9\3\2\2\2\u00ab\25\3\2\2\2\u00ac\u00ad\5\30\r\2\u00ad")
        buf.write("\u00ae\7C\2\2\u00ae\u00af\5\26\f\2\u00af\u00b2\3\2\2\2")
        buf.write("\u00b0\u00b2\5\30\r\2\u00b1\u00ac\3\2\2\2\u00b1\u00b0")
        buf.write("\3\2\2\2\u00b2\27\3\2\2\2\u00b3\u00b4\5\32\16\2\u00b4")
        buf.write("\u00b5\t\4\2\2\u00b5\u00b6\5\32\16\2\u00b6\u00b9\3\2\2")
        buf.write("\2\u00b7\u00b9\5\32\16\2\u00b8\u00b3\3\2\2\2\u00b8\u00b7")
        buf.write("\3\2\2\2\u00b9\31\3\2\2\2\u00ba\u00bb\5\34\17\2\u00bb")
        buf.write("\u00bc\t\5\2\2\u00bc\u00bd\5\34\17\2\u00bd\u00c0\3\2\2")
        buf.write("\2\u00be\u00c0\5\34\17\2\u00bf\u00ba\3\2\2\2\u00bf\u00be")
        buf.write("\3\2\2\2\u00c0\33\3\2\2\2\u00c1\u00c2\b\17\1\2\u00c2\u00c3")
        buf.write("\5\36\20\2\u00c3\u00c9\3\2\2\2\u00c4\u00c5\f\4\2\2\u00c5")
        buf.write("\u00c6\t\6\2\2\u00c6\u00c8\5\36\20\2\u00c7\u00c4\3\2\2")
        buf.write("\2\u00c8\u00cb\3\2\2\2\u00c9\u00c7\3\2\2\2\u00c9\u00ca")
        buf.write("\3\2\2\2\u00ca\35\3\2\2\2\u00cb\u00c9\3\2\2\2\u00cc\u00cd")
        buf.write("\b\20\1\2\u00cd\u00ce\5 \21\2\u00ce\u00d4\3\2\2\2\u00cf")
        buf.write("\u00d0\f\4\2\2\u00d0\u00d1\t\7\2\2\u00d1\u00d3\5 \21\2")
        buf.write("\u00d2\u00cf\3\2\2\2\u00d3\u00d6\3\2\2\2\u00d4\u00d2\3")
        buf.write("\2\2\2\u00d4\u00d5\3\2\2\2\u00d5\37\3\2\2\2\u00d6\u00d4")
        buf.write("\3\2\2\2\u00d7\u00d8\b\21\1\2\u00d8\u00d9\5\"\22\2\u00d9")
        buf.write("\u00df\3\2\2\2\u00da\u00db\f\4\2\2\u00db\u00dc\t\b\2\2")
        buf.write("\u00dc\u00de\5\"\22\2\u00dd\u00da\3\2\2\2\u00de\u00e1")
        buf.write("\3\2\2\2\u00df\u00dd\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0")
        buf.write("!\3\2\2\2\u00e1\u00df\3\2\2\2\u00e2\u00e3\7+\2\2\u00e3")
        buf.write("\u00e6\5\"\22\2\u00e4\u00e6\5$\23\2\u00e5\u00e2\3\2\2")
        buf.write("\2\u00e5\u00e4\3\2\2\2\u00e6#\3\2\2\2\u00e7\u00e8\7\'")
        buf.write("\2\2\u00e8\u00eb\5$\23\2\u00e9\u00eb\5&\24\2\u00ea\u00e7")
        buf.write("\3\2\2\2\u00ea\u00e9\3\2\2\2\u00eb%\3\2\2\2\u00ec\u00ed")
        buf.write("\b\24\1\2\u00ed\u00ee\5(\25\2\u00ee\u00f3\3\2\2\2\u00ef")
        buf.write("\u00f0\f\4\2\2\u00f0\u00f2\t\t\2\2\u00f1\u00ef\3\2\2\2")
        buf.write("\u00f2\u00f5\3\2\2\2\u00f3\u00f1\3\2\2\2\u00f3\u00f4\3")
        buf.write("\2\2\2\u00f4\'\3\2\2\2\u00f5\u00f3\3\2\2\2\u00f6\u00f7")
        buf.write("\b\25\1\2\u00f7\u00f8\5*\26\2\u00f8\u00fe\3\2\2\2\u00f9")
        buf.write("\u00fa\f\4\2\2\u00fa\u00fb\7#\2\2\u00fb\u00fd\5*\26\2")
        buf.write("\u00fc\u00f9\3\2\2\2\u00fd\u0100\3\2\2\2\u00fe\u00fc\3")
        buf.write("\2\2\2\u00fe\u00ff\3\2\2\2\u00ff)\3\2\2\2\u0100\u00fe")
        buf.write("\3\2\2\2\u0101\u0102\b\26\1\2\u0102\u0103\5,\27\2\u0103")
        buf.write("\u0109\3\2\2\2\u0104\u0105\f\4\2\2\u0105\u0106\7$\2\2")
        buf.write("\u0106\u0108\5*\26\5\u0107\u0104\3\2\2\2\u0108\u010b\3")
        buf.write("\2\2\2\u0109\u0107\3\2\2\2\u0109\u010a\3\2\2\2\u010a+")
        buf.write("\3\2\2\2\u010b\u0109\3\2\2\2\u010c\u010d\7\31\2\2\u010d")
        buf.write("\u010e\7\61\2\2\u010e\u0111\5,\27\2\u010f\u0111\5.\30")
        buf.write("\2\u0110\u010c\3\2\2\2\u0110\u010f\3\2\2\2\u0111-\3\2")
        buf.write("\2\2\u0112\u0115\7>\2\2\u0113\u0116\5\30\r\2\u0114\u0116")
        buf.write("\3\2\2\2\u0115\u0113\3\2\2\2\u0115\u0114\3\2\2\2\u0116")
        buf.write("\u0117\3\2\2\2\u0117\u0123\7?\2\2\u0118\u0123\7\23\2\2")
        buf.write("\u0119\u0123\7\63\2\2\u011a\u0123\7\62\2\2\u011b\u0123")
        buf.write("\7\n\2\2\u011c\u0123\7\13\2\2\u011d\u0123\7;\2\2\u011e")
        buf.write("\u0123\7\61\2\2\u011f\u0123\5V,\2\u0120\u0123\5P)\2\u0121")
        buf.write("\u0123\5\60\31\2\u0122\u0112\3\2\2\2\u0122\u0118\3\2\2")
        buf.write("\2\u0122\u0119\3\2\2\2\u0122\u011a\3\2\2\2\u0122\u011b")
        buf.write("\3\2\2\2\u0122\u011c\3\2\2\2\u0122\u011d\3\2\2\2\u0122")
        buf.write("\u011e\3\2\2\2\u0122\u011f\3\2\2\2\u0122\u0120\3\2\2\2")
        buf.write("\u0122\u0121\3\2\2\2\u0123/\3\2\2\2\u0124\u0125\7\61\2")
        buf.write("\2\u0125\u0128\7>\2\2\u0126\u0129\5\26\f\2\u0127\u0129")
        buf.write("\3\2\2\2\u0128\u0126\3\2\2\2\u0128\u0127\3\2\2\2\u0129")
        buf.write("\u012a\3\2\2\2\u012a\u012b\7?\2\2\u012b\61\3\2\2\2\u012c")
        buf.write("\u012d\t\3\2\2\u012d\u0130\7>\2\2\u012e\u0131\5\64\33")
        buf.write("\2\u012f\u0131\3\2\2\2\u0130\u012e\3\2\2\2\u0130\u012f")
        buf.write("\3\2\2\2\u0131\u0132\3\2\2\2\u0132\u0133\7?\2\2\u0133")
        buf.write("\u0134\5:\36\2\u0134\63\3\2\2\2\u0135\u0136\5\66\34\2")
        buf.write("\u0136\u0137\7B\2\2\u0137\u0138\5\64\33\2\u0138\u013b")
        buf.write("\3\2\2\2\u0139\u013b\5\66\34\2\u013a\u0135\3\2\2\2\u013a")
        buf.write("\u0139\3\2\2\2\u013b\65\3\2\2\2\u013c\u013d\58\35\2\u013d")
        buf.write("\u013e\7D\2\2\u013e\u013f\5\24\13\2\u013f\67\3\2\2\2\u0140")
        buf.write("\u0141\7\61\2\2\u0141\u0142\7C\2\2\u0142\u0145\58\35\2")
        buf.write("\u0143\u0145\7\61\2\2\u0144\u0140\3\2\2\2\u0144\u0143")
        buf.write("\3\2\2\2\u01459\3\2\2\2\u0146\u0149\7@\2\2\u0147\u014a")
        buf.write("\5<\37\2\u0148\u014a\3\2\2\2\u0149\u0147\3\2\2\2\u0149")
        buf.write("\u0148\3\2\2\2\u014a\u014b\3\2\2\2\u014b\u014c\7A\2\2")
        buf.write("\u014c;\3\2\2\2\u014d\u014e\5> \2\u014e\u014f\5<\37\2")
        buf.write("\u014f\u0152\3\2\2\2\u0150\u0152\5> \2\u0151\u014d\3\2")
        buf.write("\2\2\u0151\u0150\3\2\2\2\u0152=\3\2\2\2\u0153\u015c\5")
        buf.write("\16\b\2\u0154\u015c\5@!\2\u0155\u015c\5B\"\2\u0156\u015c")
        buf.write("\5F$\2\u0157\u015c\5H%\2\u0158\u015c\5J&\2\u0159\u015c")
        buf.write("\5L\'\2\u015a\u015c\5N(\2\u015b\u0153\3\2\2\2\u015b\u0154")
        buf.write("\3\2\2\2\u015b\u0155\3\2\2\2\u015b\u0156\3\2\2\2\u015b")
        buf.write("\u0157\3\2\2\2\u015b\u0158\3\2\2\2\u015b\u0159\3\2\2\2")
        buf.write("\u015b\u015a\3\2\2\2\u015c?\3\2\2\2\u015d\u015e\t\3\2")
        buf.write("\2\u015e\u015f\7/\2\2\u015f\u0160\5\30\r\2\u0160\u0161")
        buf.write("\7B\2\2\u0161A\3\2\2\2\u0162\u0163\7\6\2\2\u0163\u0164")
        buf.write("\7>\2\2\u0164\u0165\5\30\r\2\u0165\u0166\7?\2\2\u0166")
        buf.write("\u0169\5:\36\2\u0167\u016a\5D#\2\u0168\u016a\3\2\2\2\u0169")
        buf.write("\u0167\3\2\2\2\u0169\u0168\3\2\2\2\u016a\u016e\3\2\2\2")
        buf.write("\u016b\u016c\7\b\2\2\u016c\u016f\5:\36\2\u016d\u016f\3")
        buf.write("\2\2\2\u016e\u016b\3\2\2\2\u016e\u016d\3\2\2\2\u016fC")
        buf.write("\3\2\2\2\u0170\u0171\7\7\2\2\u0171\u0172\7>\2\2\u0172")
        buf.write("\u0173\5\30\r\2\u0173\u0174\7?\2\2\u0174\u0175\5:\36\2")
        buf.write("\u0175\u0176\5D#\2\u0176\u0179\3\2\2\2\u0177\u0179\3\2")
        buf.write("\2\2\u0178\u0170\3\2\2\2\u0178\u0177\3\2\2\2\u0179E\3")
        buf.write("\2\2\2\u017a\u017b\7\t\2\2\u017b\u017c\7>\2\2\u017c\u017d")
        buf.write("\t\3\2\2\u017d\u017e\7\r\2\2\u017e\u017f\7\63\2\2\u017f")
        buf.write("\u0180\7\3\2\2\u0180\u0185\7\63\2\2\u0181\u0182\7<\2\2")
        buf.write("\u0182\u0183\7\63\2\2\u0183\u0186\7=\2\2\u0184\u0186\3")
        buf.write("\2\2\2\u0185\u0181\3\2\2\2\u0185\u0184\3\2\2\2\u0186\u0187")
        buf.write("\3\2\2\2\u0187\u0188\7?\2\2\u0188\u0189\5:\36\2\u0189")
        buf.write("G\3\2\2\2\u018a\u018b\7\4\2\2\u018b\u018c\7B\2\2\u018c")
        buf.write("I\3\2\2\2\u018d\u018e\7\5\2\2\u018e\u018f\7B\2\2\u018f")
        buf.write("K\3\2\2\2\u0190\u0191\7\22\2\2\u0191\u0192\5\30\r\2\u0192")
        buf.write("\u0193\7B\2\2\u0193M\3\2\2\2\u0194\u0199\5d\63\2\u0195")
        buf.write("\u0199\5j\66\2\u0196\u0199\5h\65\2\u0197\u0199\5f\64\2")
        buf.write("\u0198\u0194\3\2\2\2\u0198\u0195\3\2\2\2\u0198\u0196\3")
        buf.write("\2\2\2\u0198\u0197\3\2\2\2\u0199\u019a\3\2\2\2\u019a\u019b")
        buf.write("\7B\2\2\u019bO\3\2\2\2\u019c\u019d\7\f\2\2\u019d\u019e")
        buf.write("\7>\2\2\u019e\u019f\5R*\2\u019f\u01a0\7?\2\2\u01a0Q\3")
        buf.write("\2\2\2\u01a1\u01a2\5T+\2\u01a2\u01a3\7C\2\2\u01a3\u01a4")
        buf.write("\5R*\2\u01a4\u01a7\3\2\2\2\u01a5\u01a7\5T+\2\u01a6\u01a1")
        buf.write("\3\2\2\2\u01a6\u01a5\3\2\2\2\u01a7S\3\2\2\2\u01a8\u01a9")
        buf.write("\t\n\2\2\u01a9U\3\2\2\2\u01aa\u01ab\7\f\2\2\u01ab\u01ac")
        buf.write("\7>\2\2\u01ac\u01ad\5X-\2\u01ad\u01ae\7?\2\2\u01aeW\3")
        buf.write("\2\2\2\u01af\u01b0\5Z.\2\u01b0\u01b1\7C\2\2\u01b1\u01b2")
        buf.write("\5X-\2\u01b2\u01b5\3\2\2\2\u01b3\u01b5\5Z.\2\u01b4\u01af")
        buf.write("\3\2\2\2\u01b4\u01b3\3\2\2\2\u01b5Y\3\2\2\2\u01b6\u01b9")
        buf.write("\5V,\2\u01b7\u01b9\5P)\2\u01b8\u01b6\3\2\2\2\u01b8\u01b7")
        buf.write("\3\2\2\2\u01b9[\3\2\2\2\u01ba\u01bb\7\f\2\2\u01bb\u01bc")
        buf.write("\7<\2\2\u01bc\u01bd\5^\60\2\u01bd\u01be\7C\2\2\u01be\u01bf")
        buf.write("\5`\61\2\u01bf\u01c0\7=\2\2\u01c0]\3\2\2\2\u01c1\u01c7")
        buf.write("\7\16\2\2\u01c2\u01c7\7\17\2\2\u01c3\u01c7\7\20\2\2\u01c4")
        buf.write("\u01c7\5\\/\2\u01c5\u01c7\7\21\2\2\u01c6\u01c1\3\2\2\2")
        buf.write("\u01c6\u01c2\3\2\2\2\u01c6\u01c3\3\2\2\2\u01c6\u01c4\3")
        buf.write("\2\2\2\u01c6\u01c5\3\2\2\2\u01c7_\3\2\2\2\u01c8\u01c9")
        buf.write("\7\63\2\2\u01c9a\3\2\2\2\u01ca\u01cb\7\61\2\2\u01cb\u01cc")
        buf.write("\7<\2\2\u01cc\u01cd\7\63\2\2\u01cd\u01ce\7=\2\2\u01ce")
        buf.write("c\3\2\2\2\u01cf\u01d0\5\30\r\2\u01d0\u01d1\7#\2\2\u01d1")
        buf.write("\u01d2\7\61\2\2\u01d2e\3\2\2\2\u01d3\u01d4\7\61\2\2\u01d4")
        buf.write("\u01d5\7$\2\2\u01d5\u01d6\7\60\2\2\u01d6g\3\2\2\2\u01d7")
        buf.write("\u01d8\5\30\r\2\u01d8\u01d9\7#\2\2\u01d9\u01da\7\61\2")
        buf.write("\2\u01da\u01dd\7>\2\2\u01db\u01de\5\26\f\2\u01dc\u01de")
        buf.write("\3\2\2\2\u01dd\u01db\3\2\2\2\u01dd\u01dc\3\2\2\2\u01de")
        buf.write("\u01df\3\2\2\2\u01df\u01e0\7?\2\2\u01e0i\3\2\2\2\u01e1")
        buf.write("\u01e2\7\61\2\2\u01e2\u01e3\7$\2\2\u01e3\u01e4\7\60\2")
        buf.write("\2\u01e4\u01e7\7>\2\2\u01e5\u01e8\5\26\f\2\u01e6\u01e8")
        buf.write("\3\2\2\2\u01e7\u01e5\3\2\2\2\u01e7\u01e6\3\2\2\2\u01e8")
        buf.write("\u01e9\3\2\2\2\u01e9\u01ea\7?\2\2\u01eak\3\2\2\2\u01eb")
        buf.write("\u01ec\7\31\2\2\u01ec\u01ed\7\61\2\2\u01ed\u01f0\7>\2")
        buf.write("\2\u01ee\u01f1\5\26\f\2\u01ef\u01f1\3\2\2\2\u01f0\u01ee")
        buf.write("\3\2\2\2\u01f0\u01ef\3\2\2\2\u01f1\u01f2\3\2\2\2\u01f2")
        buf.write("\u01f3\7?\2\2\u01f3m\3\2\2\2+u{\u0080\u008b\u008f\u0098")
        buf.write("\u00a2\u00aa\u00b1\u00b8\u00bf\u00c9\u00d4\u00df\u00e5")
        buf.write("\u00ea\u00f3\u00fe\u0109\u0110\u0115\u0122\u0128\u0130")
        buf.write("\u013a\u0144\u0149\u0151\u015b\u0169\u016e\u0178\u0185")
        buf.write("\u0198\u01a6\u01b4\u01b8\u01c6\u01dd\u01e7\u01f0")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'..'", "'Break'", "'Continue'", "'If'", 
                     "'Elseif'", "'Else'", "'Foreach'", "'True'", "'False'", 
                     "'Array'", "'In'", "'Int'", "'Float'", "'Boolean'", 
                     "'String'", "'Return'", "'Null'", "'Class'", "'Val'", 
                     "'Var'", "'Constructor'", "'Destructor'", "'New'", 
                     "'By'", "'Self'", "'!='", "'<='", "'>='", "'>'", "'<'", 
                     "'==.'", "'+.'", "'.'", "'::'", "'->'", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", 
                     "'='", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'\b'", "'\f'", "'\r'", "'\n'", "'\t'", "'''", "'\\'", 
                     "<INVALID>", "'['", "']'", "'('", "')'", "'{'", "'}'", 
                     "';'", "','", "':'", "'##'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "BREAK", "CONTINUE", "IF", 
                      "ELSEIF", "ELSE", "FOREACH", "TRUE", "FALSE", "ARRAY", 
                      "IN", "INTTYPE", "FLOATTYPE", "BOOLEAN", "STRING", 
                      "RETURN", "NULL", "CLASS", "VAL", "VAR", "CONSTRUCTOR", 
                      "DESTRUCTOR", "NEW", "BY", "SELF", "NOTEQUAL", "NOTLARGER", 
                      "NOTSMALLER", "LARGER", "SMALLER", "COMPARSTR", "CONCAT", 
                      "INSTANT", "STATICATTR", "INDEXOPR", "ADD", "MINUS", 
                      "MULTI", "DIV", "PERCENT", "NOT", "AND", "OR", "COMPAR", 
                      "EQUAL", "STATIC", "ID", "FLOAT", "INT", "BACKSPACE", 
                      "FORMFEED", "CARRETURN", "NEWLINE", "HORTAB", "SINGQ", 
                      "BACKSLASH", "STR", "LS", "RS", "LB", "RB", "LP", 
                      "RP", "SEMI", "COMMA", "COLON", "COMMENT", "WS", "ERROR_CHAR", 
                      "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_classdecls = 1
    RULE_classdecl = 2
    RULE_superclass = 3
    RULE_memberlist = 4
    RULE_member = 5
    RULE_attr = 6
    RULE_attrtype = 7
    RULE_idlist = 8
    RULE_typ = 9
    RULE_exprlist = 10
    RULE_expr = 11
    RULE_exp1 = 12
    RULE_exp2 = 13
    RULE_exp3 = 14
    RULE_exp4 = 15
    RULE_exp5 = 16
    RULE_exp6 = 17
    RULE_exp7 = 18
    RULE_exp8 = 19
    RULE_exp9 = 20
    RULE_exp10 = 21
    RULE_exp11 = 22
    RULE_call = 23
    RULE_method = 24
    RULE_paramlist = 25
    RULE_param = 26
    RULE_idenlist = 27
    RULE_blockstate = 28
    RULE_statements = 29
    RULE_sta = 30
    RULE_lhs = 31
    RULE_ifsta = 32
    RULE_eliflist = 33
    RULE_forsta = 34
    RULE_breaksta = 35
    RULE_continuesta = 36
    RULE_returnsta = 37
    RULE_methodsta = 38
    RULE_indexedarr = 39
    RULE_literals = 40
    RULE_lit = 41
    RULE_multiarr = 42
    RULE_arrlist = 43
    RULE_arr = 44
    RULE_arrdecl = 45
    RULE_element = 46
    RULE_size = 47
    RULE_arrindex = 48
    RULE_instance = 49
    RULE_staatr = 50
    RULE_imethodi = 51
    RULE_smethodi = 52
    RULE_newsta = 53

    ruleNames =  [ "program", "classdecls", "classdecl", "superclass", "memberlist", 
                   "member", "attr", "attrtype", "idlist", "typ", "exprlist", 
                   "expr", "exp1", "exp2", "exp3", "exp4", "exp5", "exp6", 
                   "exp7", "exp8", "exp9", "exp10", "exp11", "call", "method", 
                   "paramlist", "param", "idenlist", "blockstate", "statements", 
                   "sta", "lhs", "ifsta", "eliflist", "forsta", "breaksta", 
                   "continuesta", "returnsta", "methodsta", "indexedarr", 
                   "literals", "lit", "multiarr", "arrlist", "arr", "arrdecl", 
                   "element", "size", "arrindex", "instance", "staatr", 
                   "imethodi", "smethodi", "newsta" ]

    EOF = Token.EOF
    T__0=1
    BREAK=2
    CONTINUE=3
    IF=4
    ELSEIF=5
    ELSE=6
    FOREACH=7
    TRUE=8
    FALSE=9
    ARRAY=10
    IN=11
    INTTYPE=12
    FLOATTYPE=13
    BOOLEAN=14
    STRING=15
    RETURN=16
    NULL=17
    CLASS=18
    VAL=19
    VAR=20
    CONSTRUCTOR=21
    DESTRUCTOR=22
    NEW=23
    BY=24
    SELF=25
    NOTEQUAL=26
    NOTLARGER=27
    NOTSMALLER=28
    LARGER=29
    SMALLER=30
    COMPARSTR=31
    CONCAT=32
    INSTANT=33
    STATICATTR=34
    INDEXOPR=35
    ADD=36
    MINUS=37
    MULTI=38
    DIV=39
    PERCENT=40
    NOT=41
    AND=42
    OR=43
    COMPAR=44
    EQUAL=45
    STATIC=46
    ID=47
    FLOAT=48
    INT=49
    BACKSPACE=50
    FORMFEED=51
    CARRETURN=52
    NEWLINE=53
    HORTAB=54
    SINGQ=55
    BACKSLASH=56
    STR=57
    LS=58
    RS=59
    LB=60
    RB=61
    LP=62
    RP=63
    SEMI=64
    COMMA=65
    COLON=66
    COMMENT=67
    WS=68
    ERROR_CHAR=69
    ILLEGAL_ESCAPE=70

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classdecls(self):
            return self.getTypedRuleContext(D96Parser.ClassdeclsContext,0)


        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_program




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.classdecls()
            self.state = 109
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassdeclsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classdecl(self):
            return self.getTypedRuleContext(D96Parser.ClassdeclContext,0)


        def classdecls(self):
            return self.getTypedRuleContext(D96Parser.ClassdeclsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_classdecls




    def classdecls(self):

        localctx = D96Parser.ClassdeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_classdecls)
        try:
            self.state = 115
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 111
                self.classdecl()
                self.state = 112
                self.classdecls()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 114
                self.classdecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassdeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(D96Parser.CLASS, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def superclass(self):
            return self.getTypedRuleContext(D96Parser.SuperclassContext,0)


        def memberlist(self):
            return self.getTypedRuleContext(D96Parser.MemberlistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_classdecl




    def classdecl(self):

        localctx = D96Parser.ClassdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_classdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(D96Parser.CLASS)
            self.state = 118
            self.match(D96Parser.ID)
            self.state = 121
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COLON]:
                self.state = 119
                self.superclass()
                pass
            elif token in [D96Parser.LP]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 123
            self.match(D96Parser.LP)
            self.state = 126
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR, D96Parser.STATIC, D96Parser.ID]:
                self.state = 124
                self.memberlist()
                pass
            elif token in [D96Parser.RP]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 128
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SuperclassContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_superclass




    def superclass(self):

        localctx = D96Parser.SuperclassContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_superclass)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(D96Parser.COLON)
            self.state = 131
            self.match(D96Parser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberlistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member(self):
            return self.getTypedRuleContext(D96Parser.MemberContext,0)


        def memberlist(self):
            return self.getTypedRuleContext(D96Parser.MemberlistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_memberlist




    def memberlist(self):

        localctx = D96Parser.MemberlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_memberlist)
        try:
            self.state = 137
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.member()
                self.state = 134
                self.memberlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 136
                self.member()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attr(self):
            return self.getTypedRuleContext(D96Parser.AttrContext,0)


        def method(self):
            return self.getTypedRuleContext(D96Parser.MethodContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_member




    def member(self):

        localctx = D96Parser.MemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_member)
        try:
            self.state = 141
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 139
                self.attr()
                pass
            elif token in [D96Parser.STATIC, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 140
                self.method()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttrContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attrtype(self):
            return self.getTypedRuleContext(D96Parser.AttrtypeContext,0)


        def idlist(self):
            return self.getTypedRuleContext(D96Parser.IdlistContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def typ(self):
            return self.getTypedRuleContext(D96Parser.TypContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def EQUAL(self):
            return self.getToken(D96Parser.EQUAL, 0)

        def exprlist(self):
            return self.getTypedRuleContext(D96Parser.ExprlistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_attr




    def attr(self):

        localctx = D96Parser.AttrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_attr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.attrtype()
            self.state = 144
            self.idlist()
            self.state = 145
            self.match(D96Parser.COLON)
            self.state = 146
            self.typ()
            self.state = 150
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.EQUAL]:
                self.state = 147
                self.match(D96Parser.EQUAL)
                self.state = 148
                self.exprlist()
                pass
            elif token in [D96Parser.SEMI]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 152
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttrtypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_attrtype




    def attrtype(self):

        localctx = D96Parser.AttrtypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_attrtype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdlistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def idlist(self):
            return self.getTypedRuleContext(D96Parser.IdlistContext,0)


        def STATIC(self):
            return self.getToken(D96Parser.STATIC, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_idlist




    def idlist(self):

        localctx = D96Parser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_idlist)
        self._la = 0 # Token type
        try:
            self.state = 160
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 156
                _la = self._input.LA(1)
                if not(_la==D96Parser.STATIC or _la==D96Parser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 157
                self.match(D96Parser.COMMA)
                self.state = 158
                self.idlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 159
                _la = self._input.LA(1)
                if not(_la==D96Parser.STATIC or _la==D96Parser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLEAN(self):
            return self.getToken(D96Parser.BOOLEAN, 0)

        def INTTYPE(self):
            return self.getToken(D96Parser.INTTYPE, 0)

        def FLOATTYPE(self):
            return self.getToken(D96Parser.FLOATTYPE, 0)

        def STRING(self):
            return self.getToken(D96Parser.STRING, 0)

        def arrdecl(self):
            return self.getTypedRuleContext(D96Parser.ArrdeclContext,0)


        def CLASS(self):
            return self.getToken(D96Parser.CLASS, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_typ




    def typ(self):

        localctx = D96Parser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_typ)
        try:
            self.state = 168
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BOOLEAN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.match(D96Parser.BOOLEAN)
                pass
            elif token in [D96Parser.INTTYPE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 163
                self.match(D96Parser.INTTYPE)
                pass
            elif token in [D96Parser.FLOATTYPE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 164
                self.match(D96Parser.FLOATTYPE)
                pass
            elif token in [D96Parser.STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 165
                self.match(D96Parser.STRING)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 166
                self.arrdecl()
                pass
            elif token in [D96Parser.CLASS]:
                self.enterOuterAlt(localctx, 6)
                self.state = 167
                self.match(D96Parser.CLASS)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprlistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def exprlist(self):
            return self.getTypedRuleContext(D96Parser.ExprlistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exprlist




    def exprlist(self):

        localctx = D96Parser.ExprlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_exprlist)
        try:
            self.state = 175
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 170
                self.expr()
                self.state = 171
                self.match(D96Parser.COMMA)
                self.state = 172
                self.exprlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 174
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Exp1Context)
            else:
                return self.getTypedRuleContext(D96Parser.Exp1Context,i)


        def CONCAT(self):
            return self.getToken(D96Parser.CONCAT, 0)

        def COMPARSTR(self):
            return self.getToken(D96Parser.COMPARSTR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr




    def expr(self):

        localctx = D96Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 182
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.exp1()
                self.state = 178
                _la = self._input.LA(1)
                if not(_la==D96Parser.COMPARSTR or _la==D96Parser.CONCAT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 179
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 181
                self.exp1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Exp2Context)
            else:
                return self.getTypedRuleContext(D96Parser.Exp2Context,i)


        def COMPAR(self):
            return self.getToken(D96Parser.COMPAR, 0)

        def NOTEQUAL(self):
            return self.getToken(D96Parser.NOTEQUAL, 0)

        def NOTSMALLER(self):
            return self.getToken(D96Parser.NOTSMALLER, 0)

        def NOTLARGER(self):
            return self.getToken(D96Parser.NOTLARGER, 0)

        def LARGER(self):
            return self.getToken(D96Parser.LARGER, 0)

        def SMALLER(self):
            return self.getToken(D96Parser.SMALLER, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp1




    def exp1(self):

        localctx = D96Parser.Exp1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_exp1)
        self._la = 0 # Token type
        try:
            self.state = 189
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 184
                self.exp2(0)
                self.state = 185
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.NOTEQUAL) | (1 << D96Parser.NOTLARGER) | (1 << D96Parser.NOTSMALLER) | (1 << D96Parser.LARGER) | (1 << D96Parser.SMALLER) | (1 << D96Parser.COMPAR))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 186
                self.exp2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 188
                self.exp2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(D96Parser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(D96Parser.Exp2Context,0)


        def AND(self):
            return self.getToken(D96Parser.AND, 0)

        def OR(self):
            return self.getToken(D96Parser.OR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp2



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_exp2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 199
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 194
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 195
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.AND or _la==D96Parser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 196
                    self.exp3(0) 
                self.state = 201
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self):
            return self.getTypedRuleContext(D96Parser.Exp4Context,0)


        def exp3(self):
            return self.getTypedRuleContext(D96Parser.Exp3Context,0)


        def ADD(self):
            return self.getToken(D96Parser.ADD, 0)

        def MINUS(self):
            return self.getToken(D96Parser.MINUS, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp3



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_exp3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 210
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 205
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 206
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ADD or _la==D96Parser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 207
                    self.exp4(0) 
                self.state = 212
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp5(self):
            return self.getTypedRuleContext(D96Parser.Exp5Context,0)


        def exp4(self):
            return self.getTypedRuleContext(D96Parser.Exp4Context,0)


        def MULTI(self):
            return self.getToken(D96Parser.MULTI, 0)

        def DIV(self):
            return self.getToken(D96Parser.DIV, 0)

        def PERCENT(self):
            return self.getToken(D96Parser.PERCENT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp4



    def exp4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_exp4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.exp5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 221
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                    self.state = 216
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 217
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.MULTI) | (1 << D96Parser.DIV) | (1 << D96Parser.PERCENT))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 218
                    self.exp5() 
                self.state = 223
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp5Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(D96Parser.NOT, 0)

        def exp5(self):
            return self.getTypedRuleContext(D96Parser.Exp5Context,0)


        def exp6(self):
            return self.getTypedRuleContext(D96Parser.Exp6Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp5




    def exp5(self):

        localctx = D96Parser.Exp5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_exp5)
        try:
            self.state = 227
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 224
                self.match(D96Parser.NOT)
                self.state = 225
                self.exp5()
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.MINUS, D96Parser.ID, D96Parser.FLOAT, D96Parser.INT, D96Parser.STR, D96Parser.LB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
                self.exp6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp6Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(D96Parser.MINUS, 0)

        def exp6(self):
            return self.getTypedRuleContext(D96Parser.Exp6Context,0)


        def exp7(self):
            return self.getTypedRuleContext(D96Parser.Exp7Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp6




    def exp6(self):

        localctx = D96Parser.Exp6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_exp6)
        try:
            self.state = 232
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 229
                self.match(D96Parser.MINUS)
                self.state = 230
                self.exp6()
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.ID, D96Parser.FLOAT, D96Parser.INT, D96Parser.STR, D96Parser.LB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 231
                self.exp7(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp7Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp8(self):
            return self.getTypedRuleContext(D96Parser.Exp8Context,0)


        def exp7(self):
            return self.getTypedRuleContext(D96Parser.Exp7Context,0)


        def LS(self):
            return self.getToken(D96Parser.LS, 0)

        def RS(self):
            return self.getToken(D96Parser.RS, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp7



    def exp7(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp7Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_exp7, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.exp8(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 241
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp7)
                    self.state = 237
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 238
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.LS or _la==D96Parser.RS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume() 
                self.state = 243
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp8Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp9(self):
            return self.getTypedRuleContext(D96Parser.Exp9Context,0)


        def exp8(self):
            return self.getTypedRuleContext(D96Parser.Exp8Context,0)


        def INSTANT(self):
            return self.getToken(D96Parser.INSTANT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp8



    def exp8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_exp8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.exp9(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 252
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp8)
                    self.state = 247
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 248
                    self.match(D96Parser.INSTANT)
                    self.state = 249
                    self.exp9(0) 
                self.state = 254
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp9Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp10(self):
            return self.getTypedRuleContext(D96Parser.Exp10Context,0)


        def exp9(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Exp9Context)
            else:
                return self.getTypedRuleContext(D96Parser.Exp9Context,i)


        def STATICATTR(self):
            return self.getToken(D96Parser.STATICATTR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp9



    def exp9(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp9Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_exp9, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.exp10()
            self._ctx.stop = self._input.LT(-1)
            self.state = 263
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp9Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp9)
                    self.state = 258
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 259
                    self.match(D96Parser.STATICATTR)
                    self.state = 260
                    self.exp9(3) 
                self.state = 265
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp10Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(D96Parser.NEW, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def exp10(self):
            return self.getTypedRuleContext(D96Parser.Exp10Context,0)


        def exp11(self):
            return self.getTypedRuleContext(D96Parser.Exp11Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp10




    def exp10(self):

        localctx = D96Parser.Exp10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_exp10)
        try:
            self.state = 270
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 266
                self.match(D96Parser.NEW)
                self.state = 267
                self.match(D96Parser.ID)
                self.state = 268
                self.exp10()
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.ID, D96Parser.FLOAT, D96Parser.INT, D96Parser.STR, D96Parser.LB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 269
                self.exp11()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp11Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def NULL(self):
            return self.getToken(D96Parser.NULL, 0)

        def INT(self):
            return self.getToken(D96Parser.INT, 0)

        def FLOAT(self):
            return self.getToken(D96Parser.FLOAT, 0)

        def TRUE(self):
            return self.getToken(D96Parser.TRUE, 0)

        def FALSE(self):
            return self.getToken(D96Parser.FALSE, 0)

        def STR(self):
            return self.getToken(D96Parser.STR, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def multiarr(self):
            return self.getTypedRuleContext(D96Parser.MultiarrContext,0)


        def indexedarr(self):
            return self.getTypedRuleContext(D96Parser.IndexedarrContext,0)


        def call(self):
            return self.getTypedRuleContext(D96Parser.CallContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp11




    def exp11(self):

        localctx = D96Parser.Exp11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_exp11)
        try:
            self.state = 288
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 272
                self.match(D96Parser.LB)
                self.state = 275
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.MINUS, D96Parser.NOT, D96Parser.ID, D96Parser.FLOAT, D96Parser.INT, D96Parser.STR, D96Parser.LB]:
                    self.state = 273
                    self.expr()
                    pass
                elif token in [D96Parser.RB]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 277
                self.match(D96Parser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 278
                self.match(D96Parser.NULL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 279
                self.match(D96Parser.INT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 280
                self.match(D96Parser.FLOAT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 281
                self.match(D96Parser.TRUE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 282
                self.match(D96Parser.FALSE)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 283
                self.match(D96Parser.STR)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 284
                self.match(D96Parser.ID)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 285
                self.multiarr()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 286
                self.indexedarr()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 287
                self.call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def exprlist(self):
            return self.getTypedRuleContext(D96Parser.ExprlistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_call




    def call(self):

        localctx = D96Parser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            self.match(D96Parser.ID)
            self.state = 291
            self.match(D96Parser.LB)
            self.state = 294
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.MINUS, D96Parser.NOT, D96Parser.ID, D96Parser.FLOAT, D96Parser.INT, D96Parser.STR, D96Parser.LB]:
                self.state = 292
                self.exprlist()
                pass
            elif token in [D96Parser.RB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 296
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def blockstate(self):
            return self.getTypedRuleContext(D96Parser.BlockstateContext,0)


        def STATIC(self):
            return self.getToken(D96Parser.STATIC, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def paramlist(self):
            return self.getTypedRuleContext(D96Parser.ParamlistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_method




    def method(self):

        localctx = D96Parser.MethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            _la = self._input.LA(1)
            if not(_la==D96Parser.STATIC or _la==D96Parser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 299
            self.match(D96Parser.LB)
            self.state = 302
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID]:
                self.state = 300
                self.paramlist()
                pass
            elif token in [D96Parser.RB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 304
            self.match(D96Parser.RB)
            self.state = 305
            self.blockstate()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamlistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(D96Parser.ParamContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def paramlist(self):
            return self.getTypedRuleContext(D96Parser.ParamlistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_paramlist




    def paramlist(self):

        localctx = D96Parser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_paramlist)
        try:
            self.state = 312
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 307
                self.param()
                self.state = 308
                self.match(D96Parser.SEMI)
                self.state = 309
                self.paramlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 311
                self.param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idenlist(self):
            return self.getTypedRuleContext(D96Parser.IdenlistContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def typ(self):
            return self.getTypedRuleContext(D96Parser.TypContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_param




    def param(self):

        localctx = D96Parser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            self.idenlist()
            self.state = 315
            self.match(D96Parser.COLON)
            self.state = 316
            self.typ()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdenlistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def idenlist(self):
            return self.getTypedRuleContext(D96Parser.IdenlistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_idenlist




    def idenlist(self):

        localctx = D96Parser.IdenlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_idenlist)
        try:
            self.state = 322
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 318
                self.match(D96Parser.ID)
                self.state = 319
                self.match(D96Parser.COMMA)
                self.state = 320
                self.idenlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 321
                self.match(D96Parser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockstateContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def statements(self):
            return self.getTypedRuleContext(D96Parser.StatementsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_blockstate




    def blockstate(self):

        localctx = D96Parser.BlockstateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_blockstate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.match(D96Parser.LP)
            self.state = 327
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.IF, D96Parser.FOREACH, D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.RETURN, D96Parser.NULL, D96Parser.VAL, D96Parser.VAR, D96Parser.NEW, D96Parser.MINUS, D96Parser.NOT, D96Parser.STATIC, D96Parser.ID, D96Parser.FLOAT, D96Parser.INT, D96Parser.STR, D96Parser.LB]:
                self.state = 325
                self.statements()
                pass
            elif token in [D96Parser.RP]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 329
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sta(self):
            return self.getTypedRuleContext(D96Parser.StaContext,0)


        def statements(self):
            return self.getTypedRuleContext(D96Parser.StatementsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_statements




    def statements(self):

        localctx = D96Parser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_statements)
        try:
            self.state = 335
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 331
                self.sta()
                self.state = 332
                self.statements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 334
                self.sta()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attr(self):
            return self.getTypedRuleContext(D96Parser.AttrContext,0)


        def lhs(self):
            return self.getTypedRuleContext(D96Parser.LhsContext,0)


        def ifsta(self):
            return self.getTypedRuleContext(D96Parser.IfstaContext,0)


        def forsta(self):
            return self.getTypedRuleContext(D96Parser.ForstaContext,0)


        def breaksta(self):
            return self.getTypedRuleContext(D96Parser.BreakstaContext,0)


        def continuesta(self):
            return self.getTypedRuleContext(D96Parser.ContinuestaContext,0)


        def returnsta(self):
            return self.getTypedRuleContext(D96Parser.ReturnstaContext,0)


        def methodsta(self):
            return self.getTypedRuleContext(D96Parser.MethodstaContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_sta




    def sta(self):

        localctx = D96Parser.StaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_sta)
        try:
            self.state = 345
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 337
                self.attr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 338
                self.lhs()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 339
                self.ifsta()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 340
                self.forsta()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 341
                self.breaksta()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 342
                self.continuesta()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 343
                self.returnsta()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 344
                self.methodsta()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL(self):
            return self.getToken(D96Parser.EQUAL, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def STATIC(self):
            return self.getToken(D96Parser.STATIC, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_lhs




    def lhs(self):

        localctx = D96Parser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_lhs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            _la = self._input.LA(1)
            if not(_la==D96Parser.STATIC or _la==D96Parser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 348
            self.match(D96Parser.EQUAL)
            self.state = 349
            self.expr()
            self.state = 350
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(D96Parser.IF, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def blockstate(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.BlockstateContext)
            else:
                return self.getTypedRuleContext(D96Parser.BlockstateContext,i)


        def eliflist(self):
            return self.getTypedRuleContext(D96Parser.EliflistContext,0)


        def ELSE(self):
            return self.getToken(D96Parser.ELSE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_ifsta




    def ifsta(self):

        localctx = D96Parser.IfstaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_ifsta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352
            self.match(D96Parser.IF)
            self.state = 353
            self.match(D96Parser.LB)
            self.state = 354
            self.expr()
            self.state = 355
            self.match(D96Parser.RB)
            self.state = 356
            self.blockstate()
            self.state = 359
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 357
                self.eliflist()
                pass

            elif la_ == 2:
                pass


            self.state = 364
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ELSE]:
                self.state = 361
                self.match(D96Parser.ELSE)
                self.state = 362
                self.blockstate()
                pass
            elif token in [D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.IF, D96Parser.FOREACH, D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.RETURN, D96Parser.NULL, D96Parser.VAL, D96Parser.VAR, D96Parser.NEW, D96Parser.MINUS, D96Parser.NOT, D96Parser.STATIC, D96Parser.ID, D96Parser.FLOAT, D96Parser.INT, D96Parser.STR, D96Parser.LB, D96Parser.RP]:
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EliflistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSEIF(self):
            return self.getToken(D96Parser.ELSEIF, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def blockstate(self):
            return self.getTypedRuleContext(D96Parser.BlockstateContext,0)


        def eliflist(self):
            return self.getTypedRuleContext(D96Parser.EliflistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_eliflist




    def eliflist(self):

        localctx = D96Parser.EliflistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_eliflist)
        try:
            self.state = 374
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ELSEIF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 366
                self.match(D96Parser.ELSEIF)
                self.state = 367
                self.match(D96Parser.LB)
                self.state = 368
                self.expr()
                self.state = 369
                self.match(D96Parser.RB)
                self.state = 370
                self.blockstate()
                self.state = 371
                self.eliflist()
                pass
            elif token in [D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.IF, D96Parser.ELSE, D96Parser.FOREACH, D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.RETURN, D96Parser.NULL, D96Parser.VAL, D96Parser.VAR, D96Parser.NEW, D96Parser.MINUS, D96Parser.NOT, D96Parser.STATIC, D96Parser.ID, D96Parser.FLOAT, D96Parser.INT, D96Parser.STR, D96Parser.LB, D96Parser.RP]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForstaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOREACH(self):
            return self.getToken(D96Parser.FOREACH, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def IN(self):
            return self.getToken(D96Parser.IN, 0)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.INT)
            else:
                return self.getToken(D96Parser.INT, i)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def blockstate(self):
            return self.getTypedRuleContext(D96Parser.BlockstateContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def STATIC(self):
            return self.getToken(D96Parser.STATIC, 0)

        def LS(self):
            return self.getToken(D96Parser.LS, 0)

        def RS(self):
            return self.getToken(D96Parser.RS, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_forsta




    def forsta(self):

        localctx = D96Parser.ForstaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_forsta)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            self.match(D96Parser.FOREACH)
            self.state = 377
            self.match(D96Parser.LB)
            self.state = 378
            _la = self._input.LA(1)
            if not(_la==D96Parser.STATIC or _la==D96Parser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 379
            self.match(D96Parser.IN)
            self.state = 380
            self.match(D96Parser.INT)
            self.state = 381
            self.match(D96Parser.T__0)
            self.state = 382
            self.match(D96Parser.INT)
            self.state = 387
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LS]:
                self.state = 383
                self.match(D96Parser.LS)
                self.state = 384
                self.match(D96Parser.INT)
                self.state = 385
                self.match(D96Parser.RS)
                pass
            elif token in [D96Parser.RB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 389
            self.match(D96Parser.RB)
            self.state = 390
            self.blockstate()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakstaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(D96Parser.BREAK, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_breaksta




    def breaksta(self):

        localctx = D96Parser.BreakstaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_breaksta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 392
            self.match(D96Parser.BREAK)
            self.state = 393
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinuestaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(D96Parser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_continuesta




    def continuesta(self):

        localctx = D96Parser.ContinuestaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_continuesta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
            self.match(D96Parser.CONTINUE)
            self.state = 396
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnstaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(D96Parser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_returnsta




    def returnsta(self):

        localctx = D96Parser.ReturnstaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_returnsta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            self.match(D96Parser.RETURN)
            self.state = 399
            self.expr()
            self.state = 400
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodstaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def instance(self):
            return self.getTypedRuleContext(D96Parser.InstanceContext,0)


        def smethodi(self):
            return self.getTypedRuleContext(D96Parser.SmethodiContext,0)


        def imethodi(self):
            return self.getTypedRuleContext(D96Parser.ImethodiContext,0)


        def staatr(self):
            return self.getTypedRuleContext(D96Parser.StaatrContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_methodsta




    def methodsta(self):

        localctx = D96Parser.MethodstaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_methodsta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 402
                self.instance()
                pass

            elif la_ == 2:
                self.state = 403
                self.smethodi()
                pass

            elif la_ == 3:
                self.state = 404
                self.imethodi()
                pass

            elif la_ == 4:
                self.state = 405
                self.staatr()
                pass


            self.state = 408
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexedarrContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def literals(self):
            return self.getTypedRuleContext(D96Parser.LiteralsContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_indexedarr




    def indexedarr(self):

        localctx = D96Parser.IndexedarrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_indexedarr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
            self.match(D96Parser.ARRAY)
            self.state = 411
            self.match(D96Parser.LB)
            self.state = 412
            self.literals()
            self.state = 413
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lit(self):
            return self.getTypedRuleContext(D96Parser.LitContext,0)


        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def literals(self):
            return self.getTypedRuleContext(D96Parser.LiteralsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_literals




    def literals(self):

        localctx = D96Parser.LiteralsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_literals)
        try:
            self.state = 420
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 415
                self.lit()
                self.state = 416
                self.match(D96Parser.COMMA)
                self.state = 417
                self.literals()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 419
                self.lit()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(D96Parser.INT, 0)

        def FLOAT(self):
            return self.getToken(D96Parser.FLOAT, 0)

        def TRUE(self):
            return self.getToken(D96Parser.TRUE, 0)

        def FALSE(self):
            return self.getToken(D96Parser.FALSE, 0)

        def STR(self):
            return self.getToken(D96Parser.STR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_lit




    def lit(self):

        localctx = D96Parser.LitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.FLOAT) | (1 << D96Parser.INT) | (1 << D96Parser.STR))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiarrContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def arrlist(self):
            return self.getTypedRuleContext(D96Parser.ArrlistContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_multiarr




    def multiarr(self):

        localctx = D96Parser.MultiarrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_multiarr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 424
            self.match(D96Parser.ARRAY)
            self.state = 425
            self.match(D96Parser.LB)
            self.state = 426
            self.arrlist()
            self.state = 427
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrlistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arr(self):
            return self.getTypedRuleContext(D96Parser.ArrContext,0)


        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def arrlist(self):
            return self.getTypedRuleContext(D96Parser.ArrlistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_arrlist




    def arrlist(self):

        localctx = D96Parser.ArrlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_arrlist)
        try:
            self.state = 434
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 429
                self.arr()
                self.state = 430
                self.match(D96Parser.COMMA)
                self.state = 431
                self.arrlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 433
                self.arr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiarr(self):
            return self.getTypedRuleContext(D96Parser.MultiarrContext,0)


        def indexedarr(self):
            return self.getTypedRuleContext(D96Parser.IndexedarrContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_arr




    def arr(self):

        localctx = D96Parser.ArrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_arr)
        try:
            self.state = 438
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 436
                self.multiarr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 437
                self.indexedarr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrdeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LS(self):
            return self.getToken(D96Parser.LS, 0)

        def element(self):
            return self.getTypedRuleContext(D96Parser.ElementContext,0)


        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def size(self):
            return self.getTypedRuleContext(D96Parser.SizeContext,0)


        def RS(self):
            return self.getToken(D96Parser.RS, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_arrdecl




    def arrdecl(self):

        localctx = D96Parser.ArrdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_arrdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 440
            self.match(D96Parser.ARRAY)
            self.state = 441
            self.match(D96Parser.LS)
            self.state = 442
            self.element()
            self.state = 443
            self.match(D96Parser.COMMA)
            self.state = 444
            self.size()
            self.state = 445
            self.match(D96Parser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTTYPE(self):
            return self.getToken(D96Parser.INTTYPE, 0)

        def FLOATTYPE(self):
            return self.getToken(D96Parser.FLOATTYPE, 0)

        def BOOLEAN(self):
            return self.getToken(D96Parser.BOOLEAN, 0)

        def arrdecl(self):
            return self.getTypedRuleContext(D96Parser.ArrdeclContext,0)


        def STRING(self):
            return self.getToken(D96Parser.STRING, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_element




    def element(self):

        localctx = D96Parser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_element)
        try:
            self.state = 452
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTTYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 447
                self.match(D96Parser.INTTYPE)
                pass
            elif token in [D96Parser.FLOATTYPE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 448
                self.match(D96Parser.FLOATTYPE)
                pass
            elif token in [D96Parser.BOOLEAN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 449
                self.match(D96Parser.BOOLEAN)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 4)
                self.state = 450
                self.arrdecl()
                pass
            elif token in [D96Parser.STRING]:
                self.enterOuterAlt(localctx, 5)
                self.state = 451
                self.match(D96Parser.STRING)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SizeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(D96Parser.INT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_size




    def size(self):

        localctx = D96Parser.SizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_size)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 454
            self.match(D96Parser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrindexContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LS(self):
            return self.getToken(D96Parser.LS, 0)

        def INT(self):
            return self.getToken(D96Parser.INT, 0)

        def RS(self):
            return self.getToken(D96Parser.RS, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_arrindex




    def arrindex(self):

        localctx = D96Parser.ArrindexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_arrindex)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 456
            self.match(D96Parser.ID)
            self.state = 457
            self.match(D96Parser.LS)
            self.state = 458
            self.match(D96Parser.INT)
            self.state = 459
            self.match(D96Parser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstanceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def INSTANT(self):
            return self.getToken(D96Parser.INSTANT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_instance




    def instance(self):

        localctx = D96Parser.InstanceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_instance)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 461
            self.expr()
            self.state = 462
            self.match(D96Parser.INSTANT)
            self.state = 463
            self.match(D96Parser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StaatrContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def STATICATTR(self):
            return self.getToken(D96Parser.STATICATTR, 0)

        def STATIC(self):
            return self.getToken(D96Parser.STATIC, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_staatr




    def staatr(self):

        localctx = D96Parser.StaatrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_staatr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 465
            self.match(D96Parser.ID)
            self.state = 466
            self.match(D96Parser.STATICATTR)
            self.state = 467
            self.match(D96Parser.STATIC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImethodiContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def INSTANT(self):
            return self.getToken(D96Parser.INSTANT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def exprlist(self):
            return self.getTypedRuleContext(D96Parser.ExprlistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_imethodi




    def imethodi(self):

        localctx = D96Parser.ImethodiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_imethodi)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 469
            self.expr()
            self.state = 470
            self.match(D96Parser.INSTANT)
            self.state = 471
            self.match(D96Parser.ID)
            self.state = 472
            self.match(D96Parser.LB)
            self.state = 475
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.MINUS, D96Parser.NOT, D96Parser.ID, D96Parser.FLOAT, D96Parser.INT, D96Parser.STR, D96Parser.LB]:
                self.state = 473
                self.exprlist()
                pass
            elif token in [D96Parser.RB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 477
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SmethodiContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def STATICATTR(self):
            return self.getToken(D96Parser.STATICATTR, 0)

        def STATIC(self):
            return self.getToken(D96Parser.STATIC, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def exprlist(self):
            return self.getTypedRuleContext(D96Parser.ExprlistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_smethodi




    def smethodi(self):

        localctx = D96Parser.SmethodiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_smethodi)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 479
            self.match(D96Parser.ID)
            self.state = 480
            self.match(D96Parser.STATICATTR)
            self.state = 481
            self.match(D96Parser.STATIC)
            self.state = 482
            self.match(D96Parser.LB)
            self.state = 485
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.MINUS, D96Parser.NOT, D96Parser.ID, D96Parser.FLOAT, D96Parser.INT, D96Parser.STR, D96Parser.LB]:
                self.state = 483
                self.exprlist()
                pass
            elif token in [D96Parser.RB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 487
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NewstaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(D96Parser.NEW, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def exprlist(self):
            return self.getTypedRuleContext(D96Parser.ExprlistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_newsta




    def newsta(self):

        localctx = D96Parser.NewstaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_newsta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 489
            self.match(D96Parser.NEW)
            self.state = 490
            self.match(D96Parser.ID)
            self.state = 491
            self.match(D96Parser.LB)
            self.state = 494
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.MINUS, D96Parser.NOT, D96Parser.ID, D96Parser.FLOAT, D96Parser.INT, D96Parser.STR, D96Parser.LB]:
                self.state = 492
                self.exprlist()
                pass
            elif token in [D96Parser.RB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 496
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[13] = self.exp2_sempred
        self._predicates[14] = self.exp3_sempred
        self._predicates[15] = self.exp4_sempred
        self._predicates[18] = self.exp7_sempred
        self._predicates[19] = self.exp8_sempred
        self._predicates[20] = self.exp9_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp4_sempred(self, localctx:Exp4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def exp7_sempred(self, localctx:Exp7Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def exp8_sempred(self, localctx:Exp8Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def exp9_sempred(self, localctx:Exp9Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         




