import urllib.error as error
def search():
    try:
        from googlesearch import search
    except ImportError:
        print('No module named googlesearch found')

    result = []
    try:
      for i in search(query="news", tld='com', num=10, stop=10, pause=10 ):
        result.append(i)
      return result
    except urllib.error.HTTPErrori as e:
        print(e)
        pass
    except error:
        pass
