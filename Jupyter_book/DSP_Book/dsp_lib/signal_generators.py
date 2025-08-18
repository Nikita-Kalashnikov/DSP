# signal_generators.py
import numpy as np

def gen_sin(amplitude: float, frequency: float, phase: float, n_samples: int) -> np.ndarray:
    n = np.arange(n_samples)
    return amplitude * np.sin(2 * np.pi * (1/frequency) * n + phase)

def gen_cos(amplitude: float, frequency: float, phase: float, n_samples: int) -> np.ndarray:
    n = np.arange(n_samples)
    return amplitude * np.cos(2 * np.pi * (1/frequency) * n + phase)