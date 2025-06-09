import random
import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def rolar_dado(lados):
    return random.randint(1, lados)

# Criação de personagem
def criar_personagem():
    input("Pressione Enter para continuar")
    limpar_tela()
    print("----- RETORNO DO REI -----")

    nome = input("Digite o nome do seu personagem: ")

    genero = ""
    while True:
        escolha = input("Escolha o gênero do seu personagem:\n 1 - Masculino\n 2 - Feminino\n")
        if escolha == "1":
            genero = "Masculino"
            break
        elif escolha == "2":
            genero = "Feminino"
            break
        else:
            print("Escolha inválida.")

    classes = {
        "1": "Guerreiro",
        "2": "Arqueiro",
        "3": "Mago",
        "4": "Paladino",
        "5": "Bruxo"
    }

    classe = ""
    while classe == "":
        escolha_classe = input("Escolha a classe do seu personagem:\n 1 - Guerreiro\n 2 - Arqueiro\n 3 - Mago\n 4 - Paladino\n 5 - Bruxo\n")
        classe = classes.get(escolha_classe, "")
        if classe == "":
            print("Escolha inválida.")

    explicacoes = {
        "Guerreiro": "Força > Constituição",
        "Arqueiro": "Destreza > Constituição",
        "Mago": "Inteligência > Constituição",
        "Paladino": "Sabedoria > Constituição",
        "Bruxo": "Carisma > Constituição"
    }

    print(f"Atributos recomendados para {classe}: {explicacoes[classe]}")

    atributos_disponiveis = [17, 14, 12, 10, 8, 6]
    atributos_nome = ["Força", "Destreza", "Constituição", "Inteligência", "Sabedoria", "Carisma"]
    atributos_personagem = {}

    for atributo in atributos_nome:
        while True:
            print(f"\nEscolha um valor para {atributo}:")
            for i, val in enumerate(atributos_disponiveis):
                print(f"{i+1} - {val}")
            escolha = input("Digite o número correspondente ao valor desejado: ")
            if escolha.isdigit() and 1 <= int(escolha) <= len(atributos_disponiveis):
                valor = atributos_disponiveis.pop(int(escolha) - 1)
                atributos_personagem[atributo] = valor
                break
            else:
                print("Escolha inválida.")

    def mod(valor): return (valor - 10) // 2
    modificadores = {atributo: mod(valor) for atributo, valor in atributos_personagem.items()}

    print("\n====== Ficha do Personagem =====")
    print(f"Nome: {nome}")
    print(f"Gênero: {genero}")
    print(f"Classe: {classe}")
    for atr, val in atributos_personagem.items():
        print(f"{atr}: {val} (mod {modificadores[atr]:+})")

    input("\nPressione Enter para iniciar a aventura...")
    limpar_tela()

    return nome, classe, atributos_personagem, modificadores

import time

def narrar(texto, atraso=2):
    for linha in texto.split('\n'):
        print(linha)
        time.sleep(atraso)
    print("\n")

introducao_reino = """
Capítulo 1: Surgimento


Em meio a colinas verdesjantes e vastos campos de lavanda, ergue-se o Reino de Velmir. 
Um lugar onde o tempo parece respeitar a natureza e os ventos sussurram histórias de eras antigas.

Árvores milenares cobrem a paisagem, com copas tão largas que ocultam a luz do sol, 
criando um manto de sombra fresca e constante. Animais mágicos percorrem as florestas — 
cervos com chifres de cristal, pássaros de penas douradas e até felinos com olhos cintilantes como estrelas.

No coração do reino, reluzente como uma joia, ergue-se o castelo de mármore branco e torres douradas: 
o Castelo de Elarion. Os telhados escarlates brilham à luz do dia, guardando os segredos de gerações de reis e magos. 
Riquezas de todo o mundo repousam em seus cofres e bibliotecas arcanas, mas é sua sabedoria, dizem, o maior tesouro.

E é para esse mundo encantado que você foi chamado. Um destino ainda não escrito... mas prestes a começar.
"""

# Executar a narração
narrar(introducao_reino, atraso=2)


