import random
#preciso saber quantos itens cabem na bolsa de forma a descobrir a melhor utilidade
#a bolsa cabe x espaços
#cada item tem Descrição, utilidade e espaço

class Bolsa:
    def __init__(self, espaços):
        self.espaços = espaços
        self.items = []
class Item:
    def __init__(self,nome, descriçao, utilidade, espaço):
        self.nome = nome
        self.descriçao = descriçao
        self.utilidade = utilidade
        self.espaço = espaço

#define o tamanho da bolsa

minhaBolsa = Bolsa(500)

#define os items
itens =[
    Item("notebook", "item de trabalho", 2000, 300),
    Item("headphones", "ouvir música", 350, 95),
    Item("roupas", "ficar cheiroso", 150, 40),
    Item("balas", "glicose para energia", 20, 10),
    Item("carteira", "pagamentos", 400, 50),
    Item("relógio", "olhar as horas", 90, 20),
    #pode ser interessante aumentar o valor de utilidade como conjunto caso lápis e caneta estejam juntos
    #porém, esse seria outro desafio de código para ser implementado no futuro
    Item("caderno", "escrever ou ler", 1000, 150 ),
    Item("caneta", "escrever", 5, 5 ),
    Item("óculos de sol", "proteger os olhos do sol", 70, 10),
    Item("garrafa de água", "hidratação", 30, 20),
    Item("laptop", "computação móvel", 1800, 250),
    Item("chave de fenda", "ferramenta para parafusos", 10, 5),
    Item("protetor solar", "proteger a pele do sol", 25, 15),
    Item("guarda-chuva", "proteção contra chuva", 40, 30),
    Item("câmera", "capturar momentos", 800, 120),
    Item("fones de ouvido sem fio", "ouvir música sem fio", 200, 40),
    Item("tênis de corrida", "para atividade física", 100, 60),
    Item("tênis de basquete", "para jogar basquete", 120, 80),
    Item("chaveiro", "organizar chaves", 5, 5),
    Item("protetor labial", "proteger os lábios", 8, 3),
    Item("carregador de celular", "manter o celular carregado", 15, 10),
    Item("guarda-roupa", "guardar roupas", 350, 150),
    Item("adesivos", "diversão decorativa", 2, 2),
    Item("notebook pequeno", "computação portátil", 800, 120),
    Item("livro", "leitura para o lazer", 50, 30),
    Item("escova de dentes", "higiene bucal", 10, 5),
    Item("pasta de dente", "para escovação", 8, 5),
    Item("saco de dormir", "para acampamento", 200, 150),
    Item("lanterna", "iluminação portátil", 25, 15),
    Item("kit de primeiros socorros", "para emergências", 50, 30)
    
]

#um indivíduo da população é a lista completa de itens com os genes ativos ou desativados um indivíduo representa
#uma combinação. Também pode ser chamada de geração, para princpios de coerência com a biologia


class individuo:
    def __init__(self, geneindividual, id):
        self.geneindividual = geneindividual
        self.id = id
        
        

class geração:
    def __init__(self, individuos, id):
        self.individuos = individuos
        self.id = id
    #aqui será criado uma função de geração de população com o tamanho a ser especificado, recebendo os valores de 
    # indivíduos em uma lista
    def criarGeração(tamanho_da_população):
        população = []
        for i in range(tamanho_da_população):
            indiv = individuo(gene.DNAgen(itens),i)
            população.append(indiv)
        return população

#define uma cadeia booleana para representar os genes presentes em cada individuo
#o primeiro número da cadeia chamada DNA representará a existência do item dentro da bolsa, se ele estiver dentro = true, se fora = false
#define o tamanho da cadeia booleana baseado na quantidade de itens

