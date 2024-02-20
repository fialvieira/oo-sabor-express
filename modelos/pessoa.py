class Pessoa():
    def __init__(self, nome, idade, profissao = ''):
        self._nome = nome.title()
        self._idade = idade
        self._profissao = profissao.title()

    def __str__(self) -> str:
        return f'{self._nome}, {self._idade} anos, {self._profissao}.'
    
    def aniversario(self):
        self._idade += 1

    @property
    def saudadacao(self):
        if self._profissao:
            return f'Olá, sou {self._nome}, tenho {self._idade} anos e trabalho como {self._profissao}.'
        else:
            return f'Olá, sou {self._nome}, tenho {self._idade} anos.'
        
pessoa = Pessoa('Filipe', 41, 'analista de sistemas')
pessoa.aniversario()
print(pessoa.saudadacao)