def main():
    a = float(input("Ingrese el primer valor: "))
    b = float(input("Ingrese el segundo valor: "))

    print(f"Suma: {a + b}")
    print(f"Resta: {a - b}")
    print(f"Multiplicación: {a * b}")
    print(f"División: {a / b if b != 0 else '∞'}")


if __name__ == "__main__":
    main()
