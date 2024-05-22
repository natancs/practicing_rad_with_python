import pandas as pd


def save_data(instance):
    try:
        nome_planilha = "./dados/planilhaAlunos.xlsx"
        dados = []
        del (instance.treeMedias.get()[0])

        for linha in instance.treeMedias.get():
            lstDados = []
            index = instance.treeMedias.get().index(linha)
            for valor in instance.treeMedias.get_row(index):
                lstDados.append(valor)

            dados.append(lstDados)

        frame = pd.DataFrame(data=dados, columns=instance.dadosCulunas)
        frame.to_excel(nome_planilha, index=False)
        print('Dados salvos')
    except Exception as e:
        print('Não foi possível salvar os dados', e)
