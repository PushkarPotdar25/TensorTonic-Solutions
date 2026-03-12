import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    if len(x) != len(p):
        raise ValueError("x and p must have same length")
    
    if not np.isclose(sum(p), 1):
        raise ValueError("Probabilities must sum to 1")
    
    sol = 0
    for i in range(len(x)):
        sol += x[i] * p[i]

    return float(sol)