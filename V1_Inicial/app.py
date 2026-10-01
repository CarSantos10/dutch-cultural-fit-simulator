# Simulador de Fit Cultural Holandês 
# Criado por: Carlos Santos

pontuacao = 0

print("Bem-vindo ao Simulador de Fit Cultural Holandês!")
print("Responda às perguntas abaixo para descobrir o quanto você se adapta à cultura holandesa.")

# Pergunta 1
print("\nPergunta 1: Você prefere trabalhar em equipe ou individualmente?")
print("1. Em equipe")
print("2. Individualmente")
resposta1 = input("Digite o número da sua resposta:")

if resposta1 == "1":
    pontuacao += 1

# Pergunta 2
print("\nPergunta 2: Você gosta de horarios flexíveis ou prefere horárrios fixos?")
print("1. Horários flexíveis")
print("2. Horários fixos")
resposta2 = input("Digite o número da sua resposta:")

# if resposta2 == "1":
#     pontuacao += 1

# Pergunta 3
print("\nPergunta 3: Você valoriza a pontualidade?")
print("1. Sim")
print("2. Não")
resposta3 = input("Digite o número da sua resposta:")

if resposta3 == "1":
    pontuacao += 1

    # Pergunta 4
    print("\nPergunta 4: Você prefere uma comunicação direta ou indireta?")
    print("1. Direta")
    print("2. Indireta")
    resposta4= input("Digite o número da sua resposta: ")

    if resposta4 == "1":
        pontuacao += 1

        # Pergunta 5
        print("\nPergunta 5: Você gosta de tomar decisões rapidamente ou prefere analisar todas as opções antes?")
        print("1. Tomar decisões rapidamente")
        print("2. Analisar todas as opções antes")
        resposta5 = input("Digite o número da sua resposta: ")

        if resposta5 == "1":
            pontuacao += 1

        print("\nSua pontuação final é:", pontuacao)

        if pontuacao >= 4:
            print("Parabéns! Você tem um bom fit cultural com a cultura holandesa.")
        else:
            print("Você pode ter algumas dificuldades em se adaptar á cultura holandesa, mas não se preocupe, com o tempo você pode se adaptar melhor.")
            