def palindromo(frase):
    frase = frase.lower()
    frase = frase.replace(' ','')
    if frase == frase[::-1]:
        print('es palindromo')
        print(frase)
    else:
        print('no es palindromo')
        print(frase)

while True:
    frase =input('ingrese una frase o palabra: ')
    palindromo()
