nome = []
medias = []

aluno_posição = 1
alunos = int(input("quantos alunos para cadastrar a media de suas notas: "))

for i in range(alunos):
    aluno = input(f"\nqual o nome do aluno {aluno_posição}: ")
    media = float(input(f"qual a media do aluno {aluno_posição}: "))
    

    nome.append(aluno)
    medias.append(media)
    aluno_posição = aluno_posição + 1

soma_notas = sum(medias)
numero_notas = len(medias)
media_sala = soma_notas / numero_notas
maior_nota = max(medias)
indice_maior = medias.index(maior_nota)
melhor_aluno = nome[indice_maior]

print(f"\nlista de alunos: {nome}")
print(f'\nmedias de cada alunos: {medias}')
print(f"\nmedia da sala: {media_sala}")
print(f"\nmelhor aluno foi: {melhor_aluno}, media nota: {indice_maior}")
