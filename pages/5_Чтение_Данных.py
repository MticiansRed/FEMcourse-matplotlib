import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


with st.sidebar:
    type = st.radio(
        "Выберите раздел",
        ["О чтении данных", "Чтение из стороннего файла", "Чтение сгенерированных данных"],
    )

# Заголовок приложения
st.title("Чтение расчётных данных")

if type == "О чтении данных":


	# Описание тематики
	st.write("""
	### О чём эта часть?
	Мы рассмотрим, как:
	- Читать данные из различных источников (CSV, Excel, базы данных).
	- Обрабатывать и анализировать данные с помощью **Pandas** и **NumPy**.
	- Строить графики и визуализировать результаты расчётов с помощью **Matplotlib**.


	### Что вы узнаете?
	- Как загружать данные из файлов.
	- Как обрабатывать данные для построения графиков.
	""")	


if type == "Чтение из стороннего файла":
	
	# Раздел: Чтение данных
	st.write("""
	Для чтения данных можно использовать библиотеку `pandas`. Она поддерживает множество форматов, таких как CSV, Excel, JSON и другие.
	""")

	# Пример кода для чтения данных
	st.header("Чтение данных из CSV")
	st.code("""
	import pandas as pd

	# Чтение данных из CSV-файла
	data = pd.read_csv('data.csv') 
	# pd.read_excel('data.xls') - для Excel
	# pd.read_json('data.json') - для JSON
	# pd.read_xml('data.xml') - для XML
	# и т.д. (см. https://pandas.pydata.org/docs/reference/io.html)

	""", language='python')

	st.write("""
<details>
<summary><b>Параметры функции pd.read_csv</b></summary>
<b>filepath_or_buffer</b>: <i>str, path object, or file-like object</i><br>
Путь к файлу или объект с данными для чтения.<br>


<details>
<summary><b>sep</b>: <i>str, optional, по умолчанию: ','</i></summary>
Разделитель столбцов в файле. Например, ',' для CSV или '\t' для TSV.<br>
</details>
<details>
<summary><b>delimiter</b>: <i>str, optional</i></summary>
Альтернативное имя для параметра `sep`. Используется для указания разделителя.<br>
</details>
<details>
<summary><b>header</b>: <i>int, list of int, optional, по умолчанию: 'infer'</i></summary>
Номер строки, которая будет использоваться как заголовок столбцов. Если 'infer', заголовок определяется автоматически.<br>
</details>
<details>
<summary><b>names</b>: <i>array-like, optional</i></summary>
Список имен для столбцов. Если файл не содержит заголовка, этот параметр задает имена столбцов.<br>
</details>
<details>
<summary><b>index_col</b>: <i>int, str, sequence of int/str, or False, optional</i></summary>
Столбец (или столбцы), который будет использоваться как индекс строк.<br>
</details>
<details>
<summary><b>usecols</b>: <i>list-like или callable, optional</i></summary>
Список столбцов для чтения. Можно указать номера столбцов или их имена.<br>
</details>
<details>
<summary><b>dtype</b>: <i>dict, optional</i></summary>
Словарь, указывающий типы данных для конкретных столбцов.<br>
</details>
<details>
<summary><b>engine</b>: <i>{'c', 'python'}, optional</i></summary>
Движок для парсинга файла. 'c' — быстрее, 'python' — более гибкий.<br>
</details>
<details>
<summary><b>skiprows</b>: <i>list-like, int, optional</i></summary>
Количество строк или список строк, которые нужно пропустить в начале файла.<br>
</details>
<details>
<summary><b>skipfooter</b>: <i>int, optional</i></summary>
Количество строк, которые нужно пропустить в конце файла.<br>
</details>
<details>
<summary><b>nrows</b>: <i>int, optional</i></summary>
Количество строк для чтения из файла.<br>
</details>
<details>
<summary><b>na_values</b>: <i>scalar, str, list-like, или dict, optional</i></summary>
Значения, которые будут интерпретироваться как пропущенные (NaN).<br>
</details>
<details>
<summary><b>keep_default_na</b>: <i>bool, optional, по умолчанию: True</i></summary>
Определяет, использовать ли стандартные значения для пропущенных данных.<br>
</details>
<details>
<summary><b>encoding</b>: <i>str, optional</i></summary>
Кодировка файла (например, 'utf-8', 'latin1').<br>
</details>
<details>
<summary><b>parse_dates</b>: <i>bool, list of int или str, optional</i></summary>
Определяет, нужно ли парсить указанные столбцы как даты.<br>
</details>
<details>
<summary><b>thousands</b>: <i>str, optional</i></summary>
Разделитель тысяч в числах (например, ',' или '.').<br>
</details>
<details>
<summary><b>decimal</b>: <i>str, optional, по умолчанию: '.'</i></summary>
Разделитель десятичных знаков в числах.<br>
</details>
<details>
<summary><b>comment</b>: <i>str, optional</i></summary>
Символ, обозначающий начало комментария в строке.<br>
</details>
<details>
<summary><b>skip_blank_lines</b>: <i>bool, optional, по умолчанию: True</i></summary>
Пропускать ли пустые строки в файле.<br>
</details>
<details>
<summary><b>low_memory</b>: <i>bool, optional</i></summary>
Режим чтения файла с минимальным использованием памяти. Может повлиять на производительность.<br>
</details>

<details>
<summary><b>memory_map</b>: <i>bool, optional</i></summary>
Использовать ли отображение файла в памяти для чтения.<br>
</details>

<details>
<summary><b>float_precision</b>: <i>str, optional</i></summary>
Точность для чисел с плавающей точкой (например, 'high', 'round_trip').<br>
</details>
</details><br>
""", unsafe_allow_html=True)

	enter_toggle = st.toggle("Загрузить свой CSV-файл")
	if enter_toggle:
	    # Загрузка файла пользователем
		uploaded_file = st.file_uploader("Загрузите CSV-файл", type=["csv"])
	else:
		uploaded_file = "pages/data/test.csv"

	if uploaded_file is not None:
	    # Чтение данных из загруженного файла
	    
		data = pd.read_csv(uploaded_file)
		st.write("Первые 5 строк данных:")
		st.write(data.head())

		# Раздел: Визуализация данных
		st.header("Визуализация данных")
		st.write("""
		После загрузки данных можно построить график с помощью Matplotlib. Например, линейный график.
		""")

		# Выбор столбцов для построения графика
		columns = data.columns.tolist()
		x_axis = st.selectbox("Выберите столбец для оси X", columns, index=0)
		y_axis = st.selectbox("Выберите столбец для оси Y", columns, index=1)

		# Построение графика
		if st.button("Построить график"):
			fig, ax = plt.subplots()
			ax.plot(data[x_axis], data[y_axis], label=f"{y_axis} относительно {x_axis}")
			ax.set_xlabel(x_axis)
			ax.set_ylabel(y_axis)
			ax.set_title(f"График {y_axis} относительно {x_axis}")
			ax.legend()
			ax.grid(True)

			# Отображение графика в Streamlit
			st.pyplot(fig)