# Classe Personagem
class Personagem:
    def __init__(self, nome, classe, atributos, modificadores):
        self.nome = nome
        self.classe = classe
        self.defesa = 10 + modificadores["Constituição"] #vai utilizar a contituição como defesa
        self.atributos = atributos
        self.modificadores = modificadores
        self.atributo_ataque = self.definir_atributo_ataque()
        self.hp = self.vida_inicial()

    def definir_atributo_ataque(self):
        return {
            "Guerreiro": "Força",
            "Arqueiro": "Destreza",
            "Mago": "Inteligência",
            "Paladino": "Sabedoria",
            "Bruxo": "Carisma"
        }.get(self.classe, "Força")  # Default para Força caso algo dê errado
    
    def vida_inicial(self):
        base_hp_por_classe = {
            "Guerreiro": 35,
            "Arqueiro": 30,
            "Mago": 20,
            "Paladino": 40,
            "Bruxo": 25
        }
        base_hp = base_hp_por_classe.get(self.classe, 20)
        return base_hp + self.modificadores["Constituição"]

    def atacar(self, alvo):
        rolagem = rolar_dado(20)
        print(f"{self.nome} rola {rolagem} para atacar {alvo.nome}.")

        if rolagem >= 10:
            dado_dano = rolar_dado(8)
            modificador_ataque = self.modificadores[self.atributo_ataque]
            dano = dado_dano + modificador_ataque
            alvo.hp -= max(0, dano)
            print(f"{self.nome} usa {self.atributo_ataque} e causa {dano} de dano em {alvo.nome}!")
        else:
            print(f"{self.nome} erra o ataque!")

    def esta_vivo(self):
        return self.hp > 0

# Fluxo do jogo
def combate(inimigo):
    global jogador

    if rolar_dado(20) > rolar_dado(20):
        turno = [jogador, inimigo]
    else:
        turno = [inimigo, jogador]

    while jogador.esta_vivo() and inimigo.esta_vivo():
        atacante = turno[0]
        defensor = turno[1]

        if atacante == jogador:
            acao = input("Digite 'A' para atacar ou 'F' para fugir: ").strip().upper()
            if acao == "F":
                if rolar_dado(20) >= 15:
                    print("Você fugiu com sucesso!")
                    return
                else:
                    print("Você falhou em fugir!")
                    atacante.atacar(defensor)
            elif acao == "A":
                atacante.atacar(defensor)
            else:
                print("Comando inválido!")
        else:
            atacante.atacar(defensor)

        turno.reverse()
        print(f"\n{jogador.nome}: {jogador.hp} HP | {inimigo.nome}: {inimigo.hp} HP\n")

    if jogador.esta_vivo():
        print(f"{jogador.nome} venceu a batalha!")
    else:
        print(f"{jogador.nome} foi derrotado...")


nome, classe, atributos, modificadores = criar_personagem()
jogador = Personagem(nome, classe, atributos, modificadores) #recebe Jogador

import time

def narrar(texto, atraso=2):
    for linha in texto.strip().split('\n'):
        print(linha)
        time.sleep(atraso)
    print()

def escolher_opcao(pergunta, opcoes):
    print(pergunta)
    for i, opcao in enumerate(opcoes, 1):
        print(f"{i}. {opcao}")
    
    while True:
        try:
            escolha = int(input("Digite o número da sua escolha: "))
            if 1 <= escolha <= len(opcoes):
                return escolha
            else:
                print("Escolha inválida. Tente novamente.")
        except ValueError:
            print("Por favor, digite um número.")

parte2 = """
Ao adentrar no reino, alguém parece ter alertado ao rei a respeito de um novo visitante.
Dois soldados surgem pela trilha em suas armaduras de prata azulada, com o brasão do sol dourado no peito.

Soldado alto:
— Ei, você aí! Você é quem foi chamado pelo rei Julian IV, certo?

Soldado bonitão:
— Venha conosco. O rei deseja conhecê-lo pessoalmente. Mas antes... temos algumas perguntas.
"""

narrar(parte2)

pergunta1 = "De onde você vem, forasteiro?"
opcoes1 = [
    "Das montanhas cinzentas, onde os ventos cantam entre as pedras.",
    "Do litoral sul, onde os pescadores vendem histórias junto com o peixe.",
    "De lugar algum, caminho onde o destino me leva."
]
resposta1 = escolher_opcao(pergunta1, opcoes1)

if resposta1 == 1:
    narrar("Soldado alto: — As montanhas? Gente dura vive por lá. Gostei.")
elif resposta1 == 2:
    narrar("Soldado bonitão: — Ah! Gosto de histórias. Tomara que traga uma boa.")
elif resposta1 == 3:
    narrar("Soldado alto: — Um andarilho, hein? O rei adora enigmas...")

