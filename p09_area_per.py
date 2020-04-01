#Programa que calcula el área y el perímetro de un triángulo, un rectángulo y un trapecio

B = 7
b = 5
h = 8
l = 3

def medida_triangulo(b, h):
	return (b*h) / 2, b*3

val1, val2 = medida_triangulo(b, h)

print("El perímetro del triángulo es {}".format(val2))
print("El área del triángulo es {}".format(val1))

def medida_rectangulo(b, h):
	return b*h, b*4

val3, val4 = medida_rectangulo(b, h)

print("El perímetro del rectángulo es {}".format(val4))
print("El área del rectángulo es {}".format(val3))

def medida_trapecio(b, B, h, l):
	return b+B+2*l, (h*(b+B))/2

val5, val6 = medida_trapecio(b, B, h, l)

print("El perímetro del trapecio es {}".format(val5))
print("El área del trapecio es {}".format(val6))