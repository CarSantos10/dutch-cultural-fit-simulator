# Simulador de Fit Cultural Holandês!
# Criado por: Carlos Santos

pontuacao = 0

print("Cem-vindo ao Simulador de Fit Cultural Holandês!")
print("Vamos ver o quanto o seu jeito combina com a cultura holandesa de trabalho.\n")

# Pergunta 1 - Franqueza
resposta1= input("Você gosta de dizer o que pensa de forma direta, mesmo que soe duro? (sim/nao):").lower().strip()

while resposta1 != "sim" and resposta1 != "nao":
    print("Resposta inválida. Por favor, digite apenas 'sim' ou 'nao'.")
    resposta1 = input("Você gosta de dizer o que pensa de forma direta, mesmo que soe duro? (sim/nao): ").lower().strip()
 
if resposta1 == "sim":
    pontuacao = pontuacao + 1
 
# Pergunta 2 - Almoço
resposta2 = input("Você prefere um almoço rápido e simples ao invés de uma refeição longa? (sim/nao): ").lower().strip()
 
while resposta2 != "sim" and resposta2 != "nao":
    print("Resposta inválida. Por favor, digite apenas 'sim' ou 'nao'.")
    resposta2 = input("Você prefere um almoço rápido e simples ao invés de uma refeição longa? (sim/nao): ").lower().strip()
 
if resposta2 == "sim":
    pontuacao = pontuacao + 1
 
# Pergunta 3 - Pontualidade
resposta3 = input("Você valoriza pontualidade? (sim/nao): ").lower().strip()
 
while resposta3 != "sim" and resposta3 != "nao":
    print("Resposta inválida. Por favor, digite apenas 'sim' ou 'nao'.")
    resposta3 = input("Você valoriza pontualidade? (sim/nao): ").lower().strip()
 
if resposta3 == "sim":
    pontuacao = pontuacao + 1
 
# Pergunta 4 - Comunicação
resposta4 = input("Você prefere uma comunicação direta ou indireta? (direta/indireta): ").lower().strip()
 
while resposta4 != "direta" and resposta4 != "indireta":
    print("Resposta inválida. Por favor, digite apenas 'direta' ou 'indireta'.")
    resposta4 = input("Você prefere uma comunicação direta ou indireta? (direta/indireta): ").lower().strip()
 
if resposta4 == "direta":
    pontuacao = pontuacao + 1
 
# Pergunta 5 - Horário de saída
resposta5 = input("Você prefere sair do trabalho no horário certo, mesmo com tarefas pendentes? (sim/nao): ").lower().strip()
 
while resposta5 != "sim" and resposta5 != "nao":
    print("Resposta inválida. Por favor, digite apenas 'sim' ou 'nao'.")
    resposta5 = input("Você prefere sair do trabalho no horário certo, mesmo com tarefas pendentes? (sim/nao): ").lower().strip()
 
if resposta5 == "sim":
    pontuacao = pontuacao + 1
 
# Resultado final
    print("\nSua pontuação final foi:", pontuacao)
 
if pontuacao >= 3:
    print("Parabéns! Você tem um ótimo fit com a cultura de trabalho holandesa!")
else:
    print("Você ainda tem um pouco a estudar sobre a cultura holandesa, mas está no caminho certo!")