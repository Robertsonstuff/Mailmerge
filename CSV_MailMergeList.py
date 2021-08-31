import csv
import pyperclip

with open("blank.csv", "r") as file:
    reader = csv.reader(file)
    particulars = []
    for part in reader:
        particulars.append(f"hi {part[0]}, please do {part[1]} and then {part[2]}.\nThanks for your help! ")
    for item in particulars:
        print(item)
	pyperclip.copy(item)
        input("Copied to clipboard..")

print("\ndone\n")
