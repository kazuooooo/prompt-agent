# 試作プロンプト改善エージェント
![2-1](https://github.com/kazuooooo/prompt-agent/assets/6919381/5dff6692-f738-4c46-87ad-b9b4657d234e)
詳しい内容は[Zennの記事](https://zenn.dev/kazuwombat/articles/2095668882245d)をご覧ださい。

# 使い方
1. レポジトリをClone
2. パッケージのインストール: `pip install -r requirements.txt`
3. .env.exampleファイルをコピー: `cp .env.example .env`
4. 環境変数を設定
  ```
  OPENAI_API_KEY=sk-...
  LLM_MODEL=gpt-4-0613 # alternatively, gpt-3.5-turbo-0613
  ```
5. `prompt_agent.py`の現在のプロンプト、理想の出力、いてレーションを設定
  ```
  desired_output = "4+4=8です"
  prompt = "1+1はいくつですか？"
  iteration = 3
  ```
6. 実行: `python3 prompt_agent.py`
