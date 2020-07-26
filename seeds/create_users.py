from faker import Faker
from databases import mycollection

user = Faker()
for _ in range(20):

    # generate and insert fake user data in database
    name = user.first_name()
    last_name = user.last_name()
    email = user.ascii_email()
    password = user.password(length=8)

    document = {
        "name": name,
        "last_name": last_name,
        "email": email,
        "password": password
    }
    userid = mycollection.insert_one(document)
    
print("OK")