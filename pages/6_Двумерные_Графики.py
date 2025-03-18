import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import time


with st.sidebar:
    type = st.radio(
        "Выберите раздел",
        ["О двумерных графиках", "Линейный (Plot)", "Точечный (Scatter Plot)", "Барный (Bar Plot)", "Стержневой (Stem Plot)", "Заливка области между (Fill_between)", "Стековый (Stackplot)", "Ступенчатый (Stairs Plot)"],
    )

st.title("Двумерные графики в Matplotlib")

if type == "О двумерных графиках":
    # Общая информация
    st.header("Двумерные графики")
    st.markdown(
        """
        **Двумерные графики** позволяют визуализировать данные в двухмерном пространстве. Это полезный инструмент для:

        - Представления функций или данных, зависящих от одной переменной.
        - Помощь в выявлении закономерностей, трендов и корреляций между переменными.
        - Более глубокое понимание распределения данных.
        - Возможность выделить потенциальные выбросы или кластеры в данных.

        Примеры применения:
        - **Статистический анализ**: Визуализация многомерных данных для выявления корреляционных связей между переменными.
        - **Анализ данных**: Построение матриц рассеяния для оценки качества предсказаний моделей машинного обучения.
        - **Научные исследования**: Анализ влияния различных факторов на конечный результат эксперимента.
        - **Машинное обучение**: Оценка взаимодействия признаков при построении и анализе моделей классификации и регрессии.
        
        """
    )
    

if type == "Линейный (Plot)":

    multi = '''
#### График зависимости y от x.

**Описание**:
График Plot отображает двухмерную график зависимости y от x. Линейные графики полезны для отображения изменений данных во времени. 
Они помогают выявить тенденции и сравнить несколько наборов данных.

<details>
<summary><b>Где используется</b></summary>
1) <b>Визуализация данных:</b> Plot используется для создания графиков, которые помогают визуализировать данные. Например, построение линейных графиков изменения цен на акции или температуры за определенный период.<br>
2) <b>Анализ зависимостей:</b> Plot применяется для изучения взаимосвязей между переменными. Например, график зависимости расхода топлива от расстояния или корреляции между возрастом и доходом.<br>
3) <b>Сравнение данных:</b> Plot позволяет сравнивать различные наборы данных. Например, сравнение продаж разных продуктов за год или эффективности различных методов обучения.<br>
4) <b>Создание научных графиков:</b> широко используется в научных исследованиях для визуализации экспериментальных данных. Например, графики результатов физических экспериментов или биологических измерений.<br>

</details>
<br>


**Пример**: динамика продажи компании за последние 12 месяцев.
```
y = [100, 250, 180, 220, 300, 270, 240, 210, 190, 200, 230, 170]
```

<details>
<summary><b>Параметры для графика</b></summary>
<b>x</b>, <b>y</b>: <i>array-like</i> или <i>float</i><br>
Горизонтальные / вертикальные координаты точек данных. Значения x необязательны и по умолчанию равны range(len(y)). Обычно эти параметры представляют собой одномерные массивы. Они также могут быть скалярами или двумерными (в этом случае столбцы представляют собой отдельные наборы данных). Эти аргументы не могут быть переданы в качестве ключевых слов.<br><br>
<details>
<summary><b>fmt</b>: <i>str</i>, <i>optional</i></summary>
Строка формата, например, 'ro' для красных кругов. Полное описание формата см. в разделе Примечания для полного описания строк формата. Строки формата - это просто аббревиатура для быстрого задания основных свойств линии. Всем этим и многим другим можно также управляться с помощью аргументов ключевых слов. Этот аргумент не может быть передан как ключевое слово.<br>
</details>
<details>
<summary><b>data</b>: <i>indexable object</i>, <i>optional</i></summary>
Объект с помеченными данными. Если задано, укажите имена меток для построить график по x и y.
</details>
<details>
<summary><b>**kwargs</b>: <i>optional</i></summary>
Дополнительные параметры, которые могут быть переданы в функцию построения графика.<br>
</details>
</details>
	
    '''  
    st.markdown(multi, unsafe_allow_html=True)
    st.divider()
    graph_color = st.color_picker("Цвет графика", value="#31D115")
    
    text = '''
    x = ["Jan", "Feb", "March", "April", "May", "June", "July", "August", "Sep", "Oct", "Nov", "Dec",]
    y = [100, 250, 180, 220, 300, 270, 240, 210, 190, 200, 230, 170]

    fig, ax = plt.subplots()
    ax.plot(x, y)'''
    st.code(text)
    
    enter_toggle = st.toggle("Ввести свои значения по y")
    if enter_toggle:
        y_text = st.text_area("Введите массив для y (через запятую с пробелом)", value="100, 250, 180, 220, 300, 270, 240, 210, 190, 200, 230, 170", height=68)
        y_array = np.array(list(y_text.split(', ')), dtype=float)
        st.code("!!! В y можно вводить только числа.")

    # make data
    x = ["Jan", "Feb", "March", "April", "May", "June", "July", "August", "Sep", "Oct", "Nov", "Dec",]
    y = [100, 250, 180, 220, 300, 270, 240, 210, 190, 200, 230, 170]

    # plot
    fig, ax = plt.subplots()
    ax.plot(x, y if not enter_toggle else y_array, graph_color)
    st.pyplot(fig)

