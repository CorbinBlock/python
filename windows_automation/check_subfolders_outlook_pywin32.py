from win32com.client import Dispatch

outlook = Dispatch("Outlook.Application").GetNamespace("MAPI")
root_folder = outlook.Folders.Item(1)
print(root_folder.Name)

for folder in root_folder.Folders:
    print (folder.Name)

inbox = outlook.GetDefaultFolder(6)

messages = inbox.Items


try:
    for message in list(messages):
        try:
            print(message)
        except Exception as e:
            print("error when printing message:" + str(e))
except Exception as e:
    print("error when processing emails messages:" + str(e))