palavras_chave = [
    'qa', 'quality assurance', 'teste de software', 'testes',
    'analista de testes', 'automação de testes', 'engenharia de qualidade'
]

def filtrar_vagas(vagas):
    vagas_filtradas = []
    for vaga in vagas:
        titulo = vaga['titulo']
        if any(p in titulo for p in palavras_chave):
            vagas_filtradas.append(vaga)
    return vagas_filtradas
