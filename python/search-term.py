def search():
  try:
    from googlesearch import search
  except ImportError:
    print('No module named googlesearch found')

  for i in search(query="boise news", tld='com', num=10, stop=10, pause=2 ):
    print(i)

search()
