import csv


def intro():
  print('Welcome to the Spanish and French translator app.\nPlease enter an English word and press the "Enter" key.\nType "done" at any time to exit')

def exit():
  print(f'\nThanks for using the translator app, {name}. Have a great day!')

translations = {}
name = ["Stacy"]

with open("translations.csv","r") as words:
  reader = csv.DictReader(words, delimiter=",")
  for line in reader:
    english = line["English"].lower()
    spanish = line["Spanish"].lower()
    french = line["French"].lower()
    translations[english] = [spanish, french]
  
done = False

intro()

while not done: 
  word = input("Type a word in English to recieve the   Spanish and French translations")
  word = word.lower()
  exit()
  
  if word == "done":
    done = True 
  elif word in translations:
    print(f'\nSPANISH: {translations[word][0]}')
    print(f'\nFRENCH: {translations[word][1]}')
    
  else:
    print("\nWord not found in translation dictionary...we will update our data soon!")
    
    
  
  
  