if type == 'Точечный (Scatter Plot)':

    multi = '''
#### Точечный график


**Описание**:
Точечный график позволяет увидеть взаимосвязи между двумя или более наборами числовых значений. 

Он помогает выявить закономерности (например, корреляцию или тренды), обнаружить выбросы или аномалии в данных, сравнить группы данных (например, кластеризация), анализировать распределение точек на плоскости.

<details>
<summary><b>Где используется</b></summary>
1) <b>Анализ взаимосвязей:</b> Scatter Plot используется для изучения взаимосвязей между двумя переменными. Например, зависимость роста от веса у людей или связь между затратами на рекламу и объемом продаж.<br>
2) <b>Выявление трендов:</b> Scatter Plot помогает визуализировать тренды в данных. Например, изменение температуры воздуха в зависимости от времени года или рост производительности труда с увеличением опыта сотрудников.<br>
3) <b>Обнаружение выбросов:</b> Scatter Plot применяется для выявления аномалий или выбросов в данных. Например, обнаружение необычных значений в финансовых данных или результатах экспериментов.<br>
4) <b>Кластеризация данных:</b> Scatter Plot используется для визуализации кластеров или групп в данных. Например, разделение клиентов на группы по уровню дохода и расходов или классификация данных в машинном обучении.<br>	    	
</details>
<br>


**Пример**: Набор данных о клиентах интернет-магазина, включая их возраст и количество заказов. Необходимо визуализировать связь между этими двумя показателями.
```
ages = [25, 32, 41, 19, 35, 27, 22, 37, 45, 21, 34, 28]
orders = [5, 10, 20, 3, 8, 15, 7, 12, 18, 4, 11, 9]
```
<details>
<summary><b>Параметры для графика</b></summary>
<b>x</b>, <b>y</b>: <i>array-like</i> или <i>float</i>, <i>shape (n, )</i><br>
Позиции данных на графике. <b>x</b> и <b>y</b> определяют координаты точек на оси абсцисс и ординат соответственно.<br><br>
<details>
<summary><b>s</b>: <i>scalar</i> или <i>array-like</i>, <i>shape (n, )</i>, <i>optional</i></summary>
Размер маркеров в точках. Может быть скаляром (одинаковый размер для всех точек) или массивом (разные размеры для каждой точки).<br>
</details>
<details>
<summary><b>c</b>: <i>color</i> или <i>array-like</i>, <i>shape (n, )</i>, <i>optional</i></summary>
Цвет маркеров. Может быть строкой (например, 'r' для красного), RGB-значением или массивом значений для цветовой карты.<br>
</details>
<details>
<summary><b>marker</b>: <i>str</i> или <i>MarkerStyle</i>, <i>optional</i></summary>
Стиль маркера. Например, 'o' для кругов, 's' для квадратов, 'D' для ромбов и т.д.<br>
</details>
<details>
<summary><b>cmap</b>: <i>str</i> или <i>Colormap</i>, <i>optional</i></summary>
Цветовая карта, используемая для отображения значений, если <b>c</b> является массивом.<br>
</details>
<details>
<summary><b>norm</b>: <i>Normalize</i>, <i>optional</i></summary>
Нормализация данных для цветовой карты. Используется, если <b>c</b> является массивом.<br>
</details>
<details>
<summary><b>vmin</b>, <b>vmax</b>: <i>float</i>, <i>optional</i></summary>
Минимальное и максимальное значения для нормализации данных. Используется, если <b>c</b> является массивом.<br>
</details>
<details>
<summary><b>alpha</b>: <i>float</i>, <i>optional</i></summary>
Прозрачность маркеров. Значение от 0 (полностью прозрачный) до 1 (полностью непрозрачный).<br>
</details>
<details>
<summary><b>linewidths</b>: <i>scalar</i> или <i>array-like</i>, <i>optional</i></summary>
Толщина границы маркеров. Может быть скаляром или массивом.<br>
</details>
<details>
<summary><b>edgecolors</b>: <i>color</i> или <i>array-like</i>, <i>optional</i></summary>
Цвет границы маркеров. Может быть строкой, RGB-значением или массивом.<br>
</details>
<details>
<summary><b>plotnonfinite</b>: <i>bool</i>, <i>optional</i></summary>
Если <b>True</b>, точки с нечисловыми значениями (NaN, inf) будут отображены.<br>
</details>
<details>
<summary><b>data</b>: <i>dict</i>, <i>optional</i></summary>
Словарь с данными, которые могут быть использованы для подстановки в <b>x</b>, <b>y</b>, <b>s</b>, <b>c</b> и другие параметры.<br>
</details>
<details>
<summary><b>**kwargs</b>: <i>optional</i></summary>
Дополнительные параметры, которые могут быть переданы в функцию построения графика.<br>
</details>  
</details>  

'''  
    st.markdown(multi, unsafe_allow_html=True)
    st.divider()
    st.write("Цвета и размеры в данном примере задаются случайно, поэтому при изменении прозрачности меняются цвета и размеры.")
    
    text = '''
    x = [25, 32, 41, 19, 35, 27, 22, 37, 45, 21, 34, 28]
    y = [5, 10, 20, 3, 8, 15, 7, 12, 18, 4, 11, 9]

    sizes = np.random.uniform(1, 200, len(x))
    colors = np.random.uniform(15, 80, len(x))

    fig, ax = plt.subplots()
    ax.scatter(x, y)'''
    st.code(text)
    enter_toggle = st.toggle("Ввести свои значения")
    if enter_toggle:
        x_text = st.text_area("Введите массив для x (через запятую с пробелом)", value="25, 32, 41, 19, 35, 27, 22, 37, 45, 21, 34, 28", height=68)
        y_text = st.text_area("Введите массив для y (через запятую с пробелом)", value="5, 10, 20, 3, 8, 15, 7, 12, 18, 4, 11, 9", height=68)
        x_array = np.array(list(x_text.split(', ')))
        y_array = np.array(list(y_text.split(', ')), dtype=float)
        st.code("!!! В массив y можно вводить только числа.")
    # make the data
    x = [25, 32, 41, 19, 35, 27, 22, 37, 45, 21, 34, 28]
    y = [5, 10, 20, 3, 8, 15, 7, 12, 18, 4, 11, 9]
    # size and color:
    sizes = np.random.uniform(1, 200, len(x))
    colors = np.random.uniform(15, 80, len(x))
    # plot
    fig, ax = plt.subplots()
    ax.scatter(x if not enter_toggle else x_array, y if not enter_toggle else y_array, s=sizes, c=colors)
    st.pyplot(fig)

