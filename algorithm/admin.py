from django.contrib import admin
from algorithm.models import ProgrammingLanguage, Classification, Algorithm, Implementation, Interest, ProeficiencyScale, ProgrammingLanguageProeficiencyScale, ClassificationProeficiencyScale, Question,QuestionAnswer,UserQuestion,ImplementationQuestion,ImplementationQuestionAnswer,UserQuestionAnswer

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
admin.site.register(ProgrammingLanguage)
admin.site.register(UserQuestionAnswer)
admin.site.register(Classification, ClassificationAdmin)
admin.site.register(Algorithm, AlgorithmAdmin)
admin.site.register(Implementation, ImplementationAdmin)
admin.site.register(Interest)
admin.site.register(ProeficiencyScale)
admin.site.register(ProgrammingLanguageProeficiencyScale)
admin.site.register(ClassificationProeficiencyScale)
admin.site.register(Question)
admin.site.register(QuestionAnswer)
admin.site.register(UserQuestion)
admin.site.register(ImplementationQuestion)
admin.site.register(ImplementationQuestionAnswer)
