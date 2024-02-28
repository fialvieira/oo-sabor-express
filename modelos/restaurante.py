from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria) -> None:
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self) -> str:
        return f'nome: {self._nome} | categoria: {self._categoria} | ativo: {self.ativo}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f"{'nome'.title().ljust(20)} | {'categoria'.title().ljust(20)} | {'Avaliação'.ljust(20)} | {'Status'}")
        for restaurante in cls.restaurantes:
            print(f'{str(restaurante._nome).ljust(20)} | {str(restaurante._categoria).ljust(20)} | {str(restaurante.media_avaliacoes).ljust(20)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return 'verdadeiro' if self._ativo else 'falso'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 0
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media