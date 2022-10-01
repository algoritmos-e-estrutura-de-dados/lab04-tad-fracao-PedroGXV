from fracao_utils import FracaoUtils

class Fracao:
	numerador = 1
	denominador = 1

	def __init__(self, numerador, denominador):
		self.numerador = numerador
		self.denominador = denominador

	def somar(self, fracao):
		# caso tenha denominadores iguais
		if (self.denominador == fracao.denominador):
			return Fracao(
				self.numerador + fracao.numerador,
				self.denominador
			)
		
		mmc = FracaoUtils.mmc(self, fracao)

		numerador1 = ((mmc / self.denominador) * self.numerador)
		numerador2 = ((mmc / fracao.denominador) * fracao.numerador)

		return Fracao(numerador1 + numerador2, mmc)

	def subtrair(self, fracao):
		mmc = FracaoUtils.mmc(self, fracao)

		numerador1 = ((mmc / self.denominador) * self.numerador)
		numerador2 = ((mmc / fracao.denominador) * fracao.numerador)

		return Fracao(numerador1 - numerador2, mmc)

	def multiplicar(self, fracao):
		return Fracao(
			self.numerador * fracao.numerador, 
			self.denominador * fracao.denominador, 
		)

	def dividir(self, fracao):
		return Fracao(
			self.numerador * fracao.denominador, 
			self.denominador * fracao.numerador
		)

	def simplificar(self):
		return self
	def valorReal(self):
		return self.numerador / self.denominador

	def __str__(self):
		return f"{self.numerador} / {self.denominador}"