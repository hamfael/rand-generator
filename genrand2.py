from random import uniform
import csv

def gen_random(start, end, quantity):
	i = 0
	rnd_list = []
	while i < quantity:
		rnd_list.append(uniform(start, end))
		i += 1
	rnd_list = sorted(rnd_list)
	with open('randomico.csv', mode='w', newline='') as randomico:
		randomico_writer = csv.writer(randomico)
		for num in rnd_list:
			csv_list = [num]
			randomico_writer.writerow(csv_list)
	randomico.close()
	print("FEITO!")
	

print("*********GERADOR DE RANDOMICOS*********")
print("\n")
a = float(input("Numero inicial: "))
print("\n")
b = float(input("Numero final: "))
print("\n")
q = int(input("quantidade entre: "))
print("\n")
gen_random(a, b, q)
print("\n")
input("Pressione ENTER pra finalizar")