letter = '''Mr. <NAME>
I am Happy to tell you that you are selected in this software house

<DATE>
Regards
Zahoor
'''

name = input("Enter Your Name\n")
date = input ("Enter date\n")
letter =letter.replace("NAME",name)
letter =letter.replace("DATE",date)
print(letter)