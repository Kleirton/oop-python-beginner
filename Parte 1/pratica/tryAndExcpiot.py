class ErroKleber(Exception):
    pass

try:
    print('Tente fazer isso')
    raise ErroKleber('Houve um erro')

except ErroKleber as erro:
    print(erro)
