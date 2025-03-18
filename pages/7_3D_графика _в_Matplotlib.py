import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import axes3d
from matplotlib.colors import Normalize
 
menu = st.sidebar.radio('***',
	(
	"Общая информация", 
	"Простейший 3D-график",
	"Поверхности",
	"Векторные поля"
	)
)
  
if menu == "Общая информация":
	r"""
##### Общая информация

Кроме двумерных графиков, рассмотренных в разделах выше, Matplotlib поддерживает и различные виды трехмерной графики. К таковым можно отнести:

- Кривые в пространстве
- Поверхности
- Векторные поля
-  ...и многое другое!

Необходимые импорты:
	""" 
	codes = ['''import streamlit''', '''import matplotlib.pyplot''', '''import numpy''', '''from mpl_toolkits import mplot3d''', '''from mpl_toolkits import axes3d''',  '''import matplotlib.colors''']
	for code in codes:
		st.code(code, language = "python")
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

		x,y,z=parse_inp(inp)
		# plotting a 3D line graph with X-coordinate,
		# Y-coordinate and Z-coordinate respectively
		ax.plot3D(x, y, z, 'red')
		 
		# plotting a scatter plot with X-coordinate,
		# Y-coordinate and Z-coordinate respectively
		# and defining the points color as cividis
		# and defining c as z which basically is a 
		# definition of 2D array in which rows are RGB
		#or RGBA
		ax.scatter3D(x, y, z, c=z, cmap='plasma');
		 
		# Showing the above plot
		c1, c2, = st.columns([5,1]) 
		c1.pyplot(fig)
	
	def plot_curve_points_random():
		# creating an empty canvas
		fig = plt.figure()
		 
		# defining the axes with the projection
		# as 3D so as to plot 3D graphs
		ax = plt.axes(projection="3d")
		n = np.random.randint(low=5, high=11)
		x = np.random.randint(low = -5, high = 5, size = (3*n))
		y = np.random.randint(low = -5, high = 5, size = (3*n))
		z = np.random.randint(low = -5, high = 5, size = (3*n))
		# plotting a 3D line graph with X-coordinate,
		# Y-coordinate and Z-coordinate respectively
		ax.plot3D(x, y, z, 'red')
		 
		# plotting a scatter plot with X-coordinate,
		# Y-coordinate and Z-coordinate respectively
		# and defining the points color as cividis
		# and defining c as z which basically is a 
		# definition of 2D array in which rows are RGB
		#or RGBA
		ax.scatter3D(x, y, z, c=z, cmap='plasma');
		 
		# Showing the above plot
		c1, c2, = st.columns([5,1]) 
		c1.pyplot(fig)
	def showcode_1():
		code = '''
		def plot_curve_points(inp):
		fig = plt.figure()
		ax = plt.axes(projection="3d")
		x,y,z=parse_inp(inp)
		ax.plot3D(x, y, z, 'red')
		ax.scatter3D(x, y, z, c=z, cmap='plasma');
		c1, c2, = st.columns([5,1]) 
		c1.pyplot(fig)'''
		st.code(code, language = "python")
	
	def makepage():
		default_points = "(0,0,0), (1,1,1), (2,4,4), (3,9,9), (4,16,16), (5,25,25), (6,36,36)"
		inp = st.text_input("Введите точки...", value=default_points, key = "input1")

		c1, c2, = st.columns([1,1])
		if c1.button("Построить график"):
			try:
				plot_curve_points(inp)
			except:
				st.write("Некорректный ввод!")
		if c2.button("Случайный график"):
			plot_curve_points_random()
	makepage()
	c1, c2, = st.columns([1,1])
	if c1.button("Показать код"):
		showcode_1()


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
		ax.set_xlabel('x', fontsize=12)
		ax.set_ylabel('y', fontsize=12)
		ax.set_zlabel('z', fontsize=12)
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
		ax.set_xlabel('x', fontsize=12)
		ax.set_ylabel('y', fontsize=12)
		ax.set_zlabel('z', fontsize=12)
		ax.plot_surface(x1, y1, z1, color="red")
		# Showing the above plot
		c1, c2, = st.columns([5,1]) 
		c1.pyplot(fig)
	def plot2ord():
		option = st.selectbox("Выберите поверхность",("Эллиптический параболоид", "Гиперболический параболоид", "Эллипсоид"),)
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
	"""
	Matplotlib поддерживает также и окраску поверхностей. 
	Для этого существует широкий выбор цветовых карт. Подробнее можно прочитать здесь:
	"""
	def plotcolored(colormap, a):
		x = np.linspace(-10, 10, 40)
		y = np.linspace(-10, 10, 40)
		n = len(x)
		m = len(y)
		X, Y = np.meshgrid(x, y)
		f = -(X**2+Y**2)
		Z = f+np.random.normal(f, 10, size=(m,n))
		print(Z)

		fig = plt.figure(figsize=(10, 8))
		ax = plt.axes(projection='3d')

		ax.plot_surface(X, Y, Z, cmap=colormap, alpha=a)

		ax.set_title('3D Contour', fontsize=14)
		ax.set_xlabel('x', fontsize=12)
		ax.set_ylabel('y', fontsize=12)
		ax.set_zlabel('z', fontsize=12)
		c1, c2, = st.columns([5,1]) 
		c1.pyplot(fig)
	def plot2ord_2():
		st.link_button("Цветовые карты Matplotlib", "https://matplotlib.org/stable/users/explain/colors/colormaps.html")
		option = st.selectbox("Выберите colormap",("plasma", "binary", "Reds", "hsv"),)
		a = st.slider("альфа", 0., 1., value = 0.5, step = 0.1)
		plotcolored(str(option), a)
	plot2ord_2()
	def showcode_2():
		code = '''
		def cos_pix2(x):
			return np.cos(x* np.pi/2)
		def sin_pix2(x):
			return np.sin(x* np.pi/2)
		def xpow2(x):
			return x**2
		def frac_1_x(x):
			return 1/x
		def plot_surface_fromfunc(f, domain_x, domain_y):
			fig = plt.figure()
			# defining a sub-plot with 1x2 axis and defining 
			# it as first plot with projection as 3D
			ax = fig.add_subplot(1, 2, 1, projection='3d')
			 
			x1= np.arange(domain_x[0], domain_x[1], domain_x[2])
			y1= np.arange(domain_y[0], domain_y[1], domain_y[2])
			 
			# Creating a mesh grid with x ,y and x1,
			# y1 which creates an n-dimensional
			# array
			x1,y1= np.meshgrid(x1,y1)
			z1= f(x1)
			ax.set_xlabel('x', fontsize=12)
			ax.set_ylabel('y', fontsize=12)
			ax.set_zlabel('z', fontsize=12)
			ax.plot_surface(x1, y1, z1, color="red")
			c1, c2, = st.columns([5,1]) 
			c1.pyplot(fig)
			
			
		def hyperbolic_paraboloid(x,y,a,b):
			return (0.5)*(x**2/a**2-y**2/b**2)
		def elliptic_paraboloid(x,y,a,b):
			return (0.5)*(x**2/a**2+y**2/b**2)
		def ellipsoid(x,y,a,b): #c = 1
			return np.sqrt(1-x**2/a**2-y**2/b**2) if (1-x**2/a**2-y**2/b**2).any () >0 else 0
		def plot_surface_2ord(f, a, b, domain_x, domain_y):
			fig = plt.figure()
			 
			# defining a sub-plot with 1x2 axis and defining 
			# it as first plot with projection as 3D
			ax = fig.add_subplot(1, 2, 1, projection='3d')
			x1= np.arange(domain_x[0], domain_x[1], domain_x[2])
			y1= np.arange(domain_y[0], domain_y[1], domain_y[2])
			 
			# Creating a mesh grid with x ,y and x1,
			# y1 which creates an n-dimensional
			# array
			x1,y1= np.meshgrid(x1,y1)
			z1= f(x1, y1, a,b)
			ax.set_xlabel('x', fontsize=12)
			ax.set_ylabel('y', fontsize=12)
			ax.set_zlabel('z', fontsize=12)
			ax.plot_surface(x1, y1, z1, color="red")
			c1, c2, = st.columns([5,1]) 
			c1.pyplot(fig)'''
		st.code(code, language = "python")
	
	c1, c2, = st.columns([1,1])
	if c1.button("Показать код"):
		showcode_2()

