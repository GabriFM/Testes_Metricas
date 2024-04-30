def converter_para_dolar(valor_em_real):
    taxa_de_cambio = 0.192  # Exemplo de taxa de câmbio: 1 real = 0.192 dólar
    valor_em_dolar = valor_em_real * taxa_de_cambio
    return valor_em_dolar

# Test cases
test_cases = [
    (262.5, 50),
    (625, 100),
    (140, 20)
]

# Run test cases
for entrada, saida_esperada in test_cases:
    resultado_obtido = converter_para_dolar(entrada)
    print(f"Entrada: {entrada} - Saída esperada: {saida_esperada}, Saída obtida: {resultado_obtido}")
