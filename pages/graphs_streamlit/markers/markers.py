import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def show_markers():
    
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

    