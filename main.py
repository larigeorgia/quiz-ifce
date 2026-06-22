from perguntas import perguntas
from funcoes import exibir_menu, fazer_pergunta

while True:
    opcao = exibir_menu()

    if opcao == 1:
        while True:
            nome_jogador = input("Nome do jogador: ").strip().capitalize()
            if len(nome_jogador) >= 2:
                break
            print("Nome muito curto! O nome deve ter pelo menos 2 caracteres.")
            
        print("=" * 40)
        print(f"         BOA SORTE, {nome_jogador}!     ")
        print("=" * 40)
        
        pontuacao = 0
        total_perguntas = len(perguntas)
        
        for index, item in enumerate(perguntas, start=1):
            print(f"\nPergunta {index}: ", end="")
            
            acertou = fazer_pergunta(item)
            if acertou:
                pontuacao += 1
                
            print("-" * 40)
            
        print("=" * 40)
        print(f"{nome_jogador}, você acertou {pontuacao} de {total_perguntas} perguntas!")
        print("=" * 40)
        
    elif opcao == 2:
        print("\nAté logo!")
        break