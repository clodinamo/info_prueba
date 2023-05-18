porcentaje_comision: float = 0.06
nombre_vendedor: str = input('Ingrese el nombre del vendedor: ')
valor_venta: float = float(input('Ingrese el valor de la venta: $'))


def calcular_comision(
	valor_venta:float,
	porcentaje_comision: float) -> float:
	return valor_venta * porcentaje_comision

monto_comision