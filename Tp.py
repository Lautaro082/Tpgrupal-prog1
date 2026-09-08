#Integrantes:Lautaro Nicolas Dominguez, Nahieli Celeste Insfran

# Ejercicio 1: Funciones puras con parámetros opcionales y keyword arguments
def calcular_factura_final(
    monto_base: float,
    impuesto: float = 21.0,
    descuento: float = 0.0,
    envio_prioritario: float | None = None,
) -> float:
  subtotal = monto_base * (1 - descuento / 100)
  total_con_impuesto = subtotal * (1 + impuesto / 100)
  if envio_prioritario is not None:
    total_con_impuesto += envio_prioritario
  return round(total_con_impuesto, 2)


print(calcular_factura_final(1000.0))
print(calcular_factura_final(1000.0, descuento=10.0))
print(
    calcular_factura_final(
        1000.0, impuesto=10.0, descuento=5.0, envio_prioritario=150.0
    )
)


# Ejercicio 2: Métodos Estáticos (@staticmethod) como Librería de Utilidades
class ValidadorFinanciero:

  @staticmethod
  def es_cuit_valido(cuit: str) -> bool:
    return cuit.isdigit() and len(cuit) == 11

  @staticmethod
  def convertir_moneda(
      monto: float, tasa_cambio: float, comision: float = 0.02
  ) -> float:
    monto_convertido = monto * tasa_cambio
    monto_final = monto_convertido * (1 - comision)
    return monto_final


print(ValidadorFinanciero.es_cuit_valido("20384920194"))
print(ValidadorFinanciero.es_cuit_valido("20-38492019-4"))
print(ValidadorFinanciero.convertir_moneda(100.0, 1000.0, comision=0.05))


# Ejercicio 3: Interacción Inter-Clase, Métodos de Instancia y Delegación
class Notificador:

  def enviar_recibo(self, cliente: str, total: float) -> None:
    print("--- RECIBO DE PAGO ---")
    print(f"Cliente: {cliente}")
    print(f"Total abonado: ${total:.2f}")
    print("----------------------")


class ProcesadorPagos:

  def __init__(self, notificador: Notificador | None = None):
    self.notificador = notificador if notificador else Notificador()

  def procesar_transaccion(
      self, cliente: str, items: list[dict], descuento_cupon: float = 0.0
  ) -> float:
    subtotal = sum(item["precio"] for item in items)
    total = subtotal - descuento_cupon
    if total < 0:
      total = 0.0
    self.notificador.enviar_recibo(cliente, total)
    return total


carrito = [{"nombre": "Teclado", "precio": 50.0}, {"nombre": "Mouse", "precio": 30.0}]
procesador = ProcesadorPagos()
procesador.procesar_transaccion("Ana Gómez", carrito, descuento_cupon=10.0)


# Ejercicio 4: Manejo de Aridad Variable (*args y **kwargs)
def generar_auditoria_sistema(
    modulo: str, *mensajes: str, **metadatos
) -> str:
  reporte = f"MÓDULO: {modulo.upper()}\n"
  reporte += "--- EVENTOS ---\n"
  for i, mensaje in enumerate(mensajes, start=1):
    reporte += f"[{i}] {mensaje}\n"
  reporte += "--- METADATOS ---\n"
  for clave, valor in metadatos.items():
    reporte += f"{clave.upper()}: {valor}\n"
  return reporte


log = generar_auditoria_sistema(
    "auth", "Intento fallido", "Bloqueo de IP", usuario="admin", ip="192.168.1.10"
)
print(log)


# Ejercicio 5: Sistema Integrador (POO, Estáticos, Métodos y Kwargs)
class CalculadoraFitness:

  @staticmethod
  def calcular_imc(peso_kg: float, altura_m: float) -> float:
    if altura_m == 0:
      return 0.0
    return peso_kg / (altura_m**2)

  @staticmethod
  def clasificar_nivel(imc: float) -> str:
    if imc < 18.5:
      return "Bajo peso"
    elif imc < 25.0:
      return "Normal"
    else:
      return "Sobrepeso"


class Atleta:

  def __init__(self, nombre: str, peso: float, altura: float):
    self.nombre = nombre
    self.peso = peso
    self.altura = altura

  def obtener_reporte(
      self, incluir_recomendacion: bool = False, **metricas_extra
  ) -> str:
    imc = CalculadoraFitness.calcular_imc(self.peso, self.altura)
    nivel = CalculadoraFitness.clasificar_nivel(imc)

    reporte = f"--- REPORTE DE ATLETA: {self.nombre} ---\n"
    reporte += f"Peso: {self.peso} kg | Altura: {self.altura} m\n"
    reporte += f"IMC: {imc:.2f} ({nivel})\n"

    if metricas_extra:
      reporte += "--- MÉTRICAS EXTRA ---\n"
      for clave, valor in metricas_extra.items():
        reporte += f"{clave.replace('_', ' ').capitalize()}: {valor}\n"

    if incluir_recomendacion:
      reporte += "--- RECOMENDACIÓN ---\n"
      if nivel == "Bajo peso":
        reporte += (
            "Se sugiere aumentar la ingesta calórica y sumar ejercicios de"
            " fuerza.\n"
        )
      elif nivel == "Normal":
        reporte += (
            "¡Felicitaciones! Mantén tu rutina actual de alimentación y"
            " entrenamiento.\n"
        )
      else:
        reporte += (
            "Se recomienda planificar un leve déficit calórico y sumar"
            " ejercicio aeróbico.\n"
        )

    return reporte


atleta1 = Atleta("Carlos Pérez", 78.5, 1.75)
print(
    atleta1.obtener_reporte(
        incluir_recomendacion=True,
        frecuencia_cardiaca_reposo=58,
        horas_sueno=7.5,
        hidratacion_litros=3.0,
    )
)
