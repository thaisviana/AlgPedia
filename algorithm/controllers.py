import os, math
from algorithm.models import Paradigm,UserReputation,Classification,UniversityRank, Implementation, Algorithm, ProgrammingLanguage, Interest, ProeficiencyScale, ProgrammingLanguageProeficiencyScale, ClassificationProeficiencyScale, Question, QuestionOption, UserQuestion, ImplementationQuestion, ImplementationQuestionAnswer, UserQuestionAnswer
from extractor.FileWriters import RDFWriter
from django.contrib.auth.models import User
from django.db.models import Q
from django.db import connection
import itertools
from django.shortcuts import get_object_or_404

def cosine_similarity(vec1, vec2):
	 intersection = set(vec1.keys()) & set(vec2.keys())
	 numerator = sum([vec1[x] * vec2[x] for x in intersection])
	 sum1 = sum([vec1[x] ** 2 for x in vec1.keys()])
	 sum2 = sum([vec2[x] ** 2 for x in vec2.keys()])
	 denominator = math.sqrt(sum1) * math.sqrt(sum2)
	 if not denominator:
	 	return 0.0
	 else:
	 	return float(numerator) / denominator

def f_bayes(tag, id, sim_matriz, vecTag):
	similares = 0.0
	tagsEmSimilares = 0.0

	for j in xrange(len(sim_matriz)):
		if sim_matriz[id][j] > 0.2 and id <> j:
			similares += 1
			if tag in vecTag[j]:
				tagsEmSimilares += 1
	if similares == 0:
		return 0.0
	if(tagsEmSimilares / similares <> 0.0):
		print tagsEmSimilares / similares
	return  tagsEmSimilares / similares

def get_university_by_position(u_position):
	return UniversityRank.objects.get(position=u_position)

def get_user_univertisy(u_username):
	u_user = User.objects.get(username=u_username)
	try:
		ur = UserReputation.objects.get(user=u_user)
		if(ur.university is not None):
			return ur.university.position
		else:
			return ""
	except UserReputation.DoesNotExist:
		return ""
		
def save_university(u_username, u_university):
	u_user = User.objects.get(username=u_username)
	try:
		ur = UserReputation.objects.get(user=u_user)
		ur.university = u_university
		ur.save()
	except UserReputation.DoesNotExist:
		ur = UserReputation(user=u_user, reputation=1, university=u_university)
		ur.save()
	
def add_user_point(u_username):
	u_user = User.objects.get(username=u_username)
	try:
		ur = UserReputation.objects.get(user=u_user)
		ur.reputation = ur.reputation + 1
		ur.save()
	except UserReputation.DoesNotExist:
		ur = UserReputation(user=u_user, reputation=1)
		ur.save()
	
def is_database_empty():
	empty = 0

	empty += Classification.objects.count()
	empty += Implementation.objects.count()
	empty += Algorithm.objects.count()
	empty += ProgrammingLanguage.objects.count()

	return False if empty > 0 else True

def wipe_database():
	Algorithm.objects.all().delete()
	Classification.objects.all().delete()
	Implementation.objects.all().delete()
	ProgrammingLanguage.objects.all().delete()

# returns user interested classifications
def get_user_interested_classifications(username=None):
	if username == None:
		return []

	names = []
	links = []

	user = User.objects.get(username=username)
	user_interests = Interest.objects.filter(user=user).only("classification").order_by("classification__name")

	for interest in user_interests:
		names.append(interest.classification.name)
		links.append("/show/cat/id/" + str(interest.classification.id))
		# collection[classification.name] = "/show/cat/id/" + str(classification.id)

	classif = [{'name' : t[0], 'link' : t[1]} for t in zip(names, links)]

	return classif

# returns a tuple (names, links) of classifications
def get_all_classifications_name_link(search=None):
	# collection = dict()

	names = []
	links = []
	ids = []

	filters = {}
	if search:
		filters['name__icontains'] = search

	classifications = Classification.objects.filter(**filters).order_by("name")

	for classification in classifications:
		names.append(classification.name)
		links.append("/show/cat/id/" + str(classification.id))
		ids.append(classification.id)
		# collection[classification.name] = "/show/cat/id/" + str(classification.id)

	classif = [{'name' : t[0], 'link' : t[1], 'id': t[2]} for t in zip(names, links, ids)]

	return classif

