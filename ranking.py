def adicionar_ao_ranking(ranking, nome, pontuacao):
    """
    Cria um dicionário com os dados do jogador e anexa à lista de ranking.
    """
    jogador = {"nome": nome, "pontuacao": pontuacao}
    ranking.append(jogador)


def exibir_ranking(ranking):
    """
    Ordena os jogadores da maior para a menor pontuação usando sorted com lambda
    e exibe o resultado formatado usando enumerate.
    """
    print("\n" + "=" * 40)
    print("             RANKING ATUAL")
    print("=" * 40)
    
    if not ranking:
        print("Nenhum jogador registrado ainda. Seja o primeiro!")
        print("=" * 40)
        return

    ranking_ordenado = sorted(ranking, key=lambda x: x["pontuacao"], reverse=True)
    
    for idx, jogador in enumerate(ranking_ordenado, start=1):
        print(f"{idx}º — {jogador['nome']:<12} : {jogador['pt_texto'] if 'pt_texto' in jogador else jogador['pontuacao']} pontos")
        
    print("=" * 40)