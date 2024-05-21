import pandas as pd


def save_data(instance):
    try:
        nome_planilha = "./dados/planilhaAlunos.xlsx"
        dados = []

        for linha in instance.treeMedias.get_children():
            lstDados = []
            for valor in instance.treeMedias.item(linha)["values"]:
                lstDados.append(valor)

            dados.append(lstDados)

        frame = pd.DataFrame(data=dados, columns=instance.dadosCulunas)
        frame.to_excel(nome_planilha, index=False)

        print('Dados salvos')
    except Exception as e:
        print('Não foi possível salvar os dados', e)
