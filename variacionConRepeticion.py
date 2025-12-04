# Programa: variación con repetición VR(n, k)

# Mantenemos la función factorial aunque ya no la usemos para la VR
def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

n = int(input("Ingresa n (total de elementos): "))
k = int(input("Ingresa k (lugares a ordenar): "))

# En la variación con repetición, k puede ser mayor que n. 
# Solo validamos que n y k sean positivos.
if n < 0 or k < 0:
    print("n y k deben ser números no negativos.")
else:
    VR = n ** k 
    
    print("VR(", n, ",", k, ") =", VR) 


