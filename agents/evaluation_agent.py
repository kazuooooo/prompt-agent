import openai
import json
import os

def evaluate(
  output: str,
  desired_output: str,
) -> list[str]:
  """
  Evaluate output compared to desired output, and return a list of improvements

  Paramters:
    output(str)
    desired_output(str)
  
  Returns:
    list[str]: Improvments for desired output
  """

  agent_prompt: str = f"""
  現在の出力と理想の出力を比較して、現在の出力が理想の出力に近づくための改善点をリストアップしてください。

  現在の出力
  ```
  {output}
  ```

  理想の出力
  ```
  {desired_output}
  ```
  """

  response = openai.ChatCompletion.create( #type: ignore
    model=os.environ.get("LLM_MODEL"),
    messages=[{"role": "system", "content": agent_prompt }],
    functions=[
      {
        "name": "show_improvements",
        "description": "現在の出力と理想の出力を比較して、現在の出力が理想の出力に近づくための改善点をリストアップする。",
        "parameters": {
          "type": "object",
          "properties": {
            "improvements": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          }
        }
      }
    ],
    function_call={ "name": "show_improvements"},
    temperature=0
  )

  response_message = response["choices"][0]["message"] #type: ignore
  function_args = json.loads(response_message["function_call"]["arguments"]) #type: ignore
  return function_args["improvements"]