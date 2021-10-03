
sexo = int(input("Escolha: 1- Sexo Masculino / 2- Sexo Feminino: "))
h = float(input("Altura:"))


peso_ideal = (72.7*h) - 58 if sexo == 1 else (62.1*h) - 44.7

if sexo == 1:
	print("seu peso ideal é:",peso_ideal)
else:
	print("seu peso ideal é:",peso_ideal)

