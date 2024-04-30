def valida_cpf(cpf):
    # Remove caracteres não numéricos do CPF
    cpf = ''.join(filter(str.isdigit, cpf))

    # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False
    
    # Verifica se todos os dígitos são iguais
    if cpf == cpf[0] * 11:
        return False
    
    # Calcula o primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = soma % 11
    if resto < 2:
        digito_verif_1 = 0
    else:
        digito_verif_1 = 11 - resto

    # Verifica o primeiro dígito verificador
    if int(cpf[9]) != digito_verif_1:
        return False

    # Calcula o segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = soma % 11
    if resto < 2:
        digito_verif_2 = 0
    else:
        digito_verif_2 = 11 - resto

    # Verifica o segundo dígito verificador
    if int(cpf[10]) != digito_verif_2:
        return False

    return True

# Test cases
test_cases = [
    ("012.567.98000", False),
    ("012.345.678-90", True),
    ("54612399321", False)
]

# Run test cases
for cpf, expected_result in test_cases:
    result = valida_cpf(cpf)
    print(f"CPF: {cpf} - Resultado esperado: {expected_result}, Resultado obtido: {result}")
