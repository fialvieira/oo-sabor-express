class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Bistrô'
restaurante_praca.categoria = 'Italiana'

restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'
restaurante_pizza.ativo = True

print('É Fast Food' if restaurante_pizza.categoria == 'Fast Food' else 'Não é Fast Food')
print(f'{restaurante_pizza.nome} - {restaurante_pizza.categoria}')

print(dir(restaurante_praca))
print(vars(restaurante_praca))
print('Restaurante ativo' if restaurante_praca.ativo else 'Restaurante inativo')

categoria = Restaurante.categoria