from crewai import Agent, LLM
from tools.stock_research_tool import get_stock_price
llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    temperature=0.0,
)

stock_analyst_agent = Agent(
    role="Financial Market Analyst",
    goal=("Perform Deep analysis of public stocks using real-time data,"
          "Analyze current and historical market trends, identify technical trends, and key financial signals to support decision-making"),
    backstory=("You are an expert Financial advisor with deep understanding of stock market trends,"
               "technical trend evaluation, market risk analysis and it's fundamentals."
               "you specialized in producing well organized structured report that evaluates stock performance using historical and live market indicators"
    ),
    llm=llm,
    tools=[get_stock_price],
    verbose=False
)