if type == "Барный (Bar Plot)":

    multi = '''
#### Барный график (Горизонтальная гистограмма)

**Описание**:
Барный график (Bar Plot) используется для визуализации данных, представленных в виде категориальных групп с количественными значениями. 
Это может быть полезно для сравнения значений между разными категориями, анализа распределений и выявления тенденций.

<details>
<summary><b>Где используется</b></summary>
1) <b>Сравнение категорий:</b> Bar Plot используется для сравнения значений между различными категориями. Например, сравнение продаж разных продуктов, посещаемости сайтов или результатов выборов по регионам.<br>
2) <b>Визуализация частот:</b> Bar Plot помогает отобразить частоту или количество наблюдений в каждой категории. Например, количество студентов в разных группах или частота заболеваний по типам.<br>
3) <b>Анализ временных данных:</b> Bar Plot может использоваться для отображения изменений данных во времени, например, ежемесячных продаж, уровня безработицы или температуры по месяцам.<br>
4) <b>Представление пропорций:</b> Bar Plot применяется для визуализации пропорций или долей, например, распределения бюджета по статьям расходов или процентного соотношения голосов на выборах.<br>	    	
</details>
<br>

**Пример**: Данные о продажах трех продуктов в разные месяцы. Необходимо сравнить показатели.
```
product_names = ['Product A', 'Product B', 'Product C']
january_sales = [100, 150, 200]
february_sales = [120, 180, 220]
march_sales = [110, 170, 250]
```
<details>
<summary><b>Параметры для графика</b></summary>
<b>x</b>: <i>array-like</i> или <i>float</i><br>
Координаты столбцов по оси X. Может быть массивом чисел или отдельным числом.<br>


<b>height</b>: <i>array-like</i> или <i>float</i><br>
Высота столбцов (значения по оси Y). Может быть массивом чисел или отдельным числом.<br>

<details>
<summary><b>width</b>: <i>float</i>, <i>optional</i>, по умолчанию: 0.8</summary>
Ширина столбцов. Задается числом.<br>
</details>
<details>
<summary><b>bottom</b>: <i>array-like</i> или <i>float</i>, <i>optional</i>, по умолчанию: 0</summary>
Нижняя граница столбцов. Может быть массивом чисел или отдельным числом.<br>
</details>
<details>
<summary><b>align</b>: <i>{'center', 'edge'}</i>, <i>optional</i>, по умолчанию: 'center'</summary>
Выравнивание столбцов: 'center' — по центру, 'edge' — по краю.<br>
</details>
<details>
<summary><b>data</b>: <i>dict</i>, <i>optional</i></summary>
Словарь данных для использования в качестве источника для X и Y.<br>
</details>
<details>
<summary><b>**kwargs</b>: <i>optional</i></summary>
Дополнительные параметры, которые могут быть переданы в функцию построения графика.<br>
</details>
</details>

    '''  
    st.markdown(multi, unsafe_allow_html=True)
    st.divider()
    width = st.number_input("Ширина", value=1.0, min_value=0.0, step=0.05)
    align = st.selectbox("Привязка", ['center', 'edge'])
    linewidth = st.number_input("Ширина границы", value=0.8, min_value=0.0, step=0.05)
    edgecolor = st.color_picker("Цвет границы")
    log = st.selectbox("Логарифмическая шкала оси Y", [False, True])

    # make data:
    text = '''
    product_names = ['Product A', 'Product B', 'Product C']
    january_sales = [100, 150, 200]
    february_sales = [120, 180, 220]
    march_sales = [110, 170, 250]

    fig, ax = plt.subplots()
    ax.bar(product_names, january_sales)
    ax.bar(product_names, february_sales, bottom=january_sales)
    ax.bar(product_names, march_sales, bottom=[x + y for x, y in zip(january_sales, february_sales)])'''
    st.code(text)

    product_names = ['Product A', 'Product B', 'Product C']
    january_sales = [100, 150, 200]
    february_sales = [120, 180, 220]
    march_sales = [110, 170, 250]
    # plot
    fig, ax = plt.subplots()
    ax.bar(product_names, january_sales, width=width, edgecolor=edgecolor, linewidth=linewidth, align=align, log=log, label="January")
    ax.bar(product_names, february_sales, bottom=january_sales, width=width, edgecolor=edgecolor, linewidth=linewidth, align=align, log=log, label="February",)
    ax.bar(product_names, march_sales, bottom=[x + y for x, y in zip(january_sales, february_sales)], width=width, edgecolor=edgecolor, linewidth=linewidth, align=align, log=log, label="March")
    ax.legend()
    st.pyplot(fig)


