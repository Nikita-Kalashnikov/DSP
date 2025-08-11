# Описание библиотеки bokeh. Библиотека используется для 2d графиков.
# Эта библиотека понравилась мне тем, что графики можно динамически изменять. Приближать рассматривая интересующие участоки графиков.
# https://docs.bokeh.org/en/latest/docs/first_steps/installation.html
# https://habr.com/ru/companies/otus/articles/755358/

# Здесь мы импортируем figure для создания графической фигуры, output_file для указания 
# имени файла для сохранения графика и show для отображения графика в браузере.
from bokeh.plotting import figure, output_file, show

# from bokeh.plotting import figure, show
# from bokeh.io import output_notebook
from bokeh.layouts import column

import numpy as np

# from bokeh.models import Range1d

# Активируем вывод графиков в ноутбук
# output_notebook()



# Создание графической фигуры
p = figure(title='Пример линейного графика', x_axis_label='X-ось', y_axis_label='Y-ось')

# Данные для графика
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

# Добавление линии на график
p.line(x, y, legend_label='Линия', line_width=2)

# Отображение графика
output_file('линейный_график.html')
show(p)


from bokeh.plotting import figure
from bokeh.io import show, output_notebook
import numpy as np

# Активируем режим отображения для VS Code
output_notebook(notebook_type='vscode')  # Ключевая настройка!

# Создание графической фигуры с увеличенными размерами
p = figure(
    title='График в VS Code',
    x_axis_label='X-ось',
    y_axis_label='Y-ось',
    width=900,  # Важно для правильного отображения
    height=600,
    tools='pan,wheel_zoom,box_zoom,reset,save'  # Интерактивные инструменты
)

# Генерация данных
x = npsds.linspace(0, 4 * np.pi, 200)
y = np.sin(x)

# Добавление линий
p.line(x, y, legend_label='sin(x)', line_width=3, color='blue')
p.circle(x[::10], y[::10], size=8, color='red', alpha=0.5)

# Настройка легенды
p.legend.location = 'top_right'
p.legend.click_policy = 'hide'  # Клик скрывает элементы

# Отображение графика
show(p)