def get_all_classifications_ordered_name_link(username=None, search=None):
	all_classifications = get_all_classifications_name_link(search)
	user_interested_classifications = get_user_interested_classifications(username)
	# ordered_classifications = list(user_interested_classifications)
	ordered_classifications = []
	for classification in all_classifications:
		if classification not in ordered_classifications:
			ordered_classifications.append(classification)

	return ordered_classifications

# returns a	classification object
def get_classification_by_id(c_id):
	try:
		classification = Classification.objects.get(id=c_id)
		return classification
	except Classification.DoesNotExist:
		return []

# returns a	paradigm object
def get_paradigm_by_id(p_id):
	try:
		paradigm = Paradigm.objects.get(id=p_id)
		return paradigm
	except Paradigm.DoesNotExist:
		return []

# returns a	user question answer by question
def get_questionaswer_by_question_id(question_id):
	try:
		questionaswer = QuestionOption.objects.filter(question__id=question_id)
		return questionaswer
	except QuestionOption.DoesNotExist:
		return []

def get_userquestionanswer_by_question_id_and_user(username, question_id):
	try:
		user_question_answer = UserQuestionAnswer.objects.get(user__username=username, user_question__id=question_id)
		return user_question_answer.question_option
	except:
		return []

def get_algorithms_by_classification(a_classification):
	try:
		algs = Algorithm.objects.filter(classification=a_classification).order_by("-reputation")
		return algs
	except Algorithm.DoesNotExist:
		return []

def get_all_universities():
	try:
		u = UniversityRank.objects.all().order_by("position")
		return u
	except UniversityRank.DoesNotExist:
		return []
		
def insert_classification_db(c_name, c_uri):
	try:
		classif = Classification.objects.get(name=c_name)
		return classif
	except Classification.DoesNotExist:
		aux = Classification(name=c_name, uri=c_uri)
		aux.save()
		return aux

def insert_paradigm(p_label, p_abstract, p_w_page, p_db_page):
	try:
		paradigm = Paradigm.objects.get(label=p_label)
		return paradigm
	except Paradigm.DoesNotExist:
		aux = Paradigm(dbpedia_uri=p_db_page, wikipedia_uri=p_w_page, label=p_label,abstract=p_abstract)
		aux.save()
		return aux

def delete_algorithm_db(alg):
	try:
		Algorithm.objects.filter(id=alg.id).delete()
	except Algorithm.DoesNotExist:
		return None

	return True

def insert_algorithm(alg_name, alg_about, alg_classification, alg_visible, alg_user):
	algorithm = Algorithm(name=alg_name, description=alg_about, classification=alg_classification, visible=alg_visible, user=alg_user)
	algorithm.save()

	return algorithm

def insert_algorithm_db(a_name, a_about, a_classif, a_uri, a_visible):

	alg, created = Algorithm.objects.get_or_create(name=a_name, description=a_about, classification=a_classif, uri=a_uri, visible=a_visible, user=None)
	return alg

def insert_programming_langage_db(i_language):
	p_lang, created = ProgrammingLanguage.objects.get_or_create(name=i_language.upper())
	return p_lang

def insert_implementation_db(i_alg, i_language_id, i_code, i_visible):
	p_lang = insert_programming_langage_db(i_language_id)

	implementation = Implementation(algorithm=i_alg, code=i_code, programming_language=p_lang, visible=i_visible, user=None)
	implementation.save()

	return implementation

def get_all_algorithms(search=None, classification_id=None):
	filters = {}
	if search:
		filters['name__icontains'] = search
	if classification_id:
		filters['classification_id'] = classification_id
	qs = Algorithm.objects.filter(**filters).order_by('name')
	return qs

def get_all_userquestions():
	return UserQuestion.objects.order_by("text")

