from decimal import Decimal
from django.db.models.loading import get_model
from scripts.descriptions import *
from lojinha.settings import MEDIA_URL
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


def make_product(code, title, description, price, category, quantity,
                 photo, metadata):
    product = Product(code=code, title=title, description=description,
                      price=price, category=category, quantity=quantity,
                      photo=photo)
    product.save()
    set_metadata(product, metadata)
    return product


def make_data():
    livro = make_category('Livro')
    dvd = make_category('DVD')
    dvd_filme = make_category('DVD filme', dvd)
    dvd_show = make_category('DVD show', dvd)
    dvd_software = make_category('DVD software', dvd)
    relogios = make_category('Relógios')
    perfume = make_category('Perfume')

    photo = MEDIA_URL + 'images/paul.jpg'
    metadata = {'artista': 'Paul McCartney', 'numero_de_musicas': 27}
    make_product('0001', 'Paul McCartney - Paul is Live', DESCRIPTION1,
                 Decimal('22.41'), dvd_show, 3, photo, metadata)

    photo = MEDIA_URL + 'img/products/bussunda.jpg'
    metadata = {'autor': 'Guilherme Fiuza', 'genero': 'Biografia'}
    make_product('0002', 'Bussunda - A vida do Casseta', DESCRIPTION2,
                 Decimal(53.90), livro, 2, photo, metadata)

    photo = MEDIA_URL + 'images/principe.jpg'
    metadata = {
        'autor': 'Antoine de Saint-Exupery',
        'genero': 'Livros de Infantil'
    }
    make_product('0003', 'O Pequeno Príncipe', DESCRIPTION3, Decimal('34.90'),
                 livro, 4, photo, metadata)

    photo = MEDIA_URL + 'images/verissimo.jpg'
    metadata = {'autor': 'Luis Fernando Verissimo', 'genero': 'Humor'}
    make_product('0004', 'Diálogos Impossíveis', DESCRIPTION4,
                 Decimal('32.90'), livro, 1, photo, metadata)

    photo = MEDIA_URL + 'images/amor.jpg'
    metadata = {'diretor': 'Michael Haneke', 'ano_lancamento': 2013}
    make_product('0005', 'Amor', DESCRIPTION5, Decimal('42.00'), dvd_filme,
                 1, photo, metadata)

    photo = MEDIA_URL + 'images/windows.jpg'
    metadata = {
        'versao': '8.1',
        'requisitos_do_sistema': '''Processador: 1 gigahertz (GHz) ou mais rápido com suporte para PAE, NX, e SSE2
        Memória RAM: 1 gigabyte (GB) (32 bits) ou 2 GB (64-bit)
        Espaço em HD: 16 GB (32 bits) ou 20 GB (64-bit)'''
    }
    make_product('0006', 'Windows 8 Pro - Versão Atualizada - PC',
                 DESCRIPTION6, Decimal('269.00'), dvd_software, 5, photo,
                 metadata)


def run():
    clear_data()
    make_data()
