import pandas as pd


def loading_data(instance):
    try:
        nome_planilha = "./dados/planilhaAlunos.xlsx"
        dados = pd.read_excel(nome_planilha)

        nn = len(dados['Aluno'])
        for i in range(nn):
            nome = dados["Aluno"][i]
            nota1 = str(dados["Nota1"][i])
            nota2 = str(dados["Nota2"][i])
            media = str(dados["Média"][i])
            situacao = dados["Situação"][i]
            values = (nome, nota1, nota2, media, situacao)

            instance.treeMedias.insert(
                '', 'end', iid=instance.iid, values=(values))
            instance.iid = instance.iid + 1
            instance.id = instance.id + 1
    except Exception as e:
        print('Ainda não existem dados para carregar: ', e)
