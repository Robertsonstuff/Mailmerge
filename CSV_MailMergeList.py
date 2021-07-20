import csv
import pyperclip

f = open('mailmergelist.csv', 'r')

reader = csv.reader(f)

Particulars = []

for row in reader:
    Particulars.append('Hi ' + (row[3]) + ' I am missing device' + (row[5]) + " from ticket " + (row[4]))

print("Let's start our mailmerge:")

for item in Particulars:
    print(item)
    pyperclip.copy(item)
    input("Copied to clipboard..")

	

