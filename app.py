
import streamlit as st
from chat_component import chat_component
from chart_component import chart_component
from table_component import table_component
from sql_component import sql_component
from get_reults import get_result


# Set page configuration
st.set_page_config(layout="wide", page_title='Conversational BI', page_icon= ':speech_balloon:')
st.title ='Converstaional BI'

# Main layout
st.markdown(
    """
    <style>
    .main {padding-top: 0rem;}
    </style>
    """
, unsafe_allow_html=True)

# Create two columns
col1, col2 = st.columns([1, 1])
prompt = st.chat_input("Ask me anything!")
data = None
fig = None
response =None
if prompt:
    data,fig,response = get_result(prompt)
    
with col1:    
        chat_component(prompt)


with col2:
    with st.expander("Chart"):
        chart_component(fig)
    with st.expander("Table"):
        table_component(data)
    with st.expander("SQL Query"):
        sql_component(response)
