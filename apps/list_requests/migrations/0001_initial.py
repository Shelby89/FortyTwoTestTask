# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'StoredRequests'
        db.create_table(u'list_requests_storedrequests', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('request_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('method', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('path_info', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('server_protocol', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('server_port', self.gf('django.db.models.fields.IntegerField')()),
            ('remote_address', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'list_requests', ['StoredRequests'])


    def backwards(self, orm):
        # Deleting model 'StoredRequests'
        db.delete_table(u'list_requests_storedrequests')


    models = {
        u'list_requests.storedrequests': {
            'Meta': {'object_name': 'StoredRequests'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'path_info': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'remote_address': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'request_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'server_port': ('django.db.models.fields.IntegerField', [], {}),
            'server_protocol': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['list_requests']