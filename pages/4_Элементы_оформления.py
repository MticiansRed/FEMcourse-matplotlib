import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Заголовок приложения
st.title("Элементы оформления в Matplotlib")

# Основная информация (отображается по умолчанию)
if "section" not in st.session_state:
    st.session_state.section = "Основная информация"

# Боковая панель для навигации
section = st.sidebar.radio(
    "Разделы",  
    [
        "Основная информация",
        "Оси",
        "Линии",
        "Маркеры",
        "Легенда",
        "Заголовок",
        "Метки осей",
        "Сетка",
        "Текстовые аннотации",
        "Цветовая палитра",
    ],
    index=0,  
    label_visibility="collapsed",
)

# Обновляем состояние приложения
if section != st.session_state.section:
    st.session_state.section = section

# Основная часть приложения
if st.session_state.section == "Основная информация":
    st.markdown("""
    **Matplotlib** предоставляет множество инструментов для настройки внешнего вида графиков. С помощью этой библиотеки можно настроить следующие параметры отображения:
    - **Оси**: область, где строится график.
    - **Линии**: линии на графике (например, линии графиков, сетки).
    - **Маркеры**: точки на графике (например, кружки, квадраты, треугольники).
    - **Легенда**: объяснение элементов графика.
    - **Заголовок**: заголовок графика.
    - **Метки осей**: названия осей X и Y.
    - **Сетка**: линии сетки на графике.
    - **Текстовые аннотации**: текстовые пояснения на графике.
    - **Цветовая палитра**: цветовые схемы для градиентов.
    """)

elif st.session_state.section == "Оси":
 
    # Пример для осей (Axes)
    st.markdown("#### Оси")
    st.markdown("""
    **Описание аргументов:**
    - `fig, ax = plt.subplots()`: создает фигуру (`fig`) и оси (`ax`), на которых строится график.
    - `ax.plot(x, y)`: рисует график по данным `x` и `y`.
    - `ax.set_title("Заголовок")`: устанавливает заголовок графика.
    """)
    st.markdown("Пример использования в Python:")
    st.code("""
    fig, ax = plt.subplots()
    ax.plot([0, 1, 2, 3], [0, 1, 4, 9])
    ax.set_title("Пример осей")
    plt.show()
    """)
    fig, ax = plt.subplots()
    ax.plot([0, 1, 2, 3], [0, 1, 4, 9])
    ax.set_title("Пример осей")
    st.pyplot(fig)

elif st.session_state.section == "Линии":

    # Пример для линий (Line)
    st.markdown("#### Линии")
    st.markdown("""
    **Описание аргументов:**
    - `linestyle`: стиль линии (например, `"-"` — сплошная, `"--"` — пунктирная, `"-."` — штрих-пунктирная, `":"` — точечная).
    - `color`: цвет линии (например, `"red"`, `"blue"`, `"green"` или HEX-код).
    - `label`: метка для легенды.
    """)
    st.markdown("Пример использования в Python:")
    st.code("""
    fig, ax = plt.subplots()
    ax.plot([0, 1, 2, 3], [0, 1, 4, 9], linestyle="--", color="red", label="Линия")
    ax.legend()
    ax.set_title("Пример линий")
    plt.show()
    """)
    fig, ax = plt.subplots()
    ax.plot([0, 1, 2, 3], [0, 1, 4, 9], linestyle="--", color="red", label="Линия")
    ax.legend()
    ax.set_title("Пример линий")
    st.pyplot(fig)

elif st.session_state.section == "Маркеры":

    # Пример для маркеров (Markers)
    st.markdown("#### Маркеры")
    st.markdown("""
    **Описание аргументов:**
    - `marker`: стиль маркера (например, `"o"` — кружки, `"s"` — квадраты, `"^"` — треугольники).
    - `linestyle`: стиль линии (если не нужен, используйте `""`).
    - `label`: метка для легенды.
    """)
    st.markdown("Пример использования в Python:")
    st.code("""
    fig, ax = plt.subplots()
    ax.plot([0, 1, 2, 3], [0, 1, 4, 9], marker="o", linestyle="", label="Маркеры")
    ax.legend()
    ax.set_title("Пример маркеров")
    plt.show()
    """)
    fig, ax = plt.subplots()
    ax.plot([0, 1, 2, 3], [0, 1, 4, 9], marker="o", linestyle="", label="Маркеры")
    ax.legend()
    ax.set_title("Пример маркеров")
    st.pyplot(fig)

elif st.session_state.section == "Легенда":

    # Пример для легенды (Legend)
    st.markdown("#### Легенда")
    st.markdown("""
    **Описание аргументов:**
    - `label`: метка для каждого графика.
    - `loc`: расположение легенды (например, `"upper right"`, `"lower left"`).
    - `title`: заголовок легенды.
    """)
    st.markdown("Пример использования в Python:")
    st.code("""
    fig, ax = plt.subplots()
    ax.plot([0, 1, 2, 3], [0, 1, 4, 9], label="График 1")
    ax.plot([0, 1, 2, 3], [0, 2, 5, 10], label="График 2")
    ax.legend(loc="upper left", title="Легенда")
    ax.set_title("Пример легенды")
    plt.show()
    """)
    fig, ax = plt.subplots()
    ax.plot([0, 1, 2, 3], [0, 1, 4, 9], label="График 1")
    ax.plot([0, 1, 2, 3], [0, 2, 5, 10], label="График 2")
    ax.legend(loc="upper left", title="Легенда")
    ax.set_title("Пример легенды")
    st.pyplot(fig)

