# Parte 3 — main.py
# Este arquivo deve:

# Importar a lista de perguntas.py
# Importar as funções de funcoes.py
# Conter apenas o menu principal com while True e o fluxo da partida, chamando as funções importadas

from funcoes import *
import perguntas

# testando se a conexão funciona
exibir_menu()
fazer_pergunta()


print("=" * 40)
print("           BEM-VINDO AO QUIZ!")
print("=" * 40)

while True:
    print('''
1 - Jogar
2 - Sair
''')
    opcao = int(input("Opção:"))
    if opcao not in [1, 2]:
        print("Opção inválida! Escolha 1 para Jogar ou 2 para Sair.\n")
        pass
    if opcao == 2:
        print("\nAté logo!\n")
        break

    while True:
        nome_jogador = input("Nome do jogador: ").strip().capitalize()
        if len(nome_jogador) >= 2:
            break
        print("Nome muito curto! O nome deve ter pelo menos 2 caracteres.")
            
    print("=" * 40)
    print(f"         BOA SORTE, {nome_jogador}!     ")
    print("=" * 40)
        
    pontuacao = 0
    letras = ["A", "B", "C", "D"]
    total_perguntas = len(perguntas)
        
    for index, item in enumerate(perguntas, start=1):
        print(f"\nPergunta {index}: {item['enunciado']}")
            
        for i, opcao_texto in enumerate(item["opcoes"]):
            print(f"  {letras[i]}. {opcao_texto}")
                
        while True:
            resposta_usuario = input("Sua resposta: ").strip().upper()
            if resposta_usuario in letras:
                break
            print("Resposta inválida! Digite apenas A, B, C ou D.")
                
        if resposta_usuario == item["resposta"]:
            print("✔ Correto!")
            pontuacao += 1
        else:
            indice_correto = letras.index(item["resposta"])
            texto_correto = item["opcoes"][indice_correto]
            print(f"✘ Errado! A resposta correta era: {item['resposta']}. {texto_correto}")
                
        print("-" * 40)
        
    print("=" * 40)
    print(f"{nome_jogador}, você acertou {pontuacao} de {total_perguntas} perguntas!")
    print("=" * 40)