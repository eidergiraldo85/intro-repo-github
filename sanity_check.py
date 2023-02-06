import os

print("--------------------")
print("RUNNING THE SANITY CHECK")
print("--------------------")

#### Basic check of the translator
# Running the translator
os.system("python tranzlator.py")
print("\n\n--------------------\n\n")
# Checking that the lolcat file was generated and is not empty
if os.path.exists("lolcat.txt"):
    lolcat_file = open("lolcat.txt", "r").read()
    if len(lolcat_file) > 0:
        print("The lolcat.txt file was generated successfully.")
    else:
        raise Exception("The lolcat.txt file is empty!")
else:
    raise Exception("The lolcat.txt file was not generated successfully!")

# Checking that the lolcat.txt file and the reference.txt file are similar
os.system("pip install nltk")
import nltk
nltk.download('punkt')
tokenizer = nltk.RegexpTokenizer(r"\w+")

lolcat_file = open("lolcat.txt", "r").read().lower()
lolcat_file = tokenizer.tokenize(lolcat_file)
lolcat_file = " ".join(lolcat_file)
reference_file = open("reference.txt", "r").read().lower()
reference_file = tokenizer.tokenize(reference_file)
reference_file = " ".join(reference_file)

print("\n\n======= Comparing the files. This may take some time...")

from difflib import SequenceMatcher
similarity = SequenceMatcher(None, lolcat_file, reference_file).ratio()
if similarity > 0.8:
    print("\n\n**** All good! Teh file seemz 2 has been tranzlated correctly! (similarity = " + str(similarity) + ")")
else:
    raise Exception("**** Oops! Teh file doesn't seem 2 has been translatd correctly! Try 2 mak teh output vary similar 2 teh reference.txt file (similarity = " + str(similarity) + ")")