class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria) -> None:
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self) -> str:
        return f'nome: {self.nome} | categoria: {self.categoria} | ativo: {self.ativo}'
    
    def listar_restaurantes():
        print(f"{'nome'.ljust(20)} | {'categoria'.ljust(20)} | ativo")
        for restaurante in Restaurante.restaurantes:
            print(f'{str(restaurante.nome).ljust(20)} | {str(restaurante.categoria).ljust(20)} | {restaurante.ativo}')

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

Restaurante.listar_restaurantes()