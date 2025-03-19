import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def show_labels():
    
    # Пример для меток осей (Labels)
    st.markdown("#### Метки осей")
    st.markdown("""
    **Описание аргументов:**
    - `ax.set_xlabel("Ось X")`: устанавливает метку для оси X.
    - `ax.set_ylabel("Ось Y")`: устанавливает метку для оси Y.
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

    