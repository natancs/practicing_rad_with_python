def check_status(nota1, nota2):
    media = (nota1+nota2)/2
    if (media >= 7.0):
        situacao = 'Aprovado'
    elif (media >= 5.0):
        situacao = 'Em Recuperação'
    else:
        situacao = 'Reprovado'

    return media, situacao
