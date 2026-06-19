# 🎮 Projeto Final — Quiz Interativo - Parte 1

# Discentes: 
# José Eduardo - Matrícula - 20261322030013
# Lariça Geórgia - Matrícula - 20261322030049
# Carlos Jefferson - Matrícula - 20261322030005

perguntas = [
    {
        "enunciado": "Qual é o maior país em extensão territorial da América do Sul?",
        "opcoes"   : ["Argentina", "Colômbia", "Peru", "Brasil"],
        "resposta" : "D"
    },
    {
        "enunciado": "O território brasileiro é dividido politicamente em quantas Regiões Oficiais pelo IBGE?",
        "opcoes"   : ["4 Regiões", "5 Regiões", "6 Regiões", "7 Regiões"],
        "resposta" : "B"
    },
    {
        "enunciado": "Qual é o estado brasileiro que possui a maior extensão territorial?",
        "opcoes"   : ["Pará", "Mato Grosso", "Amazonas", "Minas Gerais"],
        "resposta" : "C"
    },
    {
        "enunciado": "Qual é o único estado da Região Nordeste que é cortado pelo Rio São Francisco e também possui o maior número de municípios da região?",
        "opcoes"   : ["Pernambuco", "Bahia", "Ceará", "Maranhão"],
        "resposta" : "B"
    },
    {
        "enunciado": "Qual é o bioma exclusivamente brasileiro que ocupa grande parte da Região Nordeste?",
        "opcoes"   : ["Caatinga", "Cerrado", "Mata Atlântica", "Pantanal"],
        "resposta" : "A"
    },
    {
        "enunciado": "O ponto mais alto do relevo brasileiro é o Pico da Neblina. Em qual estado ele se localiza?",
        "opcoes"   : ["Roraima", "Minas Gerais", "Rio de Janeiro", "Amazonas" ],
        "resposta" : "D"
    },
    {
        "enunciado": "Qual é a principal bacia hidrográfica totalmente localizada em território brasileiro, famosa pelo rio 'Velho Chico'?",
        "opcoes"   : ["Bacia do Amazonas", "Bacia do Rio São Francisco", "Bacia do Paraná", "Bacia do Rio Uruguai"],
        "resposta" : "B"
    },
    {
        "enunciado": "Qual linha imaginária do globo terrestre corta a porção sul do território brasileiro, cruzando estados como São Paulo e Paraná?",
        "opcoes"   : [ "Trópico de Capricórnio", "Linha do Equador", "Trópico de Câncer", "Meridiano de Greenwich"],
        "resposta" : "A"
    },
    {
        "enunciado": "A Região Sul do Brasil destaca-se por apresentar qual tipo de clima predominante?",
        "opcoes"   : ["Clima Equatorial", "Clima Semiárido", "Clima Subtropical", "Clima Tropical Atlântico"],
        "resposta" : "C"
    },
    {
        "enunciado": "O Brasil possui uma das maiores costas litorâneas do mundo. Qual oceano banha todo o nosso território?",
        "opcoes"   : ["Oceano Pacífico", "Oceano Índico", "Oceano Atlântico", "Oceano Glacial Ártico"],
        "resposta" : "C"
    }
]

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
