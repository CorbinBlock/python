import ezgmail
import os

def send_email():
    #driveletter = "C:"
    #filepath = os.path.join(driveletter, "Users\\Corbin\\PycharmProjects\\finance\\venv\\Scripts\\GOEV.csv")
    localfile = 'GOEV.csv'
    ezgmail.send('cblock0@gmail.com', 'GOEV Data', 'View Attachment',
    [localfile])

send_email()