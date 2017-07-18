import tf_idf
import tf_idf_query
import sys

QUERIES = ['Dijkstra', 'Neural Evolution', 'Graph Search', 'Board Game AI', 'Shortest Path', 'Graph Painting', 'Sorting Algorithm']

def test_queries(queries):
  for i in range(len(queries)):
    result = tf_idf_query.query(queries[i])
    

def main():
  if len(sys.argv) < 2:
    return

  n_svd_components = int(sys.argv[1])
  tf_idf.SVD_COMPONENTS = n_svd_components
  tf_idf.main()
  
  tf_idf_query.load_artifacts()
  
  test_queries(QUERIES)

if __name__ == "__main__":
  main()
