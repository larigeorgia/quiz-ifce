from perguntas import perguntas
from ranking import adicionar_ao_ranking

def exibir_menu():
    """
    Exibe o menu principal do quiz na tela e faz a validação robusta da entrada.
    """
    while True:
        print("\n" + "=" * 40)
        print("         BEM-VINDO AO QUIZ!")
        print("=" * 40)
        print("1 - Novo jogador")
        print("2 - Ver ranking")
        print("3 - Sair")
        print("=" * 40)
        
        entrada = input("Opção: ").strip()
        if entrada in ["1", "2", "3"]:
            return int(entrada)
        print("Opção inválida! Escolha 1, 2 ou 3.")


def fazer_pergunta(pergunta):
    """
    Exibe o enunciado, as opções, valida e avalia a resposta digitada.
    """
    print(f"\n{pergunta['enunciado']}")
    letras = ["A", "B", "C", "D"]
    
    for i, opcao_texto in enumerate(pergunta["opcoes"]):
        print(f"  {letras[i]}. {opcao_texto}")
        
    while True:
        resposta_usuario = input("Resposta: ").strip().upper()
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


def classificar_desempenho(pontuacao):
    """
    Retorna a frase de feedback de desempenho baseada na pontuação final.
    """
    if pontuacao == 10:
        return "Perfeito! Você é um gênio!"
    elif pontuacao in [8, 9]:
        return "Excelente desempenho!"
    elif pontuacao in [6, 7]:
        return "Bom trabalho!"
    elif pontuacao in [4, 5]:
        return "Você pode melhorar!"
    else:
        return "Continue estudando!"


def jogar(lista_perguntas, lista_ranking):
    """
    Gerencia o fluxo completo de uma rodada para um jogador específico.
    """
    while True:
        nome_jogador = input("\nNome do jogador: ").strip().capitalize()
        if len(nome_jogador) >= 2:
            break
        print("Nome muito curto! O nome deve ter pelo menos 2 caracteres.")
        
    print("\n" + "=" * 40)
    print(f"         BOA SORTE, {nome_jogador}!")
    print("=" * 40)
    
    pontuacao = 0
    for idx, pergunta in enumerate(lista_perguntas, start=1):
        print(f"\nPergunta {idx}:", end="")
        if fazer_pergunta(pergunta):
            pontuacao += 1
        print("-" * 40)
        
    msg_desempenho = classificar_desempenho(pontuacao)
    
    print("\n" + "=" * 40)
    print(f"         RESULTADO DE {nome_jogador.upper()}")
    print("=" * 40)
    print(f"Pontuação : {pontuacao} de {len(lista_perguntas)}")
    print(f"Desempenho: {msg_desempenho}")
    print("=" * 40)
    
    adicionar_ao_ranking(lista_ranking, nome_jogador, pontuacao)