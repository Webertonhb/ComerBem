print("quero da o cu")
#variaveis (str - nome)
# (int - numeros inteiros)
# (float - numeros quebrados)

# boleolean
is_puthon = True
is_java = False

# armazenamento condicoes
ingressos  = 50
compradores = 250
tem_ingresso_suficiente = (ingressos >= compradores)
print(tem_ingresso_suficiente) 
 

 #_________________________________________________________________

nome = input("digite seu nome:")
idade = int(input("digite sua idade:"))
peso = float(input("informe seu peso:"))
print (nome)
print (type(idade))
print (type(peso))

#__________________________________________________________________

soma = 1 + 1
multiplicacao = 4 * 4
divisao = 30 / 3
potencia = 7 ** 2

print("soma", soma)
print("multiplicacao", multiplicacao)
print("divisao", divisao)
print("potencia", )

#_________________________________________________________________

salario = float(input("informe seu salario: "))

if salario <= 1400:
    print("jovem aprendiz")
elif salario > 1400 and salario <= 2800:
    print("salario minimo")
else:
    print("a cima de 2 salrios minimos")

#_________________________________________________________________

lista_numeros =[1, 2, 3]
        #index: 0, 1, 2
print(lista_numeros[0])
print(lista_numeros[1])
print(lista_numeros[2])

# append | item          | mutador    | acrescenta um novo item no final da lista
# insert | posição, item | mutador    | insere um novo item na posição dada
# pop    | nenhum        | hibrido    | remove e retorna o último item
# pop    | posição       | hibrido    | remove e retorna o item da posição
# sort   | nenhum        | mutador    | ordena a lista
# reverse| nenhum        | mutador    | ordena a lista em ordem reversa
# index  | item          | retorna idx| retorna a posição da primeira ocorrência do item
# count  | item          | retorna ct | retorna o numero de ocorrências do item
# remove | item          | mutador    | remove a primeira ocorrência do item

#_________________________________________________________________

notas =[]

for x in range(5):
    codigo_aluno = input("RM: ")
    nota + float(input("Nota: "))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)

    print(" quantidade de notas", len(notas))

    for n in notas:
        codigo_aluno = n[0]
        nota = n[1]
        print("o RM", codigo_aluno, "tirou a nota: ", nota)

    

notas2 = []

contador = 1

while contador <= 5:
    codigo_aluno2 = input("RM: ")
    nota + float(input("Nota: "))
    resultado2 =[codigo_aluno, notas2]
    notas.append(resultado)

    contador = contador + 1

print( "quantidade de notas", len (notas))

#_________________________________________________________________

pessoa = {
    "nome": "weberton",
    "level": 99,
    "hp": 99,
    "xp": 99,
    "dano": 98,
}

npc = [
    {"nome": "Marretinha", "dano": 1, "hp": 1, "xp": 1},
    {"nome": "Marreta", "dano": -1, "hp": -1, "xp": -1},

]

print( pessoa['nome'])
print( pessoa['level'])
print( pessoa['hp'])
print( pessoa['xp'])
print( pessoa['dano'])

print( npc['nome'])
print( npc['level'])
print( npc['hp'])
print( npc['xp'])
print( npc['dano'])

#_________________________________________________________________

#funções
def minha_funcao(valor1, valor2):
    return valor1 + valor2
resposta = minha_funcao(10, 10)

print("resposta", resposta)