import numpy as np
import matplotlib.pyplot as plt

def gen_sin(amplitude: float, frequency: float, phase: float, n_samples: int) -> np.ndarray:
    """
    Генерация синусоидального сигнала
    
    Параметры:
        amplitude: амплитуда сигнала
        frequency: частота сигнала (циклов на отсчет)
        phase: начальная фаза в радианах
        n_samples: количество отсчетов
    
    Возвращает:
        Массив отсчетов сигнала
    """
    # Создание шкалы отсчетов
    n = np.arange(n_samples)
    # Формула синусоиды: A * sin(2πfn + φ)
    return amplitude * np.sin(2 * np.pi * frequency * n + phase)


def gen_cos(amplitude: float, frequency: float, phase: float, n_samples: int) -> np.ndarray:
    """
    Генерация косинусоидального сигнала
    
    Параметры аналогичны gen_sin()
    """
    n = np.arange(n_samples)
    # Формула косинусоиды: A * cos(2πfn + φ)
    return amplitude * np.cos(2 * np.pi * frequency * n + phase)


# Пример использования
if __name__ == "__main__":
    # Параметры сигнала
    AMPLITUDE = 1.5
    FREQUENCY = 0.05  # 0.05 циклов на отсчет = 1 цикл на 20 отсчетов
    PHASE = np.pi/4   # 45° в радианах
    N_SAMPLES = 100   # Количество отсчетов
    
    # Генерация сигналов
    sin_wave = gen_sin(AMPLITUDE, FREQUENCY, PHASE, N_SAMPLES)
    cos_wave = gen_cos(AMPLITUDE, FREQUENCY, PHASE, N_SAMPLES)
    
    # Визуализация
    n = np.arange(N_SAMPLES)
    
    plt.figure(figsize=(12, 6))
    
    plt.subplot(2, 1, 1)
    plt.stem(n, sin_wave, 'b-', label=f'sin: {FREQUENCY:.3f} циклов/отсчет')
    plt.title('Синусоидальный сигнал')
    plt.xlabel('Номер отсчета (n)')
    plt.ylabel('Амплитуда')
    plt.grid(True)
    plt.legend()
    
    plt.subplot(2, 1, 2)
    plt.stem(n, cos_wave, 'r-', label=f'cos: {FREQUENCY:.3f} циклов/отсчет')
    plt.title('Косинусоидальный сигнал')
    plt.xlabel('Номер отсчета (n)')
    plt.ylabel('Амплитуда')
    plt.grid(True)
    plt.legend()
    
    plt.tight_layout()
    plt.show()