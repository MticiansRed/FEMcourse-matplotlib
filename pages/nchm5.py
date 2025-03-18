import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Создаем боковое меню
menu = st.sidebar.radio(
    'Меню',
    (
        "Одномерные графики",
        "Линейный график",
        "Гистограмма",
        "Boxplot (Ящик с усами)"
    )
)

if menu == "Одномерные графики":
    st.markdown("""
    ### Одномерные графики
    Теперь, когда мы познакомились с основными возможностями Matplotlib, давайте сосредоточимся на **одномерных графиках**. Эти графики — мощный инструмент для анализа и визуализации данных, которые зависят от одного измерения (например, времени, индекса или категории). В библиотеке существует множество типов одномерных графиков, но мы рассмотрим только основные из них.
    """)


if menu == "Линейный график":
    st.markdown("""
    ### Линейный график
    Линейный график отображает изменение одной переменной (например, y) по индексу или времени.
    - **Как использовать**: функция plt.plot().
    """)
    
    def plot_line_graph(y_values, line_color, line_style, line_width, show_legend, show_grid, figsize):
        x_values = np.arange(len(y_values))  # Индексы для оси X
        fig, ax = plt.subplots(figsize=figsize)
        ax.plot(x_values, y_values, label="y = f(x)", color=line_color, linestyle=line_style, linewidth=line_width)
        ax.set_xlabel("Индекс")
        ax.set_ylabel("Значение")

        if show_legend:
            ax.legend()

        if show_grid:
            ax.grid(True)

        st.pyplot(fig)

    def line_graph_page():
        y_input = st.text_input("Введите значения Y через запятую", value="1,4,9,16,25")
        y_values = list(map(float, y_input.split(',')))

        # Настройки графика
        st.markdown("### Настройки графика")
        line_color = st.color_picker("Выберите цвет линии", "#1f77b4")
        line_style = st.selectbox("Выберите стиль линии", ["-", "--", "-.", ":"])
        line_width = st.slider("Толщина линии", 1, 10, 2)
        show_legend = st.checkbox("Показать легенду", value=True)
        show_grid = st.checkbox("Показать сетку", value=True)
        figsize = st.slider("Размер графика", 5, 15, 10)

        if st.button("Построить график"):
            plot_line_graph(y_values, line_color, line_style, line_width, show_legend, show_grid, (figsize, figsize))

    line_graph_page()

# Раздел "Гистограмма"
if menu == "Гистограмма":
    st.markdown("""
    ### Гистограмма
    Гистограмма показывает распределение одной переменной, разбивая данные на интервалы (бины) и отображая частоту попадания данных в каждый интервал.
    - **Как использовать**: функция plt.hist().
    """)

    def plot_histogram(data, bins, bar_color, edge_color, show_grid, figsize):
        fig, ax = plt.subplots(figsize=figsize)
        ax.hist(data, bins=bins, color=bar_color, edgecolor=edge_color)
        ax.set_xlabel("Значения")
        ax.set_ylabel("Частота")

        if show_grid:
            ax.grid(True)

        st.pyplot(fig)

    def histogram_page():
        num_data = st.number_input("Количество данных:", min_value=10, max_value=1000, value=100)
        num_bins = st.number_input("Количество интервалов:", min_value=5, max_value=50, value=10)

        # Настройки гистограммы
        st.markdown("### Настройки гистограммы")
        bar_color = st.color_picker("Выберите цвет столбцов", "#1f77b4")
        edge_color = st.color_picker("Выберите цвет границ столбцов", "#000000")
        show_grid = st.checkbox("Показать сетку", value=True)
        figsize = st.slider("Размер графика", 5, 15, 10)

        if st.button("Сгенерировать данные и построить гистограмму"):
            data = np.random.normal(0, 1, num_data)  # Генерация случайных данных
            plot_histogram(data, num_bins, bar_color, edge_color, show_grid, (figsize, figsize))

    histogram_page()

# Раздел "Boxplot (Ящик с усами)"
if menu == "Boxplot (Ящик с усами)":
    st.markdown("""
    ### Boxplot (Ящик с усами)
    Boxplot визуализирует статистику одной переменной, включая медиану, квантили, выбросы и разброс данных.
    - **Как использовать**: функция plt.boxplot().
    """)

    def plot_boxplot(data, figsize):
        fig, ax = plt.subplots(figsize=figsize)
        ax.boxplot(data)
        ax.set_ylabel("Значения")
        st.pyplot(fig)

    def boxplot_page():
        num_data = st.number_input("Количество данных:", min_value=10, max_value=1000, value=100)
        figsize = st.slider("Размер графика", 5, 15, 10)

        if st.button("Сгенерировать данные и построить Boxplot"):
            data = np.random.normal(0, 1, num_data)  # Генерация случайных данных
            plot_boxplot(data, (figsize, figsize))

    boxplot_page()
