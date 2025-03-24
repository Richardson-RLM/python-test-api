import re
from validate_docbr import CPF

def clean_cpf(cpf):
    return re.sub(r'\D', '', cpf)

def load_blacklist():
    try:
        with open("blacklist.txt", "r") as file:
            return set(clean_cpf(line.strip()) for line in file)
    except FileNotFoundError:
        return set()

def verify_cpf(cpf, blacklist):
    cpf_clean = clean_cpf(cpf)

    cpf_validator = CPF()
    if not cpf_validator.validate(cpf_clean):
        return "BLOCK" if cpf_clean in blacklist else "INVALID CPF"
    
    return "BLOCK" if cpf_clean in blacklist else "FREE"