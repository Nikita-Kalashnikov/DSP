# signal_generators.py
import numpy as np
# 2 * np.pi - можно представить как 360°. 
# 2 * np.pi / frequency - 360°/количество частей одного периода
# n - число частей одного периода которые будут воспроизведены
# phase - смещение всех значений на угол
# phase*np.pi/180 - перевод из градусов в радианы

def gen_sin(amplitude: float, frequency: float, phase: float, n_samples: int) -> np.ndarray:
    n = np.arange(n_samples)
    phase_radian = phase*np.pi/180
    return amplitude * np.sin(2 * np.pi / frequency * n + phase_radian)

def gen_cos(amplitude: float, frequency: float, phase: float, n_samples: int) -> np.ndarray:
    n = np.arange(n_samples)
    phase_radian = phase*np.pi/180
    return amplitude * np.cos(2 * np.pi / frequency * n + phase_radian)