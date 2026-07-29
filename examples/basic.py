from docscrub import Cleaner


text = """
Hello        World


This     is     DocScrub
"""


cleaner = Cleaner()

result = cleaner.clean(text)

print(result)