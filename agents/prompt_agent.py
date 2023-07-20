import openai
import json

def fix_prompt(
  current_prompt: str,
  improvements: list[str],
) -> str:
  """
  Given a prompt, a response, and a desired response, return a new prompt

  Paramters:
    current_prompt(str)
    current_response(str)
    desired_response(str)
    improvements(list): list of improvements suggested by evaluation_agent
  
  Returns:
    str: Fixed prompt
  """

  agent_prompt: str = f"""
  あなたはプロンプトエンジニアです。
  このプロンプトを改善点に基づいて、修正してください。

  プロンプト
  ```
  {current_prompt}
  ```

  改善点
  ```
  {improvements}
  ```
  """

  print("agent_prompt", agent_prompt)

  response = openai.ChatCompletion.create( #type: ignore
    model="gpt-4-0613",
    messages=[{"role": "system", "content": agent_prompt }],
    functions=[
      {
        "name": "fix_prompt",
        "description": "現在のプロンプトを改善点に基づいて修正する",
        "parameters": {
          "type": "object",
          "properties": {
            "fixed_prompt": {
              "type": "string"
            }
          }
        }
      }
    ],
    function_call={ "name": "fix_prompt"},
    temperature=0
  )

  response_message = response["choices"][0]["message"] #type: ignore
  function_args = json.loads(response_message["function_call"]["arguments"])
  return function_args['fixed_prompt']