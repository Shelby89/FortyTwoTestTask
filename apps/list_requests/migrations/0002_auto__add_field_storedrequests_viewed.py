# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'StoredRequests.viewed'
        db.add_column(u'list_requests_storedrequests', 'viewed',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'StoredRequests.viewed'
        db.delete_column(u'list_requests_storedrequests', 'viewed')


    models = {
        u'list_requests.storedrequests': {
            'Meta': {'object_name': 'StoredRequests'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'path_info': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'remote_address': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'request_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'server_port': ('django.db.models.fields.IntegerField', [], {}),
            'server_protocol': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'viewed': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['list_requests']