elif st.session_state.section == "Заголовок":

    # Пример для заголовка (Title)
    st.markdown("#### Заголовок")
    st.markdown("""
    **Описание аргументов:**
    - `ax.set_title("Заголовок")`: устанавливает заголовок графика.
    """)
    st.markdown("Пример использования в Python:")
    st.code("""
    fig, ax = plt.subplots()
    ax.plot([0, 1, 2, 3], [0, 1, 4, 9])
    ax.set_title("Пример заголовка")
    plt.show()
    """)
    fig, ax = plt.subplots()
    ax.plot([0, 1, 2, 3], [0, 1, 4, 9])
    ax.set_title("Пример заголовка")
    st.pyplot(fig)

elif st.session_state.section == "Метки осей":

    # Пример для меток осей (Labels)
    st.markdown("#### Метки осей")
    st.markdown("""
    **Описание аргументов:**
    - `ax.set_xlabel("Ось X")`: устанавливает метку для оси X.
    - `ax.set_ylabel("Ось Y")`: Устанавливает метку для оси Y.
    """)
    st.markdown("Пример использования в Python:")
    st.code("""
    fig, ax = plt.subplots()
    ax.plot([0, 1, 2, 3], [0, 1, 4, 9])
    ax.set_xlabel("Ось X")
    ax.set_ylabel("Ось Y")
    ax.set_title("Пример меток осей")
    plt.show()
    """)
    fig, ax = plt.subplots()
    ax.plot([0, 1, 2, 3], [0, 1, 4, 9])
    ax.set_xlabel("Ось X")
    ax.set_ylabel("Ось Y")
    ax.set_title("Пример меток осей")
    st.pyplot(fig)

elif st.session_state.section == "Сетка":

    # Пример для сетки (Grid)
    st.markdown("#### Сетка")
    st.markdown("""
    **Описание аргументов:**
    - `ax.grid(True)`: включает сетку.
    - `linestyle`: стиль линий сетки (например, `"--"`, `":"`).
    - `alpha`: прозрачность сетки (от 0 до 1).
    """)
    st.markdown("Пример использования в Python:")
    st.code("""
    fig, ax = plt.subplots()
    ax.plot([0, 1, 2, 3], [0, 1, 4, 9])
    ax.grid(True, linestyle="--", alpha=0.5)
    ax.set_title("Пример сетки")
    plt.show()
    """)
    fig, ax = plt.subplots()
    ax.plot([0, 1, 2, 3], [0, 1, 4, 9])
    ax.grid(True, linestyle="--", alpha=0.5)
    ax.set_title("Пример сетки")
    st.pyplot(fig)

elif st.session_state.section == "Текстовые аннотации":

    # Пример для текстовых аннотаций (Annotations)
    st.markdown("#### Текстовые аннотации")
    st.markdown("""
    **Описание аргументов:**
    - `ax.annotate("Текст", xy=(x, y), xytext=(x_text, y_text))`: добавляет аннотацию.
    - `arrowprops`: настройки стрелки (например, `dict(facecolor="black", shrink=0.05)`).
    """)
    st.markdown("Пример использования в Python:")
    st.code("""
    fig, ax = plt.subplots()
    ax.plot([0, 1, 2, 3], [0, 1, 4, 9])
    ax.annotate("Максимум", xy=(2, 4), xytext=(1, 6),
                arrowprops=dict(facecolor="black", shrink=0.05))
    ax.set_title("Пример аннотации")
    plt.show()
    """)
    fig, ax = plt.subplots()
    ax.plot([0, 1, 2, 3], [0, 1, 4, 9])
    ax.annotate("Максимум", xy=(2, 4), xytext=(1, 6),
                arrowprops=dict(facecolor="black", shrink=0.05))
    ax.set_title("Пример аннотации")
    st.pyplot(fig)

elif st.session_state.section == "Цветовая палитра":

    # Пример для цветовой палитры (Colormap)
    st.markdown("#### Цветовая палитра")
    st.markdown("""
    **Описание аргументов:**
    - `cmap = plt.get_cmap("название")`: получает цветовую палитру (например, `"viridis"`, `"plasma"`).
    - `color=cmap(i / N)`: применяет цвет из палитры к элементу.
    """)
    st.markdown("Пример использования в Python:")
    st.code("""
    fig, ax = plt.subplots()
    cmap = plt.get_cmap("viridis")
    for i in range(10):
        ax.plot([0, 1, 2, 3], [i, i + 1, i + 2, i + 3], color=cmap(i / 10))
    ax.set_title("Пример цветовой палитры")
    plt.show()
    """)
    fig, ax = plt.subplots()
    cmap = plt.get_cmap("viridis")
    for i in range(10):
        ax.plot([0, 1, 2, 3], [i, i + 1, i + 2, i + 3], color=cmap(i / 10))
    ax.set_title("Пример цветовой палитры")
    st.pyplot(fig)