if type == "Стержневой (Stem Plot)":

    multi = '''
#### Stem-график

**Описание**:
Stem Plot в библиотеке Matplotlib используется для визуализации данных, представленных в виде дискретных значений вдоль одной оси. 
Это позволяет удобно сравнивать различные группы данных, например, распределение возраста сотрудников компании или частоту появления определенных событий.

<details>
<summary><b>Где используется</b></summary>
1) <b>Анализ небольших наборов данных:</b> Stem Plot используется для визуализации небольших наборов данных, где важно сохранить точность значений. Например, анализ оценок студентов или результатов коротких экспериментов.<br>
2) <b>Изучение распределения данных:</b> Stem Plot помогает быстро оценить форму распределения данных, например, частоту появления определенных значений в статистических исследованиях.<br>
3) <b>Сравнение групп данных:</b> Stem Plot может использоваться для сравнения двух или более наборов данных, например, сравнение результатов тестов двух классов или групп пациентов.<br>
4) <b>Предварительный анализ данных:</b> Stem Plot полезен для быстрого предварительного анализа данных перед применением более сложных методов, например, в научных исследованиях или инженерных задачах.	    	
</details>
<br>


**Пример**: Визуализация данных о посещениях сайта в разные дни недели
```
days  = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
visits = [100, 150, 200, 120, 180, 220, 300]
```
<details>
<summary><b>Параметры для графика</b></summary>

<b>locs</b>: <i>array-like</i>, <i>default: (0, 1, ..., len(heads) - 1)</i><br>
Для вертикальных графиков стеблей - положение стеблей по оси x. Для горизонтальных графиков стеблей - положения стеблей по оси y.<br>
<b>heads</b>: <i>array-like</i><br>
Для вертикальных стеблевых графиков - значения y головок стеблей. Для горизонтальных стеблевых графиков - x-значения головок стеблей.<br>


<details>
<summary><b>linefmt</b>: <i>str</i>, <i>optional</i>, по умолчанию: 'C0-'</summary>
Формат линии стебля (например, 'b-' для синей линии).<br>
</details>
<details>
<summary><b>markerfmt</b>: <i>str</i>, <i>optional</i>, по умолчанию: 'C0o'</summary>
Формат маркера (например, 'ro' для красных кружков).<br>
</details>
<details>
<summary><b>basefmt</b>: <i>str</i>, <i>optional</i>, по умолчанию: 'C3-'</summary>
Формат базовой линии (например, 'g--' для зеленой пунктирной линии).<br>
</details>
<details>
<summary><b>bottom</b>: <i>float</i>, <i>optional</i>, по умолчанию: 0</summary>
Координата Y базовой линии.<br>
</details>
<details>
<summary><b>label</b>: <i>str</i>, <i>optional</i></summary>
Метка для легенды графика.<br>
</details>
<details>
<summary><b>orientation</b>: <i>{'vertical', 'horizontal'}</i>, <i>optional</i>, по умолчанию: 'vertical'</summary>
Ориентация стеблей: 'vertical' — вертикальная, 'horizontal' — горизонтальная.<br>
</details>
<details>
<summary><b>data</b>: <i>dict</i>, <i>optional</i></summary>
Словарь данных для использования в качестве источника для X и Y.<br>
</details>
</details>


'''  
    st.markdown(multi, unsafe_allow_html=True)
    st.divider()
    orientation = st.selectbox("Ориентация", ['vertical', 'horizontal'])
    linefmt_choose = st.selectbox("Стиль линий", ['Сплошная линия', 'Пунктирная линия', 'Штрихпунктирная линия', 'Линия в виде точек'])
    match linefmt_choose:
        case 'Пунктирная линия': 
            linefmt = '--'
        case 'Штрихпунктирная линия': 
            linefmt = '-.'
        case 'Линия в виде точек': 
            linefmt = ':'
        case _:
            linefmt = '-'
    

    tab1, tab2 = st.tabs(["Пример №1", "Пример №2"])
    text = '''
    fig1, ax1 = plt.subplots()

    x = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    y = [100, 150, 200, 120, 180, 220, 300]

    ax1.stem(x, y)'''
    tab1.code(text)
    # plot №1
    fig1, ax1 = plt.subplots()

    x = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    y = [100, 150, 200, 120, 180, 220, 300]

    ax1.stem(x, y, orientation=orientation, linefmt=linefmt)
    tab1.pyplot(fig1)

    # plot №2
    text = '''
    fig2, ax2 = plt.subplots()

    x = np.linspace(0.1, 2 * np.pi, 41) 
    y = np.exp(np.sin(x))

    ax2.stem(x, y)'''
    tab2.code(text)

    fig2, ax2 = plt.subplots()

    x = np.linspace(0.1, 2 * np.pi, 41) 
    y = np.exp(np.sin(x))

    ax2.stem(x, y, orientation=orientation, linefmt=linefmt)
    tab2.pyplot(fig2)

