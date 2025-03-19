import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def show_legend():
    
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

    