import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def show_annotations():
    
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

    