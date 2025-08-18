# signal_generators.py
import numpy as np
# 2 * np.pi - можно представить как 360°. 
# 2 * np.pi / frequency - 360°/количество частей одного периода
# n - число частей одного периода
# phase - смещение всех значений на угол

def gen_sin(amplitude: float, frequency: float, phase: float, n_samples: int) -> np.ndarray:
    n = np.arange(n_samples)
    return amplitude * np.sin(2 * np.pi / frequency * n + phase)

def gen_cos(amplitude: float, frequency: float, phase: float, n_samples: int) -> np.ndarray:
    n = np.arange(n_samples)
    return amplitude * np.cos(2 * np.pi / frequency * n + phase)