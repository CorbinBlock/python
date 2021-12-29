import ezgmail
import os

filename = "credentials.json"
jsonpath = os.path.join("C:\\Users\\Corbin\\PycharmProjects\\python\\file_management\\venv\\Scripts", filename)
os.chdir(jsonpath)
ezgmail.init()
