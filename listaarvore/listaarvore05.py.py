"""05 - Verifique se uma árvore binária é balanceada"""

def balanceada(raiz):
    if raiz is None:
        return True

    altura_esq = altura(raiz.esquerda)
    altura_dir = altura(raiz.direita)
    if abs(altura_esq - altura_dir) > 1:
        return False

    return balanceada(raiz.esquerda) and balanceada(raiz.direita)