class CuentaBancaria:
    def __init__(self, nombre, saldo_inicial=0):
        """Constructor: Inicializa el nombre del titular y el saldo de la cuenta."""
        self.nombre = nombre
        self.saldo = saldo_inicial
        print(f'Cuenta de {self.nombre} abierta con un saldo inicial de {self.saldo}.')

    def depositar(self, monto):
        """Método para depositar dinero en la cuenta."""
        self.saldo += monto
        print(f'Depósito de {monto} realizado. Nuevo saldo: {self.saldo}.')

    def retirar(self, monto):
        """Método para retirar dinero de la cuenta."""
        if monto > self.saldo:
            print("Fondos insuficientes.")
        else:
            self.saldo -= monto
            print(f'Retiro de {monto} realizado. Nuevo saldo: {self.saldo}.')

    def __del__(self):
        """Destructor: Realiza el cierre de la cuenta y muestra el saldo final."""
        print(f'Cuenta de {self.nombre} cerrada con saldo final de {self.saldo}.')


# Crear y usar el objeto
cuenta = CuentaBancaria('Luis', 500)
cuenta.depositar(200)
cuenta.retirar(100)
del cuenta  # Destructor llamado aquí