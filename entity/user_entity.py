from uuid import uuid4


class UserEntity:
    def __init__(self, nome, email, password) -> None:
        self.id = uuid4()
        self.nome = nome
        self.email = email
        self.password = password