if type == "Заливка области между (Fill_between)":

    multi = '''
#### Линейный график с заливкой области между

**Описание**:
Fill_between используется для заливки областей графика. С её помощью можно заполнить цветом промежуток между любыми несколькими линиями или любыми двумя горизонтальными кривыми на 2D-плоскости.

<details>
<summary><b>Где используется</b></summary>
1) <b>Выделение ключевых областей:</b> Это помогает акцентировать внимание зрителя на значимых точках данных или просто добавить эстетический штрих к графикам.<br>
2) <b>Создание условной заливки:</b> SС её помощью можно выделить определённые периоды или закономерности в данных.<br>
3) <b>Обозначение доверительных полос:</b> SЕщё одно распространённое применение fill_between — обозначение доверительных полос.<br>
    	
</details>
<br>

**Пример**: Визуализация доверительных интервалов вокруг среднего значения случайных данных. Этот метод часто применяется в статистике и машинном обучении для оценки неопределенности модели.
    
<details>
<summary><b>Параметры для графика</b></summary>

<b>x</b>: <i>array-like</i> или <i>float</i><br>
Координаты по оси X. Может быть массивом чисел или отдельным числом.<br>
<b>y1</b>: <i>array-like</i> или <i>float</i><br>
Верхние границы заливки. Может быть массивом чисел или отдельным числом.<br>
<b>y2</b>: <i>array-like</i> или <i>float</i>, <i>optional</i>, по умолчанию: 0<br>
Нижние границы заливки. Может быть массивом чисел или отдельным числом.<br>

<details>
<summary><b>where</b>: <i>array-like</i>, <i>optional</i></summary>
Булев массив, указывающий, где применять заливку.<br>
</details>
<details>
<summary><b>interpolate</b>: <i>bool</i>, <i>optional</i>, по умолчанию: False</summary>
Интерполяция между точками, если y1 и y2 пересекаются.<br>
</details>
<details>
<summary><b>step</b>: <i>{'pre', 'post', 'mid'}</i>, <i>optional</i></summary>
Тип шага для заливки: 'pre' — до точки, 'post' — после точки, 'mid' — по центру.<br>
</details>
<details>
<summary><b>data</b>: <i>dict</i>, <i>optional</i></summary>
Словарь данных для использования в качестве источника для X, Y1 и Y2.<br>
</details>
<details>
<summary><b>**kwargs</b>: <i>optional</i></summary>
Дополнительные параметры, которые могут быть переданы в функцию построения графика.<br>
</details>
</details>
    
    '''  
    st.markdown(multi, unsafe_allow_html=True)
    st.divider()
    alpha = st.number_input("Прозрачность графика", value=0.5, min_value=0.0, max_value=1.0)

    tab1, tab2 = st.tabs(["С одной кривой", "С двумя кривыми"])

    # make data
    np.random.seed(1)

    x_1 = np.arange(0.0, 5, 0.01)
    y_1 = np.cos(x_1*np.pi)

    x_2 = np.linspace(0, 8, 16)
    y1_2 = 2 + 5*x_2/7 + np.random.uniform(0.0, 0.5, len(x_2))
    y2_2 = 1 + 3*x_2/8 + np.random.uniform(-2, 7, len(x_2))


    # plot №1
    text = '''
    x_1 = np.arange(0.0, 5, 0.01)
    y_1 = np.cos(x_1*np.pi)

    fig1, ax1 = plt.subplots()
    ax1.fill_between(x_1, y_1, 0)
    ax1.plot(x_1, y_1)'''
    tab1.code(text)

    fig1, ax1 = plt.subplots()

    ax1.fill_between(x_1, y_1, 0, alpha=alpha)
    ax1.plot(x_1, y_1)

    tab1.pyplot(fig1)

    # plot №2
    text = '''
    x_2 = np.linspace(0, 8, 16)
    y1_2 = 2 + 5*x_2/7 + np.random.uniform(0.0, 0.5, len(x_2))
    y2_2 = 1 + 3*x_2/8 + np.random.uniform(-2, 7, len(x_2))

    fig2, ax2 = plt.subplots()
    ax2.fill_between(x_2, y1_2, y2_2)
    ax2.plot(x_2, y1_2, x_2, y2_2,)
    	'''
    tab2.code(text)
    fig2, ax2 = plt.subplots()

    ax2.fill_between(x_2, y1_2, y2_2, alpha=alpha)
    ax2.plot(x_2, y1_2, x_2, y2_2)
    
    tab2.pyplot(fig2)
    
