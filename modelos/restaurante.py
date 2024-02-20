class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria) -> None:
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self) -> str:
        return f'nome: {self._nome} | categoria: {self._categoria} | ativo: {self.ativo}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f"{'nome'.ljust(20)} | {'categoria'.ljust(20)} | ativo")
        for restaurante in cls.restaurantes:
            print(f'{str(restaurante._nome).ljust(20)} | {str(restaurante._categoria).ljust(20)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return 'verdadeiro' if self._ativo else 'falso'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_praca.alternar_estado()
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

Restaurante.listar_restaurantes()