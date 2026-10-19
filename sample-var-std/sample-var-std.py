import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    n = len(x)
    x = np.asarray(x)
    x_bar = np.mean(x)
    variance = np.sum((x - x_bar)**2) * 1 / (n - 1)
    standard_deviation = np.sqrt(variance)
    return {"variance": float(variance), "standard_deviation": float(standard_deviation)}