def evaluate(
  fixed_prompt_response: str,
  desired_response: str,
) -> list[str]:
  """
  Evaluate fixed_prompt_response compared to desired response, and return a list of improvements

  Paramters:
    fixed_prompt_response(str)
    desired_respons(str)
  
  Returns:
    list[str]: Improvments to the fixed_prompt_response
  """
  return ['response']