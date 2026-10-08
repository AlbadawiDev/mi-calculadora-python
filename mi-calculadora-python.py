import math


def calcular(a, b):
    """Calcula con valores finitos; None representa división indefinida."""
    if not math.isfinite(a) or not math.isfinite(b):
        raise ValueError("Ingrese números finitos.")
    return {"Suma": a + b, "Resta": a - b,
            "Multiplicación": a * b, "División": a / b if b != 0 else None}


def calculadora(a, b):
    for operacion, resultado in calcular(a, b).items():
        print(f"{operacion}: {resultado if resultado is not None else 'No definida (divisor cero)'}")

def main():
    try:
        a = float(input("Ingrese el primer valor: "))
        b = float(input("Ingrese el segundo valor: "))
        calculadora(a, b)
    except (ValueError, EOFError):
        print("Entrada inválida: ingrese dos números finitos.")
        return 1
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
