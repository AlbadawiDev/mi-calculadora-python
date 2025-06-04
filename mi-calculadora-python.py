def calculadora(a, b):
    print(f"Suma: {a + b}")
    print(f"Resta: {a - b}")
    print(f"Multiplicación: {a * b}")
    print(f"División: {a / b if b != 0 else '∞'}")

def main():
    a = float(input("Ingrese el primer valor: "))
    b = float(input("Ingrese el segundo valor: "))
    calculadora(a, b)

if __name__ == "__main__":
    main()
