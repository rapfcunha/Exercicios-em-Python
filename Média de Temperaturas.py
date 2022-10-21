#Questão 1
#Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, 
# calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, 
# e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).


mediam = []
mediamaior = []
mes = []
total = 0
mediaanual = 0

for i in range(12):
    x = float(input(f"Informe a temperatura media do mes {i+1}: "))
    mediam.append(x)
    total += x 
    mediaanual = total/12

for i in range(12):
    if mediam[i] > mediaanual:
        mediamaior.append(mediam[i])


for i in range(12):
    if mediam[i] > mediaanual:
        if i == 0:
            mes.append("Janeiro")
        elif i == 1:
            mes.append("Fevereiro")
        elif i == 2:
            mes.append("Março")
        elif i == 3:
            mes.append("Abril")
        elif i == 4:
             mes.append("Maio")
        elif i == 5:
             mes.append("Junho")
        
        elif i == 6:
             mes.append("Julho")
                   
        elif i == 7:
             mes.append("Agosto")
            
        elif i == 8:
             mes.append("Setembro")
        
        elif i == 9:
             mes.append("Outubro")
        
        elif i == 10:
             mes.append("Novembro")
        
        else :
             mes.append("Dezembro")
print("A média anual é %.2f" %mediaanual)  
print(mediamaior)
print(mes)