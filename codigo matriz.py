def soma(a, b):
    return a + b


def multiplicacao(a, b):
    return a * b


def ler_matriz(nome):
    n = int(input(f"Digite o tamanho N da matriz {nome} (NxN): "))
    matriz = []
    print(f"Digite os elementos da matriz {nome}:")
    for i in range(n):
        linha = list(map(float, input(f"Linha {i + 1}: ").split()))
        matriz.append(linha)
    return matriz


def verificar_quadrada(matriz):
    n = len(matriz)
    return all(len(linha) == n for linha in matriz)


def multiplicar_matrizes(A, B):
    n = len(A)
    resultado = [[0 for _ in range(n)] for _ in range(n)]

    print("\n=== Passo a passo da multiplicação ===")
    for i in range(n):
        for j in range(n):
            soma_temp = 0
            for k in range(n):
                mult = multiplicacao(A[i][k], B[k][j])
                print(f"A[{i + 1},{k + 1}] * B[{k + 1},{j + 1}] = {A[i][k]} * {B[k][j]} = {mult}")
                soma_temp = soma(soma_temp, mult)
            resultado[i][j] = soma_temp
            print(f"Soma final para C[{i + 1},{j + 1}] = {soma_temp}\n")
    return resultado


def mostrar_matriz(matriz, nome):
    print(f"\nMatriz {nome}:")
    for linha in matriz:
        print(" ".join(f"{valor:8.2f}" for valor in linha))


# Programa principal
A = ler_matriz("A")
B = ler_matriz("B")

if not verificar_quadrada(A) or not verificar_quadrada(B):
    print("Erro: Ambas as matrizes devem ser quadradas!")
else:
    if len(A) != len(B):
        print("Erro: As matrizes devem ter o mesmo tamanho para multiplicação!")
    else:
        mostrar_matriz(A, "A")
        mostrar_matriz(B, "B")

        C = multiplicar_matrizes(A, B)

        mostrar_matriz(C, "Resultado C = A x B")
