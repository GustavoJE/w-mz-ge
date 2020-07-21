# smarted-test

An API for creating and listing users

---

## Summary

An API that creates a user entry, and lists all users

## Requirements

The following packages are required by smarted-test

| Package Name | URL                                                           | Minimum required version |
|--------------|---------------------------------------------------------------|--------------------------|
| Python       | https://www.python.org/downloads/                             | `3.7`                    |
| git          | https://git-scm.com/book/en/v2/Getting-Started-Installing-Git | `latest`                 |
| pip          | https://pip.pypa.io/en/stable/installing/                     | `19.2.3`                 |
| mongodb      | https://docs.mongodb.com/manual/installation/                 | `3.9.0  `                |

## Directory structure

```bash
$ tree
├── config
├── app.py
└── README.md
```

| Dirname | Description                                                         |
|---------|---------------------------------------------------------------------|
| config  | This directory contains `application` and `database` configurations |


## Installation

1. Checkout the repo
```bash
$ git clone git@github.com:GustavoJE/w-mz-ge.git
```

2. Install the dependencies
```bash
$ pip install -r requirements.txt
```

3. Run the application
```bash
$ python app.py
```

### Available environment configuration variables

| Name             | Description                         | Default Value                            | Required |
|------------------|-------------------------------------|------------------------------------------|----------|
| **Database**     |                                     |                                          |          |
| MONGO_HOST       | The hostname of the mongodb         | `mongodb://admin:admin@localhost:27017/` | **yes**  |
| MONGO_DATABASE   | The name of the mongo's database    | `Smarted`                                | no       |
| MONGO_COLLECTION | The name of the mongo's collection  | `Smartedexam`                            | no       |
| **Application**  |                                     |                                          |          | 
| APP_PORT         | The port of the application         | `8000`                                   | no       |
| APP_DEBUG        | Enables hot reloading for debugging | `False`                                  | no       |


## Documentation

For documenting the API, I used Swagger functionality that comes built in `flask_restplus` framework. In order to create and present the `swagger.json` file, please Run the API and visit the endpoint `http://HOST:{PORT}/`. You should see the documentation of the API's endpoints

