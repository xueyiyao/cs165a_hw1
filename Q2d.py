def factorial(n):
  """
  @input:
    n: a positive integer. 
  @output:
    an integer of n!.
  """
  #TODO
  if(n == 1):
      return 1
  return n * factorial(n-1)      
  
print(factorial(3))

"""
Output example:
6
"""
