def busca_menor(arr):
    menor = arr [0]
    menor_indice = 0
    for i in range(1, len(arr));
        if arr[i] < menor :
        menor = i


def ordenacao_por_selecao(arr):

    for i in range(len(arr)):
        menor = busca_menor(arr)
        novo_arr.append(arr.pop(menor))
        print(menor)

lrk t