import streamlit as st


def default_component():
    # Example message with formatting and constrained line length
    message = """
    ### 📊 Welcome to our Sales Data Analyzer for Nigeria!
    \nHarness the power of our tool to effortlessly explore sales data. 
    Ask questions in plain language,and our LLM generates SQL queries. 
    Get dynamic charts, insightful analyses,and comprehensive tables tailored to your needs.

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
    st.write(message, unsafe_allow_html=True)

