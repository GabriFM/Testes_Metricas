import re

def valida_placa(placa):
    # Expressão regular para verificar o formato da placa
    padrao = r'^[A-Z]{3}\d{4}$'
    if re.match(padrao, placa):
        return "Valido"
    else:
        return "Invalido"

# Test cases
test_cases = [
    ("1161ABG", "Invalido"),
    ("ABC7S86", "Valido"),
    ("8A09ABG", "Invalido")
]

# Run test cases
for placa, saida_esperada in test_cases:
    resultado_obtido = valida_placa(placa)
    print(f"Placa: {placa} - Saída esperada: {saida_esperada}, Saída obtida: {resultado_obtido}")
