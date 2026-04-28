nomes = []
nota_tecnica = []
aprovados = []

n_candidatos = int(input("são quantos candidatos: "))
posicao = 1

for i in range(n_candidatos):
    candidatos = input(f"\nqual o nome do candidato {posicao}: ")
    nota = float(input(f"qual a nota de compertencia de (0 a 10) desse candidato {posicao}: "))

    while nota > 10 or nota < 0:
        print("\nNOTA INFALIDA, tem que ser entre (0 a 10),digite novamente")
        nota = float(input(f" qual a nota de compertencia de (0 a 10) desse candidato {posicao}:"))

    nomes.append(candidatos)
    nota_tecnica.append(nota)
    posicao = posicao + 1

for i in range(len(nota_tecnica)):
    if nota_tecnica[i] >= 7:
        
        aprovados.append(nomes[i])

if len(aprovados) == 0:
    print("infelismente nenhum candidato foi aprovado")

elif len(aprovados) == 1:
    print(f"apenas: {aprovados},foi aprovado ")

else:
    print(f"{aprovados}, foram aprovados")
