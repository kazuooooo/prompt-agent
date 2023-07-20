import openai
def execute(
  prompt: str
) -> str:
  """
  Execute a prompt and return the output

  Paramters:
    propmt: str
  
  Returns:
    str: output of the fixed prompt
  """
  response = openai.ChatCompletion.create( #type: ignore
    model="gpt-4-0613",
    messages=[{"role": "system", "content": prompt }],
    temperature=0
  )
  return response["choices"][0]["message"].content #type: ignore