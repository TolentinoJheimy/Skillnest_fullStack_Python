class SuscripcionStreaming:
    costos_suscripcion = {"Gratis": 0, "Estándar": 5.99, "Premium": 10.99}

    def __init__(self, usuario, tipo_suscripcion="Gratis"):
        self.usuario = usuario
        if tipo_suscripcion in SuscripcionStreaming.costos_suscripcion:
            self.tipo_suscripcion = tipo_suscripcion
        else:
            self.tipo_suscripcion = "Gratis"

        self.costo_mensual = SuscripcionStreaming.costos_suscripcion[self.tipo_suscripcion]
        self.saldo_pendiente = 0

    def realizar_pago(self, monto):
        if monto <= 0:
            print(f"{self.usuario}: El monto debe ser mayor que 0.")
            return

        self.saldo_pendiente -= monto
        if self.saldo_pendiente < 0:
            self.saldo_pendiente = 0

        print(f"{self.usuario} realizó un pago de ${monto:.2f}. Saldo pendiente: ${self.saldo_pendiente:.2f}")

    def cambiar_suscripcion(self, nuevo_tipo):
        if nuevo_tipo in SuscripcionStreaming.costos_suscripcion:
            self.tipo_suscripcion = nuevo_tipo
            self.costo_mensual = SuscripcionStreaming.costos_suscripcion[nuevo_tipo]
            print(f"{self.usuario} cambió a suscripción {nuevo_tipo}. Costo mensual: ${self.costo_mensual}")
        else:
            print("Tipo de suscripción inválido.")

    def ver_contenido_exclusivo(self):
        if self.tipo_suscripcion == "Gratis":
            print(f"{self.usuario} no tiene acceso a contenido exclusivo.")
        else:
            print(f"{self.usuario} está viendo contenido exclusivo en plan {self.tipo_suscripcion}.")

    def mostrar_info_suscripcion(self):
        print("Información de Suscripción:")
        print(f"Usuario: {self.usuario}")
        print(f"Tipo de suscripción: {self.tipo_suscripcion}")
        print(f"Costo mensual: ${self.costo_mensual}")
        print(f"Saldo pendiente: ${self.saldo_pendiente}")

    def generar_cobro_mensual(self):
        """Simula el cobro mensual."""
        self.saldo_pendiente += self.costo_mensual
        print(f"{self.usuario} ha sido cobrado ${self.costo_mensual}. Saldo pendiente: ${self.saldo_pendiente}")

# Crear 3 usuarios
usuario1 = SuscripcionStreaming("Juan", "Gratis")
usuario2 = SuscripcionStreaming("Luis", "Estándar")
usuario3 = SuscripcionStreaming("Daniel", "Premium")

# Cobros mensuales
usuario1.generar_cobro_mensual()
usuario2.generar_cobro_mensual()
usuario3.generar_cobro_mensual()

print(f"\n - {usuario1.usuario}: ")
usuario1.ver_contenido_exclusivo()
usuario1.cambiar_suscripcion("Premium")
usuario1.generar_cobro_mensual()
usuario1.realizar_pago(15)
usuario1.mostrar_info_suscripcion()

print(f"\n - {usuario2.usuario}: ")
usuario2.ver_contenido_exclusivo()
usuario2.cambiar_suscripcion("Premium")
usuario2.generar_cobro_mensual()
usuario2.realizar_pago(5)
usuario2.realizar_pago(10)
usuario2.mostrar_info_suscripcion()

print(f"\n - {usuario3.usuario}: ")
usuario3.realizar_pago(2)
usuario3.ver_contenido_exclusivo()
usuario3.mostrar_info_suscripcion()