import tf_idf
import tf_idf_query
import sys

QUERIES = ['Dijkstra', 'Neural Evolution', 'Graph Search', 'Board Game AI']

def test_queries(queries):
  for i in range(len(queries)):
    result = tf_idf_query.query(queries[i])
    
    print ""
    print "{}) {}".format(i+1, queries[i])
    for j in range(len(result)):
      print "-- {}. {}".format(j+1, result[j])

def main():
  if len(sys.argv) < 2:
    print "Uso:", sys.argv[0], "[N_COMPONENTS_SVD]"
    return

  n_svd_components = int(sys.argv[1])
  tf_idf.SVD_COMPONENTS = n_svd_components
  tf_idf.main()
  
  tf_idf_query.load_artifacts()
  
  test_queries(QUERIES)

if __name__ == "__main__":
  main()
