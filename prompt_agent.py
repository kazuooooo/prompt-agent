# from agents.prompt_agent import fix_prompt
from agents.evaluation_agent import evaluate
# from agents.execution_agent import execute

# current_prompt = "こんにちは"
# improvments = ['足し算をするようにお願いしましょう']

improvments = evaluate("こんにちは", "1+1の結果は2です。")
print("improvments", improvments)
# evaluate("こんにちは", "こんにちは")
# output = execute("こんにちは")
# print("output", output)
# fixed_prompt = fix_prompt(
#   current_prompt=current_prompt,
#   improvements=improvments
# )
# print("fixed_prompt", fixed_prompt)