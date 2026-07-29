from docscrub import Cleaner


text = """
    Welcome to Website


    Visit https://example.com


    Contact admin@example.com


    Page 5 of 20


    FranÃ§ais
"""


cleaner = Cleaner()

result = cleaner.clean(text)

print(result)