from CepBR import CepBr

cep = int(input("Digite o CEP: "))
objeto_cep = CepBr(cep)
objeto_cep_api = objeto_cep.api_via_cep()

print(objeto_cep_api)