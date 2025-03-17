import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np 
import scipy.interpolate as interpolate 
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
 
menu = st.sidebar.radio('***',
	(
	"Общая информация", 
	"Простейший 3D-график",
	"Поверхности",
	"Контуры"
	)
)
  
if menu == "Общая информация":
	r"""
##### Общая информация

тесттесттест

	""" 

if menu == "Простейший 3D-график":
	r"""
##### Простейший 3D-график

Построим трехмерную кривую.

Введите координаты точек в формате: $(x_1,y_1,z_1), (x_2,y_2,z_2)$ ...

	"""
	def parse_inp(inp):
		# Удаляем пробелы из строки
		inp = inp.replace(" ", "")
		
		# Разделяем строку по запятым, окруженным скобками
		points = inp.split("),")
		
		# Убираем лишние скобки
		points = [point.strip("()") for point in points]
		
		# Создаем три списка для координат
		x_coords = []
		y_coords = []
		z_coords = []
		
		# Разбираем каждую точку
		for point in points:
			#Разделяем координаты
			x, y, z = point.split(",")
			
			#Преобразуем в числа и добавляем в соответствующие списки
			x_coords.append(float(x))
			y_coords.append(float(y))
			z_coords.append(float(z))
		return x_coords, y_coords, z_coords
	
	def plot_curve_points(inp):
		# creating an empty canvas
		fig = plt.figure()
		 
		# defining the axes with the projection
		# as 3D so as to plot 3D graphs
		ax = plt.axes(projection="3d")
		 
		# creating a wide range of points x,y,z 
		#x=[0,1,2,3,4,5,6]
		#y=[0,1,4,9,16,25,36]
		#z=[0,1,4,9,16,25,36]
		x,y,z=parse_inp(inp)
		print(x)
		print(y)
		print(z)
		# plotting a 3D line graph with X-coordinate,
		# Y-coordinate and Z-coordinate respectively
		ax.plot3D(x, y, z, 'red')
		 
		# plotting a scatter plot with X-coordinate,
		# Y-coordinate and Z-coordinate respectively
		# and defining the points color as cividis
		# and defining c as z which basically is a 
		# definition of 2D array in which rows are RGB
		#or RGBA
		ax.scatter3D(x, y, z, c=z, cmap='cividis');
		 
		# Showing the above plot
		#plt.show()
		c1, c2, = st.columns([5,1]) 
		c1.pyplot(fig)
	
	def makepage():

		default_points = "(0,0,0), (1,1,1), (2,4,4), (3,9,9), (4,16,16), (5,25,25), (6,36,36)"
		inp = st.text_input("Введите точки...", value=default_points, key = "input1")

		c1, c2, = st.columns([1,1])
		if c1.button("Построить график"):
			try:
				plot_curve_points(inp)
			except:
				st.write("Некорректный ввод!")
	makepage()


