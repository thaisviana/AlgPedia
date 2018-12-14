from django.contrib import admin
from algorithm.models import ProgrammingLanguage, classification, algorithm, Implementation, Interest, ProeficiencyScale, ProgrammingLanguageProeficiencyScale, classificationProeficiencyScale, question,questionOption,UserQuestion,ImplementationQuestion,ImplementationQuestionAnswer,UserQuestionAnswer

class ClassificationAdmin(admin.ModelAdmin):
	list_display = ('name', 'uri')
	search_fields = ('name',)
	
class AlgorithmAdmin(admin.ModelAdmin):
	list_display = ('name', 'description', 'classification')
	search_fields = ('name', 'classification__name')
	
class ImplementationAdmin(admin.ModelAdmin):
	list_display = ('algorithm', 'programming_language')
	search_fields = ('algorithm', 'programming_language')

	
###################ALGPEDIA_PERFIL###################
	
###################REGISTER###################
# admin.site.register(ProgrammingLanguage)
# admin.site.register(UserQuestionAnswer)
# admin.site.register(ClassificationAdmin)
# admin.site.register(AlgorithmAdmin)
# admin.site.register(ImplementationAdmin)
# admin.site.register(Implementation)
# admin.site.register(Interest)
# admin.site.register(ProeficiencyScale)
# admin.site.register(ProgrammingLanguageProeficiencyScale)
# admin.site.register(classificationProeficiencyScale)
# admin.site.register(question)
# admin.site.register(questionOption)
# admin.site.register(UserQuestion)
# admin.site.register(ImplementationQuestion)
# admin.site.register(ImplementationQuestionAnswer)