if type == "Стековый (Stackplot)":

    multi = '''
#### Стековый график

**Описание**:
Stackplot используется для создания так называемых стековых диаграмм, которые позволяют наглядно представлять данные, состоящие из нескольких временных рядов, где каждый следующий ряд строится поверх предыдущего. 
Такой вид диаграммы особенно удобен для анализа совокупной величины, составленной из отдельных компонентов.


<details>
<summary><b>Где используется</b></summary>
1) <b>Анализ совокупных величин:</b> Стековая диаграмма позволяет видеть общую картину изменений, связанных с несколькими компонентами. Например, вы можете отслеживать, как изменяются общие расходы компании в течение времени и какие компоненты вносят наибольший вклад в эти изменения.<br>
2) <b>Оценка вклада каждого компонента:</b> Каждый слой диаграммы соответствует отдельной категории данных, поэтому легко оценить, какой процент общей суммы приходится на каждую категорию.<br>
3) <b>Простота интерпретации:</b> В отличие от обычных графиков, где линии могут пересекаться и затруднять восприятие, стековая диаграмма чётко показывает, как изменяется общая сумма и её составляющие.<br>
</details>
<br>

**Пример**: Анализ расходов компании за месяц по разным категориям: аренда офиса, зарплата сотрудников, маркетинговые затраты и другие операционные расходы. 
Стековая диаграмма поможет увидеть общую динамику расходов и вклад каждой категории в эту сумму.

<details>
<summary><b>Параметры для графика</b></summary>

<b>x</b>: <i>(N,) array-like</i><br>
Координаты по оси X. Может быть массивом чисел или отдельным числом.<br>
<b>y</b>: <i>(M, N) array-like</i><br>
Данные для построения стека. y имеет размеры (M, N). Может быть массивом или списком массивов.<br>

<details>
<summary><b>baseline</b>: <i>{'zero', 'sym', 'wiggle', 'weighted_wiggle'}</i>, <i>optional</i>, по умолчанию: 'zero'</summary>
Метод расчета базовой линии: 'zero' — от нуля, 'sym' — симметрично, 'wiggle' — минимизация наклона, 'weighted_wiggle' — взвешенная минимизация.<br>
</details>
<details>
<summary><b>labels</b>: <i>list of str</i>, <i>optional</i></summary>
Метки для каждого стека. Используется для легенды.<br>
</details>
<details>
<summary><b>colors</b>: <i>list of color</i>, <i>optional</i></summary>
Цвета для каждого стека. Может быть списком строк (например, ['red', 'blue']).<br>
</details>
<details>
<summary><b>hatch</b>: <i>str</i> или <i>list of str</i>, <i>optional</i></summary>
Тип штриховки для стека (например, '/', '\\', '|', '-').<br>
</details>
<details>
<summary><b>data</b>: <i>dict</i>, <i>optional</i></summary>
Словарь данных для использования в качестве источника для X и Y.<br>
</details>
<summary><b>**kwargs</b>: <i>optional</i></summary>
Дополнительные параметры, которые могут быть переданы в функцию построения графика.<br>
</details>
</details>
   
    '''  
    st.markdown(multi, unsafe_allow_html=True)
    st.divider()
    baseline = st.selectbox("baseline", ['zero', 'sym', 'wiggle', 'weighted_wiggle'])
    text = '''
    days = np.arange(1, 31)
    rent = np.random.randint(5000, 7000, size=30)
    salary = np.random.randint(15000, 20000, size=30)
    marketing = np.random.randint(3000, 6000, size=30)
    other_expenses = np.random.randint(8000, 12000, size=30)

    fig, ax = plt.subplots()
    ax.stackplot(days, rent, salary, marketing, other_expenses)'''
    st.code(text)
    days = np.arange(1, 31)
    rent = np.random.randint(5000, 7000, size=30)
    salary = np.random.randint(15000, 20000, size=30)
    marketing = np.random.randint(3000, 6000, size=30)
    other_expenses = np.random.randint(8000, 12000, size=30)
    # plot
    fig, ax = plt.subplots()

    ax.stackplot(days, rent, salary, marketing, other_expenses, baseline=baseline)
    st.pyplot(fig)
