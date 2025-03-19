import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def show_colormap():
    
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