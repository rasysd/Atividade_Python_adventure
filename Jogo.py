import random
import os

input("Pressione Enter Para Continuar")
print(" ----- Retorno do REI ------")

def limpar_ficha():
    os.system("cls" if os.name == "nt" else "clear")

def criar_per():
    personagem = input("Digite nome do seu personagem\n")

    genero = ""
    while True: #vai permitir que apenas 1 desses 2 sejam escolhidos e qualquer outro volta ao inicio
        escolha = input("Escolha o genero do seu personagem:\n 1 - Masculino\n 2 - Feminino\n")
        if escolha == "1":
            genero = "Masculino"
            break
        elif escolha == "2":
            genero = "Feminino"
            break
        else:
            print("escolha inválida.")

    arquetipo = ""
    while True: #mesma coisa que o genero
        arquetipo_escolha = input("Escolha a classe do seu personagem:\n 1 - Lutador\n 2 - Arqueiro\n 3 - Mago\n 4 - Paladino\n 5 - Bruxo\n")
        if arquetipo_escolha == "1":
            arquetipo = "Lutador"
            break
        elif arquetipo_escolha == "2":
            arquetipo = "Arqueiro"
            break
        elif arquetipo_escolha == "3":
            arquetipo = "Mago"
            break
        elif arquetipo_escolha == "4":
            arquetipo = "Paladino"
            break
        elif arquetipo_escolha == "5":
            arquetipo = "Bruxo"
            break
        else:
            print("escolha inválida")

    if arquetipo == "Lutador":
        print("ATRIBUTO PRINCIPAL DE UM GUERREIRO É A FORÇA SEGUIDO DA CONSTITUIÇÃO\n GUERREIROS SÃO OTIMOS LUTADORES E TENDEM A ENFRENTAR SEUS INIMIGOS COM ESPADAS, LANÇAS OU CLAVAS.")
    elif arquetipo == "Arqueiro":
        print("ATRIBUTO PRINCIPAL DE UM ARQUEIRO É A DESTREZA SEGUIDO DA CONSTITUIÇÃO\n ARQUEIROS SÃO LUTADORES DAS FLORESTAS TENDEM A SE ESPREITAR E ATACAR NO MOMENTO MAIS OPORTUNO UTILIZAM VARIOS TIPOS DE FLECHAS DENTRE ELAS A COMUM E A MAGICA.")
    elif arquetipo == "Mago":
        print("ATRIBUTO PRINCIPAL DE UM MAGO É A INTELIGENCIA SEGUIDO DA CONSTITUIÇÃO\n MAGO SÃO ESTUDIOSOS E UTILIZAM DA SUA INTELIGENCIA PARA UTILIZAR MAGIAS QUE APRENDERAM NÃO SÃO MUITOS FORTES POIS DEDICARAM SEUS TEMPOS EM ESTUDOS NAS BIBLIOTECAS E ESCOLAS DE MAGIAS, POREM PODEM DESFERIR ENORMES EXPLOSÕES MAGICAS.")
    elif arquetipo == "Paladino":
        print("ATRIBUTO PRINCIPAL DE UM PALADINO É A SABEDORIA SEGUIDO DA FORÇA\n ESCOLHIDOS PELOS DEUSES PALADINOS SÃO GUERREIROS QUE LUTAM EM NOME DA FÉ EXPURGANDO TUDO AQUILO QUE FOR MALIGNO, NÃO DEIXANDO SOBRAR NADA, POREM TAMBEM EXISTEM AQUELES QUE NÃO HONRAM A SUA DIVINDADE SÃO CONHECIDOS COMO PERJURADORES, PALADINOS UTILIZAM ALABARDAS MISTURADAS COM ATAQUES DIVINOS.")
    elif arquetipo == "Bruxo":
        print("ATRIBUTO PRINCILAP DE UM BRUXO É O CARISMA SEGUIDO DA FORÇA\n ESCOLHIDOS POR UMA ENTIDADE DIVINA, PORÉM NÃO TÃO DIVINA ASSIM, BRUXOS SÃO CAÇADORES DE TUDO AQUILO QUE NÃO É BOM E NEM MAL, É IMPOSSIVEL DESCREVER OQUE SE PASSA NA CABEÇA DE UM BRUXO ELES NORMALMENTES UTILIZAM DE MAGIAS EXTREMAMENTES PODEROSAS OFERECIDAS POR SEUS PATRONOS QUE PODEM SER TANTO UM DOS DEUSES ANTIGOS QUANTO DE UM DEMONIO ATÉ MESMO DE UMA FADA.")

    atributos_num = [17, 14, 12, 10, 8, 6]
    atributos = ["Força", "Destreza", "Constituição", "Inteligência", "Sabedoria", "Carisma"]

    atributos_jogador = {}
    for atributo in atributos:
        while True:
            print(f"\nEscolha um valor para {atributo}:")
            for i, val in enumerate(atributos_num): #enumerate coloca uma especie de numeração da lista
                print(f"{i+1} - {val}")
            escolha_atri = input("Digite o numero correspondente ao valor desejado:\n")
            if escolha_atri.isdigit():    #vai evitar que algum espertinho escreva letra
                escolha_atri = int(escolha_atri)
                if 1 <= escolha_atri <= len(atributos_num):
                    valor_escolhido = atributos_num.pop(escolha_atri - 1) #esse pop ai vai removar a o atributo da lista pra ngm repitir
                    atributos_jogador[atributo] = valor_escolhido
                    break
                else:
                    print("Numero fora do intervalo. Escolha um número válido.\n")
            else:
                print("Entrada invalida. Digite apenas o numero da opção.")
    def valor_oculto(valor):
        return (valor - 10) // 2
    modificador = {}
    for atributo, valor in atributos_jogador.items():
        mod = valor_oculto(valor)
        modificador[atributo] = mod
        print(f"{atributo}: modificador {mod:+}")
    print("\n====== Ficha do Personagem =====")
    print(f"\nNome: {personagem}")
    print(f"Gênero: {genero}")
    print(f"Classe: {arquetipo}")

    while True:
        iniciar = input("Deseja continuar? \n 1 - Sim \n 2 - Não\n")
        if iniciar == "1":
            return personagem, genero, arquetipo, atributos_jogador
        elif iniciar == "2":
            print("\n Retornando a criação de personagem")
            return criar_per()
        else:
            print("\n ESCOLHA INVALIDA")

