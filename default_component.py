import streamlit as st


def default_component():
    # Example message with formatting and constrained line length
    message = """
    ### Welcome to our Sales Data Analyzer for Nigeria!
    \nHarness the power of our tool to effortlessly explore sales data. 
    

    🔍 **Query Generation:** 
    Ask questions, get SQL queries instantly. 
    For Example: "Give me top five items based on sales in USD."

    📈 **Chart Visualization:** 
    Visualize sales trends with stunning charts.

    💡 **Insightful Analysis:** 
    Discover hidden patterns and trends.

    📊 **Comprehensive Tables:** 
    Get organized, detailed data for quick analysis.

    Experience data-driven decision-making. Start exploring today!
    """

    # Write the formatted message to the Streamlit app
    # st.write(message, unsafe_allow_html=True)

    return message


def default_quick_component():
    message = """
    ### Welcome to our Quick Anlysis tool
    \nHarness the power of our tool to effortlessly explore the data.
    
    🤖 Talk to your data! With our LLM, 
    you can upload CSV files and interact with your data using natural language.
    Just ask questions in plain English, and get instant insights. No coding required! 
    Streamline your data analysis process, 
    save time, and make data-driven decisions with ease. 
    Perfect for business professionals, researchers, and anyone who wants to harness the power 
    of their data without technical barriers. 📊💬🚀"
    """

    return message
