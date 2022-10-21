#Implemente uma função recursiva para calcular 1 + 1/2 + 1/3 + 1/4 + ... + 1/N .
def divisor(n):
  if n == 1:
    return 1
  return 1/n + divisor(n-1)

divide = divisor(2)
print("Valor final %.2f" %divide)