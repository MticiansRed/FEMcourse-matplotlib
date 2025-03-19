import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def show_axis():
    
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

    