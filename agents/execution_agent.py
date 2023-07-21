import openai
import os
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
    model=os.environ.get("LLM_MODEL"),
    messages=[{"role": "system", "content": prompt }],
    temperature=0
  )
  return response["choices"][0]["message"].content #type: ignore