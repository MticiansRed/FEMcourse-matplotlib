import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Создаем боковое меню
menu = st.sidebar.radio(
    'Меню',
    (
        "Одномерные графики",
        "Круговая диаграмма",
        "Гистограмма",
        "Boxplot (Ящик с усами)"
    )
)

if menu == "Одномерные графики":
    st.markdown("""
    ### Одномерные графики
    Теперь, когда мы познакомились с основными возможностями Matplotlib, давайте сосредоточимся на **одномерных графиках**. Эти графики — мощный инструмент для анализа и визуализации данных, которые зависят от одного измерения (например, времени, индекса или категории). В библиотеке существует множество типов одномерных графиков, но мы рассмотрим только основные из них.
    """)

# Раздел "Круговая диаграмма"
if menu == "Круговая диаграмма":
    st.markdown("""
    ### Круговая диаграмма
    Круговая диаграмма используется для визуализации пропорций или процентного соотношения частей целого.
        
    """)

    def plot_pie_chart(sizes, labels, colors, figsize):
        fig, ax = plt.subplots(figsize=figsize)
        ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')  # Чтобы диаграмма была круглой
        st.pyplot(fig)

    def pie_chart_page():
        sizes_input = st.text_input("Введите значения для каждой категории через запятую", value="30, 20, 50")
        labels_input = st.text_input("Введите названия категорий через запятую", value="Категория A, Категория B, Категория C")

        sizes = list(map(float, sizes_input.split(',')))
        labels = labels_input.split(',')

        # Настройки диаграммы
        st.markdown("### Настройки круговой диаграммы")
        colors = st.multiselect(
            "Выберите цвета для категорий",
            ["red", "blue", "green", "yellow", "purple", "orange"],
            default=["red", "blue", "green"]
        )
        figsize = st.slider("Размер графика", 5, 15, 8)

        if st.button("Построить круговую диаграмму"):
            if len(colors) < len(sizes):
                st.warning("Количество цветов должно быть не меньше количества категорий.")
            else:
                plot_pie_chart(sizes, labels, colors, (figsize, figsize))

    pie_chart_page()

    # Кнопка "Показать код"
    def showcode_pie():
        code = '''
        def plot_pie_chart(sizes, labels, colors, figsize):
            fig, ax = plt.subplots(figsize=figsize)
            ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
            ax.axis('equal')
            st.pyplot(fig)
        '''
        st.code(code, language="python")

    st.markdown("---")
    if st.button("Показать код для круговой диаграммы"):
        showcode_pie()

# Раздел "Гистограмма"
if menu == "Гистограмма":
    st.markdown("""
    ### Гистограмма
    Гистограмма показывает распределение одной переменной, разбивая данные на интервалы (бины) и отображая частоту попадания данных в каждый интервал.
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

    # Кнопка "Показать код"
    def showcode_hist():
        code = '''
        def plot_histogram(data, bins, bar_color, edge_color, show_grid, figsize):
            fig, ax = plt.subplots(figsize=figsize)
            ax.hist(data, bins=bins, color=bar_color, edgecolor=edge_color)
            ax.set_xlabel("Значения")
            ax.set_ylabel("Частота")
            if show_grid:
                ax.grid(True)
            st.pyplot(fig)
        '''
        st.code(code, language="python")

    st.markdown("---")
    if st.button("Показать код для гистограммы"):
        showcode_hist()

# Раздел "Boxplot (Ящик с усами)"
if menu == "Boxplot (Ящик с усами)":
    st.markdown("""
    ### Boxplot (Ящик с усами)
    Boxplot визуализирует статистику одной переменной, включая медиану, квантили, выбросы и разброс данных.
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

    # Кнопка "Показать код"
    def showcode_boxplot():
        code = '''
        def plot_boxplot(data, figsize):
            fig, ax = plt.subplots(figsize=figsize)
            ax.boxplot(data)
            ax.set_ylabel("Значения")
            st.pyplot(fig)
        '''
        st.code(code, language="python")

    st.markdown("---")
    if st.button("Показать код для Boxplot"):
        showcode_boxplot()