pergunta2 = "Qual arma prefere usar?"
opcoes2 = [
    "Espada longa, fiel e direta.",
    "Cajado de carvalho, canal da minha magia.",
    "Adagas ocultas. Rápidas, silenciosas."
]
resposta2 = escolher_opcao(pergunta2, opcoes2)

if resposta2 == 1:
    narrar("Soldado alto: — Um guerreiro de verdade! Boa escolha.")
elif resposta2 == 2:
    narrar("Soldado alto: — Magia... perigosa, mas útil.")
elif resposta2 == 3:
    narrar("Soldado bonitão: — Silêncio pode matar mais que um grito. Interessante.")

pergunta3 = "Por que busca servir o rei?"
opcoes3 = [
    "Desejo glória e ouro.",
    "Para proteger inocentes.",
    "Por respostas que só o trono pode me dar."
]
resposta3 = escolher_opcao(pergunta3, opcoes3)

if resposta3 == 1:
    narrar("Soldado bonitão: — Honesto. Raro.")
elif resposta3 == 2:
    narrar("Soldado bonitão: — Um coração nobre. Isso agrada o rei.")
elif resposta3 == 3:
    narrar("Soldado alto: — Mistérios atraem reis tanto quanto guerreiros.")

narrar("Os soldados trocam olhares e assentem com a cabeça.\nSoldado alto: — Muito bem. Siga-nos. Sua audiência com o rei o aguarda.\n")


parte3 = """
Parte 3: Diante do Rei Julian IV

Os portões do castelo se abrem com um ranger ancestral. 
Os corredores são largos e o chão de vidro reluz sob seus pés. 
Tapeçarias contam a história de guerras e paz. 
O trono de Julian IV brilha como o sol, envolto em luz mágica.

Rei Julian IV:
— Aproximem-se. Tenho observado seus passos desde a névoa do tempo. 
Mas antes de confiar-lhe um destino, devo conhecer sua essência.
"""

narrar(parte3)

pergunta1 = "O que você teme mais?"
opcoes1 = [
    "O esquecimento.",
    "O fracasso.",
    "O mal que vive em mim."
]
resposta1 = escolher_opcao(pergunta1, opcoes1)

if resposta1 == 1:
    narrar("Rei Julian IV: — Memória é imortal quando há feitos.")
elif resposta1 == 2:
    narrar("Rei Julian IV: — Quem teme o fracasso, planeja melhor.")
elif resposta1 == 3:
    narrar("Rei Julian IV: — A verdadeira coragem é encarar o espelho.")

pergunta2 = "O que salvaria em um mundo em ruínas?"
opcoes2 = [
    "A sabedoria.",
    "As crianças.",
    "A esperança."
]
resposta2 = escolher_opcao(pergunta2, opcoes2)

if resposta2 == 1:
    narrar("Rei Julian IV: — O conhecimento é semente para um novo jardim.")
elif resposta2 == 2:
    narrar("Rei Julian IV: — A juventude renova os sonhos.")
elif resposta2 == 3:
    narrar("Rei Julian IV: — Esperança alimenta até os famintos.")

pergunta3 = "Você acredita nos deuses?"
opcoes3 = [
    "Sim, com todo meu ser.",
    "Não. Apenas no que posso ver.",
    "Talvez... se eles acreditarem em mim."
]
resposta3 = escolher_opcao(pergunta3, opcoes3)

if resposta3 == 1:
    narrar("Rei Julian IV: — A fé move montanhas e exércitos.")
elif resposta3 == 2:
    narrar("Rei Julian IV: — Um idiota assim como imaginei.")
elif resposta3 == 3:
    narrar("Rei Julian IV: — Uma resposta digna de um herói.")

encerramento = """
Rei Julian IV:
— Suas respostas traçam um caminho. O destino o aguarda. 
Irá para as Terras da Floresta Putrida, mas o caminho... passa primeiro por um deserto.
Prepare-se.
"""

import time

def narrar(texto, atraso=1):
    for linha in texto.strip().split('\n'):
        print(linha)
        time.sleep(atraso)
    print()

