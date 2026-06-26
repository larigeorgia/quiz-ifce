# 🎮 Projeto Final — Quiz Interativo - Parte 2

# Discentes: 
# José Eduardo - Matrícula - 20261322030013
# Lariça Geórgia - Matrícula - 20261322030049
# Carlos Jefferson - Matrícula - 20261322030005


from perguntas import perguntas
from funcoes import exibir_menu, jogar
from ranking import exibir_ranking

def main():
    ranking_sessao = []
    
    while True:
        opcao = exibir_menu()
        
        match opcao:
            case 1:
                jogar(perguntas, ranking_sessao)
            case 2:
                exibir_ranking(ranking_sessao)
            case 3:
                print("\nAté logo!")
                break

if __name__ == "__main__":
    main()