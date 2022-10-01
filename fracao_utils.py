class FracaoUtils:
	def mmc(fracao1, fracao2):
		divisores = []
		
		selfDen = fracao1.denominador
		fracDen = fracao2.denominador
		divisor = 2
		while (selfDen > 1 or fracDen > 1):
			if (selfDen % divisor == 0 or fracDen % divisor == 0):
				divisores.append(divisor)
				if (selfDen % divisor == 0):
					selfDen /= divisor
				elif (fracDen % divisor == 0):
					fracDen /= divisor
				continue

			divisor += 1

		mmc = 1
		for x in divisores:
			mmc *= x
  
		return mmc