from agents.fix_prompt_agent import fix_prompt
from agents.evaluation_agent import evaluate
from agents.execution_agent import execute
from dotenv import load_dotenv
load_dotenv()

# Desired output
desired_output = "4+4=8です"
# Initial prompt
prompt = "1+1はいくつですか？"
# Iteration
iteration = 3

print("*****設定*****")
print("理想の出力:", desired_output)
print("初期プロンプト:", prompt)
print("イテレーション:", iteration, "\n")


for i in range(iteration):
  output = execute(prompt)
  improvments = evaluate(output, desired_output)
  prompt = fix_prompt(prompt, improvments)

print("*****最終結果*****")
print("プロンプト:", prompt) #type: ignore
print("出力:", output) #type: ignore