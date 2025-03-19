import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def show_title():
   
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

    