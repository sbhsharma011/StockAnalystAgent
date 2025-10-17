from crewai import Task
from agents.stock_analyst_agent import stock_analyst_agent

stock_analysis_task = Task(
    description=(
        "Analyze the recent performance of the stock: {stock}. Use the live stock information tool to retrieve "
        "current price, percentage change, trading volume, and other market data. Provide a summary of how the stock "
        "is performing today and highlight any key observations from the data."),
    expected_output=(
        "A clear, bullet-pointed summary of:\n"
        "- Current stock price\n"
        "- Daily price change and percentage\n"
        "- Volume and volatility\n"
        "- Any immediate trends or observations"
    ),
    agent=stock_analyst_agent
)