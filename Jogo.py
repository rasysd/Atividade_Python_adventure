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

# Classe Personagem
class Personagem:
    def __init__(self, nome, classe, atributos, modificadores):
        self.nome = nome
        self.classe = classe
        self.hp = 20 + atributos["Constituição"]
        self.defesa = modificadores["Constituição"]
        self.atributos = atributos
        self.modificadores = modificadores
        self.atributo_ataque = self.definir_atributo_ataque()

    def definir_atributo_ataque(self):
        return {
            "Guerreiro": "Força",
            "Arqueiro": "Destreza",
            "Mago": "Inteligência",
            "Paladino": "Sabedoria",
            "Bruxo": "Carisma"
        }.get(self.classe, "Força")  # Default para Força caso algo dê errado

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
def jogo():
    nome, classe, atributos, modificadores = criar_personagem()
    jogador = Personagem(nome, classe, atributos, modificadores)

    # inimigo básico genérico para teste
    inimigo = Personagem("Esqueleto", "Guerreiro", {"Constituição": 12, "Força": 10, "Destreza": 8, "Inteligência": 6, "Sabedoria": 6, "Carisma": 6},
                         {"Constituição": 1, "Força": 0, "Destreza": -1, "Inteligência": -2, "Sabedoria": -2, "Carisma": -2})

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
                if rolar_dado(20) >= 10:
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

# Iniciar o jogo
jogo()
