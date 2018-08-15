from .user import User
from .universityRank import UniversityRank
from .userReputation import UserReputation
from .programmingLanguage import ProgrammingLanguage
from .classification import Classification
from .tag import Tag
from .paradigm import Paradigm
from .algorithm import Algorithm
from .implementation import Implementation
###################
# Relacionamento de interesse entre usuario e uma classificacao
from .interest import Interest
# Classe base de proeficiencia do usuario em algo
from .proeficiencyScale import ProeficiencyScale
from .programmingLanguageProeficiencyScale import ProgrammingLanguageProeficiencyScale
from .classificationProeficiencyScale import ClassificationProeficiencyScale
# Questao de escala em relacao a algo
from .question import Question
# Respostas validas para as perguntas
from .questionOption import QuestionOption
# Pergunta em relacao ao usuario
from .userQuestion import UserQuestion
# Resposta do usuário a uma pergunta sobre seu perfil
from .userQuestionAnswer import UserQuestionAnswer
# Pergunta em relacao a uma implementacao
from .implementationQuestion import ImplementationQuestion
# Resposta de um usuario a uma determinada pergunta sobre uma determinada implementacao
from .implementationQuestionAnswer import ImplementationQuestionAnswer
from .algorithmFullText import AlgorithmFullText