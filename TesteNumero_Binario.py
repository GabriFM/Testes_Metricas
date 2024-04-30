def operacao_AND(binario1, binario2):
    resultado = ""
    for bit1, bit2 in zip(binario1, binario2):
        if bit1 == '1' and bit2 == '1':
            resultado += '1'
        else:
            resultado += '0'
    return resultado

# Test cases
test_cases = [
    ("0", "1", "0"),
    ("0", "1", "1"),
    ("1", "1", "0")
]

# Run test cases
for binario1, binario2, saida_esperada in test_cases:
    resultado_obtido = operacao_AND(binario1, binario2)
    print(f"Entrada: {binario1}, {binario2} - Saída esperada: {saida_esperada}, Saída obtida: {resultado_obtido}")
