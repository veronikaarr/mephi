def authorization(login, password, data):
    for i in data:
        if i.login == login and i.password == password:
            return i