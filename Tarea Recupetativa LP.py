from math import sqrt, pi
from pyDatalog import pyDatalog
import pprint #solo para ver mejor la salida

class FiguraPlana:
    def __init__(self, color):
        self.color = color
        
    def area(self):
        pass

    def perimetro(self):
        pass

class Cuadrado(FiguraPlana):
    def __init__(self, lado, color):
        super().__init__(color)
        self.lado = lado
    
    def area(self):
        area = lambda lado: lado ** 2
        return area
    
    def perimetro(self):
        perimetro = lambda lado: lado * 4
        return perimetro

class Triangulo(FiguraPlana):
    def __init__(self, a, b, c, color):
        super().__init__(color)
        self.a = a
        self.b = b
        self.c = c
    
    def area(self):
        #s = (a+b+c)/2
        s = (self.a + self.b + self.c) / 2
        area = lambda a, b, c: sqrt(s * (s - a) * (s - b) * (s - c))
        return area
    
    def perimetro(self):
        perimetro = lambda a, b, c: a + b + c
        return perimetro
    
class FiguraNoPoliedro:
    def superficie(self):
        pass

    def volumen(self):
        pass

class Esfera(FiguraNoPoliedro):
    def __init__(self, radio):
        self.radio = radio
    
    def superficie(self):
        superficie = lambda radio: 4 * pi * (radio ** 2)
        return superficie
    
    def volumen(self):
        volumen = lambda radio: (4/3) * pi * (radio ** 3)
        return volumen

class FiguraPoliedro:
    def superficie(self):
        pass

    def volumen(self):
        pass
    
class Cubo(FiguraPoliedro):
    def __init__(self, arista):
        self.arista = arista
    
    def superficie(self):
        superficie = lambda arista: 6 * (arista ** 2)
        return superficie
    
    def volumen(self):
        volumen = lambda arista: arista ** 3
        return volumen

#prueas
#se usa el ()(valor que se quiere evaluar) para llamar a la funcion lambda dentro del metodo es como hacer dos llamadas .area() -> lambda() -> valor
cuadrado = Cuadrado(5, "azul")
print("----- Cuadrado -----")
print("Color del cuadrado:", cuadrado.color)
print("Área del cuadrado:", cuadrado.area()(cuadrado.lado))
print("Perímetro del cuadrado:", cuadrado.perimetro()(cuadrado.lado))

tri = Triangulo(3, 4, 5, "rojo")
print("----- Triángulo -----")
print("Color del triángulo:", tri.color)
print("Área del triángulo:", tri.area()(tri.a, tri.b, tri.c))
print("Perímetro del triángulo:", tri.perimetro()(tri.a, tri.b, tri.c))

esfera = Esfera(4)
print("----- Esfera -----")
print("Superficie de la esfera:", esfera.superficie()(esfera.radio))
print("Volumen de la esfera:", esfera.volumen()(esfera.radio))

cubo = Cubo(3)
print("----- Cubo -----")
print("Superficie del cubo:", cubo.superficie()(cubo.arista))
print("Volumen del cubo:", cubo.volumen()(cubo.arista))

pyDatalog.create_terms('es_un, tiene_color, tiene_perimetro, tiene_area, tiene_superficie, tiene_volumen, X, Y')


#Relacion con las figuras
# hecho nombre(dato 1, dato 2) el nombre es la relacion
+ es_un("Cuadrado","FiguraPlana")
+ es_un("Triangulo","FiguraPlana")
+ es_un("Esfera","FiguraNoPoliedro") 
+ es_un("Cubo","FiguraPoliedro")


#Relacion con los tipos de figuras
#Cuadrado /trianguloes plano por lo que tiene color, perimetro y area
#Esfera es no poliedro por lo que tiene volumen y superficie
#Cubo es poliedro por lo que tiene volumen, superficie

# conclucion(x,y) <= condicion1(x,z) & condicion2(z,y)
# el <= es un si

#Cuadrado/triangulo -> FiguraPlana -> tiene color, perimetro, area
#Esfera -> FiguraNoPoliedro -> tiene superficie, volumen
#Cubo -> FiguraPoliedro -> tiene superficie, volumen

tiene_area(X) <= es_un(X, 'FiguraPlana')
tiene_perimetro(X) <= es_un(X, 'FiguraPlana')
tiene_color(X, Y) <= es_un(X, 'FiguraPlana')

tiene_superficie(X) <= es_un(X, 'FiguraNoPoliedro')
tiene_volumen(X) <= es_un(X, 'FiguraNoPoliedro')

tiene_superficie(X) <= es_un(X, 'FiguraPoliedro')
tiene_volumen(X) <= es_un(X, 'FiguraPoliedro')



#salida

diccionario_prueba = {
    "Cuadrado": {
        "color": "azul",
        "lado": 5,
        "area": cuadrado.area()(cuadrado.lado),
        "perimetro": cuadrado.perimetro()(cuadrado.lado),
        "tiene color": bool(pyDatalog.ask('tiene_color("Cuadrado",Y)')),

        #parte logica estas se saben que dan verdadero
        "es un figura plana": bool(pyDatalog.ask('es_un("Cuadrado","FiguraPlana")')),
        "tiene area" : bool(pyDatalog.ask('tiene_area("Cuadrado")')),
        "tiene perimetro": bool(pyDatalog.ask('tiene_perimetro("Cuadrado")')),
        
        #estas dan falso
        "es un figura no poliedro": bool(pyDatalog.ask('es_un("Cuadrado","FiguraNoPoliedro")')),
        "es un figura poliedro": bool(pyDatalog.ask('es_un("Cuadrado","FiguraPoliedro")')),
        "tiene superficie": bool(pyDatalog.ask('tiene_superficie("Cuadrado")')),
        "tiene volumen": bool(pyDatalog.ask('tiene_volumen("Cuadrado")'))
    }
}

pprint.pprint(diccionario_prueba)

print("\n--- prueba de logica ---")

print("Figuras con area:")
print(tiene_area(X))

print("Figuras con volumen:")
print(tiene_volumen(X))

print("Figuras con perimetro:")
print(tiene_perimetro(X))

print("Figuras con superficie:")
print(tiene_superficie(X))


# Consideraciones
# En la parte 2 la programacion funcional se aplica dentro de las clases de figuras geometricas. lo que permite el uso de self y el poder llamarlas al tiro si es necesario pero hay que usar el doble (), entoces una llamada para obtener un metodoq ueda como objeto.metodo()()
#Si se quiere comprobar con otra figura es cosa de copiar la estructura del diccionario y cambiat el cuadrado y la informaion por la correspondiente

#Nombre: Benjamin Campos Fernandez
#Rol: 202473094-0