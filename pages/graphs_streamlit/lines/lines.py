import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def show_lines():
    
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

    