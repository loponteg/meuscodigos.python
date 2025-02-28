nome = input("Digite o nome do aluno que deseja acessar a nota: ")
ap1 = float(input("Digite a nota da ap1 do aluno: "))
ap2 = float(input("Digite a nota da ap2 do aluno: "))
media = (ap1 + ap2)/2

if media >= 6:
    print("O aluno" ,nome,"teve média de" ,media,"e foi APROVADO!")
else:
    print("O aluno" ,nome,"teve média de" ,media,"e foi REPROVADO!")
