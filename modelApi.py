import pandas as pd
from langchain.llms import OpenAI
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain.chains import create_sql_query_chain
from langchain.chat_models import ChatOpenAI
from utilities import API_KEY,DB_PATH,META_DATA_PATH



def modelApi():
    meta = pd.read_csv(META_DATA_PATH)
    db = SQLDatabase.from_uri(DB_PATH)
    llm = OpenAI(temperature=0, verbose=False,api_key=API_KEY )
    db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=False)
    chain = create_sql_query_chain(ChatOpenAI(temperature=0,api_key= API_KEY), db)

    return db_chain,chain,meta




