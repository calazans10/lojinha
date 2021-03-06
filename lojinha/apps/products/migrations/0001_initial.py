# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Product'
        db.create_table('product', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=1500)),
            ('price', self.gf('django.db.models.fields.DecimalField')(decimal_places=2, max_digits=12)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Category'], related_name='products')),
            ('quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True, null=True)),
        ))
        db.send_create_signal('products', ['Product'])

        # Adding model 'Category'
        db.create_table('category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(to=orm['products.Category'], null=True, blank=True, related_name='children')),
            ('lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal('products', ['Category'])


    def backwards(self, orm):
        # Deleting model 'Product'
        db.delete_table('product')

        # Deleting model 'Category'
        db.delete_table('category')


    models = {
        'products.category': {
            'Meta': {'object_name': 'Category', 'db_table': "'category'"},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'to': "orm['products.Category']", 'null': 'True', 'blank': 'True', 'related_name': "'children'"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'products.product': {
            'Meta': {'object_name': 'Product', 'db_table': "'product'"},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Category']", 'related_name': "'products'"}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1500'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '12'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        }
    }

    complete_apps = ['products']