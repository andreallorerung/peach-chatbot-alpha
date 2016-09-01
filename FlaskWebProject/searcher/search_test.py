from searcher import search_session
# from search_session import SearchSession


# initialize search session
s = search_session.SearchSession()
s.add_index('inverted_integration_test.txt')
s.search('nurses')
