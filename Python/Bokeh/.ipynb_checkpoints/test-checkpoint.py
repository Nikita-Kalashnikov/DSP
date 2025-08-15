import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Polygon

# Настройка параметров сигнала
height = 0.8  # Высота прямоугольного импульса
duration = 1  # Длительность импульса
total_time = 3  # Общее время анимации
fps = 20  # Кадров в секунду

# Создаем временную ось
t = np.linspace(-1.5, 2.5, 1000)

# Функция прямоугольного сигнала
def rect_signal(x, height, start, end):
    return np.where((x >= start) & (x <= end), height, 0)

# Создаем фигуру и оси
fig, ax = plt.subplots(figsize=(10, 6), dpi=100)
plt.subplots_adjust(bottom=0.15)
ax.set_xlim(-1.5, 2.5)
ax.set_ylim(0, 1.5)
ax.set_xlabel('Время')
ax.set_ylabel('Амплитуда')
ax.grid(True, linestyle='--', alpha=0.7)
ax.set_title('Свертка прямоугольного сигнала с самим собой', fontsize=14)

# Основные элементы анимации
original_signal, = ax.plot(t, rect_signal(t, height, 0, duration), 'b-', linewidth=2, label='Исходный сигнал')
shifted_signal, = ax.plot([], [], 'orange', linewidth=2, label='Сдвинутая копия')
product_area = ax.fill_between([], [], [], facecolor='green', alpha=0.4, label='Произведение сигналов')
convolution_line, = ax.plot([], [], 'r-', linewidth=3, label='Результат свертки')
area_label = ax.text(0.02, 0.95, '', transform=ax.transAxes, fontsize=12, 
                     bbox=dict(facecolor='white', alpha=0.8))
time_label = ax.text(0.02, 0.85, '', transform=ax.transAxes, fontsize=12,
                     bbox=dict(facecolor='white', alpha=0.8))

# Вычисление аналитической свертки
def analytical_convolution(tau):
    result = np.zeros_like(tau)
    for i, t_val in enumerate(tau):
        if 0 <= t_val < 1:
            result[i] = height**2 * t_val
        elif 1 <= t_val <= 2:
            result[i] = height**2 * (2 - t_val)
    return result

conv_result = analytical_convolution(t)

# Инициализация
def init():
    shifted_signal.set_data([], [])
    convolution_line.set_data([], [])
    time_label.set_text('')
    area_label.set_text('')
    return original_signal, shifted_signal, convolution_line, time_label, area_label

# Функция обновления кадра
def update(frame):
    # Сдвинутая копия сигнала
    shifted = rect_signal(t, height, frame - duration, frame)
    shifted_signal.set_data(t, shifted)
    
    # Область произведения сигналов
    product = rect_signal(t, height, 0, duration) * shifted
    ax.collections.clear()
    ax.fill_between(t, product, 0, where=(product > 0), facecolor='green', alpha=0.4)
    
    # Результат свертки (накопленный)
    conv_display = np.where(t <= frame, conv_result, np.nan)
    convolution_line.set_data(t, conv_display)
    
    # Вычисление текущей площади
    current_area = np.trapz(product, t)
    area_label.set_text(f'Площадь: {current_area:.3f}')
    time_label.set_text(f't = {frame:.2f}')
    
    return original_signal, shifted_signal, convolution_line, time_label, area_label

# Создание анимации
ani = FuncAnimation(fig, update, frames=np.linspace(-0.5, 2.5, 100),
                    init_func=init, blit=False, interval=1000/fps)

# Добавление легенды
ax.legend(loc='upper right', framealpha=0.9)

# Сохранение в GIF
ani.save('convolution_animation.gif', writer='pillow', fps=fps)

plt.close()
print("Анимация сохранена как 'convolution_animation.gif'")