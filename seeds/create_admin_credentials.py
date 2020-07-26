from databases import mycollection
 
# creates Admin credentials using default values. Use these values to login

document = {
        "name": "ADMIN",
        "password": "123456"
}

entry = mycollection.insert_one(document)

if entry:       
      print("OK")