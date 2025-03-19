import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def show_grid():
    
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

    