"""3 - Verifique se duas árvores binárias são idênticas."""

def identicas(a, b):
    
    if a is None and b is None:
        return True

    
    if a is not None and b is not None:
        return ((a.chave == b.chave) and
                identicas(a.esquerda, b.esquerda) and
                identicas(a.direita, b.direita))

    return False