pacientes = []
atendidos = []
valores = []

def titulo(mensa, traco="-"):
    print()
    print(mensa)
    print(traco*40)

def incluir(): #1
    titulo("Inclusão de Pacientes")
    nome = input("Nome do Paciente: ")
    pacientes.append(nome)

def listar(): #2
    titulo("Lista de Pacientes em Espera")
    if len(pacientes) == 0:
        print("Não há pacientes na lista de espera")
    else:
     for i, nome in enumerate(pacientes, start=1):
      print(f"{i}. {nome}")

def atender(): #3
    titulo("Atendimento")
    if len(pacientes) == 0:
        print("Não há pacientes na lista de espera")
    else:
        print(f"Atender: {pacientes[0]}")
        atendidos.append(pacientes[0]) 
        valores.append(0) #novo
        pacientes.pop(0)

def urgencia(): #4
    titulo("Inclusão de Urgência")
    nome = input("Nome do Paciente a ser Atendido em Urgência: ")
    pacientes.insert(0, nome)

def valor(): #5
    titulo("Informe o valor")
    nome = input("Nome do Paciente: ")
    try:
        posicao = atendidos.index(nome)
        valores[posicao] = float(input("Valor da Consulta: "))
        print("Valor cadastrado.")

    except:
        print("Paciente não está na lista de atendidos.")


def atendimentos(): #6
    titulo("Lista de Pacientes já atendidos")
    for a, v in zip(atendidos, valores):
        print(f'{a:20s} {v:9.2f}')

def totalizar(): #7
    titulo("Totalizar Consultas do Dia")
    num = len(valores)
    soma = sum(valores)
    print(f"N de atendimentos: {num}")
    print(f"Total do Dias R$: {soma:9.2f}")

def resumo(): #8
    titulo("Resumo de Atendimentos")
    print(f'Pacientes atendidos: ', len(atendidos))
    if len(atendidos) == 0:
        print("Não há pacientes atendidos no dia.")
        return
    menor = min(valores)
    maior = max(valores)

    i_menor = valores.index(menor)
    i_maior = valores.index(maior)
    print(f'Menor R$: {menor:9.2f} - Paciente:{atendidos[i_menor]}')
    print(f'Maior R$: {maior:9.2f} - Paciente: {atendidos[i_maior]}')

