import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    A = np.array(A)
    N = A.shape[0]

    trace_sum = 0
    for i in range(N):
        trace_sum += A[i][i]

    return trace_sum