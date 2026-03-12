def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # Write code here
    for i in range(steps):
        grad = 2*a*x0 + b
        x1 = x0 - lr*grad
        x0 = x1
    return x0
    pass