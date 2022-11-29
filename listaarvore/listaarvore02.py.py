"""2 - Encontre o maior elemento em uma BST."""

def maximo(raiz):
    nodo = raiz
    while nodo.direita is not None:
        nodo = nodo.direita
    return nodo.chave