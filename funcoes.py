
def exibir_menu():
    """
    Exibe o menu principal do quiz na tela, solicita a opção do usuário,
    valida se a entrada é '1' ou '2' e retorna a opção escolhida.
    """
    while True:
        print("=" * 40)
        print("           BEM-VINDO AO QUIZ!")
        print("=" * 40)
        print('''
1 - Jogar
2 - Sair''')
        
        opcao = int(input("Opção: "))
        
        if opcao in [1, 2]:
            return opcao
        print("Opção inválida! Escolha 1 para Jogar ou 2 para Sair.\n")


def fazer_pergunta(pergunta):
    """
    Exibe o enunciado e as opções de uma pergunta recebida por parâmetro.
    Recebe, limpa e valida a resposta do usuário (A, B, C ou D).
    Verifica se a resposta está correta, exibe o feedback na tela
    e retorna True em caso de acerto ou False em caso de erro.
    """
    print(f"\n{pergunta['enunciado']}")
    
    letras = ["A", "B", "C", "D"]
    
    for i, opcao_texto in enumerate(pergunta["opcoes"]):
        print(f"  {letras[i]}. {opcao_texto}")
        
    while True:
        resposta_usuario = input("Sua resposta: ").strip().upper()
        if resposta_usuario in letras:
            break
        print("Resposta inválida! Digite apenas A, B, C ou D.")
        
    if resposta_usuario == pergunta["resposta"]:
        print("✔ Correto!")
        return True
    else:
        indice_correto = letras.index(pergunta["resposta"])
        texto_correto = pergunta["opcoes"][indice_correto]
        print(f"✘ Errado! A resposta correta era: {pergunta['resposta']}. {texto_correto}")
        return False