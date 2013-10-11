# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ProgrammingLanguage'
        db.create_table(u'algorithm_programminglanguage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'algorithm', ['ProgrammingLanguage'])

        # Adding model 'Classification'
        db.create_table(u'algorithm_classification', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=35)),
            ('uri', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'algorithm', ['Classification'])

        # Adding model 'Algorithm'
        db.create_table(u'algorithm_algorithm', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('classification', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['algorithm.Classification'], null=True, blank=True)),
            ('uri', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('visible', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('reputation', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'algorithm', ['Algorithm'])

        # Adding model 'Implementation'
        db.create_table(u'algorithm_implementation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('algorithm', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['algorithm.Algorithm'])),
            ('code', self.gf('django.db.models.fields.TextField')()),
            ('programming_language', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['algorithm.ProgrammingLanguage'])),
            ('visible', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('reputation', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'algorithm', ['Implementation'])

        # Adding model 'Interest'
        db.create_table(u'algorithm_interest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('classification', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['algorithm.Classification'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'algorithm', ['Interest'])

        # Adding model 'ProeficiencyScale'
        db.create_table(u'algorithm_proeficiencyscale', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'algorithm', ['ProeficiencyScale'])

        # Adding model 'ProgrammingLanguageProeficiencyScale'
        db.create_table(u'algorithm_programminglanguageproeficiencyscale', (
            (u'proeficiencyscale_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['algorithm.ProeficiencyScale'], unique=True, primary_key=True)),
            ('programming_language', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['algorithm.ProgrammingLanguage'])),
        ))
        db.send_create_signal(u'algorithm', ['ProgrammingLanguageProeficiencyScale'])

        # Adding model 'ClassificationProeficiencyScale'
        db.create_table(u'algorithm_classificationproeficiencyscale', (
            (u'proeficiencyscale_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['algorithm.ProeficiencyScale'], unique=True, primary_key=True)),
            ('classification', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['algorithm.Classification'])),
        ))
        db.send_create_signal(u'algorithm', ['ClassificationProeficiencyScale'])

        # Adding model 'Question'
        db.create_table(u'algorithm_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('priority', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'algorithm', ['Question'])

        # Adding model 'QuestionAnswer'
        db.create_table(u'algorithm_questionanswer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['algorithm.Question'])),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'algorithm', ['QuestionAnswer'])

        # Adding model 'UserQuestion'
        db.create_table(u'algorithm_userquestion', (
            (u'question_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['algorithm.Question'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'algorithm', ['UserQuestion'])

        # Adding model 'UserQuestionAnswer'
        db.create_table(u'algorithm_userquestionanswer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('user_question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['algorithm.UserQuestion'])),
            ('question_answer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['algorithm.QuestionAnswer'])),
        ))
        db.send_create_signal(u'algorithm', ['UserQuestionAnswer'])

        # Adding model 'ImplementationQuestion'
        db.create_table(u'algorithm_implementationquestion', (
            (u'question_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['algorithm.Question'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'algorithm', ['ImplementationQuestion'])

        # Adding model 'ImplementationQuestionAnswer'
        db.create_table(u'algorithm_implementationquestionanswer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('implementation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['algorithm.Implementation'])),
            ('implementation_question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['algorithm.ImplementationQuestion'])),
            ('question_answer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['algorithm.QuestionAnswer'])),
        ))
        db.send_create_signal(u'algorithm', ['ImplementationQuestionAnswer'])


    def backwards(self, orm):
        # Deleting model 'ProgrammingLanguage'
        db.delete_table(u'algorithm_programminglanguage')

        # Deleting model 'Classification'
        db.delete_table(u'algorithm_classification')

        # Deleting model 'Algorithm'
        db.delete_table(u'algorithm_algorithm')

        # Deleting model 'Implementation'
        db.delete_table(u'algorithm_implementation')

        # Deleting model 'Interest'
        db.delete_table(u'algorithm_interest')

        # Deleting model 'ProeficiencyScale'
        db.delete_table(u'algorithm_proeficiencyscale')

        # Deleting model 'ProgrammingLanguageProeficiencyScale'
        db.delete_table(u'algorithm_programminglanguageproeficiencyscale')

        # Deleting model 'ClassificationProeficiencyScale'
        db.delete_table(u'algorithm_classificationproeficiencyscale')

        # Deleting model 'Question'
        db.delete_table(u'algorithm_question')

        # Deleting model 'QuestionAnswer'
        db.delete_table(u'algorithm_questionanswer')

        # Deleting model 'UserQuestion'
        db.delete_table(u'algorithm_userquestion')

        # Deleting model 'UserQuestionAnswer'
        db.delete_table(u'algorithm_userquestionanswer')

        # Deleting model 'ImplementationQuestion'
        db.delete_table(u'algorithm_implementationquestion')

        # Deleting model 'ImplementationQuestionAnswer'
        db.delete_table(u'algorithm_implementationquestionanswer')


    models = {
        u'algorithm.algorithm': {
            'Meta': {'object_name': 'Algorithm'},
            'classification': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['algorithm.Classification']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'reputation': ('django.db.models.fields.FloatField', [], {}),
            'uri': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'algorithm.classification': {
            'Meta': {'object_name': 'Classification'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'uri': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'algorithm.classificationproeficiencyscale': {
            'Meta': {'object_name': 'ClassificationProeficiencyScale', '_ormbases': [u'algorithm.ProeficiencyScale']},
            'classification': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['algorithm.Classification']"}),
            u'proeficiencyscale_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['algorithm.ProeficiencyScale']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'algorithm.implementation': {
            'Meta': {'object_name': 'Implementation'},
            'algorithm': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['algorithm.Algorithm']"}),
            'code': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'programming_language': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['algorithm.ProgrammingLanguage']"}),
            'reputation': ('django.db.models.fields.FloatField', [], {}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'algorithm.implementationquestion': {
            'Meta': {'object_name': 'ImplementationQuestion', '_ormbases': [u'algorithm.Question']},
            u'question_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['algorithm.Question']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'algorithm.implementationquestionanswer': {
            'Meta': {'object_name': 'ImplementationQuestionAnswer'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'implementation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['algorithm.Implementation']"}),
            'implementation_question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['algorithm.ImplementationQuestion']"}),
            'question_answer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['algorithm.QuestionAnswer']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'algorithm.interest': {
            'Meta': {'object_name': 'Interest'},
            'classification': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['algorithm.Classification']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'algorithm.proeficiencyscale': {
            'Meta': {'object_name': 'ProeficiencyScale'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        u'algorithm.programminglanguage': {
            'Meta': {'object_name': 'ProgrammingLanguage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'algorithm.programminglanguageproeficiencyscale': {
            'Meta': {'object_name': 'ProgrammingLanguageProeficiencyScale', '_ormbases': [u'algorithm.ProeficiencyScale']},
            u'proeficiencyscale_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['algorithm.ProeficiencyScale']", 'unique': 'True', 'primary_key': 'True'}),
            'programming_language': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['algorithm.ProgrammingLanguage']"})
        },
        u'algorithm.question': {
            'Meta': {'object_name': 'Question'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'priority': ('django.db.models.fields.IntegerField', [], {}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        u'algorithm.questionanswer': {
            'Meta': {'object_name': 'QuestionAnswer'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['algorithm.Question']"}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        u'algorithm.userquestion': {
            'Meta': {'object_name': 'UserQuestion', '_ormbases': [u'algorithm.Question']},
            u'question_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['algorithm.Question']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'algorithm.userquestionanswer': {
            'Meta': {'object_name': 'UserQuestionAnswer'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question_answer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['algorithm.QuestionAnswer']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'user_question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['algorithm.UserQuestion']"})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['algorithm']