#coding=utf-8
#这里学习类、继承、多态
#学习完：获取对象信息。 接下来是：面向对象高级编程

class Student(object):   #这是一个类：1、类的名称一般都大写；2、括号中是这个类的继承类，如果没有继承，则写object
	def __init__(self, name, sex, score):  #这里可以理解为模板参数，将这一类中所有共有的参数都直接写进来。创建实例时必须要携带这些参数。self是本身就有的，不用传参数
		self.__name = name   #__代表这个参数是私有的。不能从外部访问
		self.score2 = score  #我们从外部设定内部参数值的时候，实际上是设定前面score2的值。例如：tony.score2=33
		self.sex = sex

	def get_name(self):
		return self.__name
	def get_score(self):
		return self.score2

	def print_score(self):
		print "%s: %s"%(self.__name, self.score2)

	def print_sex(self):
		print "%s: %s"%(self.__name, self.sex)

	def get_grade(self):
		if self.score2>=90:
			return "A"
		elif self.score2>=60:
			return "B"
		else:
			return "C"


#Animall类
class Animal(object):
	def run(self):
		print "Animal is running!"


class Dog(Animal):
	def __init__(self, name):
		self.name = name
	def print_name(self):
		print self.name

	def eating(self):
		print "Dog is eating meat."

	def run(self):
		print "Dog is running."


class Cat(Animal):
	def fund_mouse(self):
		print "Cat is finding mouse."

	def run(self):
		print "Cat is running."

class Country(object):
	def __init__ (self, name, color, area, peoples):
		self.name = name
		self.color = color
		self.area = area
		self.peoples = peoples
	def power(self):
		print "国家实力体现在面积和人口上："
		print "%s的人口是：%d；面积是：%d。国力是：%d" %(self.name, self.peoples, self.area, self.peoples*self.area)






if __name__ == '__main__':

	#这里是Student类的外部调用
	tony = Student('Tony','male',88)  #这是一个实例。实例=类名（） 这样来实现。
	lisa = Student('Lisa','female',99)  #这也是一个实例。每个实例的数据可能不同，但是方法都是一致的。都是类中的方法。
	#print tony.__score  #访问限制了。 __的参数是私有的，不能在外部访问
	tony.score2=33
	print tony.get_score()

	tony.print_score()
	lisa.print_score()
	tony.print_sex()
	tony.nianji = ('3') #这里可以动态绑定一个额外的参数给实例
	print tony.nianji

	print tony.get_grade()
	print lisa.get_grade()


	#这里是Animal类的外部调用
	my_dog = Dog('Ben')
	my_dog.print_name()
	my_dog.run()
	my_dog.eating()

	my_cat = Cat()
	my_cat.run()
	my_cat.fund_mouse()

	SSS = Animal()

	def run_twice(A): #定义这个函数，调用animall中的run方法。如果传的数据类型不同，则显示不同的run方法。比如传cat，就显示Cat中的run()
		A.run()
		A.run()
	run_twice(my_cat)

	print type(SSS)  #type函数用∫来显示变量的类型
	print isinstance(my_cat,Animal)#用来判断每个实例是否是某个类型。形式： isinstance(实例,类名)


	#这里是Country类的外部调用
	China = Country("China", "Red", 9600000, 1300000000)
	China.power()

	Japan = Country("Japan", "White", 77623, 188888888)
	Japan.power()