parte4 = """
Muito além das muralhas, há um lugar onde o verde virou cinza.
Árvores doentes, de galhos tortos e cascas enegrecidas, respiram um fedor de morte e magia antiga.
Essa é a Floresta Putrida. Mas sua hora ainda não chegou...

Os portões se fecham lentamente atrás de você.
O vento sopra como se se despedisse.
O caminho diante de ti é longo — pedras, poeira e horizontes alaranjados te esperam.
Você pisa fora do conforto e da riqueza.
Agora, começa a jornada.

O Deserto de Zhal-Kar não é feito apenas de areia.
É um mar dourado onde as dunas se movem como ondas vivas.
Cactos azuis crescem em círculos mágicos e há oásis que cantam ao luar.

As noites são frias como o toque da morte, e os dias queimam a pele como mil fogueiras.
Mas há vida — escorpiões de cristal, serpentes de fogo e aves que deixam rastros de luz ao voar.

No centro, uma cidade abandonada feita de vidro partido se ergue como um espelho da própria loucura.
A areia sussurra nomes... talvez o seu.
"""

narraçãoDZRTO = """
O calor não apenas consome — ele pesa.
A cada passo, a areia parece puxar seus pés como se quisesse soterrar seu passado.
O sol, um deus impiedoso no alto, vigia em silêncio enquanto miragens dançam no horizonte, zombando da sua sanidade.

Aos poucos, o Deserto de Zhal-Kar revela suas entranhas.
Dunas como muralhas se erguem e caem com o vento, escondendo perigos em cada curva.

Você encontra pegadas — não humanas, nem exatamente de besta.
Algo leve, veloz... e afiado.

Rochas rachadas indicam ninhos abandonados dos Vermídeos da Areia,
criaturas que deslizam por baixo do solo, atraídas por vibração e calor.
Pequenos, mas letais em bando.

Um grupo de Mirraquelhos voa baixo — seres semelhantes a morcegos de ossos finos e olhos negros que refletem o céu.
Seus guinchos parecem riscar o ar, como navalhas.

A tensão cresce. Algo o observa.
Mas a estrada chama, e o deserto... nunca se cala.
"""

import time

def narrar(texto, atraso=1):
    for linha in texto.strip().split('\n'):
        print(linha)
        time.sleep(atraso)
    print()

def encontro_bandidos():
    narrar("""
Enquanto segue em direção ao próximo oásis marcado no mapa do rei,
uma sombra se move acima de uma duna.

Quando você chega ao topo, três figuras encapuzadas já cercam você.

Líder dos Bandidos:
— Ei, andarilho. Zhal-Kar não é terra de reis.
  Aqui, quem manda é a sede... e a ponta da lâmina.
— Vemos que carrega coisas valiosas... por bem ou por mal, elas vão mudar de dono.
""")

    print("Escolha sua ação:")
    print("A) Tentar conversar com os bandidos.")
    print("B) Fingir rendição para esperar uma chance.")
    print("C) Fazer menção de lutar, assustando-os.")
    
    escolha = input("Digite A, B ou C: ").strip().upper()
    print()

    if escolha == "A":
        narrar("""
Você:
— Não sou seu inimigo. Tenho uma missão real.
  Posso dividir água e informações, mas deixem-me passar.

Líder dos Bandidos:
— Hm. Um diplomata no meio do inferno...
(pausa)
— Muito bem. Dê-nos metade da sua água, e o caminho será seu.
  Mas lembre-se: da próxima vez, não haverá conversa.

Você entrega parte dos suprimentos e eles partem,
deixando uma advertência no ar.
""")
    elif escolha == "B":
        narrar("""
Você levanta as mãos lentamente.
— Certo... não quero problemas.

Um dos bandidos se aproxima para revistar seus pertences...

...mas no último instante você se move com agilidade,
escapando da armadilha e deixando um dos bandidos atordoado na areia.

Líder dos Bandidos:
— Um truqueiro, hein?! Veremos se os vermídeos gostam de carne rápida!

Eles fogem, mas a movimentação atrai criaturas do deserto que surgem das dunas...
""")
    elif escolha == "C":
        narrar("""
Você coloca a mão na empunhadura da arma, ou murmura palavras arcanas.

— Dê mais um passo e verão do que sou capaz.

Líder dos Bandidos:
— Hah! Um bravo, então... mas olhe à sua volta.

As criaturas do deserto começam a cercar vocês — atraídas pela tensão e som.

— Sabe de uma coisa? Boa sorte com eles.

Os bandidos batem em retirada, deixando para trás apenas pegadas e risos.
""")

#Chamada da função
encontro_bandidos()

def narrar(texto, atraso=1):
    for linha in texto.strip().split('\n'):
        print(linha)
        time.sleep(atraso)
    print()

