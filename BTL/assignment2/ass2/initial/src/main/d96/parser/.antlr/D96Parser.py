# Generated from c:\Users\PC\Downloads\HK212\PPL\BTL\assignment2\ass2\initial\src\main\d96\parser\D96.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3I")
        buf.write("\u0205\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\3\2\3\2\3\2\3\3\3")
        buf.write("\3\3\3\3\3\5\3x\n\3\3\4\3\4\3\4\3\4\5\4~\n\4\3\4\3\4\3")
        buf.write("\4\5\4\u0083\n\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\5")
        buf.write("\6\u008e\n\6\3\7\3\7\5\7\u0092\n\7\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\5\b\u009b\n\b\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\n")
        buf.write("\5\n\u00a5\n\n\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u00ad")
        buf.write("\n\13\3\f\3\f\3\f\3\f\3\f\5\f\u00b4\n\f\3\r\3\r\3\r\3")
        buf.write("\r\3\r\5\r\u00bb\n\r\3\16\3\16\3\16\3\16\3\16\5\16\u00c2")
        buf.write("\n\16\3\17\3\17\3\17\3\17\3\17\3\17\7\17\u00ca\n\17\f")
        buf.write("\17\16\17\u00cd\13\17\3\20\3\20\3\20\3\20\3\20\3\20\7")
        buf.write("\20\u00d5\n\20\f\20\16\20\u00d8\13\20\3\21\3\21\3\21\3")
        buf.write("\21\3\21\3\21\7\21\u00e0\n\21\f\21\16\21\u00e3\13\21\3")
        buf.write("\22\3\22\3\22\5\22\u00e8\n\22\3\23\3\23\3\23\5\23\u00ed")
        buf.write("\n\23\3\24\3\24\5\24\u00f1\n\24\3\25\3\25\3\25\3\25\3")
        buf.write("\25\3\25\7\25\u00f9\n\25\f\25\16\25\u00fc\13\25\3\26\3")
        buf.write("\26\3\26\3\26\3\26\3\26\7\26\u0104\n\26\f\26\16\26\u0107")
        buf.write("\13\26\3\27\3\27\5\27\u010b\n\27\3\30\3\30\3\30\3\30\3")
        buf.write("\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\5\30\u0120\n\30\3\31\3\31\3\31\3")
        buf.write("\31\5\31\u0126\n\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32")
        buf.write("\3\32\5\32\u0130\n\32\3\33\3\33\3\33\3\33\3\34\3\34\3")
        buf.write("\34\5\34\u0139\n\34\3\34\3\34\3\35\3\35\3\35\3\35\5\35")
        buf.write("\u0141\n\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3")
        buf.write("\36\5\36\u014c\n\36\3\37\3\37\3\37\3\37\3\37\5\37\u0153")
        buf.write("\n\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \5 \u0160")
        buf.write("\n \3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\5!\u016c\n!\3\"\3\"")
        buf.write("\3\"\3\"\3\"\3\"\3\"\5\"\u0175\n\"\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3\"\3\"\5\"\u017e\n\"\3\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3")
        buf.write("%\3%\3%\3%\3&\3&\5&\u018f\n&\3&\3&\3\'\3\'\3\'\3\'\3\'")
        buf.write("\3(\3(\3(\3(\3(\5(\u019d\n(\3)\3)\3*\3*\3*\3*\3*\3+\3")
        buf.write("+\3+\3+\3+\5+\u01ab\n+\3,\3,\5,\u01af\n,\3-\3-\3-\3-\3")
        buf.write("-\3-\3-\3.\3.\3.\3.\3.\5.\u01bd\n.\3/\3/\3\60\3\60\3\60")
        buf.write("\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\5\61\u01cd")
        buf.write("\n\61\3\62\3\62\3\62\5\62\u01d2\n\62\3\63\3\63\3\63\3")
        buf.write("\63\3\64\3\64\3\64\3\64\3\64\3\64\3\64\5\64\u01df\n\64")
        buf.write("\3\65\3\65\3\65\3\65\3\66\3\66\5\66\u01e7\n\66\3\66\3")
        buf.write("\66\3\66\3\66\3\66\5\66\u01ee\n\66\3\66\3\66\3\67\3\67")
        buf.write("\3\67\3\67\3\67\3\67\5\67\u01f8\n\67\3\67\3\67\38\38\3")
        buf.write("8\38\38\58\u0201\n8\38\38\38\2\7\34\36 (*9\2\4\6\b\n\f")
        buf.write("\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@")
        buf.write("BDFHJLNPRTVXZ\\^`bdfhjln\2\13\3\2\25\26\3\2\62\63\3\2")
        buf.write("!\"\4\2\34 ..\3\2,-\3\2&\'\3\2(*\4\2\27\30\62\63\5\2\n")
        buf.write("\13\60\60\64\65\2\u0221\2p\3\2\2\2\4w\3\2\2\2\6y\3\2\2")
        buf.write("\2\b\u0086\3\2\2\2\n\u008d\3\2\2\2\f\u0091\3\2\2\2\16")
        buf.write("\u0093\3\2\2\2\20\u009e\3\2\2\2\22\u00a4\3\2\2\2\24\u00ac")
        buf.write("\3\2\2\2\26\u00b3\3\2\2\2\30\u00ba\3\2\2\2\32\u00c1\3")
        buf.write("\2\2\2\34\u00c3\3\2\2\2\36\u00ce\3\2\2\2 \u00d9\3\2\2")
        buf.write("\2\"\u00e7\3\2\2\2$\u00ec\3\2\2\2&\u00f0\3\2\2\2(\u00f2")
        buf.write("\3\2\2\2*\u00fd\3\2\2\2,\u010a\3\2\2\2.\u011f\3\2\2\2")
        buf.write("\60\u0121\3\2\2\2\62\u012f\3\2\2\2\64\u0131\3\2\2\2\66")
        buf.write("\u0135\3\2\2\28\u0140\3\2\2\2:\u014b\3\2\2\2<\u0152\3")
        buf.write("\2\2\2>\u0158\3\2\2\2@\u016b\3\2\2\2B\u016d\3\2\2\2D\u0182")
        buf.write("\3\2\2\2F\u0185\3\2\2\2H\u0188\3\2\2\2J\u018e\3\2\2\2")
        buf.write("L\u0192\3\2\2\2N\u019c\3\2\2\2P\u019e\3\2\2\2R\u01a0\3")
        buf.write("\2\2\2T\u01aa\3\2\2\2V\u01ae\3\2\2\2X\u01b0\3\2\2\2Z\u01bc")
        buf.write("\3\2\2\2\\\u01be\3\2\2\2^\u01c0\3\2\2\2`\u01cc\3\2\2\2")
        buf.write("b\u01d1\3\2\2\2d\u01d3\3\2\2\2f\u01de\3\2\2\2h\u01e0\3")
        buf.write("\2\2\2j\u01e6\3\2\2\2l\u01f1\3\2\2\2n\u01fb\3\2\2\2pq")
        buf.write("\5\4\3\2qr\7\2\2\3r\3\3\2\2\2st\5\6\4\2tu\5\4\3\2ux\3")
        buf.write("\2\2\2vx\5\6\4\2ws\3\2\2\2wv\3\2\2\2x\5\3\2\2\2yz\7\24")
        buf.write("\2\2z}\7\63\2\2{~\5\b\5\2|~\3\2\2\2}{\3\2\2\2}|\3\2\2")
        buf.write("\2~\177\3\2\2\2\177\u0082\7A\2\2\u0080\u0083\5\n\6\2\u0081")
        buf.write("\u0083\3\2\2\2\u0082\u0080\3\2\2\2\u0082\u0081\3\2\2\2")
        buf.write("\u0083\u0084\3\2\2\2\u0084\u0085\7B\2\2\u0085\7\3\2\2")
        buf.write("\2\u0086\u0087\7E\2\2\u0087\u0088\7\63\2\2\u0088\t\3\2")
        buf.write("\2\2\u0089\u008a\5\f\7\2\u008a\u008b\5\n\6\2\u008b\u008e")
        buf.write("\3\2\2\2\u008c\u008e\5\f\7\2\u008d\u0089\3\2\2\2\u008d")
        buf.write("\u008c\3\2\2\2\u008e\13\3\2\2\2\u008f\u0092\5\16\b\2\u0090")
        buf.write("\u0092\5\60\31\2\u0091\u008f\3\2\2\2\u0091\u0090\3\2\2")
        buf.write("\2\u0092\r\3\2\2\2\u0093\u0094\5\20\t\2\u0094\u0095\5")
        buf.write("\22\n\2\u0095\u0096\7E\2\2\u0096\u009a\5\24\13\2\u0097")
        buf.write("\u0098\7/\2\2\u0098\u009b\5\26\f\2\u0099\u009b\3\2\2\2")
        buf.write("\u009a\u0097\3\2\2\2\u009a\u0099\3\2\2\2\u009b\u009c\3")
        buf.write("\2\2\2\u009c\u009d\7C\2\2\u009d\17\3\2\2\2\u009e\u009f")
        buf.write("\t\2\2\2\u009f\21\3\2\2\2\u00a0\u00a1\t\3\2\2\u00a1\u00a2")
        buf.write("\7D\2\2\u00a2\u00a5\5\22\n\2\u00a3\u00a5\t\3\2\2\u00a4")
        buf.write("\u00a0\3\2\2\2\u00a4\u00a3\3\2\2\2\u00a5\23\3\2\2\2\u00a6")
        buf.write("\u00ad\7\20\2\2\u00a7\u00ad\7\16\2\2\u00a8\u00ad\7\17")
        buf.write("\2\2\u00a9\u00ad\7\21\2\2\u00aa\u00ad\5X-\2\u00ab\u00ad")
        buf.write("\7\63\2\2\u00ac\u00a6\3\2\2\2\u00ac\u00a7\3\2\2\2\u00ac")
        buf.write("\u00a8\3\2\2\2\u00ac\u00a9\3\2\2\2\u00ac\u00aa\3\2\2\2")
        buf.write("\u00ac\u00ab\3\2\2\2\u00ad\25\3\2\2\2\u00ae\u00af\5\30")
        buf.write("\r\2\u00af\u00b0\7D\2\2\u00b0\u00b1\5\26\f\2\u00b1\u00b4")
        buf.write("\3\2\2\2\u00b2\u00b4\5\30\r\2\u00b3\u00ae\3\2\2\2\u00b3")
        buf.write("\u00b2\3\2\2\2\u00b4\27\3\2\2\2\u00b5\u00b6\5\32\16\2")
        buf.write("\u00b6\u00b7\t\4\2\2\u00b7\u00b8\5\32\16\2\u00b8\u00bb")
        buf.write("\3\2\2\2\u00b9\u00bb\5\32\16\2\u00ba\u00b5\3\2\2\2\u00ba")
        buf.write("\u00b9\3\2\2\2\u00bb\31\3\2\2\2\u00bc\u00bd\5\34\17\2")
        buf.write("\u00bd\u00be\t\5\2\2\u00be\u00bf\5\34\17\2\u00bf\u00c2")
        buf.write("\3\2\2\2\u00c0\u00c2\5\34\17\2\u00c1\u00bc\3\2\2\2\u00c1")
        buf.write("\u00c0\3\2\2\2\u00c2\33\3\2\2\2\u00c3\u00c4\b\17\1\2\u00c4")
        buf.write("\u00c5\5\36\20\2\u00c5\u00cb\3\2\2\2\u00c6\u00c7\f\4\2")
        buf.write("\2\u00c7\u00c8\t\6\2\2\u00c8\u00ca\5\36\20\2\u00c9\u00c6")
        buf.write("\3\2\2\2\u00ca\u00cd\3\2\2\2\u00cb\u00c9\3\2\2\2\u00cb")
        buf.write("\u00cc\3\2\2\2\u00cc\35\3\2\2\2\u00cd\u00cb\3\2\2\2\u00ce")
        buf.write("\u00cf\b\20\1\2\u00cf\u00d0\5 \21\2\u00d0\u00d6\3\2\2")
        buf.write("\2\u00d1\u00d2\f\4\2\2\u00d2\u00d3\t\7\2\2\u00d3\u00d5")
        buf.write("\5 \21\2\u00d4\u00d1\3\2\2\2\u00d5\u00d8\3\2\2\2\u00d6")
        buf.write("\u00d4\3\2\2\2\u00d6\u00d7\3\2\2\2\u00d7\37\3\2\2\2\u00d8")
        buf.write("\u00d6\3\2\2\2\u00d9\u00da\b\21\1\2\u00da\u00db\5\"\22")
        buf.write("\2\u00db\u00e1\3\2\2\2\u00dc\u00dd\f\4\2\2\u00dd\u00de")
        buf.write("\t\b\2\2\u00de\u00e0\5\"\22\2\u00df\u00dc\3\2\2\2\u00e0")
        buf.write("\u00e3\3\2\2\2\u00e1\u00df\3\2\2\2\u00e1\u00e2\3\2\2\2")
        buf.write("\u00e2!\3\2\2\2\u00e3\u00e1\3\2\2\2\u00e4\u00e5\7+\2\2")
        buf.write("\u00e5\u00e8\5\"\22\2\u00e6\u00e8\5$\23\2\u00e7\u00e4")
        buf.write("\3\2\2\2\u00e7\u00e6\3\2\2\2\u00e8#\3\2\2\2\u00e9\u00ea")
        buf.write("\7\'\2\2\u00ea\u00ed\5$\23\2\u00eb\u00ed\5&\24\2\u00ec")
        buf.write("\u00e9\3\2\2\2\u00ec\u00eb\3\2\2\2\u00ed%\3\2\2\2\u00ee")
        buf.write("\u00f1\5^\60\2\u00ef\u00f1\5(\25\2\u00f0\u00ee\3\2\2\2")
        buf.write("\u00f0\u00ef\3\2\2\2\u00f1\'\3\2\2\2\u00f2\u00f3\b\25")
        buf.write("\1\2\u00f3\u00f4\5*\26\2\u00f4\u00fa\3\2\2\2\u00f5\u00f6")
        buf.write("\f\4\2\2\u00f6\u00f7\7#\2\2\u00f7\u00f9\5*\26\2\u00f8")
        buf.write("\u00f5\3\2\2\2\u00f9\u00fc\3\2\2\2\u00fa\u00f8\3\2\2\2")
        buf.write("\u00fa\u00fb\3\2\2\2\u00fb)\3\2\2\2\u00fc\u00fa\3\2\2")
        buf.write("\2\u00fd\u00fe\b\26\1\2\u00fe\u00ff\5,\27\2\u00ff\u0105")
        buf.write("\3\2\2\2\u0100\u0101\f\4\2\2\u0101\u0102\7$\2\2\u0102")
        buf.write("\u0104\5*\26\5\u0103\u0100\3\2\2\2\u0104\u0107\3\2\2\2")
        buf.write("\u0105\u0103\3\2\2\2\u0105\u0106\3\2\2\2\u0106+\3\2\2")
        buf.write("\2\u0107\u0105\3\2\2\2\u0108\u010b\5n8\2\u0109\u010b\5")
        buf.write(".\30\2\u010a\u0108\3\2\2\2\u010a\u0109\3\2\2\2\u010b-")
        buf.write("\3\2\2\2\u010c\u010d\7?\2\2\u010d\u010e\5\30\r\2\u010e")
        buf.write("\u010f\7@\2\2\u010f\u0120\3\2\2\2\u0110\u0120\7\23\2\2")
        buf.write("\u0111\u0120\7\65\2\2\u0112\u0120\7\64\2\2\u0113\u0120")
        buf.write("\7\n\2\2\u0114\u0120\7\13\2\2\u0115\u0120\7\60\2\2\u0116")
        buf.write("\u0120\7\63\2\2\u0117\u0120\7\62\2\2\u0118\u0120\5R*\2")
        buf.write("\u0119\u0120\5L\'\2\u011a\u0120\7\33\2\2\u011b\u0120\5")
        buf.write("j\66\2\u011c\u0120\5l\67\2\u011d\u0120\5d\63\2\u011e\u0120")
        buf.write("\5h\65\2\u011f\u010c\3\2\2\2\u011f\u0110\3\2\2\2\u011f")
        buf.write("\u0111\3\2\2\2\u011f\u0112\3\2\2\2\u011f\u0113\3\2\2\2")
        buf.write("\u011f\u0114\3\2\2\2\u011f\u0115\3\2\2\2\u011f\u0116\3")
        buf.write("\2\2\2\u011f\u0117\3\2\2\2\u011f\u0118\3\2\2\2\u011f\u0119")
        buf.write("\3\2\2\2\u011f\u011a\3\2\2\2\u011f\u011b\3\2\2\2\u011f")
        buf.write("\u011c\3\2\2\2\u011f\u011d\3\2\2\2\u011f\u011e\3\2\2\2")
        buf.write("\u0120/\3\2\2\2\u0121\u0122\t\t\2\2\u0122\u0125\7?\2\2")
        buf.write("\u0123\u0126\5\62\32\2\u0124\u0126\3\2\2\2\u0125\u0123")
        buf.write("\3\2\2\2\u0125\u0124\3\2\2\2\u0126\u0127\3\2\2\2\u0127")
        buf.write("\u0128\7@\2\2\u0128\u0129\5\66\34\2\u0129\61\3\2\2\2\u012a")
        buf.write("\u012b\5\64\33\2\u012b\u012c\7C\2\2\u012c\u012d\5\62\32")
        buf.write("\2\u012d\u0130\3\2\2\2\u012e\u0130\5\64\33\2\u012f\u012a")
        buf.write("\3\2\2\2\u012f\u012e\3\2\2\2\u0130\63\3\2\2\2\u0131\u0132")
        buf.write("\5\22\n\2\u0132\u0133\7E\2\2\u0133\u0134\5\24\13\2\u0134")
        buf.write("\65\3\2\2\2\u0135\u0138\7A\2\2\u0136\u0139\58\35\2\u0137")
        buf.write("\u0139\3\2\2\2\u0138\u0136\3\2\2\2\u0138\u0137\3\2\2\2")
        buf.write("\u0139\u013a\3\2\2\2\u013a\u013b\7B\2\2\u013b\67\3\2\2")
        buf.write("\2\u013c\u013d\5:\36\2\u013d\u013e\58\35\2\u013e\u0141")
        buf.write("\3\2\2\2\u013f\u0141\5:\36\2\u0140\u013c\3\2\2\2\u0140")
        buf.write("\u013f\3\2\2\2\u01419\3\2\2\2\u0142\u014c\5\16\b\2\u0143")
        buf.write("\u014c\5<\37\2\u0144\u014c\5> \2\u0145\u014c\5B\"\2\u0146")
        buf.write("\u014c\5D#\2\u0147\u014c\5F$\2\u0148\u014c\5H%\2\u0149")
        buf.write("\u014c\5J&\2\u014a\u014c\5\66\34\2\u014b\u0142\3\2\2\2")
        buf.write("\u014b\u0143\3\2\2\2\u014b\u0144\3\2\2\2\u014b\u0145\3")
        buf.write("\2\2\2\u014b\u0146\3\2\2\2\u014b\u0147\3\2\2\2\u014b\u0148")
        buf.write("\3\2\2\2\u014b\u0149\3\2\2\2\u014b\u014a\3\2\2\2\u014c")
        buf.write(";\3\2\2\2\u014d\u0153\5^\60\2\u014e\u0153\5d\63\2\u014f")
        buf.write("\u0153\5h\65\2\u0150\u0153\7\63\2\2\u0151\u0153\7\62\2")
        buf.write("\2\u0152\u014d\3\2\2\2\u0152\u014e\3\2\2\2\u0152\u014f")
        buf.write("\3\2\2\2\u0152\u0150\3\2\2\2\u0152\u0151\3\2\2\2\u0153")
        buf.write("\u0154\3\2\2\2\u0154\u0155\7/\2\2\u0155\u0156\5\30\r\2")
        buf.write("\u0156\u0157\7C\2\2\u0157=\3\2\2\2\u0158\u0159\7\6\2\2")
        buf.write("\u0159\u015a\7?\2\2\u015a\u015b\5\30\r\2\u015b\u015c\7")
        buf.write("@\2\2\u015c\u015f\5\66\34\2\u015d\u0160\5@!\2\u015e\u0160")
        buf.write("\3\2\2\2\u015f\u015d\3\2\2\2\u015f\u015e\3\2\2\2\u0160")
        buf.write("?\3\2\2\2\u0161\u0162\7\7\2\2\u0162\u0163\7?\2\2\u0163")
        buf.write("\u0164\5\30\r\2\u0164\u0165\7@\2\2\u0165\u0166\5\66\34")
        buf.write("\2\u0166\u0167\5@!\2\u0167\u016c\3\2\2\2\u0168\u0169\7")
        buf.write("\b\2\2\u0169\u016c\5\66\34\2\u016a\u016c\3\2\2\2\u016b")
        buf.write("\u0161\3\2\2\2\u016b\u0168\3\2\2\2\u016b\u016a\3\2\2\2")
        buf.write("\u016cA\3\2\2\2\u016d\u016e\7\t\2\2\u016e\u0174\7?\2\2")
        buf.write("\u016f\u0175\5^\60\2\u0170\u0175\5d\63\2\u0171\u0175\5")
        buf.write("h\65\2\u0172\u0175\7\63\2\2\u0173\u0175\7\62\2\2\u0174")
        buf.write("\u016f\3\2\2\2\u0174\u0170\3\2\2\2\u0174\u0171\3\2\2\2")
        buf.write("\u0174\u0172\3\2\2\2\u0174\u0173\3\2\2\2\u0175\u0176\3")
        buf.write("\2\2\2\u0176\u0177\7\r\2\2\u0177\u0178\5\30\r\2\u0178")
        buf.write("\u0179\7\3\2\2\u0179\u017d\5\30\r\2\u017a\u017b\7\32\2")
        buf.write("\2\u017b\u017e\5\30\r\2\u017c\u017e\3\2\2\2\u017d\u017a")
        buf.write("\3\2\2\2\u017d\u017c\3\2\2\2\u017e\u017f\3\2\2\2\u017f")
        buf.write("\u0180\7@\2\2\u0180\u0181\5\66\34\2\u0181C\3\2\2\2\u0182")
        buf.write("\u0183\7\4\2\2\u0183\u0184\7C\2\2\u0184E\3\2\2\2\u0185")
        buf.write("\u0186\7\5\2\2\u0186\u0187\7C\2\2\u0187G\3\2\2\2\u0188")
        buf.write("\u0189\7\22\2\2\u0189\u018a\5\30\r\2\u018a\u018b\7C\2")
        buf.write("\2\u018bI\3\2\2\2\u018c\u018f\5l\67\2\u018d\u018f\5j\66")
        buf.write("\2\u018e\u018c\3\2\2\2\u018e\u018d\3\2\2\2\u018f\u0190")
        buf.write("\3\2\2\2\u0190\u0191\7C\2\2\u0191K\3\2\2\2\u0192\u0193")
        buf.write("\7\f\2\2\u0193\u0194\7?\2\2\u0194\u0195\5N(\2\u0195\u0196")
        buf.write("\7@\2\2\u0196M\3\2\2\2\u0197\u0198\5P)\2\u0198\u0199\7")
        buf.write("D\2\2\u0199\u019a\5N(\2\u019a\u019d\3\2\2\2\u019b\u019d")
        buf.write("\5P)\2\u019c\u0197\3\2\2\2\u019c\u019b\3\2\2\2\u019dO")
        buf.write("\3\2\2\2\u019e\u019f\t\n\2\2\u019fQ\3\2\2\2\u01a0\u01a1")
        buf.write("\7\f\2\2\u01a1\u01a2\7?\2\2\u01a2\u01a3\5T+\2\u01a3\u01a4")
        buf.write("\7@\2\2\u01a4S\3\2\2\2\u01a5\u01a6\5V,\2\u01a6\u01a7\7")
        buf.write("D\2\2\u01a7\u01a8\5T+\2\u01a8\u01ab\3\2\2\2\u01a9\u01ab")
        buf.write("\5V,\2\u01aa\u01a5\3\2\2\2\u01aa\u01a9\3\2\2\2\u01abU")
        buf.write("\3\2\2\2\u01ac\u01af\5R*\2\u01ad\u01af\5L\'\2\u01ae\u01ac")
        buf.write("\3\2\2\2\u01ae\u01ad\3\2\2\2\u01afW\3\2\2\2\u01b0\u01b1")
        buf.write("\7\f\2\2\u01b1\u01b2\7=\2\2\u01b2\u01b3\5Z.\2\u01b3\u01b4")
        buf.write("\7D\2\2\u01b4\u01b5\5\\/\2\u01b5\u01b6\7>\2\2\u01b6Y\3")
        buf.write("\2\2\2\u01b7\u01bd\7\16\2\2\u01b8\u01bd\7\17\2\2\u01b9")
        buf.write("\u01bd\7\20\2\2\u01ba\u01bd\5X-\2\u01bb\u01bd\7\21\2\2")
        buf.write("\u01bc\u01b7\3\2\2\2\u01bc\u01b8\3\2\2\2\u01bc\u01b9\3")
        buf.write("\2\2\2\u01bc\u01ba\3\2\2\2\u01bc\u01bb\3\2\2\2\u01bd[")
        buf.write("\3\2\2\2\u01be\u01bf\7\65\2\2\u01bf]\3\2\2\2\u01c0\u01c1")
        buf.write("\5b\62\2\u01c1\u01c2\5`\61\2\u01c2_\3\2\2\2\u01c3\u01c4")
        buf.write("\7=\2\2\u01c4\u01c5\5\30\r\2\u01c5\u01c6\7>\2\2\u01c6")
        buf.write("\u01cd\3\2\2\2\u01c7\u01c8\7=\2\2\u01c8\u01c9\5\30\r\2")
        buf.write("\u01c9\u01ca\7>\2\2\u01ca\u01cb\5`\61\2\u01cb\u01cd\3")
        buf.write("\2\2\2\u01cc\u01c3\3\2\2\2\u01cc\u01c7\3\2\2\2\u01cda")
        buf.write("\3\2\2\2\u01ce\u01d2\5f\64\2\u01cf\u01d2\5j\66\2\u01d0")
        buf.write("\u01d2\5d\63\2\u01d1\u01ce\3\2\2\2\u01d1\u01cf\3\2\2\2")
        buf.write("\u01d1\u01d0\3\2\2\2\u01d2c\3\2\2\2\u01d3\u01d4\5f\64")
        buf.write("\2\u01d4\u01d5\7#\2\2\u01d5\u01d6\7\63\2\2\u01d6e\3\2")
        buf.write("\2\2\u01d7\u01df\7\63\2\2\u01d8\u01df\7\62\2\2\u01d9\u01df")
        buf.write("\5R*\2\u01da\u01df\5L\'\2\u01db\u01df\7\33\2\2\u01dc\u01df")
        buf.write("\5l\67\2\u01dd\u01df\5h\65\2\u01de\u01d7\3\2\2\2\u01de")
        buf.write("\u01d8\3\2\2\2\u01de\u01d9\3\2\2\2\u01de\u01da\3\2\2\2")
        buf.write("\u01de\u01db\3\2\2\2\u01de\u01dc\3\2\2\2\u01de\u01dd\3")
        buf.write("\2\2\2\u01dfg\3\2\2\2\u01e0\u01e1\7\63\2\2\u01e1\u01e2")
        buf.write("\7$\2\2\u01e2\u01e3\7\62\2\2\u01e3i\3\2\2\2\u01e4\u01e7")
        buf.write("\5f\64\2\u01e5\u01e7\5d\63\2\u01e6\u01e4\3\2\2\2\u01e6")
        buf.write("\u01e5\3\2\2\2\u01e7\u01e8\3\2\2\2\u01e8\u01e9\7#\2\2")
        buf.write("\u01e9\u01ea\7\63\2\2\u01ea\u01ed\7?\2\2\u01eb\u01ee\5")
        buf.write("\26\f\2\u01ec\u01ee\3\2\2\2\u01ed\u01eb\3\2\2\2\u01ed")
        buf.write("\u01ec\3\2\2\2\u01ee\u01ef\3\2\2\2\u01ef\u01f0\7@\2\2")
        buf.write("\u01f0k\3\2\2\2\u01f1\u01f2\7\63\2\2\u01f2\u01f3\7$\2")
        buf.write("\2\u01f3\u01f4\7\62\2\2\u01f4\u01f7\7?\2\2\u01f5\u01f8")
        buf.write("\5\26\f\2\u01f6\u01f8\3\2\2\2\u01f7\u01f5\3\2\2\2\u01f7")
        buf.write("\u01f6\3\2\2\2\u01f8\u01f9\3\2\2\2\u01f9\u01fa\7@\2\2")
        buf.write("\u01fam\3\2\2\2\u01fb\u01fc\7\31\2\2\u01fc\u01fd\7\63")
        buf.write("\2\2\u01fd\u0200\7?\2\2\u01fe\u0201\5\26\f\2\u01ff\u0201")
        buf.write("\3\2\2\2\u0200\u01fe\3\2\2\2\u0200\u01ff\3\2\2\2\u0201")
        buf.write("\u0202\3\2\2\2\u0202\u0203\7@\2\2\u0203o\3\2\2\2-w}\u0082")
        buf.write("\u008d\u0091\u009a\u00a4\u00ac\u00b3\u00ba\u00c1\u00cb")
        buf.write("\u00d6\u00e1\u00e7\u00ec\u00f0\u00fa\u0105\u010a\u011f")
        buf.write("\u0125\u012f\u0138\u0140\u014b\u0152\u015f\u016b\u0174")
        buf.write("\u017d\u018e\u019c\u01aa\u01ae\u01bc\u01cc\u01d1\u01de")
        buf.write("\u01e6\u01ed\u01f7\u0200")
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
                     "<INVALID>", "<INVALID>", "'\b'", "'\f'", "'\r'", "'\n'", 
                     "'\t'", "'''", "'\\'", "'['", "']'", "'('", "')'", 
                     "'{'", "'}'", "';'", "','", "':'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "BREAK", "CONTINUE", "IF", 
                      "ELSEIF", "ELSE", "FOREACH", "TRUE", "FALSE", "ARRAY", 
                      "IN", "INTTYPE", "FLOATTYPE", "BOOLEAN", "STRING", 
                      "RETURN", "NULL", "CLASS", "VAL", "VAR", "CONSTRUCTOR", 
                      "DESTRUCTOR", "NEW", "BY", "SELF", "NOTEQUAL", "NOTLARGER", 
                      "NOTSMALLER", "LARGER", "SMALLER", "COMPARSTR", "CONCAT", 
                      "INSTANT", "STATICATTR", "INDEXOPR", "ADD", "MINUS", 
                      "MULTI", "DIV", "PERCENT", "NOT", "AND", "OR", "COMPAR", 
                      "EQUAL", "STR", "BLOCKCOMMENT", "STATIC", "ID", "FLOAT", 
                      "INT", "BACKSPACE", "FORMFEED", "CARRETURN", "NEWLINE", 
                      "HORTAB", "SINGQ", "BACKSLASH", "LS", "RS", "LB", 
                      "RB", "LP", "RP", "SEMI", "COMMA", "COLON", "WS", 
                      "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
    RULE_method = 23
    RULE_paramlist = 24
    RULE_param = 25
    RULE_blockstate = 26
    RULE_statements = 27
    RULE_sta = 28
    RULE_lhs = 29
    RULE_ifsta = 30
    RULE_eliflist = 31
    RULE_forsta = 32
    RULE_breaksta = 33
    RULE_continuesta = 34
    RULE_returnsta = 35
    RULE_methodsta = 36
    RULE_indexedarr = 37
    RULE_literals = 38
    RULE_lit = 39
    RULE_multiarr = 40
    RULE_arrlist = 41
    RULE_arr = 42
    RULE_arrdecl = 43
    RULE_element = 44
    RULE_size = 45
    RULE_eleexp = 46
    RULE_indexop = 47
    RULE_exp = 48
    RULE_instance = 49
    RULE_ins = 50
    RULE_staatr = 51
    RULE_imethodi = 52
    RULE_smethodi = 53
    RULE_objcreate = 54

    ruleNames =  [ "program", "classdecls", "classdecl", "superclass", "memberlist", 
                   "member", "attr", "attrtype", "idlist", "typ", "exprlist", 
                   "expr", "exp1", "exp2", "exp3", "exp4", "exp5", "exp6", 
                   "exp7", "exp8", "exp9", "exp10", "exp11", "method", "paramlist", 
                   "param", "blockstate", "statements", "sta", "lhs", "ifsta", 
                   "eliflist", "forsta", "breaksta", "continuesta", "returnsta", 
                   "methodsta", "indexedarr", "literals", "lit", "multiarr", 
                   "arrlist", "arr", "arrdecl", "element", "size", "eleexp", 
                   "indexop", "exp", "instance", "ins", "staatr", "imethodi", 
                   "smethodi", "objcreate" ]

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
    STR=46
    BLOCKCOMMENT=47
    STATIC=48
    ID=49
    FLOAT=50
    INT=51
    BACKSPACE=52
    FORMFEED=53
    CARRETURN=54
    NEWLINE=55
    HORTAB=56
    SINGQ=57
    BACKSLASH=58
    LS=59
    RS=60
    LB=61
    RB=62
    LP=63
    RP=64
    SEMI=65
    COMMA=66
    COLON=67
    WS=68
    ERROR_CHAR=69
    UNCLOSE_STRING=70
    ILLEGAL_ESCAPE=71

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

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
            self.state = 110
            self.classdecls()
            self.state = 111
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassdeclsContext(ParserRuleContext):
        __slots__ = 'parser'

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
            self.state = 117
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.classdecl()
                self.state = 114
                self.classdecls()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 116
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
        __slots__ = 'parser'

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
            self.state = 119
            self.match(D96Parser.CLASS)
            self.state = 120
            self.match(D96Parser.ID)
            self.state = 123
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COLON]:
                self.state = 121
                self.superclass()
                pass
            elif token in [D96Parser.LP]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 125
            self.match(D96Parser.LP)
            self.state = 128
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR, D96Parser.CONSTRUCTOR, D96Parser.DESTRUCTOR, D96Parser.STATIC, D96Parser.ID]:
                self.state = 126
                self.memberlist()
                pass
            elif token in [D96Parser.RP]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 130
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SuperclassContext(ParserRuleContext):
        __slots__ = 'parser'

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
            self.state = 132
            self.match(D96Parser.COLON)
            self.state = 133
            self.match(D96Parser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberlistContext(ParserRuleContext):
        __slots__ = 'parser'

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
            self.state = 139
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.member()
                self.state = 136
                self.memberlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
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
        __slots__ = 'parser'

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
            self.state = 143
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 141
                self.attr()
                pass
            elif token in [D96Parser.CONSTRUCTOR, D96Parser.DESTRUCTOR, D96Parser.STATIC, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 142
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
        __slots__ = 'parser'

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
            self.state = 145
            self.attrtype()
            self.state = 146
            self.idlist()
            self.state = 147
            self.match(D96Parser.COLON)
            self.state = 148
            self.typ()
            self.state = 152
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.EQUAL]:
                self.state = 149
                self.match(D96Parser.EQUAL)
                self.state = 150
                self.exprlist()
                pass
            elif token in [D96Parser.SEMI]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 154
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttrtypeContext(ParserRuleContext):
        __slots__ = 'parser'

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
            self.state = 156
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
        __slots__ = 'parser'

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
            self.state = 162
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                _la = self._input.LA(1)
                if not(_la==D96Parser.STATIC or _la==D96Parser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 159
                self.match(D96Parser.COMMA)
                self.state = 160
                self.idlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 161
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
        __slots__ = 'parser'

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


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_typ




    def typ(self):

        localctx = D96Parser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_typ)
        try:
            self.state = 170
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BOOLEAN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 164
                self.match(D96Parser.BOOLEAN)
                pass
            elif token in [D96Parser.INTTYPE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 165
                self.match(D96Parser.INTTYPE)
                pass
            elif token in [D96Parser.FLOATTYPE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 166
                self.match(D96Parser.FLOATTYPE)
                pass
            elif token in [D96Parser.STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 167
                self.match(D96Parser.STRING)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 168
                self.arrdecl()
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 169
                self.match(D96Parser.ID)
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
        __slots__ = 'parser'

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
            self.state = 177
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 172
                self.expr()
                self.state = 173
                self.match(D96Parser.COMMA)
                self.state = 174
                self.exprlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 176
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
        __slots__ = 'parser'

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
            self.state = 184
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 179
                self.exp1()
                self.state = 180
                _la = self._input.LA(1)
                if not(_la==D96Parser.COMPARSTR or _la==D96Parser.CONCAT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 181
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 183
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
        __slots__ = 'parser'

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
            self.state = 191
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 186
                self.exp2(0)
                self.state = 187
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.NOTEQUAL) | (1 << D96Parser.NOTLARGER) | (1 << D96Parser.NOTSMALLER) | (1 << D96Parser.LARGER) | (1 << D96Parser.SMALLER) | (1 << D96Parser.COMPAR))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 188
                self.exp2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 190
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
        __slots__ = 'parser'

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
            self.state = 194
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 201
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 196
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 197
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.AND or _la==D96Parser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 198
                    self.exp3(0) 
                self.state = 203
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
        __slots__ = 'parser'

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
            self.state = 205
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 212
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 207
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 208
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ADD or _la==D96Parser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 209
                    self.exp4(0) 
                self.state = 214
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
        __slots__ = 'parser'

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
            self.state = 216
            self.exp5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 223
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                    self.state = 218
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 219
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.MULTI) | (1 << D96Parser.DIV) | (1 << D96Parser.PERCENT))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 220
                    self.exp5() 
                self.state = 225
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
        __slots__ = 'parser'

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
            self.state = 229
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 226
                self.match(D96Parser.NOT)
                self.state = 227
                self.exp5()
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.MINUS, D96Parser.STR, D96Parser.STATIC, D96Parser.ID, D96Parser.FLOAT, D96Parser.INT, D96Parser.LB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 228
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
        __slots__ = 'parser'

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
            self.state = 234
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 231
                self.match(D96Parser.MINUS)
                self.state = 232
                self.exp6()
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.STR, D96Parser.STATIC, D96Parser.ID, D96Parser.FLOAT, D96Parser.INT, D96Parser.LB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 233
                self.exp7()
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def eleexp(self):
            return self.getTypedRuleContext(D96Parser.EleexpContext,0)


        def exp8(self):
            return self.getTypedRuleContext(D96Parser.Exp8Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp7




    def exp7(self):

        localctx = D96Parser.Exp7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_exp7)
        try:
            self.state = 238
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 236
                self.eleexp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 237
                self.exp8(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp8Context(ParserRuleContext):
        __slots__ = 'parser'

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
            self.state = 241
            self.exp9(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 248
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp8)
                    self.state = 243
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 244
                    self.match(D96Parser.INSTANT)
                    self.state = 245
                    self.exp9(0) 
                self.state = 250
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
        __slots__ = 'parser'

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
            self.state = 252
            self.exp10()
            self._ctx.stop = self._input.LT(-1)
            self.state = 259
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp9Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp9)
                    self.state = 254
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 255
                    self.match(D96Parser.STATICATTR)
                    self.state = 256
                    self.exp9(3) 
                self.state = 261
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def objcreate(self):
            return self.getTypedRuleContext(D96Parser.ObjcreateContext,0)


        def exp11(self):
            return self.getTypedRuleContext(D96Parser.Exp11Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp10




    def exp10(self):

        localctx = D96Parser.Exp10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_exp10)
        try:
            self.state = 264
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 262
                self.objcreate()
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.SELF, D96Parser.STR, D96Parser.STATIC, D96Parser.ID, D96Parser.FLOAT, D96Parser.INT, D96Parser.LB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 263
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

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

        def STATIC(self):
            return self.getToken(D96Parser.STATIC, 0)

        def multiarr(self):
            return self.getTypedRuleContext(D96Parser.MultiarrContext,0)


        def indexedarr(self):
            return self.getTypedRuleContext(D96Parser.IndexedarrContext,0)


        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def imethodi(self):
            return self.getTypedRuleContext(D96Parser.ImethodiContext,0)


        def smethodi(self):
            return self.getTypedRuleContext(D96Parser.SmethodiContext,0)


        def instance(self):
            return self.getTypedRuleContext(D96Parser.InstanceContext,0)


        def staatr(self):
            return self.getTypedRuleContext(D96Parser.StaatrContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp11




    def exp11(self):

        localctx = D96Parser.Exp11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_exp11)
        try:
            self.state = 285
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 266
                self.match(D96Parser.LB)
                self.state = 267
                self.expr()
                self.state = 268
                self.match(D96Parser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 270
                self.match(D96Parser.NULL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 271
                self.match(D96Parser.INT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 272
                self.match(D96Parser.FLOAT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 273
                self.match(D96Parser.TRUE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 274
                self.match(D96Parser.FALSE)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 275
                self.match(D96Parser.STR)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 276
                self.match(D96Parser.ID)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 277
                self.match(D96Parser.STATIC)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 278
                self.multiarr()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 279
                self.indexedarr()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 280
                self.match(D96Parser.SELF)
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 281
                self.imethodi()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 282
                self.smethodi()
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 283
                self.instance()
                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 284
                self.staatr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def blockstate(self):
            return self.getTypedRuleContext(D96Parser.BlockstateContext,0)


        def CONSTRUCTOR(self):
            return self.getToken(D96Parser.CONSTRUCTOR, 0)

        def DESTRUCTOR(self):
            return self.getToken(D96Parser.DESTRUCTOR, 0)

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
        self.enterRule(localctx, 46, self.RULE_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.CONSTRUCTOR) | (1 << D96Parser.DESTRUCTOR) | (1 << D96Parser.STATIC) | (1 << D96Parser.ID))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 288
            self.match(D96Parser.LB)
            self.state = 291
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.STATIC, D96Parser.ID]:
                self.state = 289
                self.paramlist()
                pass
            elif token in [D96Parser.RB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 293
            self.match(D96Parser.RB)
            self.state = 294
            self.blockstate()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamlistContext(ParserRuleContext):
        __slots__ = 'parser'

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
        self.enterRule(localctx, 48, self.RULE_paramlist)
        try:
            self.state = 301
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 296
                self.param()
                self.state = 297
                self.match(D96Parser.SEMI)
                self.state = 298
                self.paramlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 300
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idlist(self):
            return self.getTypedRuleContext(D96Parser.IdlistContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def typ(self):
            return self.getTypedRuleContext(D96Parser.TypContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_param




    def param(self):

        localctx = D96Parser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.idlist()
            self.state = 304
            self.match(D96Parser.COLON)
            self.state = 305
            self.typ()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockstateContext(ParserRuleContext):
        __slots__ = 'parser'

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
        self.enterRule(localctx, 52, self.RULE_blockstate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self.match(D96Parser.LP)
            self.state = 310
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.IF, D96Parser.FOREACH, D96Parser.ARRAY, D96Parser.RETURN, D96Parser.VAL, D96Parser.VAR, D96Parser.SELF, D96Parser.STATIC, D96Parser.ID, D96Parser.LP]:
                self.state = 308
                self.statements()
                pass
            elif token in [D96Parser.RP]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 312
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementsContext(ParserRuleContext):
        __slots__ = 'parser'

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
        self.enterRule(localctx, 54, self.RULE_statements)
        try:
            self.state = 318
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 314
                self.sta()
                self.state = 315
                self.statements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 317
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
        __slots__ = 'parser'

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


        def blockstate(self):
            return self.getTypedRuleContext(D96Parser.BlockstateContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_sta




    def sta(self):

        localctx = D96Parser.StaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_sta)
        try:
            self.state = 329
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 320
                self.attr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 321
                self.lhs()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 322
                self.ifsta()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 323
                self.forsta()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 324
                self.breaksta()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 325
                self.continuesta()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 326
                self.returnsta()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 327
                self.methodsta()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 328
                self.blockstate()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL(self):
            return self.getToken(D96Parser.EQUAL, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def eleexp(self):
            return self.getTypedRuleContext(D96Parser.EleexpContext,0)


        def instance(self):
            return self.getTypedRuleContext(D96Parser.InstanceContext,0)


        def staatr(self):
            return self.getTypedRuleContext(D96Parser.StaatrContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def STATIC(self):
            return self.getToken(D96Parser.STATIC, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_lhs




    def lhs(self):

        localctx = D96Parser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_lhs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 331
                self.eleexp()
                pass

            elif la_ == 2:
                self.state = 332
                self.instance()
                pass

            elif la_ == 3:
                self.state = 333
                self.staatr()
                pass

            elif la_ == 4:
                self.state = 334
                self.match(D96Parser.ID)
                pass

            elif la_ == 5:
                self.state = 335
                self.match(D96Parser.STATIC)
                pass


            self.state = 338
            self.match(D96Parser.EQUAL)
            self.state = 339
            self.expr()
            self.state = 340
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstaContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def blockstate(self):
            return self.getTypedRuleContext(D96Parser.BlockstateContext,0)


        def eliflist(self):
            return self.getTypedRuleContext(D96Parser.EliflistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_ifsta




    def ifsta(self):

        localctx = D96Parser.IfstaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_ifsta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self.match(D96Parser.IF)
            self.state = 343
            self.match(D96Parser.LB)
            self.state = 344
            self.expr()
            self.state = 345
            self.match(D96Parser.RB)
            self.state = 346
            self.blockstate()
            self.state = 349
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 347
                self.eliflist()
                pass

            elif la_ == 2:
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EliflistContext(ParserRuleContext):
        __slots__ = 'parser'

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


        def ELSE(self):
            return self.getToken(D96Parser.ELSE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_eliflist




    def eliflist(self):

        localctx = D96Parser.EliflistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_eliflist)
        try:
            self.state = 361
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ELSEIF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 351
                self.match(D96Parser.ELSEIF)
                self.state = 352
                self.match(D96Parser.LB)
                self.state = 353
                self.expr()
                self.state = 354
                self.match(D96Parser.RB)
                self.state = 355
                self.blockstate()
                self.state = 356
                self.eliflist()
                pass
            elif token in [D96Parser.ELSE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 358
                self.match(D96Parser.ELSE)
                self.state = 359
                self.blockstate()
                pass
            elif token in [D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.IF, D96Parser.FOREACH, D96Parser.ARRAY, D96Parser.RETURN, D96Parser.VAL, D96Parser.VAR, D96Parser.SELF, D96Parser.STATIC, D96Parser.ID, D96Parser.LP, D96Parser.RP]:
                self.enterOuterAlt(localctx, 3)

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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOREACH(self):
            return self.getToken(D96Parser.FOREACH, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def IN(self):
            return self.getToken(D96Parser.IN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExprContext,i)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def blockstate(self):
            return self.getTypedRuleContext(D96Parser.BlockstateContext,0)


        def eleexp(self):
            return self.getTypedRuleContext(D96Parser.EleexpContext,0)


        def instance(self):
            return self.getTypedRuleContext(D96Parser.InstanceContext,0)


        def staatr(self):
            return self.getTypedRuleContext(D96Parser.StaatrContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def STATIC(self):
            return self.getToken(D96Parser.STATIC, 0)

        def BY(self):
            return self.getToken(D96Parser.BY, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_forsta




    def forsta(self):

        localctx = D96Parser.ForstaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_forsta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
            self.match(D96Parser.FOREACH)
            self.state = 364
            self.match(D96Parser.LB)
            self.state = 370
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 365
                self.eleexp()
                pass

            elif la_ == 2:
                self.state = 366
                self.instance()
                pass

            elif la_ == 3:
                self.state = 367
                self.staatr()
                pass

            elif la_ == 4:
                self.state = 368
                self.match(D96Parser.ID)
                pass

            elif la_ == 5:
                self.state = 369
                self.match(D96Parser.STATIC)
                pass


            self.state = 372
            self.match(D96Parser.IN)
            self.state = 373
            self.expr()
            self.state = 374
            self.match(D96Parser.T__0)
            self.state = 375
            self.expr()
            self.state = 379
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BY]:
                self.state = 376
                self.match(D96Parser.BY)
                self.state = 377
                self.expr()
                pass
            elif token in [D96Parser.RB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 381
            self.match(D96Parser.RB)
            self.state = 382
            self.blockstate()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakstaContext(ParserRuleContext):
        __slots__ = 'parser'

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
        self.enterRule(localctx, 66, self.RULE_breaksta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self.match(D96Parser.BREAK)
            self.state = 385
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinuestaContext(ParserRuleContext):
        __slots__ = 'parser'

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
        self.enterRule(localctx, 68, self.RULE_continuesta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.match(D96Parser.CONTINUE)
            self.state = 388
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnstaContext(ParserRuleContext):
        __slots__ = 'parser'

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
        self.enterRule(localctx, 70, self.RULE_returnsta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 390
            self.match(D96Parser.RETURN)
            self.state = 391
            self.expr()
            self.state = 392
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodstaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def smethodi(self):
            return self.getTypedRuleContext(D96Parser.SmethodiContext,0)


        def imethodi(self):
            return self.getTypedRuleContext(D96Parser.ImethodiContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_methodsta




    def methodsta(self):

        localctx = D96Parser.MethodstaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_methodsta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 396
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 394
                self.smethodi()
                pass

            elif la_ == 2:
                self.state = 395
                self.imethodi()
                pass


            self.state = 398
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexedarrContext(ParserRuleContext):
        __slots__ = 'parser'

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
        self.enterRule(localctx, 74, self.RULE_indexedarr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 400
            self.match(D96Parser.ARRAY)
            self.state = 401
            self.match(D96Parser.LB)
            self.state = 402
            self.literals()
            self.state = 403
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralsContext(ParserRuleContext):
        __slots__ = 'parser'

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
        self.enterRule(localctx, 76, self.RULE_literals)
        try:
            self.state = 410
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 405
                self.lit()
                self.state = 406
                self.match(D96Parser.COMMA)
                self.state = 407
                self.literals()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 409
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
        __slots__ = 'parser'

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
        self.enterRule(localctx, 78, self.RULE_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 412
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.STR) | (1 << D96Parser.FLOAT) | (1 << D96Parser.INT))) != 0)):
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
        __slots__ = 'parser'

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
        self.enterRule(localctx, 80, self.RULE_multiarr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 414
            self.match(D96Parser.ARRAY)
            self.state = 415
            self.match(D96Parser.LB)
            self.state = 416
            self.arrlist()
            self.state = 417
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrlistContext(ParserRuleContext):
        __slots__ = 'parser'

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
        self.enterRule(localctx, 82, self.RULE_arrlist)
        try:
            self.state = 424
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 419
                self.arr()
                self.state = 420
                self.match(D96Parser.COMMA)
                self.state = 421
                self.arrlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 423
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
        __slots__ = 'parser'

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
        self.enterRule(localctx, 84, self.RULE_arr)
        try:
            self.state = 428
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 426
                self.multiarr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 427
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
        __slots__ = 'parser'

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
        self.enterRule(localctx, 86, self.RULE_arrdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 430
            self.match(D96Parser.ARRAY)
            self.state = 431
            self.match(D96Parser.LS)
            self.state = 432
            self.element()
            self.state = 433
            self.match(D96Parser.COMMA)
            self.state = 434
            self.size()
            self.state = 435
            self.match(D96Parser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementContext(ParserRuleContext):
        __slots__ = 'parser'

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
        self.enterRule(localctx, 88, self.RULE_element)
        try:
            self.state = 442
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTTYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 437
                self.match(D96Parser.INTTYPE)
                pass
            elif token in [D96Parser.FLOATTYPE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 438
                self.match(D96Parser.FLOATTYPE)
                pass
            elif token in [D96Parser.BOOLEAN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 439
                self.match(D96Parser.BOOLEAN)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 4)
                self.state = 440
                self.arrdecl()
                pass
            elif token in [D96Parser.STRING]:
                self.enterOuterAlt(localctx, 5)
                self.state = 441
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(D96Parser.INT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_size




    def size(self):

        localctx = D96Parser.SizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_size)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 444
            self.match(D96Parser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EleexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def indexop(self):
            return self.getTypedRuleContext(D96Parser.IndexopContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_eleexp




    def eleexp(self):

        localctx = D96Parser.EleexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_eleexp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 446
            self.exp()
            self.state = 447
            self.indexop()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LS(self):
            return self.getToken(D96Parser.LS, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RS(self):
            return self.getToken(D96Parser.RS, 0)

        def indexop(self):
            return self.getTypedRuleContext(D96Parser.IndexopContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_indexop




    def indexop(self):

        localctx = D96Parser.IndexopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_indexop)
        try:
            self.state = 458
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 449
                self.match(D96Parser.LS)
                self.state = 450
                self.expr()
                self.state = 451
                self.match(D96Parser.RS)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 453
                self.match(D96Parser.LS)
                self.state = 454
                self.expr()
                self.state = 455
                self.match(D96Parser.RS)
                self.state = 456
                self.indexop()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ins(self):
            return self.getTypedRuleContext(D96Parser.InsContext,0)


        def imethodi(self):
            return self.getTypedRuleContext(D96Parser.ImethodiContext,0)


        def instance(self):
            return self.getTypedRuleContext(D96Parser.InstanceContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp




    def exp(self):

        localctx = D96Parser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_exp)
        try:
            self.state = 463
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 460
                self.ins()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 461
                self.imethodi()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 462
                self.instance()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstanceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ins(self):
            return self.getTypedRuleContext(D96Parser.InsContext,0)


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
            self.state = 465
            self.ins()
            self.state = 466
            self.match(D96Parser.INSTANT)
            self.state = 467
            self.match(D96Parser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def STATIC(self):
            return self.getToken(D96Parser.STATIC, 0)

        def multiarr(self):
            return self.getTypedRuleContext(D96Parser.MultiarrContext,0)


        def indexedarr(self):
            return self.getTypedRuleContext(D96Parser.IndexedarrContext,0)


        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def smethodi(self):
            return self.getTypedRuleContext(D96Parser.SmethodiContext,0)


        def staatr(self):
            return self.getTypedRuleContext(D96Parser.StaatrContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_ins




    def ins(self):

        localctx = D96Parser.InsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_ins)
        try:
            self.state = 476
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 469
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 470
                self.match(D96Parser.STATIC)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 471
                self.multiarr()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 472
                self.indexedarr()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 473
                self.match(D96Parser.SELF)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 474
                self.smethodi()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 475
                self.staatr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StaatrContext(ParserRuleContext):
        __slots__ = 'parser'

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
        self.enterRule(localctx, 102, self.RULE_staatr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 478
            self.match(D96Parser.ID)
            self.state = 479
            self.match(D96Parser.STATICATTR)
            self.state = 480
            self.match(D96Parser.STATIC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImethodiContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INSTANT(self):
            return self.getToken(D96Parser.INSTANT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def ins(self):
            return self.getTypedRuleContext(D96Parser.InsContext,0)


        def instance(self):
            return self.getTypedRuleContext(D96Parser.InstanceContext,0)


        def exprlist(self):
            return self.getTypedRuleContext(D96Parser.ExprlistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_imethodi




    def imethodi(self):

        localctx = D96Parser.ImethodiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_imethodi)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 484
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.state = 482
                self.ins()
                pass

            elif la_ == 2:
                self.state = 483
                self.instance()
                pass


            self.state = 486
            self.match(D96Parser.INSTANT)
            self.state = 487
            self.match(D96Parser.ID)
            self.state = 488
            self.match(D96Parser.LB)
            self.state = 491
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.MINUS, D96Parser.NOT, D96Parser.STR, D96Parser.STATIC, D96Parser.ID, D96Parser.FLOAT, D96Parser.INT, D96Parser.LB]:
                self.state = 489
                self.exprlist()
                pass
            elif token in [D96Parser.RB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 493
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SmethodiContext(ParserRuleContext):
        __slots__ = 'parser'

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
        self.enterRule(localctx, 106, self.RULE_smethodi)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 495
            self.match(D96Parser.ID)
            self.state = 496
            self.match(D96Parser.STATICATTR)
            self.state = 497
            self.match(D96Parser.STATIC)
            self.state = 498
            self.match(D96Parser.LB)
            self.state = 501
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.MINUS, D96Parser.NOT, D96Parser.STR, D96Parser.STATIC, D96Parser.ID, D96Parser.FLOAT, D96Parser.INT, D96Parser.LB]:
                self.state = 499
                self.exprlist()
                pass
            elif token in [D96Parser.RB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 503
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjcreateContext(ParserRuleContext):
        __slots__ = 'parser'

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
            return D96Parser.RULE_objcreate




    def objcreate(self):

        localctx = D96Parser.ObjcreateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_objcreate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 505
            self.match(D96Parser.NEW)
            self.state = 506
            self.match(D96Parser.ID)
            self.state = 507
            self.match(D96Parser.LB)
            self.state = 510
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.MINUS, D96Parser.NOT, D96Parser.STR, D96Parser.STATIC, D96Parser.ID, D96Parser.FLOAT, D96Parser.INT, D96Parser.LB]:
                self.state = 508
                self.exprlist()
                pass
            elif token in [D96Parser.RB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 512
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
         

    def exp8_sempred(self, localctx:Exp8Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def exp9_sempred(self, localctx:Exp9Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




