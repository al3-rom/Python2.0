"""
Supongamos que estás construyendo un sistema de gestión de empleados
para una empresa. Crea un sistema de clases que maneje la información de
los empleados, incluyendo empleados a tiempo completo y empleados a
tiempo parcial.
- Clase base: `Empleado`
 - Atributos: nombre, apellido, salario base
- Clase derivada: `EmpleadoTiempoCompleto` (hereda de `Empleado`)
 - Atributo adicional: bono anual
- Clase derivada: `EmpleadoTiempoParcial` (hereda de `Empleado`)
 - Atributo adicional: horas trabajadas por semana
Resuelve el problema creando instancias de estas clases y calculando los
salarios totales para diferentes tipos de empleados.

"""

class Empleado:
    def __init__(self,nombre,apellido,salario_base):
        self.nombre = nombre
        self.apellido = apellido
        self.salario_base = salario_base
    
    def mostrar_empleado(self):
        print(f"El empleado {self.nombre} {self.apellido} cobra {self.salario_base}$")
    

class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, apellido, salario_base,bono_anual):
        super().__init__(nombre, apellido, salario_base)
        self.bono_anual = bono_anual
    
    def mostrar_empleado(self):
        print(f"El empleado {self.nombre} {self.apellido} cobra {self.salario_base}$ al mes y dispone a bono anual de {self.bono_anual}")
        

class EmpleadoTiempoParcial(Empleado):
    def __init__(self, nombre, apellido, salario_base, horas_semana):
        super().__init__(nombre, apellido, salario_base)
        self.horas_semana = horas_semana
    
    def salario_total(self):
        return self.horas_semana * 4 * self.salario_base
    
    def mostrar_empleado(self):
        print(f"El empleado {self.nombre} {self.apellido} cobra {self.salario_base}$ por hora, su salario total por {self.horas_semana * 4} horas en un mes es {self.salario_total()}" )

empleado1 = Empleado("Alejandro","Romero",1250)
empleado2 = EmpleadoTiempoCompleto("Alex", "Chitenco", 1500, 3000)
empleado3 = EmpleadoTiempoParcial("Alvaro", "StriclyHipHop",12,40)

empleado1.mostrar_empleado()

empleado2.mostrar_empleado()

empleado3.mostrar_empleado()
    


