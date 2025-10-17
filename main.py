import os
from dotenv import load_dotenv

# Find .env relative to the script location
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
dotenv_path = os.path.join(BASE_DIR, ".env")

# Load it
load_dotenv(dotenv_path)
#print(os.getenv("GROQ_API_KEY"))
#from config import GROQ_API_KEY


from crew import stock_crew
import streamlit as st

st.set_page_config(
    page_title="Stock Trading Expert",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.set_page_config(
    page_title="Stock Trading Expert",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------
# App Title
# ----------------------------
st.title("📊 Stock Trading Expert")
st.subheader("Analyze and get insights on your favorite stocks")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# load the chat history on the page
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ----------------------------
# Sidebar for user input
# ----------------------------
st.sidebar.header("User Input")
symbol_input = st.sidebar.text_input(
    "Enter your Stock (e.g., AAPL, MSFT, GOOGL):"
)

if symbol_input:
    with st.chat_message("user"):
        st.markdown(symbol_input)

    result = stock_crew.kickoff(inputs={"stock": symbol_input})

    with st.chat_message("assistant"):
        st.markdown(result)

    st.session_state.chat_history.append({"role": "assistant", "content": result})




# def run():
#     print("***** Your Stock Trading expert ********")
#     while True:
#         print("**"*100)
#         user_input = input("You: ")
#         if user_input.lower() in ["quit", "exit"]:
#             break
#         result = stock_crew.kickoff(inputs={"stock": user_input})
#         print(result)
#
#
# if __name__=="__main__":
#     run()