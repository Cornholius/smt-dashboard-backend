from django.test import TestCase

# Create your tests here.
data = {'title': '123', 'text': '123', 'tags': '123 456 789'}

for i in data['tags'].split():
    print(i)