class gene:
    def __init__(self, DNA):
        self.DNA = DNA
        
    def DNAgen(RNA):
        #o RNA é a lista de itens
        #tamanho da cadeia:
        RNAtamanho = len(RNA)
        #cada valor de dentro da cadeia do RNA será chamada de base, em referência às bases nitrogenadas da biologia
        #!!! nessa simplificação, parece não ser muito bem escalável, mas ainda assim, se torna útil para genes
        #que terão utilidades além de existência ou inexistência. Ainda não está muito claro como será
        #apesar de inexistência do gene parecer válido, a sua função parece necessitar de um valor além de 0 e 1
        base = [0,1]
        cadeia_de_RNA = []
        for i in range(RNAtamanho):
            cadeia_de_RNA.append(random.choice(base))
        return cadeia_de_RNA

#define a fitness function, ela julgará cada indivíduo
#receberá o valor de cada base e a lista de itens
#percorrerá a lista de RNA e se for verdadeiro, somará à variável de utilidade total e espaço total
#encontrará na lista de itens os valores de utilidade e espaço
#verificará se o valor de espaços é maior do que os espaços da mochila
#se o valor de espaços for maior do que a da mochila, receberá o valor 0
# o valor ideal será o com utilidade somada mais alta. Em resumo, o mais fitness será o com mais utilidade

def fitness(DNA, itens, mochila):
    utilidadeTotal = 0
    espaçoTotal = 0
    for indice, i in enumerate(DNA, start=0):
        if i == 1:
            utilidadeTotal += itens[indice].utilidade
            espaçoTotal += itens[indice].espaço
    if espaçoTotal > mochila.espaços:
        utilidadeTotal = 0
    return utilidadeTotal

#seleção
#a seleção residirá sobre uma geração
#pegará a lista da população
#atribuirá a fitness function em cada indivíduo da população
#resultará numa lista dentro da lista contendo dois valores: quoeficientefitness e o indivíduo
#sorteará e classificará os melhores
#aplicará um critério de seleção informado (x para os top x da lista)
def seleção(população, top):
    rankeamento_da_população = []
    for i in população:
        rankeamento_da_população.append([fitness(i.geneindividual, itens, minhaBolsa), i.id, i.geneindividual])
    rankeamento_da_população.sort()
    rankeamento_da_população.reverse()
    melhores_individuos = []
    for s in range(top):
        melhores_individuos.append(rankeamento_da_população[s])
    return melhores_individuos

#cruzamento
#pegará uma lista de indivíduos (idealmente a lista dos mais selcionados, mas não necessariamente)
#selecionará um indivíduo aleatório para dar match com outro indivíduo aleatório
#para isso, escolherá aleatoraimente algum indivíduo da lista, depois escolherá algum valor aleatório menor do que a lista para acasalar
#dividirá na metade o gene do indivíduo e somará com a outra metade do segundo indivíduo da lista
def cruzamento(amantes):
    ninhada = []
    copuladores = amantes.copy()
    while len(copuladores) >= 2:
        amante1 = random.choice(copuladores)
        copuladores.remove(amante1)

        amante2 = random.choice(copuladores)
        copuladores.remove(amante2)
        #chamarei de gameta a metade da lista de um amante

        metade_amante1 = len(amante1[2])//2
        metade_amante2 = len(amante2[2])//2

        gameta1 = amante1[2][:metade_amante1]
        gameta2 = amante2[2][:metade_amante2]

        filho = gameta1+gameta2 
        ninhada.append(filho)
    if len(copuladores) >= 1:
        ninhada.append(copuladores[0][2])
    return print(ninhada)

#mutação
#recebe uma lista de indivíduos
#recebe a probabilidade de mutação
#se numa rolagem aleatória o valor for maior do que a probabilidade de mutação,  a  mutação ocorre, caso o contrário, segue
#seleciona um valor aleatório do DNA e troca pelo seu inverso se 0, logo 1; se 1, logo 0


#variáveis:
top = 40
pop = 200
umageração = geração.criarGeração(pop)
#for i in umageração:
#    print(f"individuo {i.id}: {i.geneindividual} possui {fitness(i.geneindividual, itens, minhaBolsa)} de aptidão")

ranked = seleção(umageração,top)
cruzamento(ranked)


