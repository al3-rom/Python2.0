"""
CUENTA BANCARIA
Crea una clase "CuentaBancaria" con atributos como número de cuenta y
saldo. Implementa métodos para depositar y retirar dinero, y muestra el
saldo actual.

"""

class CuentaBancaria:
    def __init__(self,numero_cuenta, saldo):
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo
        print(f"Tienes en la cuenta {self.numero_cuenta}: {self.saldo}")

    def depositar_dinero(self,cantidad):
        self.saldo += cantidad
        print(f"Deposito con exito! Has depositado {cantidad}. Ahora tienes en tu cuenta {self.numero_cuenta}:{self.saldo} $")
    
    def retirar_dinero(self,cantidad):
        if cantidad > self.saldo:
            print(f"No tienes saldo suficiente! Tienes en la cuenta:{self.numero_cuenta}:{self.saldo} $")
        else:
            self.saldo -= cantidad
            print("Retiro con exito! Has retirado",cantidad,
                   "Te quedan :", self.saldo, "$", "en tu cuenta",self.numero_cuenta)
            
    def mostrar_saldo(self):
        print(f"Tu saldo actual en tu cuenta {self.numero_cuenta} es {self.saldo}")
Cuenta1 = CuentaBancaria(1,1500)
Cuenta2 = CuentaBancaria(2,3000)

Cuenta1.depositar_dinero(200)
Cuenta2.depositar_dinero(300)

Cuenta1.retirar_dinero(1600)
Cuenta2.retirar_dinero(2000)

Cuenta1.mostrar_saldo()
Cuenta2.mostrar_saldo()