def insert_user_question_answer(username, question_id, question_answer_id):
	user = User.objects.get(username=username)

	try:
		question = UserQuestion.objects.get(id=question_id)
		existing_question_answer = UserQuestionAnswer.objects.get(user=user, user_question=question)

		if question_answer_id and existing_question_answer.question_option.id != question_answer_id:
			question_option = QuestionOption.objects.get(id=question_answer_id)
			existing_question_answer.question_option = question_option
			existing_question_answer.save()
	except UserQuestionAnswer.DoesNotExist:
		question_answer = QuestionOption.objects.get(id=question_answer_id)
		UserQuestionAnswer.objects.create(user=user, user_question=question, question_option=question_answer)

def delete_user_question_answer(username, question_id):
	try:
		existing_question_answer = UserQuestionAnswer.objects.get(user__username=username, user_question__id=question_id)
		existing_question_answer.delete()
	except UserQuestionAnswer.DoesNotExist:
		pass

def exec_sp_update_user_evaluation_contribution(implementation_id, user_id):
	cursor = connection.cursor()
	cursor.callproc('calculate_user_evaluation_contribution', (implementation_id, user_id))
	cursor.close()

def insert_user_impl_question_answer(username, impl_id, question_id, question_answer_id):
	user = User.objects.get(username=username)

	try:
		# Updating the answer
		existing_question_answer = ImplementationQuestionAnswer.objects.get(user=user, implementation__id=impl_id, implementation_question_id=question_id)
		raise Exception(u"Cannot vote twice for an implementation")
# 		if question_answer_id and existing_question_answer.question_option.id != question_answer_id:
# 			question_option = QuestionOption.objects.get(id=question_answer_id)
# 			existing_question_answer.question_option = question_option
# 			existing_question_answer.save()
	except ImplementationQuestionAnswer.DoesNotExist:
		implementation = Implementation.objects.get(id=impl_id)
		question_option = QuestionOption.objects.get(id=question_answer_id)

		existing_question_answer = ImplementationQuestionAnswer.objects.create(user=user, implementation=implementation, implementation_question_id=question_id, question_option=question_option)
		# returns a list with user weight and reputation
		result = [existing_question_answer.calculate_reputation(), existing_question_answer.calculate_user_weight()]
		return result

def get_user_votes_by_algorithm(username, algorithm_id):
	user = User.objects.get(username=username)
	algorithm = Algorithm.objects.get(id=algorithm_id)

	try:
		# impl_questions = ImplementationQuestion.objects.get()
		implementations = Implementation.objects.filter(algorithm=algorithm)
		impl_question_answers = []

		for impl in implementations:
			answer = ImplementationQuestionAnswer.objects.filter(user=user, implementation=impl)

			if answer:
				impl_question_answers.append({"iq" : int(impl.id), "iqa" : ImplementationQuestionAnswer.objects.filter(user=user, implementation=impl)})

		if len(impl_question_answers) == 0:
			return []

		return impl_question_answers

	except ImplementationQuestionAnswer.DoesNotExist:
		return []

def get_user_programming_languages_proeficiencies(user):
	return ProgrammingLanguageProeficiencyScale.objects.filter(user=user)


def get_user_programming_languages_proeficiencies_ids(username):
	try:
		pls = []

		for pl in ProgrammingLanguageProeficiencyScale.objects.filter(user__username=username).only("programming_language"):
			pls.append(pl.programming_language.id)

		return pls
	except ProgrammingLanguageProeficiencyScale.DoesNotExist:
		return []

def get_user_classifications_interests_ids(username):
	try:
		classifications = []

		for i in Interest.objects.filter(user__username=username).only("classification"):
			classifications.append(i.classification.id)

		return classifications
	except Interest.DoesNotExist:
		return []

def get_user_classifications_proeficiencies_ids(username):
	try:
		classifications = []

		for cps in ClassificationProeficiencyScale.objects.filter(user__username=username).only("classification"):
			classifications.append(cps.classification.id)

		return classifications
	except ClassificationProeficiencyScale.DoesNotExist:
		return []

