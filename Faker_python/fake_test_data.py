'''
Faker is a Python package that generates fake data for you.
Whether you need to bootstrap your database, 
create good-looking XML documents, fill-in your persistence to stress 
test it, or anonymize data taken from a production service, 
'''
# For installing use "pip install Faker"

from faker import Faker
fake = Faker()
# print(fake.name())
# print(fake.address())
# print(fake.text())

# for _ in range(10):
#     print(fake.name())

# for _ in range(10):
#     print(fake.email())