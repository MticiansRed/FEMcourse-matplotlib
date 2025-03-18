import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from PIL import Image
import numpy as np
import io

# Сайдбар для навигации
menu = st.sidebar.radio(
    '***',
    (
        "Краткая информация", 
        "Основные возможности",
        "Где используется?"
    )
)

# Блок 1: Общая информация
if menu == "Краткая информация":
    st.write("""
    ##### Краткая информация

    **Matplotlib** — это одна из самых популярных и мощных библиотек для визуализации данных на языке Python. Она была создана Джоном Хантером (John D. Hunter) в 2003 году и с тех пор активно развивается. Matplotlib предоставляет широкие возможности для создания статических, анимированных и интерактивных графиков.
    """)

    # Добавляем изображение с логотипом Matplotlib
    image = Image.open("pages/data/s1.png")  # Убедитесь, что путь к изображению правильный
    st.image(image, caption="Логотип Matplotlib", width=300)

# Блок 2: Основные возможности
if menu == "Основные возможности":
    st.write("""
    ### Основные возможности Matplotlib:
    **Разнообразие типов графиков**: Matplotlib поддерживает множество типов графиков, включая:
    - Линейные графики (`plot`)
    - Столбчатые диаграммы (`bar`)
    - Круговые диаграммы (`pie`)
    - Гистограммы (`hist`)
    - Точечные диаграммы (`scatter`)
    - 3D-графики (`plot_surface`, `scatter3D`)
    - Контурные графики (`contour`)
    - И многое другое.
    """)

    # Выбор типа графика через выпадающий список
    graph_type = st.selectbox(
        "Выберите тип графика:",
        ["Линейный график", "Столбчатая диаграмма", "Круговая диаграмма", "Гистограмма", "Точечная диаграмма"]
    )

    # Создаём данные
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    # Создаём график в зависимости от выбора пользователя
    fig, ax = plt.subplots()

    if graph_type == "Линейный график":
        ax.plot(x, y, label="sin(x)", color="blue", linestyle="-", linewidth=2)
        ax.set_title("Линейный график")
    elif graph_type == "Столбчатая диаграмма":
        ax.bar(x[:10], y[:10], color="green")
        ax.set_title("Столбчатая диаграмма")
    elif graph_type == "Круговая диаграмма":
        sizes = [15, 30, 45, 10]
        ax.pie(sizes, labels=["A", "B", "C", "D"], autopct="%1.1f%%", startangle=90)
        ax.set_title("Круговая диаграмма")
    elif graph_type == "Гистограмма":
        data = np.random.normal(0, 1, 1000)
        ax.hist(data, bins=30, color="purple")
        ax.set_title("Гистограмма")
    elif graph_type == "Точечная диаграмма":
        ax.scatter(x, y, color="red")
        ax.set_title("Точечная диаграмма")

    ax.set_xlabel("Ось X")
    ax.set_ylabel("Ось Y")
    ax.legend()
    ax.grid(True)

    # Отображаем график в Streamlit
    st.pyplot(fig)

    st.write("""
    - **Гибкость настройки**: Matplotlib позволяет настраивать практически каждый аспект графика:
      - Цвета, стили линий и маркеров.
      - Шрифты, заголовки, подписи осей.
      - Легенды, аннотации, сетки.
      - Размеры и пропорции графиков.

    - **Интеграция с другими библиотеками**: Matplotlib легко интегрируется с такими библиотеками, как:
      - **NumPy** для работы с массивами данных.
      - **Pandas** для визуализации данных из DataFrame.
      - **SciPy** для научных вычислений.
      - **Jupyter Notebook** для интерактивной работы.

    - **Экспорт графиков**: Matplotlib позволяет сохранять графики в различных форматах, таких как PNG, PDF, SVG, EPS и другие.

    - **Поддержка анимаций и интерактивности**: С помощью дополнительных модулей, таких как `matplotlib.animation`, можно создавать анимированные графики. Также Matplotlib интегрируется с библиотеками для создания интерактивных графиков, например, `mpld3`.
    """)
    


# Блок 3: Где используется?
if menu == "Где используется?":
    st.write("""
    ### Где используется Matplotlib?
    Matplotlib активно применяется в:
    - Научных исследованиях для визуализации данных.
    - Анализе данных и машинном обучении.
    - Образовании для обучения основам визуализации.
    - Создании отчётов и презентаций.
    """)
    # Выпадающий список для выбора области применения
    use_case = st.selectbox(
        "Выберите область применения:",
        [
            "Научные исследования",
            "Анализ данных и машинное обучение",
            "Образование",
            "Создание отчётов и презентаций"
        ]
    )

    # Интерактив в зависимости от выбора
    if use_case == "Научные исследования":
        st.write("""
        #### Научные исследования
        В научных исследованиях Matplotlib используется для визуализации экспериментальных данных, построения графиков зависимостей и анализа результатов. Например, с его помощью можно:
        - Построить график зависимости одной величины от другой.
        - Визуализировать распределение данных.
        - Создать 3D-графики для анализа сложных данных.
        """)
        # Пример графика для научных исследований
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        fig, ax = plt.subplots()
        ax.plot(x, y, label="sin(x)", color="blue")
        ax.set_title("Пример графика для научных исследований")
        ax.set_xlabel("Ось X")
        ax.set_ylabel("Ось Y")
        ax.legend()
        ax.grid(True)
        st.pyplot(fig)

    elif use_case == "Анализ данных и машинное обучение":
        st.write("""
        #### Анализ данных и машинное обучение
        В анализе данных и машинном обучении Matplotlib помогает визуализировать данные, чтобы лучше понять их структуру и закономерности. Например:
        - Построение гистограмм для анализа распределения данных.
        - Визуализация корреляций между переменными.
        - Отображение результатов кластеризации или классификации.
        """)
        # Пример графика для анализа данных
        data = np.random.normal(0, 1, 1000)
        fig, ax = plt.subplots()
        ax.hist(data, bins=30, color="green")
        ax.set_title("Гистограмма для анализа данных")
        ax.set_xlabel("Значения")
        ax.set_ylabel("Частота")
        st.pyplot(fig)

    elif use_case == "Образование":
        st.write("""
        #### Образование
        Matplotlib широко используется в образовательных целях для обучения основам визуализации данных. С его помощью студенты могут:
        - Изучать основы построения графиков.
        - Визуализировать математические функции.
        - Понимать, как работают различные типы графиков.
        """)
        # Пример графика для образования
        x = np.linspace(-10, 10, 100)
        y = np.sin(x) / x
        fig, ax = plt.subplots()
        ax.plot(x, y, label="sin(x)/x", color="red")
        ax.set_title("Пример графика для образования")
        ax.set_xlabel("Ось X")
        ax.set_ylabel("Ось Y")
        ax.legend()
        ax.grid(True)
        st.pyplot(fig)

    elif use_case == "Создание отчётов и презентаций":
        st.write("""
        #### Создание отчётов и презентаций
        Matplotlib позволяет создавать профессиональные графики для включения в отчёты, презентации и публикации. Например:
        - Построение графиков для визуализации бизнес-метрик.
        - Создание диаграмм для презентаций.
        - Экспорт графиков в высококачественные форматы (PDF, SVG).
        """)
        # Пример графика для отчётов
        labels = ["A", "B", "C", "D"]
        sizes = [15, 30, 45, 10]
        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
        ax.set_title("Круговая диаграмма для отчётов")
        st.pyplot(fig)
