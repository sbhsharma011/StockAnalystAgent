from crewai import Task
from agents.stock_trader_agent import stock_trader_agent

stock_trading_task = Task(
    # description=(
    #     "Use live market data and stock performance indicators for {stock} to make a strategic trading decision. "
    #     "Assess key factors such as current price, daily change percentage, volume trends, and recent momentum. "
    #     "Go through the user history from previous chat to understand the context of the conversation"
    #     "If context is not {stock}, then just simply response this and do not response with some other analysis:"
    #     "I am sorry !! I am just a Stock market advisor. I may not be helpful for non-stock related topics"
    #     "If in the user input, user is asking for general information related to {stock}, share your analysis"
    #     "Based on your analysis, recommend whether to **Buy**, **Sell**, or **Hold** the stock."
    #     # "If user asks more information about the length when is the good time to buy, sell or hold the stock. Provide the information and on what basis you think that"
    #     # "If user asks how long should they hold the {stock} then provide a clear and bulleted recommendation"
    #     # "If User asks when is the good time to buy a specific {stock} the provide a recommendation in days or months and it's supported technical and market signals"
    # ),
    # expected_output=(
    #     "If a user asks about stock information then provide A clear and confident trading recommendation (Buy / Sell / Hold), supported by:\n"
    #         "- Current stock price and daily change\n"
    #         "- Volume and market activity observations\n"
    #         "- Justification for the trading action based on technical signals or risk-reward outlook"
    #     # "If a user is asking a specific question related to just trend of a stock or similar context then Share your analysis in bulleted points supported by:"
    #     #     "- Current stock price and daily change\n"
    #     #     "- Volume and market activity observations\n"
    #     #     "- Justification for the trading action based on technical signals or risk-reward outlook"
    #     # "If user asks how long should they hold the {stock} then provide a clear and bulleted recommendation supported by : "
    #     #     "- How long they should hold the stock"
    #     #     "- Justification for the trading action based on technical signals or risk-reward outlook"
    #     # "If User asks when is the good time to buy a specific {stock} the provide a recommendation in days or months and it's supported technical and market signals"
    # ),
    description=(
        "You are a trading strategist analyzing stock: {stock}.\n\n"
        "Use recent market data, price momentum, and technical signals provided by the Stock Analyst Agent "
        "to evaluate the best trading action.\n\n"
        "Follow these rules:\n"
        "1️⃣ If the user asks a stock-related question about {stock}, provide a detailed, data-driven analysis.\n"
        "2️⃣ If the user query is unrelated to stock trading or does not match {stock}, reply with:\n"
        "   'I am sorry! I am just a Stock Market Advisor and may not be helpful for non-stock related topics.'\n"
        "3️⃣ Base your recommendation (Buy/Sell/Hold) on both technical and business trend indicators.\n"
        "4️⃣ When applicable, provide a suggested holding period or ideal buy/sell window with reasoning.\n"
        "5️⃣ Your response should be confident, factual, and supported by recent market context."
    ),
    expected_output=(
        "Your output must bulleted when required, highlight/bold the important data and include:\n"
        "- Current price, daily % change, and trading volume\n"
        "- Market sentiment and technical trend summary (RSI, MA, volatility, etc.)\n"
        "- Your recommendation: **Buy**, **Sell**, or **Hold**\n"
        "- Justification for this recommendation\n"
        "- If applicable: holding duration or best time window"
    ),
    agent=stock_trader_agent
)