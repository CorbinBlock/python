import ezgmail
import os

filename = "credentials.json"
jsonpath = os.path.join("C:\\Users\\Corbin\\PycharmProjects\\file_mgmt\\venv\\Scripts", filename)
os.chdir(jsonpath)
ezgmail.init()
