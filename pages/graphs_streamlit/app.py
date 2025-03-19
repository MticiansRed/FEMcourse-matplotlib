import streamlit as st

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
    from axis.axis import show_axis
    show_axis()
elif st.session_state.section == "Линии":
    from lines.lines import show_lines
    show_lines()
elif st.session_state.section == "Маркеры":
    from markers.markers import show_markers
    show_markers()
elif st.session_state.section == "Легенда":
    from legend.legend import show_legend
    show_legend()
elif st.session_state.section == "Заголовок":
    from title.title import show_title
    show_title()
elif st.session_state.section == "Метки осей":
    from labels.labels import show_labels
    show_labels()
elif st.session_state.section == "Сетка":
    from grid.grid import show_grid
    show_grid()
elif st.session_state.section == "Текстовые аннотации":
    from annotations.annotations import show_annotations
    show_annotations()
elif st.session_state.section == "Цветовая палитра":
    from colormap.colormap import show_colormap
    show_colormap()