if type == "Ступенчатый (Stairs Plot)":

    multi = '''
#### Ступенчатый график

**Описание**:
Stairs Plot используется для построения ступенчатых графиков, которые полезны для отображения дискретных данных или функций, меняющихся скачками. 
Этот тип графика часто встречается в финансовых приложениях, при анализе временных рядов, а также в ситуациях, когда важно показать точные моменты изменений.

<details>
<summary><b>Где используется</b></summary>
1) <b>Отображение дискретных данных:</b> Когда данные меняются скачкообразно, ступенчатый график позволяет точно показать моменты этих изменений. Например, в финансовом анализе можно наблюдать скачки цен акций или валют.<br>
2) <b>Наглядность изменений:</b> Если важна точная фиксация момента изменения значения, то ступенчатый график лучше отражает такие переходы, чем плавные линии.<br>
3) <b>Удобство чтения:</b> Благодаря своей простоте, ступенчатый график легко воспринимается и интерпретируется пользователем.<br>
</details>
<br>


**Пример**: Данные о количестве продаж товаров в магазине за неделю. Продажи происходят неравномерно, и необходимо отобразить их изменение во времени.

<details>
<summary><b>Параметры для графика</b></summary>

<b>values</b>: <i>array-like</i><br>
Значения ступеней (высоты ступеней). Может быть массивом чисел.<br>

<details>
<summary><b>edges</b>: <i>array-like</i>, <i>optional</i></summary>
Границы ступеней по оси X. Если не указано, используется равномерное распределение.<br>
</details>
<details>
<summary><b>orientation</b>: <i>{'vertical', 'horizontal'}</i>, <i>optional</i>, по умолчанию: 'vertical'</summary>
Ориентация ступеней: 'vertical' — вертикальная, 'horizontal' — горизонтальная.<br>
</details>
<details>
<summary><b>baseline</b>: <i>float</i>, <i>optional</i>, по умолчанию: 0</summary>
Базовая линия, от которой начинаются ступени.<br>
</details>
<details>
<summary><b>fill</b>: <i>bool</i>, <i>optional</i>, по умолчанию: False</summary>
Заливка области под ступенями.
</details>
<details>
<summary><b>data</b>: <i>dict</i>, <i>optional</i></summary>
Словарь данных для использования в качестве источника для значений и границ.<br>
</details>
<details>
<summary><b>**kwargs</b>: <i>optional</i></summary>
Дополнительные параметры, которые могут быть переданы в функцию построения графика.<br>
</details>
</details>
    
 '''  
    st.markdown(multi, unsafe_allow_html=True)
    st.divider()
    fill = st.toggle("Включить заливку")
    baseline = st.number_input("Отступ", value=0.0)
    linewidth = st.number_input("Ширина графика", value=2.0)
    text = '''
    days = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
    sales = [15, 22, 18, 25, 19, 28]

    fig, ax = plt.subplots()
    ax.stairs(sales, days)'''
    st.code(text)

    # make data
    days = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
    sales = [15, 22, 18, 25, 19, 28]

    # plot
    fig, ax = plt.subplots()

    ax.stairs(sales, days, linewidth=linewidth, fill=fill, baseline=baseline)
    st.pyplot(fig)
