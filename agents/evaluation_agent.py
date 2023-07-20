def evaluate(
  fixed_prompt_output: str,
  desired_output: str,
) -> list[str]:
  """
  Evaluate fixed_prompt_output compared to desired output, and return a list of improvements

  Paramters:
    fixed_prompt_output(str)
    desired_respons(str)
  
  Returns:
    list[str]: Improvments to the fixed_prompt_output
  """
  return ['output']