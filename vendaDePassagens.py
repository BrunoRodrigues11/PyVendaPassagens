polt = [
    # 0, 1, 2, 3
    [0, 1, 0, 0],  # 0
    [0, 0, 0, 1],  # 1
    [0, 0, 0, 0],  # 2
    [0, 0, 0, 0],  # 3
    [0, 0, 1, 0],  # 4
    [0, 0, 0, 0],  # 5
    [0, 0, 1, 0],  # 6
    [0, 0, 1, 0],  # 7
    [0, 1, 0, 0],  # 8
    [0, 1, 0, 0]   # 9
]

qtdePolt = int(0)
vlrTot = float(0)
mlinha = []
lugares = []


class colors:  # classe para colorir o texto no terminal
    # Cores
    green = "\033[0;32m"
    red = "\033[0;31m"
    red_bold = "\033[1;31m"
    white = "\033[0;97m"
    white_bold = "\033[1;97m"
    yellow = "\033[0;33m"
    close = "\033[m"


def exibeMapaPoltrona():  # exibe o mapa das poltronas
    print("-"*10, "MAPA DE POLTRONAS", "-"*10)
    print("{}0{} - Poltrona desocupada".format(colors.green, colors.close))
    print("{}1{} - Poltrona ocupada".format(colors.red, colors.close))
    print(" ")

    for a in range(0, 10):
        for b in range(0, 4):
            print(f"{colors.green} {polt[a][b]} {colors.close}"
                  if polt[a][b] == 0 else f"{colors.red} {polt[a][b]} {colors.close}", end="")
        print()
    print()


def entradaDados():
    exibeMapaPoltrona()
    # input do usuário da linha e coluna que ele deseja sentar
    print("-"*10, "PASSAGENS S/A", "-"*10)
    linha, coluna = input(
        "Informe a linha(0,9) e a coluna(0,3) que você deseja sentar: ").split(" ", 1)
    print(" ")

    print("Você escolheu: Linha: {} e Coluna: {}. Confirmar?".format(linha, coluna))
    resp = str(input())

    # tranforma a resposta em letra maiuscula
    resp = resp.upper()

    if (resp == "SIM") or (resp == "S"):
        verificaPolt(linha, coluna)
    elif (resp == "NAO") or (resp == "NÃO") or (resp == "N"):
        entradaDados()


def verificaPolt(linha, coluna):
    # convertendo a linha e coluna de str para int
    # para que seja possivel fazer a comparacao
    linha = int(linha)
    coluna = int(coluna)

    # atribuindo o valor da poltrona de acordo com a
    # posição informada pelo usuário
    poltrona = polt[linha][coluna]

    # verificando se a poltrona esta vazia ou ocupada
    if poltrona == 0:
        print(" ")
        print("{}SUCESSO ✓{}".format(colors.green, colors.close))
        print("Poltrona reservada!")

        # contando as poltronas resevadas pelo usuário
        global qtdePolt
        qtdePolt += 1

        # se estava vazia, atribuir valor 1 pois esta ocupada agora
        polt[linha][coluna] = 1
        calcValorPassagem(linha, coluna, qtdePolt)

    elif poltrona == 1:
        print(" ")
        print("{}FALHOU X{}".format(colors.red, colors.close))
        print("Poltrona ocupada! Escolha outra.")
        print(" ")
        entradaDados()


def calcValorPassagem(linha, coluna, qtdePolt):
    vlrPassagem = float(20)
    acrescimo = float()

    global vlrTot

    # verifica se a poltrona é na janela
    # se sim, acrescenta 10% no valor da passagem
    if (coluna == 0) or (coluna == 3):
        acrescimo = vlrPassagem * 0.10
        vlrPassagem += acrescimo

    if (qtdePolt > 1):
        vlrTot += vlrPassagem
    else:
        vlrTot = vlrPassagem

    contaPolt(qtdePolt, linha, coluna, acrescimo, vlrPassagem, vlrTot)


def contaPolt(qtdePolt, linha, coluna, acrescimo, vlrPassagem, vlrTot):
    qtdeOcupada = int(0)
    qtdeDesocupada = int(0)

    # faz a contagem de quantas poltronas estão vazias e quantas estão ocupadas
    for x in range(0, 10):
        for y in range(0, 4):
            if polt[x][y] == 1:
                qtdeOcupada += 1
            if polt[x][y] == 0:
                qtdeDesocupada += 1

    # calcula a quantidade total de poltronas
    totalPolt = int(qtdeDesocupada+qtdeOcupada)

    # calcula a porcentagem de ocupação
    porcentOcup = float(qtdeOcupada/totalPolt * 100)

    exibeResults(qtdePolt, linha, coluna, acrescimo, vlrPassagem, qtdeOcupada,
                 qtdeDesocupada, totalPolt, porcentOcup, vlrTot)


def exibeResults(qtdePolt, linha, coluna, acrescimo, vlrPassagem, qtdeOcupada, qtdeDesocupada, totalPolt, porcentOcup, vlrTot):
    # exibe os resultados
    print("")
    print("-"*15, "BILHETE DA VIAGEM", "-"*15)
    print("")
    print(" "*15, "  PASSAGENS S/A  ", " "*15)
    print("")

    # alimenta a matriz com as localizações
    # das poltronas reservadas pelo usuário
    for x in range(0, 1):
        mcoluna = []
        for y in range(0, 1):
            mcoluna.append(linha)
            mcoluna.append(coluna)
        mlinha.append(mcoluna)

    if (qtdePolt > 1):
        print("Poltronas reservadas por você.... {}".format(qtdePolt))
        print()
        for w in range(0, qtdePolt):
            print("Sua poltrona {}: Linha: {} | Coluna: {}.".format(w+1,
                                                                    mlinha[w][0], mlinha[w][1]))
    else:
        print("Poltrona reservadas por você..... {}".format(qtdePolt))
        print("Sua poltrona: Linha: {} | Coluna: {}.".format(linha, coluna))

    print("")
    print("Valor da passagem................ R$ {:.2f}".format(20))
    print("Valor de acrescimos.............. R$ {:.2f}".format(acrescimo))
    print("Total a pagar.................... R$ {:.2f}".format(vlrPassagem))
    print("")
    print(" "*15, "INFORMAÇÕES ADICIONAIS", " "*15)
    print("")
    print("Qtde de poltronas ocupadas....... {}".format(qtdeOcupada))
    print("Qtde de poltronas deocupadas..... {}".format(qtdeDesocupada))
    print("Total de poltronas............... {}".format(totalPolt))
    print("Porcentual de ocupação........... {:.2f}%".format(porcentOcup))
    print("Total arrecadado................. R$ {:.2f}".format(vlrTot))
    print("")
    print("{}Boa viagem!{}".format(colors.white_bold, colors.close))
    print("")

    novaReserva()


def novaReserva():
    resp2 = str(input("Deseja reservar outra poltrona?: "))
    resp2 = resp2.upper()

    if (resp2 == "SIM") or (resp2 == "S"):
        entradaDados()
    elif (resp2 == "NAO") or (resp2 == "NÂO") or (resp2 == "N"):
        print("")
        print("Obrigado pela preferência. Volte sempre!")
        print("")
        print("{}Programa encerrado.{}".format(colors.red_bold, colors.close))
        print("")


# inicio
entradaDados()