personagem, genero, arquetipo, atributos = criar_per() #Quase enlouqueço fazendo isso misericordia
limpar_ficha()

print(f"\n {personagem}, está inciando sua aventura.")



#combate (luiz)

import random

def rolar_dado(lados):
    return random.randint(1, lados)


class personagem:
    def __init__(self, nome, hp, força, defesa):
        self.nome = nome
        self.hp = hp
        self.força = força
        self.defesa = defesa

    def atacar(self, alvo):
        rolagem_ataque = rolar_dado(20)
        print(f"{self.nome} rola {rolagem_ataque} para atacar {alvo}.")

        if rolagem_ataque >= 10:
            dano = rolar_dado(8) + self.força
            alvo.hp -= dano
            print(f"{self.nome} causa {dano} de dano em {alvo.nome}, na cara não!!.")
        else:
            print("erooou!!!")


    def estar_vivo(self):
        return self.hp > 0
    
nome_heroi = input("Diga seu nome:").strip()
if nome_heroi == "":
    nome_heroi = "cleiton"


jogador = personagem(nome_heroi, hp=30, força=3, defesa=2)
inimigo = personagem("Esqueleto", hp=20, força=2, defesa=1)


if rolar_dado(20) > rolar_dado(20):
    turno = [jogador, inimigo]
else:
    turno = [inimigo, jogador]


while jogador.estar_vivo() and inimigo.estar_vivo():
    atacante = turno[0]
    defensor = turno[1]


    if atacante == jogador:
        acao = input("Digite 'A' para atacar ou 'F' para fugir: ").strip().upper()
        if acao == "F":
            chance_fuga = rolar_dado(20)
            if chance_fuga >=10:
                print("Amarelou legal!!")
                break
            else:
                print("Vai amarelar??")
                atacante.atacar(defensor)
        elif acao == "A":
            atacante.atacar(defensor)
        else:
            print("A ou F porra!!")
    else:
        atacante.atacar(defensor)


    turno.reverse()


    print(f"{jogador.nome}: {jogador.hp} HP | {inimigo.nome}: {inimigo.hp} HP\n")


if jogador.estar_vivo() and inimigo.estar_vivo():
    print("Saiu com o rabo entre as perna.")
elif jogador.estar_vivo():
    print(f"{jogador} saiu por cima!!")
else:
    print(f"{ jogador.nome} Foi jogar no vasco!")