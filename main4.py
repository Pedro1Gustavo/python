from atv04 import validar_email, validar_cpf 

email = input("digite o email: ")
print("email válido", validar_email(email)) 

cpf = input("digite o cpf: ")
print("cpf válido", validar_cpf(cpf))