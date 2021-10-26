class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        if (color == "rojo" or color == "verde" or color == "amarillo" or color == "negro" or color == "blanco"):
            self.color = color

class Auto:
    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = list(asientos)
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos(self):
        num = 0
        for i in self.asientos:
            if isinstance(i, Asiento):
                num += 1
        return num

    def verificarIntegridad(self):
        bandera = True
        for i in self.asientos:
            if i != self.registro:
                bandera = False

        if (self.registro != self.motor.registro):
            bandera = False

        if bandera:
            return "Auto original"
        else:
            return "Las piezas no son originales"

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo(self, tipo):
        if (tipo == "electrico" or tipo == "gasolina"):
            self.tipo = tipo



        








        