def update_programming_languages_proeficiencies(username, programming_languages_ids):
	user_proeficiencies = set(get_user_programming_languages_proeficiencies_ids(username))
	programming_languages_ids = set(programming_languages_ids)

	# Vou remover todas as existentes menos as que ele selecionou
	to_remove = user_proeficiencies - programming_languages_ids
	to_insert = programming_languages_ids - user_proeficiencies

	ProgrammingLanguageProeficiencyScale.objects.filter(user__username=username, programming_language__id__in=to_remove).delete()

	# print "programming_language!"
	# print "to remove: ", to_remove
	# print "to_insert: ", to_insert

	if to_insert:
		insert_programming_languages_proeficiencies(username, to_insert)

def insert_programming_languages_proeficiencies(username, programming_languages_ids):
	user = User.objects.get(username=username)

	for programming_language_id in programming_languages_ids:
		programming_language = ProgrammingLanguage.objects.get(id=programming_language_id)
		ProgrammingLanguageProeficiencyScale.objects.get_or_create(user=user, programming_language=programming_language, value=1)

def update_classifications_proeficiencies(username, classifications_ids):
	user_proeficiencies = set(get_user_classifications_proeficiencies_ids(username))
	classifications_ids = set(classifications_ids)

	# Vou remover todas as existentes menos as que ele selecionou
	to_remove = user_proeficiencies - classifications_ids
	to_insert = classifications_ids - user_proeficiencies

	# print "proeficiencies!"
	# print "to remove: ", to_remove
	# print "to_insert: ", to_insert

	ClassificationProeficiencyScale.objects.filter(user__username=username, classification__id__in=to_remove).delete()

	if to_insert:
		insert_classifications_proeficiencies(username, to_insert)

def insert_classifications_proeficiencies(username, classifications_ids):
	user = User.objects.get(username=username)

	for classification_id in classifications_ids:
		classification = Classification.objects.get(id=classification_id)
		ClassificationProeficiencyScale.objects.get_or_create(user=user, classification=classification, value=1)

def update_classifications_interests(username, classifications_ids):
	user_interests = set(get_user_classifications_interests_ids(username))
	classifications_ids = set(classifications_ids)

	to_remove = user_interests - classifications_ids
	to_insert = classifications_ids - user_interests

	# print "interests!"
	# print "to remove: ", to_remove
	# print "to_insert: ", to_insert

	Interest.objects.filter(user__username=username, classification__id__in=to_remove).delete()

	if to_insert:
		insert_classifications_interests(username, to_insert)

def insert_classifications_interests(username, classifications_ids):
	user = User.objects.get(username=username)

	for classification_id in classifications_ids:
		classification = Classification.objects.get(id=classification_id)
		Interest.objects.get_or_create(user=user, classification=classification)

def get_all_implementationquestions():
	return ImplementationQuestion.objects.order_by("text")

def get_algorithm_by_id(a_id):
	alg = get_object_or_404(Algorithm, id=a_id)
	return alg

def get_all_programming_languages():
	return ProgrammingLanguage.objects.order_by("name")
	
def insert_user_reputation(u_username,u_reputation):
	u_user = User.objects.get(username=u_username)
	ur = UserReputation(user=u_user, reputation=u_reputation)
	ur.save
	
def insert_implementation_alg_p_lang(i_alg, i_p_lang, i_code, i_visible, i_user):
	imp = Implementation(algorithm=i_alg, programming_language=i_p_lang, code=i_code, visible=i_visible , user=i_user)
	imp.save()

	return imp

def get_programming_language_by_id(p_lang_id):
	try:
		p_lang = ProgrammingLanguage.objects.get(id=p_lang_id)
		return p_lang
	except ProgrammingLanguage.DoesNotExist:
		return None

def get_implementations_by_alg_id(a_id):
	try:
		implementations = Implementation.objects.filter(algorithm__id=a_id).order_by("-reputation")
		return implementations
	except Algorithm.DoesNotExist:
		return []


def get_top5_users():		
	try:
		reputations = UserReputation.objects.filter(reputation__isnull=False).order_by("-reputation")[0:5]
		reps = [ (r.reputation, r.user) for r in reputations]
		l_reputation = 	[{'reputation' : a[0], 'username' : a[1].username} for a in reps]
		return l_reputation;
	except UserReputation.DoesNotExist:
		return []
		
