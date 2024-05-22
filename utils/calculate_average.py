from utils.check_status import check_status


def calculate_average(instance):
    try:
        nome = instance.txtNome.get()
        nota1 = float(instance.txtNota1.get())
        nota2 = float(instance.txtNota2.get())
        media, situacao = check_status(nota1, nota2)
        values = (nome, str(nota1), str(nota2), str(media), situacao)

        instance.treeMedias.add_row(values)
        instance.iid = instance.iid + 1
        instance.id = instance.id + 1

        instance.fSalvarDados()
    except ValueError:
        print('Entre com valores válidos')
    finally:
        instance.txtNome.delete(0, 'end')
        instance.txtNota1.delete(0, 'end')
        instance.txtNota2.delete(0, 'end')