def batalha_mirraquelhos ():
    narrar("""
Com os bandidos fora do caminho, a verdadeira ameaça surge do chão trêmulo. 
Um Vermídeo da Areia irrompe próximo, seguido por guinchos de Mirraquelhos girando no céu. 
Mas você já estava pronto. A batalha... já começou.

Os Mirraquelhos são criaturas parecidas com morcegos, mas suas asas são quase transparentes e possuem bordas afiadas como navalhas. 
Seu corpo é coberto por uma pele fina e seca, que se camufla com a areia e as rochas do deserto.

Possuem olhos negros brilhantes, que refletem a luz como vidro líquido. 
Esses olhos não servem para enxergar no escuro, mas para hipnotizar presas desavisadas por breves segundos 
— tempo suficiente para atacar ou fugir.

Voam em bandos de 3 a 8, usando uma comunicação sonora aguda quase inaudível para humanos. 
O som deles incomoda criaturas maiores e pode causar desorientação leve.""")
    
def narrar(texto, atraso=1):
    for linha in texto.strip().split('\n'):
        print(linha)
        time.sleep(atraso)
    print()

def narração_solitária ():
    narrar("""Narração: Travessia Solitária
Horas se passam. O sol começa a declinar, tingindo o céu de vermelho e cobre. 
As dunas se tornam muralhas silenciosas, e o vento
— antes cortante — agora sussurra com um tom de aviso.

No horizonte, formas antigas surgem parcialmente engolidas pela areia: 
pilares quebrados, estátuas tombadas, paredes de pedra negra cobertas de símbolos esquecidos.

Uma ruína. Um abrigo. Ou... um túmulo.
           
Você se aproxima da entrada de uma estrutura parcialmente soterrada.
Dois obeliscos partidos guardam o portão de pedra, onde inscrições desgastadas 
ainda podem ser lidas por quem conhece as línguas antigas:

"Aqui repousam os reis sem nome. Que a morte os esqueça como o mundo os esqueceu."

Uma escadaria desce até as entranhas da ruína, protegida apenas pela escuridão.""")  





#resolvendo ak

inimigo_test = Personagem(   #Copia e cola isso pq como usamos class vai ter q ser desse tamanho todas as vezes
    "Esqueleto","Arqueiro", #muda o nome da criatura e sua classe
    {"Constituição": 12, "Força": 10, "Destreza": 8, "Inteligência": 6, "Sabedoria": 6, "Carisma": 6}, 
    {"Constituição": 1, "Força": 0, "Destreza": -1, "Inteligência": -2, "Sabedoria": -2, "Carisma": -2} #Muda apenas os parametros
)

inimigo_test = Personagem(   #Copia e cola isso pq como usamos class vai ter q ser desse tamanho todas as vezes
    "Esqueleto","Arqueiro", #muda o nome da criatura e sua classe
    {"Constituição": 12, "Força": 10, "Destreza": 8, "Inteligência": 6, "Sabedoria": 6, "Carisma": 6}, 
    {"Constituição": 1, "Força": 0, "Destreza": -1, "Inteligência": -2, "Sabedoria": -2, "Carisma": -2} #Muda apenas os parametros
)

inimigo_test = Personagem(   #Copia e cola isso pq como usamos class vai ter q ser desse tamanho todas as vezes
    "Esqueleto","Arqueiro", #muda o nome da criatura e sua classe
    {"Constituição": 12, "Força": 10, "Destreza": 8, "Inteligência": 6, "Sabedoria": 6, "Carisma": 6}, 
    {"Constituição": 1, "Força": 0, "Destreza": -1, "Inteligência": -2, "Sabedoria": -2, "Carisma": -2} #Muda apenas os parametros
)

inimigo_test = Personagem(   #Copia e cola isso pq como usamos class vai ter q ser desse tamanho todas as vezes
    "Esqueleto","Arqueiro", #muda o nome da criatura e sua classe
    {"Constituição": 12, "Força": 10, "Destreza": 8, "Inteligência": 6, "Sabedoria": 6, "Carisma": 6}, 
    {"Constituição": 1, "Força": 0, "Destreza": -1, "Inteligência": -2, "Sabedoria": -2, "Carisma": -2} #Muda apenas os parametros
)

# Iniciar o combate
combate(inimigo_test) #Sempre q for iniciar o combate la no inimigo test muda pra a criatura especifica
combate(inimigo_test)
combate(inimigo_test)
combate(inimigo_test)