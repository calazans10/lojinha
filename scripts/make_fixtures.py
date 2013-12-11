from decimal import Decimal
from django.db.models.loading import get_model
from products.models import Category, Product


def clear_model(app, model_cls):
    for obj in get_model(app, model_cls).objects.all():
        obj.delete()


def clear_data():
    clear_model('auth', 'User')
    clear_model('products', 'Category')
    clear_model('products', 'Product')


def set_metadata(product, metadata):
    if product.category.name == 'Livro':
        product.metadata['autor'] = metadata['autor']
        product.metadata['genero'] = metadata['genero']

    if product.category.name == 'DVD show':
        product.metadata['artista'] = metadata['artista']
        product.metadata['numero_de_musicas'] = metadata['numero_de_musicas']

    if product.category.name == 'DVD filme':
        product.metadata['diretor'] = metadata['diretor']
        product.metadata['ano_lancamento'] = metadata['ano_lancamento']

    if product.category.name == 'DVD software':
        product.metadata['versao'] = metadata['versao']
        product.metadata['requisitos_do_sistema'] = metadata['requisitos_do_sistema']

    if product.category.name == 'Relógios':
        product.metadata['marca'] = metadata['marca']
        product.metadata['tipo'] = metadata['tipo']

    if product.category.name == 'Perfume':
        product.metadata['marca'] = metadata['marca']
        product.metadata['quantidade_em_ml'] = metadata['quantidade_em_ml']


def make_category(name, parent=None):
    category = Category(name=name, parent=parent)
    category.save()
    return category


def make_product(code, title, description, price, category, quantity, metadata):
    product = Product(code=code, title=title, description=description,
                      price=price, category=category, quantity=quantity)
    product.save()
    set_metadata(product, metadata)
    return product


def make_data():
    livro = make_category('Livro')
    dvd = make_category('DVD')
    dvd_filme =make_category('DVD filme', dvd)
    dvd_show = make_category('DVD show', dvd)
    dvd_software = make_category('DVD software', dvd)
    relogios = make_category('Relógios')
    perfume = make_category('Perfume')

    description = 'Gravado ao vivo durante diferentes datas da turnê "New World Tour" em 1993, este DVD traz o genial Paul McCartney interpretando os grandes sucessos de sua carreira, além de hits que foram consagrados pelos inesquecíveis The Beatles.'
    metadata = {'artista': 'Paul McCartney', 'numero_de_musicas': 27}
    make_product('0001', 'Paul McCartney - Paul is Live', description,
                 Decimal('22.41'), dvd_show, 3, metadata)


def run():
    clear_data()
    make_data()
