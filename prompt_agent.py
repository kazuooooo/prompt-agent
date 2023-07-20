from agents.prompt_agent import fix_prompt
from agents.evaluation_agent import evaluate
from agents.execution_agent import execute

desired_output = "こんにちは〜大阪のおばちゃん清美やでーおばちゃん占い師やねん。なんでも聞いておくれやー"
prompt = "こんにちは"

for i in range(5):
  output = execute(prompt)
  print("output", output)

  improvments = evaluate(output, desired_output)
  print("improvements", improvments)

  prompt = fix_prompt(prompt, improvments)
  print("fixed_prompts", prompt)