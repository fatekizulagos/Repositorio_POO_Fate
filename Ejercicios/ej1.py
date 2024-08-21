# Tomando el código que hemos estado trabajando en la última clase, se solicita agregar nuevas
# Propiedades a la clase Persona:
class Persona():

    # Constructor de clase
    def __init__(self, nombre, apellido, edad,altura, peso):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.altura = float(altura)
        self.peso = float(peso)

    #Métodos (Comportamientos) (Deben estar dentro de la clase)
    def hablar(self):
        print(f"{self.nombre} está hablando") 

    def caminar(self):
        print(f"{self.nombre} está caminando")

    def calcular_imc(self): 
        imc = (self.peso / (self.altura**2))

        if imc < 18.5:
            print(f" El imc de {self.nombre} es de {imc}. Según su imc se encuentra con un peso insuficiente.")
        elif imc >= 18.5 and imc < 25:
            print(f" El imc de {self.nombre} es de {imc}. Según su imc se encuentra con un peso ideal y dentro del rango saludable.")    
        else:
            print(f" El imc de {self.nombre} es: {imc}. Según su imc se encuentra sobre peso, lo cuál es peligroso para su salud.")
        return imc





    
# Creacion de un objeto de la clase  Persona / Instanciando clase

persona1 = Persona("Rocio", "Cardenas", 27, 1.53, 63)
persona2 = Persona("Benjamin", "Concha", 19, 1.71, 60)

# imprimiendo 

persona2.calcular_imc()
persona1.calcular_imc()