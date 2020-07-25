from config.databases import mycollection
 
# prompts for Admin username and password
username = input("Please input a valid username: ")
password = input("Please choose a valid password: ")

document = {
        "name": username,
        "password": password
}
entry = mycollection.insert_one(document)