if menu == "Векторные поля":
	r"""
##### Векторные поля, или quiver plot -- функция Matplotlib, позволяющая строить произвольные векторные поля.
Рассмотрим пример: возьмем уже хорошо знакомый нам гиперболический параболоид и построим на его поверхности
 векторы градиенты $\nabla z$ задающей его функции $z=f(x,y)$.

	"""
	def hyperbolic_paraboloid(x,y,a,b):
		return (0.5)*(x**2/a**2-y**2/b**2)
	def plot_quiver3d(a, b, density, scale, normalize_flag):
		# Creating an empty figure
		# to plot a 3D graph
		fig = plt.figure()
		 
		# Creating a 3Dprojection for 
		# our 3D plots using fig.gca
		ax = fig.add_subplot(projection='3d')
		 
		# Creating a meshgrid for the range
		# of values in X,Y,Z
		
		x = np.linspace(-10, 10, int(30*density+10))
		y = np.linspace(-10, 10, int(30*density+10))
		X, Y = np.meshgrid(x, y)
		
		Z = hyperbolic_paraboloid(X, Y, a, b)
		 
		# Creating expressions for u,v,w
		# with the help of x,y and z
		# which will form the direction vectors
		u = X/a**2
		v = -Y/b**2
		norm = np.sqrt(u**2+v**2)
		norm_colors = Normalize()
		norm_flat = norm.flatten()
		colors = plt.cm.viridis(norm_colors(norm_flat))
		w = 0
		
		cbar = plt.colorbar(plt.cm.ScalarMappable(norm=norm_colors, cmap=plt.cm.viridis), ax=ax)
		cbar.set_label('Norm')
		#u = u/norm
		#v = v/norm
		# Creating a quiver plot with length of the direction
		# vector length as 0.2 ad normalise as true
		ax.plot_surface(X, Y, Z, cmap="plasma")
		ax.quiver(X, Y, Z, u, v, w, color = colors, length=scale, normalize=normalize_flag)
		 
		#showing the above plot
		c1, c2, = st.columns([5,1]) 
		c1.pyplot(fig)
	def quivers():
		a = st.slider("a", -10, 10, 1)
		b = st.slider("b", -10, 10, 1)
		density = st.slider("Плотность", 0., 1., step = 0.1, value = 0.5)
		scale = st.slider("Длина векторов", 0., 1., step = 0.1, value = 0.5)
		normalize_flag=False
		do_norm = st.checkbox("Нормировать векторы?")
		if do_norm:
			plot_quiver3d(a, b, density, scale, True)
		else:
			plot_quiver3d(a, b, density, scale, False)

	quivers()
	def showcode_3():
		code = '''
		def plot_quiver3d(a, b, density, scale, normalize_flag):
			fig = plt.figure()
			ax = fig.add_subplot(projection='3d')
			x = np.linspace(-10, 10, int(30*density+10))
			y = np.linspace(-10, 10, int(30*density+10))
			X, Y = np.meshgrid(x, y)
			
			Z = hyperbolic_paraboloid(X, Y, a, b)
			u = X/a**2
			v = Y/b**2
			norm = np.sqrt(u**2+v**2)
			norm_colors = Normalize()
			norm_flat = norm.flatten()
			colors = plt.cm.viridis(norm_colors(norm_flat))
			w = 0
			
			cbar = plt.colorbar(plt.cm.ScalarMappable(norm=norm_colors, cmap=plt.cm.viridis), ax=ax)
			cbar.set_label('Norm')
			
			ax.plot_surface(X, Y, Z, color="red")
			ax.quiver(X, Y, Z, u, v, w, color = colors, length=scale, normalize=normalize_flag)
			 
			c1, c2, = st.columns([5,1]) 
			c1.pyplot(fig)'''
		st.code(code, language = "python")
	
	c1, c2, = st.columns([1,1])
	if c1.button("Показать код"):
		showcode_3()
	
