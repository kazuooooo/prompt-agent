from agents.prompt_agent import fix_prompt

current_prompt = "こんにちは"
improvments = ['足し算をするようにお願いしましょう']

fixed_prompt = fix_prompt(
  current_prompt=current_prompt,
  improvements=improvments
)
print("fixed_prompt", fixed_prompt)