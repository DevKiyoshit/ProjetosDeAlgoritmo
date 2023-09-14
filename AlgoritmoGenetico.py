import random
#[[Função multivariável]]
#parece lidar com um problema topológico e otimização, sendo que nesse caso, o objetivo é 
#encontrar o ponto mais próximo do ponto 0 da malha 3D. 
#tem relação com a defesa do canal visão libertária a favor da não proibição do terraplanismo
#se considerarmos que o máximo de progresso científico é o ponto 0, regredir pode nos livrar de estar preso em um ponto
def func(x,y,z):
    return 2*x**3 + 4*y**2 + 5*z - 20
def linear(x,y,z):
    aprox = func(x,y,z)
    if aprox == 0:
        return 999999
    else:
        return 1/aprox

#o algoritmo gera soluções utilizando a biblioteca random armazenando os valores numa lista
#precisa ser uma função para receber os valores das melhores gerações e aplicar a mutação genética gerando a semi aleatoriedade e uma taxa percentual menor de variação

def geração(newgen):
    for i in newgen:
        return (random.uniform(0,999),random.uniform(0,999), random.uniform(0,999))


soluções = []
newgen = [random.uniform(0,999), random.uniform(0,999), random.uniform(0,999)]
for s in range(100):
    
    soluções.append(linear(newgen[0], newgen[1], newgen[2]),(geração(newgen)))
    soluções.sort()
    soluções.reverse()
    if s < 15:
        newgen = soluções[[1]:16]
    print("{:} é o melhor resultado{:}".format(s, soluções[:1]))

#O algoritmo seleciona o melhor valor e aplica uma taxa de variação pequena representando a mutação genética

"""
---                              Até aqui o código havia funcionado sem a implementação da mutação, na tentativa de realizar uma função de geração
                                com a mutação, ele parou de funcionar. Aqui encerro e busco outras alternativas que serão adicionadas posteriormente---
"""


