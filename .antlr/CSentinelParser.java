// Generated from c:/dev/CompilerProject/C-Sentinel/CSentinel.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class CSentinelParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		RULE_KEYWORD=1, BLOCK_KEYWORD=2, ON_KEYWORD=3, CALL_KEYWORD=4, IF_KEYWORD=5, 
		OVERFLOWS_KEYWORD=6, ERROR_KEYWORD=7, LBRACE=8, RBRACE=9, LPAREN=10, RPAREN=11, 
		COMMA=12, PLUS=13, MINUS=14, STAR=15, DIV=16, REQUIRE_LITERAL_FORMAT_KEYWORD=17, 
		REQUIRE_NULL_AFTER_KEYWORD=18, REQUIRE_NO_DOUBLE_FREE_KEYWORD=19, SOURCE_KEYWORD=20, 
		SINK_KEYWORD=21, SANITIZER_KEYWORD=22, NUMBER=23, ID=24, STRING=25, WS=26;
	public static final int
		RULE_senFile = 0, RULE_rule = 1, RULE_blockRule = 2, RULE_onRule = 3, 
		RULE_requireLiteralStmt = 4, RULE_requireNullStmt = 5, RULE_requireNoDoubleFreeStmt = 6, 
		RULE_ifStmt = 7, RULE_sourceRule = 8, RULE_sinkRule = 9, RULE_sanitizerRule = 10, 
		RULE_expr = 11, RULE_term = 12, RULE_factor = 13, RULE_action = 14;
	private static String[] makeRuleNames() {
		return new String[] {
			"senFile", "rule", "blockRule", "onRule", "requireLiteralStmt", "requireNullStmt", 
			"requireNoDoubleFreeStmt", "ifStmt", "sourceRule", "sinkRule", "sanitizerRule", 
			"expr", "term", "factor", "action"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'rule'", "'block'", "'on'", "'call'", "'if'", "'overflows'", "'error'", 
			"'{'", "'}'", "'('", "')'", "','", "'+'", "'-'", "'*'", "'/'", "'require_literal_format'", 
			"'require_null_after'", "'require_no_double_free'", "'source'", "'sink'", 
			"'sanitizer'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "RULE_KEYWORD", "BLOCK_KEYWORD", "ON_KEYWORD", "CALL_KEYWORD", 
			"IF_KEYWORD", "OVERFLOWS_KEYWORD", "ERROR_KEYWORD", "LBRACE", "RBRACE", 
			"LPAREN", "RPAREN", "COMMA", "PLUS", "MINUS", "STAR", "DIV", "REQUIRE_LITERAL_FORMAT_KEYWORD", 
			"REQUIRE_NULL_AFTER_KEYWORD", "REQUIRE_NO_DOUBLE_FREE_KEYWORD", "SOURCE_KEYWORD", 
			"SINK_KEYWORD", "SANITIZER_KEYWORD", "NUMBER", "ID", "STRING", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "CSentinel.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public CSentinelParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SenFileContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(CSentinelParser.EOF, 0); }
		public List<RuleContext> rule_() {
			return getRuleContexts(RuleContext.class);
		}
		public RuleContext rule_(int i) {
			return getRuleContext(RuleContext.class,i);
		}
		public SenFileContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_senFile; }
	}

	public final SenFileContext senFile() throws RecognitionException {
		SenFileContext _localctx = new SenFileContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_senFile);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(33);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==RULE_KEYWORD) {
				{
				{
				setState(30);
				rule_();
				}
				}
				setState(35);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(36);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RuleContext extends ParserRuleContext {
		public TerminalNode RULE_KEYWORD() { return getToken(CSentinelParser.RULE_KEYWORD, 0); }
		public TerminalNode ID() { return getToken(CSentinelParser.ID, 0); }
		public TerminalNode LBRACE() { return getToken(CSentinelParser.LBRACE, 0); }
		public TerminalNode RBRACE() { return getToken(CSentinelParser.RBRACE, 0); }
		public List<BlockRuleContext> blockRule() {
			return getRuleContexts(BlockRuleContext.class);
		}
		public BlockRuleContext blockRule(int i) {
			return getRuleContext(BlockRuleContext.class,i);
		}
		public List<OnRuleContext> onRule() {
			return getRuleContexts(OnRuleContext.class);
		}
		public OnRuleContext onRule(int i) {
			return getRuleContext(OnRuleContext.class,i);
		}
		public List<SourceRuleContext> sourceRule() {
			return getRuleContexts(SourceRuleContext.class);
		}
		public SourceRuleContext sourceRule(int i) {
			return getRuleContext(SourceRuleContext.class,i);
		}
		public List<SinkRuleContext> sinkRule() {
			return getRuleContexts(SinkRuleContext.class);
		}
		public SinkRuleContext sinkRule(int i) {
			return getRuleContext(SinkRuleContext.class,i);
		}
		public List<SanitizerRuleContext> sanitizerRule() {
			return getRuleContexts(SanitizerRuleContext.class);
		}
		public SanitizerRuleContext sanitizerRule(int i) {
			return getRuleContext(SanitizerRuleContext.class,i);
		}
		public RuleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_rule; }
	}

	public final RuleContext rule_() throws RecognitionException {
		RuleContext _localctx = new RuleContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_rule);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(38);
			match(RULE_KEYWORD);
			setState(39);
			match(ID);
			setState(40);
			match(LBRACE);
			setState(48);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 7340044L) != 0)) {
				{
				setState(46);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case BLOCK_KEYWORD:
					{
					setState(41);
					blockRule();
					}
					break;
				case ON_KEYWORD:
					{
					setState(42);
					onRule();
					}
					break;
				case SOURCE_KEYWORD:
					{
					setState(43);
					sourceRule();
					}
					break;
				case SINK_KEYWORD:
					{
					setState(44);
					sinkRule();
					}
					break;
				case SANITIZER_KEYWORD:
					{
					setState(45);
					sanitizerRule();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(50);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(51);
			match(RBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BlockRuleContext extends ParserRuleContext {
		public TerminalNode BLOCK_KEYWORD() { return getToken(CSentinelParser.BLOCK_KEYWORD, 0); }
		public TerminalNode ID() { return getToken(CSentinelParser.ID, 0); }
		public TerminalNode LBRACE() { return getToken(CSentinelParser.LBRACE, 0); }
		public ActionContext action() {
			return getRuleContext(ActionContext.class,0);
		}
		public TerminalNode RBRACE() { return getToken(CSentinelParser.RBRACE, 0); }
		public BlockRuleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_blockRule; }
	}

	public final BlockRuleContext blockRule() throws RecognitionException {
		BlockRuleContext _localctx = new BlockRuleContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_blockRule);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(53);
			match(BLOCK_KEYWORD);
			setState(54);
			match(ID);
			setState(55);
			match(LBRACE);
			setState(56);
			action();
			setState(57);
			match(RBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OnRuleContext extends ParserRuleContext {
		public TerminalNode ON_KEYWORD() { return getToken(CSentinelParser.ON_KEYWORD, 0); }
		public TerminalNode CALL_KEYWORD() { return getToken(CSentinelParser.CALL_KEYWORD, 0); }
		public List<TerminalNode> ID() { return getTokens(CSentinelParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(CSentinelParser.ID, i);
		}
		public TerminalNode LPAREN() { return getToken(CSentinelParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(CSentinelParser.RPAREN, 0); }
		public TerminalNode LBRACE() { return getToken(CSentinelParser.LBRACE, 0); }
		public TerminalNode RBRACE() { return getToken(CSentinelParser.RBRACE, 0); }
		public List<IfStmtContext> ifStmt() {
			return getRuleContexts(IfStmtContext.class);
		}
		public IfStmtContext ifStmt(int i) {
			return getRuleContext(IfStmtContext.class,i);
		}
		public List<RequireLiteralStmtContext> requireLiteralStmt() {
			return getRuleContexts(RequireLiteralStmtContext.class);
		}
		public RequireLiteralStmtContext requireLiteralStmt(int i) {
			return getRuleContext(RequireLiteralStmtContext.class,i);
		}
		public List<RequireNullStmtContext> requireNullStmt() {
			return getRuleContexts(RequireNullStmtContext.class);
		}
		public RequireNullStmtContext requireNullStmt(int i) {
			return getRuleContext(RequireNullStmtContext.class,i);
		}
		public List<RequireNoDoubleFreeStmtContext> requireNoDoubleFreeStmt() {
			return getRuleContexts(RequireNoDoubleFreeStmtContext.class);
		}
		public RequireNoDoubleFreeStmtContext requireNoDoubleFreeStmt(int i) {
			return getRuleContext(RequireNoDoubleFreeStmtContext.class,i);
		}
		public List<ActionContext> action() {
			return getRuleContexts(ActionContext.class);
		}
		public ActionContext action(int i) {
			return getRuleContext(ActionContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(CSentinelParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(CSentinelParser.COMMA, i);
		}
		public OnRuleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_onRule; }
	}

	public final OnRuleContext onRule() throws RecognitionException {
		OnRuleContext _localctx = new OnRuleContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_onRule);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(59);
			match(ON_KEYWORD);
			setState(60);
			match(CALL_KEYWORD);
			setState(61);
			match(ID);
			setState(62);
			match(LPAREN);
			setState(71);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(63);
				match(ID);
				setState(68);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(64);
					match(COMMA);
					setState(65);
					match(ID);
					}
					}
					setState(70);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(73);
			match(RPAREN);
			setState(74);
			match(LBRACE);
			setState(82);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 917664L) != 0)) {
				{
				setState(80);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case IF_KEYWORD:
					{
					setState(75);
					ifStmt();
					}
					break;
				case REQUIRE_LITERAL_FORMAT_KEYWORD:
					{
					setState(76);
					requireLiteralStmt();
					}
					break;
				case REQUIRE_NULL_AFTER_KEYWORD:
					{
					setState(77);
					requireNullStmt();
					}
					break;
				case REQUIRE_NO_DOUBLE_FREE_KEYWORD:
					{
					setState(78);
					requireNoDoubleFreeStmt();
					}
					break;
				case ERROR_KEYWORD:
					{
					setState(79);
					action();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(84);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(85);
			match(RBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RequireLiteralStmtContext extends ParserRuleContext {
		public TerminalNode REQUIRE_LITERAL_FORMAT_KEYWORD() { return getToken(CSentinelParser.REQUIRE_LITERAL_FORMAT_KEYWORD, 0); }
		public TerminalNode LBRACE() { return getToken(CSentinelParser.LBRACE, 0); }
		public ActionContext action() {
			return getRuleContext(ActionContext.class,0);
		}
		public TerminalNode RBRACE() { return getToken(CSentinelParser.RBRACE, 0); }
		public RequireLiteralStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_requireLiteralStmt; }
	}

	public final RequireLiteralStmtContext requireLiteralStmt() throws RecognitionException {
		RequireLiteralStmtContext _localctx = new RequireLiteralStmtContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_requireLiteralStmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(87);
			match(REQUIRE_LITERAL_FORMAT_KEYWORD);
			setState(88);
			match(LBRACE);
			setState(89);
			action();
			setState(90);
			match(RBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RequireNullStmtContext extends ParserRuleContext {
		public TerminalNode REQUIRE_NULL_AFTER_KEYWORD() { return getToken(CSentinelParser.REQUIRE_NULL_AFTER_KEYWORD, 0); }
		public TerminalNode LBRACE() { return getToken(CSentinelParser.LBRACE, 0); }
		public ActionContext action() {
			return getRuleContext(ActionContext.class,0);
		}
		public TerminalNode RBRACE() { return getToken(CSentinelParser.RBRACE, 0); }
		public RequireNullStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_requireNullStmt; }
	}

	public final RequireNullStmtContext requireNullStmt() throws RecognitionException {
		RequireNullStmtContext _localctx = new RequireNullStmtContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_requireNullStmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(92);
			match(REQUIRE_NULL_AFTER_KEYWORD);
			setState(93);
			match(LBRACE);
			setState(94);
			action();
			setState(95);
			match(RBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RequireNoDoubleFreeStmtContext extends ParserRuleContext {
		public TerminalNode REQUIRE_NO_DOUBLE_FREE_KEYWORD() { return getToken(CSentinelParser.REQUIRE_NO_DOUBLE_FREE_KEYWORD, 0); }
		public TerminalNode LBRACE() { return getToken(CSentinelParser.LBRACE, 0); }
		public ActionContext action() {
			return getRuleContext(ActionContext.class,0);
		}
		public TerminalNode RBRACE() { return getToken(CSentinelParser.RBRACE, 0); }
		public RequireNoDoubleFreeStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_requireNoDoubleFreeStmt; }
	}

	public final RequireNoDoubleFreeStmtContext requireNoDoubleFreeStmt() throws RecognitionException {
		RequireNoDoubleFreeStmtContext _localctx = new RequireNoDoubleFreeStmtContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_requireNoDoubleFreeStmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(97);
			match(REQUIRE_NO_DOUBLE_FREE_KEYWORD);
			setState(98);
			match(LBRACE);
			setState(99);
			action();
			setState(100);
			match(RBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IfStmtContext extends ParserRuleContext {
		public TerminalNode IF_KEYWORD() { return getToken(CSentinelParser.IF_KEYWORD, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode OVERFLOWS_KEYWORD() { return getToken(CSentinelParser.OVERFLOWS_KEYWORD, 0); }
		public TerminalNode LBRACE() { return getToken(CSentinelParser.LBRACE, 0); }
		public ActionContext action() {
			return getRuleContext(ActionContext.class,0);
		}
		public TerminalNode RBRACE() { return getToken(CSentinelParser.RBRACE, 0); }
		public IfStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifStmt; }
	}

	public final IfStmtContext ifStmt() throws RecognitionException {
		IfStmtContext _localctx = new IfStmtContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_ifStmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(102);
			match(IF_KEYWORD);
			setState(103);
			expr();
			setState(104);
			match(OVERFLOWS_KEYWORD);
			setState(105);
			match(LBRACE);
			setState(106);
			action();
			setState(107);
			match(RBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SourceRuleContext extends ParserRuleContext {
		public TerminalNode SOURCE_KEYWORD() { return getToken(CSentinelParser.SOURCE_KEYWORD, 0); }
		public TerminalNode ID() { return getToken(CSentinelParser.ID, 0); }
		public TerminalNode LBRACE() { return getToken(CSentinelParser.LBRACE, 0); }
		public ActionContext action() {
			return getRuleContext(ActionContext.class,0);
		}
		public TerminalNode RBRACE() { return getToken(CSentinelParser.RBRACE, 0); }
		public SourceRuleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sourceRule; }
	}

	public final SourceRuleContext sourceRule() throws RecognitionException {
		SourceRuleContext _localctx = new SourceRuleContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_sourceRule);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(109);
			match(SOURCE_KEYWORD);
			setState(110);
			match(ID);
			setState(111);
			match(LBRACE);
			setState(112);
			action();
			setState(113);
			match(RBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SinkRuleContext extends ParserRuleContext {
		public TerminalNode SINK_KEYWORD() { return getToken(CSentinelParser.SINK_KEYWORD, 0); }
		public TerminalNode ID() { return getToken(CSentinelParser.ID, 0); }
		public TerminalNode LBRACE() { return getToken(CSentinelParser.LBRACE, 0); }
		public ActionContext action() {
			return getRuleContext(ActionContext.class,0);
		}
		public TerminalNode RBRACE() { return getToken(CSentinelParser.RBRACE, 0); }
		public SinkRuleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sinkRule; }
	}

	public final SinkRuleContext sinkRule() throws RecognitionException {
		SinkRuleContext _localctx = new SinkRuleContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_sinkRule);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(115);
			match(SINK_KEYWORD);
			setState(116);
			match(ID);
			setState(117);
			match(LBRACE);
			setState(118);
			action();
			setState(119);
			match(RBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SanitizerRuleContext extends ParserRuleContext {
		public TerminalNode SANITIZER_KEYWORD() { return getToken(CSentinelParser.SANITIZER_KEYWORD, 0); }
		public TerminalNode ID() { return getToken(CSentinelParser.ID, 0); }
		public TerminalNode LBRACE() { return getToken(CSentinelParser.LBRACE, 0); }
		public TerminalNode RBRACE() { return getToken(CSentinelParser.RBRACE, 0); }
		public SanitizerRuleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sanitizerRule; }
	}

	public final SanitizerRuleContext sanitizerRule() throws RecognitionException {
		SanitizerRuleContext _localctx = new SanitizerRuleContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_sanitizerRule);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(121);
			match(SANITIZER_KEYWORD);
			setState(122);
			match(ID);
			setState(123);
			match(LBRACE);
			setState(124);
			match(RBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprContext extends ParserRuleContext {
		public List<TermContext> term() {
			return getRuleContexts(TermContext.class);
		}
		public TermContext term(int i) {
			return getRuleContext(TermContext.class,i);
		}
		public List<TerminalNode> PLUS() { return getTokens(CSentinelParser.PLUS); }
		public TerminalNode PLUS(int i) {
			return getToken(CSentinelParser.PLUS, i);
		}
		public List<TerminalNode> MINUS() { return getTokens(CSentinelParser.MINUS); }
		public TerminalNode MINUS(int i) {
			return getToken(CSentinelParser.MINUS, i);
		}
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	}

	public final ExprContext expr() throws RecognitionException {
		ExprContext _localctx = new ExprContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_expr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(126);
			term();
			setState(131);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==PLUS || _la==MINUS) {
				{
				{
				setState(127);
				_la = _input.LA(1);
				if ( !(_la==PLUS || _la==MINUS) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(128);
				term();
				}
				}
				setState(133);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TermContext extends ParserRuleContext {
		public List<FactorContext> factor() {
			return getRuleContexts(FactorContext.class);
		}
		public FactorContext factor(int i) {
			return getRuleContext(FactorContext.class,i);
		}
		public List<TerminalNode> STAR() { return getTokens(CSentinelParser.STAR); }
		public TerminalNode STAR(int i) {
			return getToken(CSentinelParser.STAR, i);
		}
		public List<TerminalNode> DIV() { return getTokens(CSentinelParser.DIV); }
		public TerminalNode DIV(int i) {
			return getToken(CSentinelParser.DIV, i);
		}
		public TermContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_term; }
	}

	public final TermContext term() throws RecognitionException {
		TermContext _localctx = new TermContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_term);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(134);
			factor();
			setState(139);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==STAR || _la==DIV) {
				{
				{
				setState(135);
				_la = _input.LA(1);
				if ( !(_la==STAR || _la==DIV) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(136);
				factor();
				}
				}
				setState(141);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FactorContext extends ParserRuleContext {
		public TerminalNode LPAREN() { return getToken(CSentinelParser.LPAREN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(CSentinelParser.RPAREN, 0); }
		public TerminalNode ID() { return getToken(CSentinelParser.ID, 0); }
		public TerminalNode NUMBER() { return getToken(CSentinelParser.NUMBER, 0); }
		public FactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor; }
	}

	public final FactorContext factor() throws RecognitionException {
		FactorContext _localctx = new FactorContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_factor);
		try {
			setState(148);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LPAREN:
				enterOuterAlt(_localctx, 1);
				{
				setState(142);
				match(LPAREN);
				setState(143);
				expr();
				setState(144);
				match(RPAREN);
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(146);
				match(ID);
				}
				break;
			case NUMBER:
				enterOuterAlt(_localctx, 3);
				{
				setState(147);
				match(NUMBER);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ActionContext extends ParserRuleContext {
		public TerminalNode ERROR_KEYWORD() { return getToken(CSentinelParser.ERROR_KEYWORD, 0); }
		public TerminalNode STRING() { return getToken(CSentinelParser.STRING, 0); }
		public ActionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_action; }
	}

	public final ActionContext action() throws RecognitionException {
		ActionContext _localctx = new ActionContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_action);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(150);
			match(ERROR_KEYWORD);
			setState(151);
			match(STRING);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u001a\u009a\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001"+
		"\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004"+
		"\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007"+
		"\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b"+
		"\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0001\u0000\u0005"+
		"\u0000 \b\u0000\n\u0000\f\u0000#\t\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0005\u0001/\b\u0001\n\u0001\f\u00012\t\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0005\u0003C\b\u0003\n\u0003\f\u0003F\t"+
		"\u0003\u0003\u0003H\b\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0005\u0003Q\b\u0003\n\u0003"+
		"\f\u0003T\t\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001"+
		"\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001\n\u0001"+
		"\n\u0001\n\u0001\u000b\u0001\u000b\u0001\u000b\u0005\u000b\u0082\b\u000b"+
		"\n\u000b\f\u000b\u0085\t\u000b\u0001\f\u0001\f\u0001\f\u0005\f\u008a\b"+
		"\f\n\f\f\f\u008d\t\f\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0003"+
		"\r\u0095\b\r\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0000\u0000"+
		"\u000f\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018"+
		"\u001a\u001c\u0000\u0002\u0001\u0000\r\u000e\u0001\u0000\u000f\u0010\u009b"+
		"\u0000!\u0001\u0000\u0000\u0000\u0002&\u0001\u0000\u0000\u0000\u00045"+
		"\u0001\u0000\u0000\u0000\u0006;\u0001\u0000\u0000\u0000\bW\u0001\u0000"+
		"\u0000\u0000\n\\\u0001\u0000\u0000\u0000\fa\u0001\u0000\u0000\u0000\u000e"+
		"f\u0001\u0000\u0000\u0000\u0010m\u0001\u0000\u0000\u0000\u0012s\u0001"+
		"\u0000\u0000\u0000\u0014y\u0001\u0000\u0000\u0000\u0016~\u0001\u0000\u0000"+
		"\u0000\u0018\u0086\u0001\u0000\u0000\u0000\u001a\u0094\u0001\u0000\u0000"+
		"\u0000\u001c\u0096\u0001\u0000\u0000\u0000\u001e \u0003\u0002\u0001\u0000"+
		"\u001f\u001e\u0001\u0000\u0000\u0000 #\u0001\u0000\u0000\u0000!\u001f"+
		"\u0001\u0000\u0000\u0000!\"\u0001\u0000\u0000\u0000\"$\u0001\u0000\u0000"+
		"\u0000#!\u0001\u0000\u0000\u0000$%\u0005\u0000\u0000\u0001%\u0001\u0001"+
		"\u0000\u0000\u0000&\'\u0005\u0001\u0000\u0000\'(\u0005\u0018\u0000\u0000"+
		"(0\u0005\b\u0000\u0000)/\u0003\u0004\u0002\u0000*/\u0003\u0006\u0003\u0000"+
		"+/\u0003\u0010\b\u0000,/\u0003\u0012\t\u0000-/\u0003\u0014\n\u0000.)\u0001"+
		"\u0000\u0000\u0000.*\u0001\u0000\u0000\u0000.+\u0001\u0000\u0000\u0000"+
		".,\u0001\u0000\u0000\u0000.-\u0001\u0000\u0000\u0000/2\u0001\u0000\u0000"+
		"\u00000.\u0001\u0000\u0000\u000001\u0001\u0000\u0000\u000013\u0001\u0000"+
		"\u0000\u000020\u0001\u0000\u0000\u000034\u0005\t\u0000\u00004\u0003\u0001"+
		"\u0000\u0000\u000056\u0005\u0002\u0000\u000067\u0005\u0018\u0000\u0000"+
		"78\u0005\b\u0000\u000089\u0003\u001c\u000e\u00009:\u0005\t\u0000\u0000"+
		":\u0005\u0001\u0000\u0000\u0000;<\u0005\u0003\u0000\u0000<=\u0005\u0004"+
		"\u0000\u0000=>\u0005\u0018\u0000\u0000>G\u0005\n\u0000\u0000?D\u0005\u0018"+
		"\u0000\u0000@A\u0005\f\u0000\u0000AC\u0005\u0018\u0000\u0000B@\u0001\u0000"+
		"\u0000\u0000CF\u0001\u0000\u0000\u0000DB\u0001\u0000\u0000\u0000DE\u0001"+
		"\u0000\u0000\u0000EH\u0001\u0000\u0000\u0000FD\u0001\u0000\u0000\u0000"+
		"G?\u0001\u0000\u0000\u0000GH\u0001\u0000\u0000\u0000HI\u0001\u0000\u0000"+
		"\u0000IJ\u0005\u000b\u0000\u0000JR\u0005\b\u0000\u0000KQ\u0003\u000e\u0007"+
		"\u0000LQ\u0003\b\u0004\u0000MQ\u0003\n\u0005\u0000NQ\u0003\f\u0006\u0000"+
		"OQ\u0003\u001c\u000e\u0000PK\u0001\u0000\u0000\u0000PL\u0001\u0000\u0000"+
		"\u0000PM\u0001\u0000\u0000\u0000PN\u0001\u0000\u0000\u0000PO\u0001\u0000"+
		"\u0000\u0000QT\u0001\u0000\u0000\u0000RP\u0001\u0000\u0000\u0000RS\u0001"+
		"\u0000\u0000\u0000SU\u0001\u0000\u0000\u0000TR\u0001\u0000\u0000\u0000"+
		"UV\u0005\t\u0000\u0000V\u0007\u0001\u0000\u0000\u0000WX\u0005\u0011\u0000"+
		"\u0000XY\u0005\b\u0000\u0000YZ\u0003\u001c\u000e\u0000Z[\u0005\t\u0000"+
		"\u0000[\t\u0001\u0000\u0000\u0000\\]\u0005\u0012\u0000\u0000]^\u0005\b"+
		"\u0000\u0000^_\u0003\u001c\u000e\u0000_`\u0005\t\u0000\u0000`\u000b\u0001"+
		"\u0000\u0000\u0000ab\u0005\u0013\u0000\u0000bc\u0005\b\u0000\u0000cd\u0003"+
		"\u001c\u000e\u0000de\u0005\t\u0000\u0000e\r\u0001\u0000\u0000\u0000fg"+
		"\u0005\u0005\u0000\u0000gh\u0003\u0016\u000b\u0000hi\u0005\u0006\u0000"+
		"\u0000ij\u0005\b\u0000\u0000jk\u0003\u001c\u000e\u0000kl\u0005\t\u0000"+
		"\u0000l\u000f\u0001\u0000\u0000\u0000mn\u0005\u0014\u0000\u0000no\u0005"+
		"\u0018\u0000\u0000op\u0005\b\u0000\u0000pq\u0003\u001c\u000e\u0000qr\u0005"+
		"\t\u0000\u0000r\u0011\u0001\u0000\u0000\u0000st\u0005\u0015\u0000\u0000"+
		"tu\u0005\u0018\u0000\u0000uv\u0005\b\u0000\u0000vw\u0003\u001c\u000e\u0000"+
		"wx\u0005\t\u0000\u0000x\u0013\u0001\u0000\u0000\u0000yz\u0005\u0016\u0000"+
		"\u0000z{\u0005\u0018\u0000\u0000{|\u0005\b\u0000\u0000|}\u0005\t\u0000"+
		"\u0000}\u0015\u0001\u0000\u0000\u0000~\u0083\u0003\u0018\f\u0000\u007f"+
		"\u0080\u0007\u0000\u0000\u0000\u0080\u0082\u0003\u0018\f\u0000\u0081\u007f"+
		"\u0001\u0000\u0000\u0000\u0082\u0085\u0001\u0000\u0000\u0000\u0083\u0081"+
		"\u0001\u0000\u0000\u0000\u0083\u0084\u0001\u0000\u0000\u0000\u0084\u0017"+
		"\u0001\u0000\u0000\u0000\u0085\u0083\u0001\u0000\u0000\u0000\u0086\u008b"+
		"\u0003\u001a\r\u0000\u0087\u0088\u0007\u0001\u0000\u0000\u0088\u008a\u0003"+
		"\u001a\r\u0000\u0089\u0087\u0001\u0000\u0000\u0000\u008a\u008d\u0001\u0000"+
		"\u0000\u0000\u008b\u0089\u0001\u0000\u0000\u0000\u008b\u008c\u0001\u0000"+
		"\u0000\u0000\u008c\u0019\u0001\u0000\u0000\u0000\u008d\u008b\u0001\u0000"+
		"\u0000\u0000\u008e\u008f\u0005\n\u0000\u0000\u008f\u0090\u0003\u0016\u000b"+
		"\u0000\u0090\u0091\u0005\u000b\u0000\u0000\u0091\u0095\u0001\u0000\u0000"+
		"\u0000\u0092\u0095\u0005\u0018\u0000\u0000\u0093\u0095\u0005\u0017\u0000"+
		"\u0000\u0094\u008e\u0001\u0000\u0000\u0000\u0094\u0092\u0001\u0000\u0000"+
		"\u0000\u0094\u0093\u0001\u0000\u0000\u0000\u0095\u001b\u0001\u0000\u0000"+
		"\u0000\u0096\u0097\u0005\u0007\u0000\u0000\u0097\u0098\u0005\u0019\u0000"+
		"\u0000\u0098\u001d\u0001\u0000\u0000\u0000\n!.0DGPR\u0083\u008b\u0094";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}