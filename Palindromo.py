#3) Implemente uma função recursiva para verificar se uma palavra é palíndromo (Ex. aba, abcba, xyzzyx).
def inverter(palavra):
    palavra = str(palavra)
    if palavra == '':
        return palavra     
    return inverter(palavra[1:]) + palavra[0]
def palindromo(palavra_n):
    nova_palavra = inverter(palavra_n)
    if nova_palavra == palavra_n:
      return "é palindromo"
    else:
      return "não é"
print(palindromo('arara'))