if menu == "Поверхности":
	r"""
##### Matplotlib поддерживает и рисование поверхностей. 

Попробуем построить поверхность, заданную $z=f(x)$.
Определите область, в которой будет строится график. Для этого введите в текстовое поле интервалы, задающие область в формате: $(x_0, x_1, $step$)$.

	"""
	def parse_inp(inp):
		# Удаляем пробелы из строки
		inp = inp.replace(" ", "")
		
		# Разделяем строку по запятым
		interval = inp.split(",")
		# Создаем три списка для координат
		domain = []
		
		# Разбираем каждую точку
		for val in interval:
			domain.append(float(val))
		print(domain)
		return domain
	def cos_pix2(x):
		return np.cos(x* np.pi/2)
	def sin_pix2(x):
		return np.sin(x* np.pi/2)
	def xpow2(x):
		return x**2
	def frac_1_x(x):
		return 1/x
	def plot_surface_fromfunc(f, domain_x, domain_y):
		# creating an empty figure for plotting
		fig = plt.figure()
		 
		# defining a sub-plot with 1x2 axis and defining 
		# it as first plot with projection as 3D
		ax = fig.add_subplot(1, 2, 1, projection='3d')
		 
		# creating a range of values for 
		# x1,y1  from -1 to 1 with 
		# a space of 0.1 between the elements so that 
		# we can create a single curve in the plot
		x1= np.arange(domain_x[0], domain_x[1], domain_x[2])
		y1= np.arange(domain_y[0], domain_y[1], domain_y[2])
		 
		# Creating a mesh grid with x ,y and x1,
		# y1 which creates an n-dimensional
		# array
		x1,y1= np.meshgrid(x1,y1)
		 
		# Creating a cosine function with the 
		# range of values from the meshgrid
		z1= f(x1)
		ax.plot_surface(x1, y1, z1, color="red")
		# Showing the above plot
		c1, c2, = st.columns([5,1]) 
		c1.pyplot(fig)
	
	def funcplot():
		option = st.selectbox("Выберите функцию z = f(x)",("cos", "sin", "x^2", "1/x"),)
		x_domain = st.text_input("x", value="-1, 1, 0.1", key = "input_x")
		y_domain = st.text_input("y", value="-1, 1, 0.1", key = "input_y")
		x_domain = parse_inp(x_domain)
		y_domain = parse_inp(y_domain)
		c1, c2, = st.columns([1,1])
		if c1.button("Построить график", key="funcplot"):
			if option == "cos":
				plot_surface_fromfunc(cos_pix2, x_domain, y_domain)
			if option == "sin":
				plot_surface_fromfunc(sin_pix2, x_domain, y_domain)
			if option == "x^2":
				plot_surface_fromfunc(xpow2, x_domain, y_domain)
			if option == "1/x":
				plot_surface_fromfunc(frac_1_x, x_domain, y_domain)
		
	funcplot()
	"""
	Попробуем теперь построить поверхность второго порядка. Выберите тип поверхности и задайте область, аналогично шагу выше.
	"""
	def hyperbolic_paraboloid(x,y,a,b):
		return (0.5)*(x**2/a**2-y**2/b**2)
	def elliptic_paraboloid(x,y,a,b):
		return (0.5)*(x**2/a**2+y**2/b**2)
	def ellipsoid(x,y,a,b): #c = 1
		return np.sqrt(1-x**2/a**2-y**2/b**2) if (1-x**2/a**2-y**2/b**2).any () >0 else 0
	def plot_surface_2ord(f, a, b, domain_x, domain_y):
		# creating an empty figure for plotting
		fig = plt.figure()
		 
		# defining a sub-plot with 1x2 axis and defining 
		# it as first plot with projection as 3D
		ax = fig.add_subplot(1, 2, 1, projection='3d')
		 
		# creating a range of values for 
		# x1,y1  from -1 to 1 with 
		# a space of 0.1 between the elements so that 
		# we can create a single curve in the plot
		x1= np.arange(domain_x[0], domain_x[1], domain_x[2])
		y1= np.arange(domain_y[0], domain_y[1], domain_y[2])
		 
		# Creating a mesh grid with x ,y and x1,
		# y1 which creates an n-dimensional
		# array
		x1,y1= np.meshgrid(x1,y1)
		 
		# Creating a cosine function with the 
		# range of values from the meshgrid
		z1= f(x1, y1, a,b)
		ax.plot_surface(x1, y1, z1, color="red")
		# Showing the above plot
		c1, c2, = st.columns([5,1]) 
		c1.pyplot(fig)
	def plot2ord():
		option = st.selectbox("Выберите поверхность",("Гиперболический параболоид", "Эллиптический параболоид", "Эллипсоид"),)
		x_domain = st.text_input("x", value="-10, 10, 0.1", key = "input_x_2ord")
		y_domain = st.text_input("y", value="-10, 10, 0.1", key = "input_y_2ord")
		x_domain = parse_inp(x_domain)
		y_domain = parse_inp(y_domain)
		a = st.slider("a", -10, 10, 1)
		b = st.slider("b", -10, 10, 1)
		c1, c2, = st.columns([1,1])
		if option == "Гиперболический параболоид":
			plot_surface_2ord(hyperbolic_paraboloid, a, b, x_domain, y_domain)
		if option == "Эллиптический параболоид":
			plot_surface_2ord(elliptic_paraboloid, a, b, x_domain, y_domain)
		if option == "Эллипсоид":
			plot_surface_2ord(ellipsoid, a, b, x_domain, y_domain)
	plot2ord()

if menu == "Контуры":
	r"""
##### Окрашивание трехмного графика. 

Частая задача визуализации -- окрашивание какой-либо поверхности цветом в зависимости от значений, которые на ней принимает некоторая функция.
Например, это могут быть модули тензора напряжений на поверхности твердого тела.

	"""
	def plot_surface(x_domain, y_domain, z):
		x_space = np.linspace(x_domain[0], x_domain[1], x_domain[2])
		y_space = np.linspace(y_domain[0], y_domain[1], y_domain[2])
		x, y = np.meshgrid(x_space, y_space)
	def contour():
		x_domain = st.text_input("x", value="-10, 10, 200", key = "input_x_2ord")
		y_domain = st.text_input("y", value="-10, 10, 200", key = "input_y_2ord")
		x_domain = parse_inp(x_domain)
		y_domain = parse_inp(y_domain)
		c1 = st.columns([1])
		if c1.button("Сгенерировать случайные данные", key=rnddata):
			a=0
