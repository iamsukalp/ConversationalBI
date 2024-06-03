def get_prompt(query,meta):
  prompt = f"""for the table named 'sales', consider the meta data to answer the question, meta_data = {meta}
  , question : {query}"""
  return prompt