def get_top5_algorithms():
	try:
		algorithms = Algorithm.objects.filter(reputation__isnull=False).order_by("-reputation")[0:5]
		# algorithms = Algorithm.objects.order_by("-reputation")[0:5]
		algs = [ (alg.get_show_url(), alg.name, alg.reputation) for alg in algorithms]
		algorithms = [{'link' : a[0], 'name' : a[1], 'reputation' : a[2]} for a in algs]
		return algorithms
	except Algorithm.DoesNotExist:
		return []

def get_top5_algorithms_by_classification(a_classification):
	try:
		algorithms = Algorithm.objects.filter(classification=a_classification, reputation__isnull=False).order_by("-reputation")[0:3]
		# algorithms = Algorithm.objects.filter(classification=a_classification).order_by("-reputation")[0:5]
		algs = [ (alg.get_show_url(), alg.name, alg.reputation) for alg in algorithms]
		algorithms = [{'link' : a[0], 'name' : a[1], 'reputation': a[2]} for a in algs]
		return algorithms
	except Algorithm.DoesNotExist:
		return []

# Returns a dict with the difference between the two dicts
def dict_diff(list1, list2):
	rest = []

	for d in list1:
		has_element = False

		for dd in list2:
			if dd['name'] == d['name']:
				has_element = True
				break

		if not has_element:
			rest.append(d)

	return rest

def try_create_algorithm_rdf(a_id):

	base_path = os.path.dirname(__file__)
	file_name = os.path.join(base_path, 'static/rdf/').replace('\\', '/')
	file_name = file_name + 'rdf_alg_%i.xml' % a_id

	if not os.path.exists(file_name):
		algorithm = get_algorithm_by_id(a_id)
		rdf_writer = RDFWriter(algorithm, file_name)

		rdf_name = rdf_writer.create_rdf_file()

		return rdf_name
	else:
		file_parts = file_name.split('/')
		file_name = '/'.join(file_parts[-2:])

	return file_name

def make_classification_link(c_id):
	# base_link = get_classification_display_url()
	# return base_link.replace("#", c_id)
	return ''

def make_algorithm_link(a_id):
	# base_link = get_algorithm_display_url()
	# return base_link.replace("#", c_id)
	return ''

def get_classification_display_url():
	return "/show/cat/id/#"

def get_algorithm_display_url():
	return "/show/alg/id/#"

""" Metodos de calculo de probalidade da matrix , depois tirar daqui"""
#returns a dictionary which the key is a possible action for an user and the value is a list containing all the users that
#have made the key action
def get_users_by_actions():
	user_action ={}
	aas = Algorithm.objects.filter(~Q(user=None))
	users_aa = [ (aa.user.id) for aa in aas]

	user_action['aa'] = users_aa
	
	ais = Implementation.objects.filter(~Q(user=None))
	users_ai = [ (ai.user.id) for ai in ais]

	user_action['ai'] = users_ai

	aps = UserQuestionAnswer.objects.filter(~Q(user=None))
	users_ap = [(ap.user.id) for ap in aps]


	user_action['ap'] = users_ap

	avs = ImplementationQuestionAnswer.objects.all()
	users_av = [(av.user.id) for av in avs]

	user_action['v'] = users_av[::3]

	return user_action

#returns all the possible combinations for all the actions an user can do
def str_historico():
	acoes = ['aa','ai','v','ap']
	historico=['']
	limiteCombinacoes = len(acoes)+1
	for i in xrange(1, limiteCombinacoes):
		for combination in itertools.combinations_with_replacement(acoes, i):
			str = "_".join(list(combination))
			historico += [str]
	return historico

#return the total of user in the database
def get_n_users():
    count_user = User.objects.all().count()
    return float(count_user)

#return all the combinations for each element of iterable combined by r
# combinations('ABCD', 2) --> AB AC AD BC BD CD
# combinations(range(4), 3) --> 012 013 023 123
def combinations(iterable, r):
    result = ""
    pool = list(iterable)
    n = len(pool)
    if r > n:
        return
    indices = range(r)
    yield '_'.join(list(pool[i] for i in indices))
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield '_'.join(list(pool[i] for i in indices))
