from validate_docbr import CPF

def validar_cpf(cpf):
    cpf_validator = CPF()
    return cpf_validator.validate(cpf)
