from django.test import TestCase
from algorithm import controllers

class SearchTests(TestCase):
    fixtures = ['algorithm_testdata.json', 'classification_testdata.json']

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_all_algorithms__search_null__should_return_all_algorithms(self):
        search_result = controllers.get_all_algorithms(None, None)
        self.assertEqual(len(search_result.values_list()), 6)

    def test_get_all_algorithms__search_match_one_algorithm__should_return_only_one_algorithm(self):
        search_result = controllers.get_all_algorithms("Fifo", None)
        self.assertEqual(len(search_result.values_list()), 1)

    def test_get_all_algorithms__search_match_3_algorithms__should_return_3_algorithms(self):
        search_result = controllers.get_all_algorithms("Algoritmo Boladao", None)
        self.assertEqual(len(search_result.values_list()), 3)

    def test_get_all_algorithms__search_not_in_database__should_return_no_algorithms(self):
        search_result = controllers.get_all_algorithms("Bubble Sort", None)
        self.assertEqual(len(search_result.values_list()), 0)
