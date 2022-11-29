"""1 - Encontre o menor elemento em uma BST"""

def minimo(raiz):
    nodo = raiz
    while nodo.esquerda is not None:
        nodo = nodo.esquerda
    return nodo.chave