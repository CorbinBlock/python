import os
import win32com.client

email = os.getenv('EMAIL')
outlook = win32com.client.Dispatch('outlook.application')
mail = outlook.CreateItem(0)

mail.To = email
mail.Subject = 'Sample Email'
mail.HTMLBody = '<h3>This is HTML Body</h3>'
mail.Body = "This is the normal body"
mail.Attachments.Add('c:\\tmp\\test_one.xlsx')
mail.Attachments.Add('c:\\tmp\\test_two.xlsx')
mail.CC = email

mail.Send()