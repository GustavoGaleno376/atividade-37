#Ler uma lista de 5 números inteiros e
#mostre cada número juntamente com a
#sua posição na lista.
lista=[0,1,2,3,4,5]
for i,p in enumerate(lista):
    print(i+1,"=>",p)
    
#Ler uma lista de 10 números reais e
#mostre-os na ordem inversa.
a=[0,1,2,3,4,5,6,7,8,9]

a.reverse()
print(a)

#Ler uma lista com 4 notas, em seguida
#o programa deve exibir as notas e a
#média.
nota=[]
for i in range(0,3):
    c=int(input("digite sua nota"))
    nota.append(c)
ope=sum(nota)/len(nota)
print(ope)
