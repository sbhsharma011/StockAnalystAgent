from crewai import Agent, LLM
#load_dotenv(".env")
llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    temperature=0.0,
)

stock_trader_agent = Agent(
    role="Stock Trader Analyst",
    goal=("Provide guidance weather we should Buy, Sell or hold the stock based on live market data,"
          "in depth evaluation of the stock report, analyze risks, and financial analysis with available data"),
    backstory=("You are a strategic trader with years of experience in timing market entry and exit points. "
        "You rely on real-time stock data, daily price movements, and volume trends to make trading decisions "
        "that optimize returns and reduce risk."),
    llm=llm,
    tools=[],
    verbose=False
)