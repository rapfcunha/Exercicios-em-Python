"""06 - Determine se uma árvore é simétrica"""

def checa_simetrica(raiz):
    def simetricas(subarvore_esq, subarvore_dir):
        if not subarvore_esq and not subarvore_dir:
            return True
        elif subarvore_esq and subarvore_dir:
            return (subarvore_esq.chave == subarvore_dir.chave and
                    simetricas(subarvore_esq.esquerda, subarvore_dir.direita) and
                    simetricas(subarvore_esq.direita, subarvore_dir.esquerda))
        return False

    return not raiz or simetricas(raiz.esquerda, raiz.direita)