# -*- coding: utf-8 -*-



def add(a, b):
   """This program adds two
   numbers and return the result"""

   result = a + b
   return result



''' ASK 1'''
class Colour(object):
	def __init__(self, r, g, b):
		'''Create a Colour with red equal to r, green equal to g, add blue equal to b.'''
		self.red = r
		self.green = g
		self.blue = b
	
	def lightness(self):
		'''Lightness of Colour self.'''
		return 0.5 * (max(self.red, self.green, self.blue) + min(self.red, self.green, self.blue))/255


##############################################################################################
''' ASK 2'''
##############################################################################################

class BankAccount:
	def __init__(self, name, afm, poso):
		self.name = name
		self.afm = afm
		self.poso = poso

	def katathesi(self, x):
		self.poso += x

	def analipsi(self, x):
		self.poso -= x

	def ypoloipo(self):
		return self.poso

	def __str__(self):
		s = '%s, %s, lefta: %s' % (self.name, self.surname, self.poso)
		return s



##############################################################################################
''' ASK 3'''
##############################################################################################
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return str(self.x) + ',' + str(self.y)

    def simx(self):
        return Point(self.x, -self.y)

    def simy(self):
        return Point(-self.x, self.y)

    def sim0(self):
        return Point(-self.x, -self.y)


##############################################################################################
''' ASK 4'''
##############################################################################################
class Rectangle:
    def __init__(self,x0,y0,x1,y1):
        self.x0=x0
        self.y0=y0
        self.x1=x1
        self.y1=y1
    def area(self):
        base=self.x1-self.x0
        height=self.y1-self.y0
        return base*height
    def contains(self,x,y):
        return (self.x0<=x<=self.x1) and  (self.y0<=y<=self.y1)    #return TRUE or FALSE



##############################################################################################
''' ASK 5'''
##############################################################################################
import math 
class Vec2D:
        def __init__(self, x, y):
                self.x = x
                self.y = y

        def __add__(self, other):
                xnew = self.x + other.x
                ynew = self.y + other.y
                return Vec2D(xnew, ynew)  ## EPISTREFEI ANTIKEIMENO THS KLASHS Vec2D

        def __sub__(self, other):
                xnew = self.x - other.x
                ynew = self.y + other.y	
                return Vec2D(xnew, ynew)  ## EPISTREFEI ANTIKEIMENO THS KLASHS Vec2D

        def __mul__(self, other):
                return self.x*other.x + self.y*other.y  ### prosoxh epistrefei ARITHMO !!!!!!!

        def __abs__(self):
                return math.sqrt(self.x**2 + self.y**2)   ### to metro enos dian/tos einai h tetrag.riza tou athroismatos twn tetragwnwn twn x,y !

        def __eq__(self, other):
                return self.x == other.x and self.y == other.y

        def __str__(self):
                return '(%s, %s)' % (self.x, self.y)

##############################################################################################
''' ASK 6'''
##############################################################################################


class fraction(object):

	def __init__(self, ar, par):
		self.ar=ar
		self.par=par

	def getar(self):
		return self.ar

	def getpar(self):
		return self.par

	def value(self): ### epistrefei thn timh tou klasmatos !!! kanei dld thn diairesh !!!!
		return self.ar/self.par

	def __str__(self):    ### epistrefei to string pou tha typwnetai otan typwnoume ena antikeimeno ths klashs fraction
		return '%s/%s'%(self.ar,self.par)

	def __add__(self,other): 
		neoAr=self.ar*other.par+self.par*other.ar
		neoPar=self.par*other.par
		return fraction(neoAr,neoPar)  ## EPISTREFEI ena neo ANTIKEIMENO THS KLASHS fraction

	def __neg__(self):
		return fraction(-self.ar,self.par)  ## EPISTREFEI ena neo ANTIKEIMENO THS KLASHS fraction

	def __sub__(self,other):
		neoAr=self.ar*other.par-self.par*other.ar
		neoPar=self.par*other.par
		return fraction(neoAr,neoPar) ## EPISTREFEI ena neo ANTIKEIMENO THS KLASHS fraction

	def __mul__(self,other): 
		neoAr=self.ar*other.ar
		neoPar=self.par*other.par
		return fraction(neoAr,neoPar)   ## EPISTREFEI ena neo ANTIKEIMENO THS KLASHS fraction

	def __truediv__(self,other): 
		neoAr=self.ar*other.par
		neoPar=self.par*other.ar
		return fraction(neoAr,neoPar) ## EPISTREFEI ena neo ANTIKEIMENO THS KLASHS fraction




########### askhsh bonus !!!

'''Φτιάξτε μια κλάση time που θα δέχεται σαν ορίσματα ώρα λεπτά δευτερόλεπτα και θα επιστρέφει την ώρα σε 24ωρη μορφη, +++ να φτιάξετε μια μέθοδο που θα προσθέτει χρόνους
με προσοχή στο τι γίνεται αν τα λεπτά και τα δευτερόλεπτα γίνουν πάνω απο 59'''


class time():
    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s
        
    def __str__(self):
        return 'H wra einai: %sh :%s m %s s' %(self.h, self.m, self.s)

    def __add__(self,other):
         new_h=self.h+other.h
         new_m=self.m+other.m   
         new_s=self.s+other.s
         if new_s>59:
             new_m +=1
             new_s-=60
         if new_m>59:
             new_h +=1
             new_m -=60
         return time(new_h,new_m,new_s)

class time_London(time):
    def __init__(self, h, m, s, r):
        time.__init__(self, h, m, s)
        self.r = r

    

### h 7 einai ektos ulhs !!!!!!s
########## APO EDW KAI KATW MH TIS DEITE ...AN DE THELETE !!!!!!!!!!!!!!!!! :) :) :) 

##############################################################################################
''' ASK 8'''
##############################################################################################
class Lesson:
    def __init__(self, name, code, year, teachers):
        self.name = name
        self.code = code
        self.year = year
        self.teachers = teachers
        self.students = []
    
    def set_grading(self, assignments, mid_term, exam):
        self.assignments = assignments
        self.mid_term = mid_term
        self.exam = exam

    def enroll(self, student):
        self.students.append(student)

    def final_grades(self, grades):
        for student in sorted(grades):
            grade = self.assignments * grades[student]['assignments'] +\
                    self.mid_term * grades[student]['mid_term'] +\
                    self.exam * grades[student]['exam']
            print(student, "->", grade)

    def __str__(self):
        teachers = ', '.join(self.teachers)
        total_students = len(self.students)
        return '{}-{} {}, {} : {} students:'.format(self.code, self.name,    \
                                          self.year, teachers, total_students)
 
