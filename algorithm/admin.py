from .models import Algorithm, Classification, Implementation, UniversityRank, Tag

Algorithm.register_admin()
Classification.register_admin()
Implementation.register_admin()
UniversityRank.register_admin()
Tag.register_admin()