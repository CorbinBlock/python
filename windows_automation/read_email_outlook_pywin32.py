from datetime import datetime, timedelta
import glob
import os
import win32com.client

# email = os.getenv('EMAIL')

outlook = win32com.client.Dispatch('outlook.application')
mapi = outlook.GetNamespace("MAPI")

for account in mapi.Accounts:
	print(account.DeliveryStore.DisplayName)

inbox = mapi.GetDefaultFolder(6)

messages = inbox.Items

received_dt = datetime.now() - timedelta(days=3)
received_dt = received_dt.strftime('%m/%d/%Y %H:%M %p')
messages = messages.Restrict("[ReceivedTime] >= '" + received_dt + "'")
# messages = messages.Restrict("[SenderEmailAddress] = 'contact@codeforests.com'")
# messages = messages.Restrict("[Subject] = 'Sample Report'")

#Let's assume we want to save the email attachment to the below directory
outputDir = r"C:\\tmp"
try:
    for message in list(messages):
        try:
            s = message.sender
            for attachment in message.Attachments:
                attachment.SaveASFile(os.path.join(outputDir, attachment.FileName))
                print(f"attachment {attachment.FileName} from {s} saved")
        except Exception as e:
            print("error when saving the attachment:" + str(e))
except Exception as e:
    print("error when processing emails messages:" + str(e))

# Delete .png files from attachments (usually junk icons from email)
# Get a list of all the file paths that ends with .txt from in specified directory

fileList = glob.glob('C:\\tmp\\*.png') + glob.glob('C:\\tmp\\*.jpg') + glob.glob('C:\\tmp\\*.gif')

# Iterate over the list of filepaths & remove each file.

for filePath in fileList:
    try:
        os.remove(filePath)
    except:
        print("Error while deleting file : ", filePath)