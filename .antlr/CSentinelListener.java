// Generated from c:/dev/CompilerProject/C-Sentinel/CSentinel.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link CSentinelParser}.
 */
public interface CSentinelListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link CSentinelParser#senFile}.
	 * @param ctx the parse tree
	 */
	void enterSenFile(CSentinelParser.SenFileContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSentinelParser#senFile}.
	 * @param ctx the parse tree
	 */
	void exitSenFile(CSentinelParser.SenFileContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSentinelParser#rule}.
	 * @param ctx the parse tree
	 */
	void enterRule(CSentinelParser.RuleContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSentinelParser#rule}.
	 * @param ctx the parse tree
	 */
	void exitRule(CSentinelParser.RuleContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSentinelParser#blockRule}.
	 * @param ctx the parse tree
	 */
	void enterBlockRule(CSentinelParser.BlockRuleContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSentinelParser#blockRule}.
	 * @param ctx the parse tree
	 */
	void exitBlockRule(CSentinelParser.BlockRuleContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSentinelParser#onRule}.
	 * @param ctx the parse tree
	 */
	void enterOnRule(CSentinelParser.OnRuleContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSentinelParser#onRule}.
	 * @param ctx the parse tree
	 */
	void exitOnRule(CSentinelParser.OnRuleContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSentinelParser#requireLiteralStmt}.
	 * @param ctx the parse tree
	 */
	void enterRequireLiteralStmt(CSentinelParser.RequireLiteralStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSentinelParser#requireLiteralStmt}.
	 * @param ctx the parse tree
	 */
	void exitRequireLiteralStmt(CSentinelParser.RequireLiteralStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSentinelParser#requireNullStmt}.
	 * @param ctx the parse tree
	 */
	void enterRequireNullStmt(CSentinelParser.RequireNullStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSentinelParser#requireNullStmt}.
	 * @param ctx the parse tree
	 */
	void exitRequireNullStmt(CSentinelParser.RequireNullStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSentinelParser#ifStmt}.
	 * @param ctx the parse tree
	 */
	void enterIfStmt(CSentinelParser.IfStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSentinelParser#ifStmt}.
	 * @param ctx the parse tree
	 */
	void exitIfStmt(CSentinelParser.IfStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSentinelParser#sourceRule}.
	 * @param ctx the parse tree
	 */
	void enterSourceRule(CSentinelParser.SourceRuleContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSentinelParser#sourceRule}.
	 * @param ctx the parse tree
	 */
	void exitSourceRule(CSentinelParser.SourceRuleContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSentinelParser#sinkRule}.
	 * @param ctx the parse tree
	 */
	void enterSinkRule(CSentinelParser.SinkRuleContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSentinelParser#sinkRule}.
	 * @param ctx the parse tree
	 */
	void exitSinkRule(CSentinelParser.SinkRuleContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSentinelParser#sanitizerRule}.
	 * @param ctx the parse tree
	 */
	void enterSanitizerRule(CSentinelParser.SanitizerRuleContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSentinelParser#sanitizerRule}.
	 * @param ctx the parse tree
	 */
	void exitSanitizerRule(CSentinelParser.SanitizerRuleContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSentinelParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(CSentinelParser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSentinelParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(CSentinelParser.ExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSentinelParser#term}.
	 * @param ctx the parse tree
	 */
	void enterTerm(CSentinelParser.TermContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSentinelParser#term}.
	 * @param ctx the parse tree
	 */
	void exitTerm(CSentinelParser.TermContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSentinelParser#factor}.
	 * @param ctx the parse tree
	 */
	void enterFactor(CSentinelParser.FactorContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSentinelParser#factor}.
	 * @param ctx the parse tree
	 */
	void exitFactor(CSentinelParser.FactorContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSentinelParser#action}.
	 * @param ctx the parse tree
	 */
	void enterAction(CSentinelParser.ActionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSentinelParser#action}.
	 * @param ctx the parse tree
	 */
	void exitAction(CSentinelParser.ActionContext ctx);
}