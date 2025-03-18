import streamlit as st
import subprocess
import sys

# Сайдбар для навигации
menu = st.sidebar.radio(
    "Выберите операционную систему или среду:",
    (
        "Windows",
        "Linux",
        "macOS"
    )
)

# Раздел: Установка на Windows
if menu == "Windows":
    st.header("Установка Matplotlib на Windows")
    st.write("""
    ### Шаг 1: Убедитесь, что Python установлен
    Проверьте, установлен ли Python, выполнив команду в командной строке:
    ```bash
    python --version
    ```
    Если Python не установлен, скачайте его с [официального сайта](https://www.python.org/).
    """)

    # Интерактив: Проверка версии Python
    if st.button("Проверить версию Python (Windows)"):
        result = subprocess.run([sys.executable, "--version"], capture_output=True, text=True)
        if result.returncode == 0:
            st.success(f"Установленная версия Python: {result.stdout}")
        else:
            st.error("Python не установлен или не настроен корректно.")

    st.write("""
    ### Шаг 2: Установите Matplotlib через pip
    Откройте командную строку и выполните команду:
    ```bash
    pip install matplotlib
    ```
    Если у вас несколько версий Python, используйте `pip3`:
    ```bash
    pip3 install matplotlib
    ```
    """)

    # Интерактив: Установка Matplotlib
    if st.button("Установить Matplotlib (Windows)"):
        result = subprocess.run([sys.executable, "-m", "pip", "install", "matplotlib"], capture_output=True, text=True)
        if result.returncode == 0:
            st.success("Matplotlib успешно установлен!")
        else:
            st.error("Ошибка при установке Matplotlib. Подробности:")
            st.code(result.stderr)

    st.write("""
    ### Шаг 3: Проверка установки Matplotlib
    После установки проверьте, что Matplotlib работает корректно. Для этого выполните следующий код:
    ```python
    import matplotlib.pyplot as plt
    plt.plot([1, 2, 3, 4])
    plt.show()
    ```
    Если график отображается, значит, Matplotlib установлен правильно.
    """)

    # Интерактив: Проверка работы Matplotlib
    if st.button("Проверить работу Matplotlib (Windows)"):
        try:
            import matplotlib.pyplot as plt
            fig, ax = plt.subplots()
            ax.plot([1, 2, 3, 4])
            ax.set_title("Проверка Matplotlib")
            ax.set_xlabel("Ось X")
            ax.set_ylabel("Ось Y")
            st.pyplot(fig)
            st.success("Matplotlib работает корректно!")
        except ImportError:
            st.error("Matplotlib не установлен или произошла ошибка при импорте.")

# Раздел: Установка на Linux
if menu == "Linux":
    st.header("Установка Matplotlib на Linux")
    st.write("""
    ### Шаг 1: Убедитесь, что Python установлен
    Проверьте, установлен ли Python, выполнив команду в терминале:
    ```bash
    python3 --version
    ```
    Если Python не установлен, установите его с помощью пакетного менеджера:
    ```bash
    sudo apt update
    sudo apt install python3
    ```
    """)

    # Интерактив: Проверка версии Python
    if st.button("Проверить версию Python (Linux)"):
        result = subprocess.run(["python3", "--version"], capture_output=True, text=True)
        if result.returncode == 0:
            st.success(f"Установленная версия Python: {result.stdout}")
        else:
            st.error("Python не установлен или не настроен корректно.")

    st.write("""
    ### Шаг 2: Установите Matplotlib через pip
    Установите Matplotlib с помощью pip:
    ```bash
    pip3 install matplotlib
    ```
    Если pip не установлен, установите его:
    ```bash
    sudo apt install python3-pip
    ```
    """)

    # Интерактив: Установка Matplotlib
    if st.button("Установить Matplotlib (Linux)"):
        result = subprocess.run(["pip3", "install", "matplotlib"], capture_output=True, text=True)
        if result.returncode == 0:
            st.success("Matplotlib успешно установлен!")
        else:
            st.error("Ошибка при установке Matplotlib. Подробности:")
            st.code(result.stderr)

    st.write("""
    ### Шаг 3: Проверка установки Matplotlib
    После установки проверьте, что Matplotlib работает корректно. Для этого выполните следующий код:
    ```python
    import matplotlib.pyplot as plt
    plt.plot([1, 2, 3, 4])
    plt.show()
    ```
    Если график отображается, значит, Matplotlib установлен правильно.
    """)

    # Интерактив: Проверка работы Matplotlib
    if st.button("Проверить работу Matplotlib (Linux)"):
        try:
            import matplotlib.pyplot as plt
            fig, ax = plt.subplots()
            ax.plot([1, 2, 3, 4])
            ax.set_title("Проверка Matplotlib")
            ax.set_xlabel("Ось X")
            ax.set_ylabel("Ось Y")
            st.pyplot(fig)
            st.success("Matplotlib работает корректно!")
        except ImportError:
            st.error("Matplotlib не установлен или произошла ошибка при импорте.")

# Раздел: Установка на macOS
if menu == "macOS":
    st.header("Установка Matplotlib на macOS")
    st.write("""
    ### Шаг 1: Убедитесь, что Python установлен
    Проверьте, установлен ли Python, выполнив команду в терминале:
    ```bash
    python3 --version
    ```
    Если Python не установлен, установите его с помощью Homebrew:
    ```bash
    brew install python
    ```
    Если Homebrew не установлен, установите его:
    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```
    """)

    # Интерактив: Проверка версии Python
    if st.button("Проверить версию Python (macOS)"):
        result = subprocess.run(["python3", "--version"], capture_output=True, text=True)
        if result.returncode == 0:
            st.success(f"Установленная версия Python: {result.stdout}")
        else:
            st.error("Python не установлен или не настроен корректно.")

    st.write("""
    ### Шаг 2: Установите Matplotlib через pip
    Установите Matplotlib с помощью pip:
    ```bash
    pip3 install matplotlib
    ```
    Если pip не установлен, установите его:
    ```bash
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python3 get-pip.py
    ```
    """)

    # Интерактив: Установка Matplotlib
    if st.button("Установить Matplotlib (macOS)"):
        result = subprocess.run(["pip3", "install", "matplotlib"], capture_output=True, text=True)
        if result.returncode == 0:
            st.success("Matplotlib успешно установлен!")
        else:
            st.error("Ошибка при установке Matplotlib. Подробности:")
            st.code(result.stderr)

    st.write("""
    ### Шаг 3: Проверка установки Matplotlib
    После установки проверьте, что Matplotlib работает корректно. Для этого выполните следующий код:
    ```python
    import matplotlib.pyplot as plt
    plt.plot([1, 2, 3, 4])
    plt.show()
    ```
    Если график отображается, значит, Matplotlib установлен правильно.
    """)

    # Интерактив: Проверка работы Matplotlib
    if st.button("Проверить работу Matplotlib (macOS)"):
        try:
            import matplotlib.pyplot as plt
            fig, ax = plt.subplots()
            ax.plot([1, 2, 3, 4])
            ax.set_title("Проверка Matplotlib")
            ax.set_xlabel("Ось X")
            ax.set_ylabel("Ось Y")
            st.pyplot(fig)
            st.success("Matplotlib работает корректно!")
        except ImportError:
            st.error("Matplotlib не установлен или произошла ошибка при импорте.")


