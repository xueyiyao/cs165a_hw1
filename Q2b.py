import numpy as np
from scipy.sparse import csr_matrix

# Note: Should use scipy.sparse library.

def generate(n):
  """
  @input:
    n: an int. 
  @return:
    None. Print to screen.
  """
  assert n > 1
  posvalues = np.ones(n-1)
  negvalues = np.negative(np.ones(n-1))
  posrange = np.arange(n-1)
  negrange = np.arange(1,n)
  A = np.zeros(20).reshape(4,5)
  A[np.arange(n-1), posrange] = posvalues
  A[np.arange(n-1), negrange] = negvalues

  A = csr_matrix(A)        
  
  return A

A = generate(5)
print(A)

"""
Output example:
  (0, 0)	1.0
  (0, 1)	-1.0
  (1, 1)	1.0
  (1, 2)	-1.0
  (2, 2)	1.0
  (2, 3)	-1.0
  (3, 3)	1.0
  (3, 4)	-1.0
"""
