#! /usr/bin/env python3

import re, pyperclip

#TODO: Create a regex for phone numbers
phoneRegex=re.compile('''
#416-555-0000, 555-0000, (415) 555-000, 555-0000 ext 12345, ext. 12345, x12345
(
((\d\d\d)|(\(\d\d\d)))?    #area code (optional)
(\s|-)                     #first separator
\d\d\d                     #first 3 digits
-                          #separator
\d\d\d\d                   #last 4 digits
(((ext (\.)?\s|x )       #extension (optional)
(\d{2,5}))?
)
''',re.VERBOSE)

#TODO: Create a regex for email addresses
emailRegex=re.compile('''
#some.+_thing@((\d{2,5}))?.com

[a-zA-z0-9_.+]+            #name part
@                          #@ symbol
[a-zA-Z0-9_.+]+            #domain name part

''',re.VERBOSE)
#TODO: Get the text off the clipboard
text = pyperclip.paste()
#TODO: Extract the phone/email from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])
# TODO: Copy the extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers)+'\n'+'\n'.join(extractedEmail)

pyperclip.copy(results)
