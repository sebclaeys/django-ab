# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Experiment'
        db.create_table(u'ab_experiment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('template_name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('goal', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
        ))
        db.send_create_signal(u'ab', ['Experiment'])

        # Adding model 'Test'
        db.create_table(u'ab_test', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('experiment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ab.Experiment'])),
            ('template_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('hits', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('conversions', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
        ))
        db.send_create_signal(u'ab', ['Test'])


    def backwards(self, orm):
        # Deleting model 'Experiment'
        db.delete_table(u'ab_experiment')

        # Deleting model 'Test'
        db.delete_table(u'ab_test')


    models = {
        u'ab.experiment': {
            'Meta': {'object_name': 'Experiment'},
            'goal': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'template_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'ab.test': {
            'Meta': {'object_name': 'Test'},
            'conversions': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'experiment': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ab.Experiment']"}),
            'hits': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'template_name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['ab']