from crewai import Crew
from tasks.stock_analysis_task import stock_analysis_task
from tasks.stock_trading_task import stock_trading_task
from agents.stock_analyst_agent import stock_analyst_agent
from agents.stock_trader_agent import stock_trader_agent

#load_dotenv(".env")

stock_crew = Crew(
    agents=[stock_analyst_agent,stock_trader_agent],
    tasks=[stock_analysis_task,stock_trading_task],
    verbose=False

)

