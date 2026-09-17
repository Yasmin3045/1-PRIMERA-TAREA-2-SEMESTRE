"CLASE PADRE"
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.saldo = saldo_inicial
    def mostrar_datos(self):
        return f"Titular: {self.titular} | Saldo Actual: ${self.saldo:.2f}"
    def depositar(self, monto):
        self.saldo += monto
        return f"Has depositado ${monto}. Nuevo saldo: ${self.saldo:.2f}"
    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            return f"Has retirado ${monto}. Nuevo saldo: ${self.saldo:.2f}"
        else:
            return "Fondos insuficientes para realizar el retiro."

"CLASES HIJAS"
class CuentaDeAhorros(CuentaBancaria):
    def __init__(self, titular, saldo_inicial, tasa_interes):
        super().__init__(titular, saldo_inicial)
        self.tasa_interes = tasa_interes 
    def aplicar_intereses(self):
        interes_ganado = self.saldo * self.tasa_interes
        self.saldo += interes_ganado
        return f"Intereses aplicados (+${interes_ganado:.2f}). Nuevo saldo: ${self.saldo:.2f}"

class CuentaCorriente(CuentaBancaria):
    def __init__(self, titular, saldo_inicial, limite_sobregiro):
        super().__init__(titular, saldo_inicial)
        self.limite_sobregiro = limite_sobregiro  
    def retirar(self, monto):
        if monto <= (self.saldo + self.limite_sobregiro):
            self.saldo -= monto
            return f"Retiro exitoso de ${monto}. Saldo actual: ${self.saldo:.2f}"
        else:
            return "Retiro rechazado: Supera el límite de sobregiro permitido."
print("---CUENTA DE AHORROS---")
cuenta_ahorros = CuentaDeAhorros("Oscar Osorio", 1000, 0.05) # 5% de interés
print(cuenta_ahorros.mostrar_datos())
print(cuenta_ahorros.depositar(500))
print(cuenta_ahorros.aplicar_intereses())
print(cuenta_ahorros.retirar(200))

print("---CUENTA CORRIENTE---")
cuenta_corriente = CuentaCorriente("Arianna Ramos", 500, 300) 
print(cuenta_corriente.mostrar_datos())
print(cuenta_corriente.retirar(700)) 
print(cuenta_corriente.mostrar_datos())
