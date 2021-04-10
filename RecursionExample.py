def string_splosion(str):
  """
  Expects a str. 
  Returns sub-combinations of str. For example, str = "Hello" --> returns "HHeHelHellHello" 
  """
  if len(str) == 1:
    return str
  else:
    return string_splosion(str[:len(str) - 1]) + str
  
