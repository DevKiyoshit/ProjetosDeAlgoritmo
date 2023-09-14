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
    Item("caneta", "escrever", 5, 5 )
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
            ind = individuo(gene.DNAgen(itens),i)
            população.append(ind)
        return população

#define uma cadeia booleana para representar os genes presentes em cada individuo
#o primeiro número da cadeia chamada DNA representará a existência do item dentro da bolsa, se ele estiver dentro = true, se fora = false
#define o tamanho da cadeia booleana baseado na quantidade de itens

class gene:
    def __init__(self, DNA):
        self.DNA = DNA
        
    def DNAgen(RNA):
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

#variáveis:
pop = 100
ind = individuo(gene.DNAgen(itens),1)
umageração = geração.criarGeração(pop)
print(ind.geneindividual) 
for ind in umageração:
    print(f"individuo {ind.id}: {ind.geneindividual}")
