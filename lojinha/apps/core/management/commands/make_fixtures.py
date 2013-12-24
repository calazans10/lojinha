# -*- coding: utf-8 -*-
from decimal import Decimal
from django.core.management.base import BaseCommand
from django.db.models.loading import get_model
from django.conf import settings
from core.management.commands import _description
from products.models import Category, Product


def clear_model(app, model_cls):
    for obj in get_model(app, model_cls).objects.all():
        obj.delete()


def clear_data():
    clear_model('auth', 'User')
    clear_model('products', 'Category')
    clear_model('products', 'Product')
    clear_model('products', 'Item')


def set_metadata(product, metadata):
    if product.category.name == u'Livro':
        product.metadata['autor'] = metadata['autor']
        product.metadata['genero'] = metadata['genero']

    if product.category.name == u'DVD show':
        product.metadata['artista'] = metadata['artista']
        product.metadata['numero_de_musicas'] = metadata['numero_de_musicas']

    if product.category.name == u'DVD filme':
        product.metadata['diretor'] = metadata['diretor']
        product.metadata['ano_lancamento'] = metadata['ano_lancamento']

    if product.category.name == u'DVD software':
        requisitos = 'requisitos_do_sistema'
        product.metadata['versao'] = metadata['versao']
        product.metadata[requisitos] = metadata[requisitos]

    if product.category.name == u'Relógios':
        product.metadata['marca'] = metadata['marca']
        product.metadata['tipo'] = metadata['tipo']

    if product.category.name == u'Perfume':
        product.metadata['marca'] = metadata['marca']
        product.metadata['quantidade_em_ml'] = metadata['quantidade_em_ml']


def make_category(name, parent=None):
    category = Category(name=name, parent=parent)
    category.save()
    print('Create Category %s' % category)
    return category


def make_product(code, title, description, price, category, quantity,
                 photo, metadata):
    product = Product(code=code, title=title, description=description,
                      price=price, category=category, quantity=quantity,
                      photo=photo)
    product.save()
    set_metadata(product, metadata)
    print('Create Product: %s' % product)
    return product


def make_data():
    livro = make_category(u'Livro')
    dvd = make_category(u'DVD')
    dvd_filme = make_category(u'DVD filme', dvd)
    dvd_show = make_category(u'DVD show', dvd)
    dvd_software = make_category(u'DVD software', dvd)
    relogios = make_category(u'Relógios')
    perfume = make_category(u'Perfume')

    photo = settings.MEDIA_URL + 'images/paul.jpg'
    metadata = {'artista': u'Paul McCartney', 'numero_de_musicas': 27}
    make_product('0001', u'Paul McCartney - Paul is Live', _description.A,
                 Decimal('22.41'), dvd_show, 3, photo, metadata)

    photo = settings.MEDIA_URL + 'images/bussunda.jpg'
    metadata = {'autor': u'Guilherme Fiuza', 'genero': u'Biografia'}
    make_product('0002', u'Bussunda - A vida do Casseta', _description.B,
                 Decimal(53.90), livro, 2, photo, metadata)

    photo = settings.MEDIA_URL + 'images/principe.jpg'
    metadata = {
        'autor': u'Antoine de Saint-Exupery',
        'genero': u'Livros de Infantil'
    }
    make_product('0003', u'O Pequeno Príncipe', _description.C,
                 Decimal('34.90'), livro, 4, photo, metadata)

    photo = settings.MEDIA_URL + 'images/verissimo.jpg'
    metadata = {'autor': u'Luis Fernando Verissimo', 'genero': u'Humor'}
    make_product('0004', u'Diálogos Impossíveis', _description.D,
                 Decimal('32.90'), livro, 1, photo, metadata)

    photo = settings.MEDIA_URL + 'images/amor.jpg'
    metadata = {'diretor': u'Michael Haneke', 'ano_lancamento': 2013}
    make_product('0005', u'Amor', _description.E, Decimal('42.00'), dvd_filme,
                 1, photo, metadata)

    photo = settings.MEDIA_URL + 'images/windows.jpg'
    metadata = {
        'versao': '8.1',
        'requisitos_do_sistema': u'''Processador: 1 gigahertz (GHz) ou mais \
        rápido com suporte para PAE, NX, e SSE2
        Memória RAM: 1 gigabyte (GB) (32 bits) ou 2 GB (64-bit)
        Espaço em HD: 16 GB (32 bits) ou 20 GB (64-bit)'''
    }
    make_product('0006', u'Windows 8 Pro - Versão Atualizada - PC',
                 _description.F, Decimal('269.00'), dvd_software, 5, photo,
                 metadata)

    photo = settings.MEDIA_URL + 'images/perfume.jpg'
    metadata = {'marca': u'Natura', 'quantidade_em_ml': '100 ml'}
    make_product('0007', u'Deo Parfum Essencial Exclusivo', _description.G,
                 Decimal('149.00'), perfume, 1, photo, metadata)

    photo = settings.MEDIA_URL + 'images/relogiod.jpg'
    metadata = {'marca': u'Nike', 'tipo': u'Digital'}
    make_product('0008', u'Relógio Nike+ Sportwatch GPS', _description.H,
                 Decimal('699.00'), relogios, 1, photo, metadata)

    photo = settings.MEDIA_URL + 'images/relogioa.jpg'
    metadata = {'marca': u'Puma', 'tipo': u'Analógico'}
    make_product('0009', u'Relógio Puma Cloud', _description.I,
                 Decimal('399.00'), relogios, 1, photo, metadata)


class Command(BaseCommand):
    def handle(self, *args, **options):
        clear_data()
        make_data()