if type == "Чтение сгенерированных данных":

	with st.sidebar:
		type1 = st.radio("Библиотека", ["NumPy", "Pandas"],)
	if type1 == "NumPy":
		# Раздел: Создание данных с помощью NumPy
		st.header("Создание данных с помощью NumPy")
		st.write("""
		NumPy часто используется для генерации данных.
		Рассмотрим пример создания массива данных и визуализации этих данных с помощью NumPy.
		""")

		# Пример кода для создания данных с помощью NumPy
		st.code("""
		import numpy as np

		# Создание массива данных
		x = np.linspace(0, 10, 100)  # 100 точек от 0 до 10
		y = np.sin(x)
		""", language='python')
		enter_toggle = st.toggle("Задать свой диапазон по x")
		if enter_toggle:
			x_min = st.text_area("Введите минимальный x", value="0", height=68)
			x_max = st.text_area("Введите максимальный x", value="10", height=68)
			step = st.text_area("Введите шаг по x", value="100", height=68)
			x = np.linspace(int(x_min), int(x_max), int(step))
		else:
			x = np.linspace(0, 10, 100)
		y = np.sin(x)
		
		# Отображение данных
		st.write("Сгенерированные данные (первые 5 точек):")
		data = pd.DataFrame({"x": x[:5], "y": y[:5]})
		st.write(data)

		st.write("""
		После создания данных можно построить график с помощью Matplotlib. Например, линейный график.
		""")
		
		st.code("""
		fig, ax = plt.subplots()
		ax.plot(x, y, label="sin(x)")
		""", language='python')
		# Построение графика
		fig, ax = plt.subplots()
		ax.plot(x, y, label="sin(x)")
		ax.set_xlabel("x")
		ax.set_ylabel("y")
		ax.set_title("График синуса")
		ax.legend()
		ax.grid(True)

		# Отображение графика в Streamlit
		st.pyplot(fig)
	if type1 == "Pandas":
		st.write("""
		Pandas — это библиотека для работы с таблицами данных. Она часто используется для анализа и обработки данных.
		Рассмотрим пример создания DataFrame с помощью Pandas.
		""")

		# Пример кода для создания DataFrame
		st.code("""
		import pandas as pd

		# Создание DataFrame
		data = pd.DataFrame({
		"x": np.linspace(0, 10, 100),
		"y": np.cos(x)
		})
		""", language='python')
		enter_toggle = st.toggle("Задать свой диапазон по x")
		if enter_toggle:
			x_min = st.text_area("Введите минимальный x", value="0", height=68)
			x_max = st.text_area("Введите максимальный x", value="10", height=68)
			step = st.text_area("Введите шаг по x", value="100", height=68)
			x = np.linspace(int(x_min), int(x_max), int(step))
		else:
			x = np.linspace(0, 10, 100)
		y = np.cos(x)
		# Создание DataFrame
		data = pd.DataFrame({"x": x, "y": y})

		# Отображение данных
		st.write("DataFrame (первые 5 строк):")
		st.write(data.head(5))
		st.write("""
		Данные из Pandas DataFrame можно легко визуализировать с помощью Matplotlib.
		""")
		st.code("""
		fig, ax = plt.subplots()
		ax.plot(data["x"], data["y"], label="cos(x)")
		""", language='python')
		# Построение графика из DataFrame
		fig, ax = plt.subplots()
		ax.plot(data["x"], data["y"], label="cos(x)")
		ax.set_xlabel("x")
		ax.set_ylabel("y")
		ax.set_title("График косинуса из DataFrame")
		ax.legend()
		ax.grid(True)

		# Отображение графика в Streamlit
		st.pyplot(fig)


