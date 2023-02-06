{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e4736e20",
   "metadata": {},
   "outputs": [],
   "source": [
    " # Step 1\n",
    "# Import the english.txt file\n",
    "import json\n",
    "english_text = open('./english.txt', 'r')\n",
    "text = english_text.readlines()\n",
    "english_text.close()\n",
    "# Step 2\n",
    "# Import the glossary (the tranzlashun.json file)\n",
    "# This dataset originally comes from the GitHub repository\n",
    "# at https://github.com/irdumbs/Dumb-Cogs and is covered by an MIT license\n",
    "with open('./tranzlashun.json') as translationFile:\n",
    "    data = json.load(translationFile)\n",
    "# Step 3\n",
    "# Translate the English text into Lolspeak\n",
    "translated_book= ''\n",
    "for line in text:\n",
    "    translated_line = \"\"\n",
    "    for word in line.split():\n",
    "        if word in data:\n",
    "            translated_line += data[word.lower()] +\" \"\n",
    "        elif word == \"\\n\":\n",
    "            translated_line += \"\"\n",
    "        else:\n",
    "            translated_line += word.lower() + \" \"\n",
    "    translated_book += translated_line\n",
    "# Step 4 :Save the translated text as the \"lolcat.txt\" file\n",
    "with open('./lolcat.txt', 'w') as lol_speak:\n",
    "    lol_speak.write(translated_book)\n",
    "lol_speak.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "2e808c87",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "--------------------\n",
      "RUNNING THE SANITY CHECK\n",
      "--------------------\n",
      "\n",
      "\n",
      "--------------------\n",
      "\n",
      "\n",
      "The lolcat.txt file was generated successfully.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[nltk_data] Downloading package punkt to /home/jovyan/nltk_data...\n",
      "[nltk_data]   Package punkt is already up-to-date!\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "\n",
      "======= Comparing the files. This may take some time...\n",
      "\n",
      "\n",
      "**** All good! Teh file seemz 2 has been tranzlated correctly! (similarity = 0.9828350879611283)\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "\n",
    "print(\"--------------------\")\n",
    "print(\"RUNNING THE SANITY CHECK\")\n",
    "print(\"--------------------\")\n",
    "\n",
    "#### Basic check of the translator\n",
    "# Running the translator\n",
    "os.system(\"python tranzlator.py\")\n",
    "print(\"\\n\\n--------------------\\n\\n\")\n",
    "# Checking that the lolcat file was generated and is not empty\n",
    "if os.path.exists(\"lolcat.txt\"):\n",
    "    lolcat_file = open(\"lolcat.txt\", \"r\").read()\n",
    "    if len(lolcat_file) > 0:\n",
    "        print(\"The lolcat.txt file was generated successfully.\")\n",
    "    else:\n",
    "        raise Exception(\"The lolcat.txt file is empty!\")\n",
    "else:\n",
    "    raise Exception(\"The lolcat.txt file was not generated successfully!\")\n",
    "\n",
    "# Checking that the lolcat.txt file and the reference.txt file are similar\n",
    "os.system(\"pip install nltk\")\n",
    "import nltk\n",
    "nltk.download('punkt')\n",
    "tokenizer = nltk.RegexpTokenizer(r\"\\w+\")\n",
    "\n",
    "lolcat_file = open(\"lolcat.txt\", \"r\").read().lower()\n",
    "lolcat_file = tokenizer.tokenize(lolcat_file)\n",
    "lolcat_file = \" \".join(lolcat_file)\n",
    "reference_file = open(\"reference.txt\", \"r\").read().lower()\n",
    "reference_file = tokenizer.tokenize(reference_file)\n",
    "reference_file = \" \".join(reference_file)\n",
    "\n",
    "print(\"\\n\\n======= Comparing the files. This may take some time...\")\n",
    "\n",
    "from difflib import SequenceMatcher\n",
    "similarity = SequenceMatcher(None, lolcat_file, reference_file).ratio()\n",
    "if similarity > 0.8:\n",
    "    print(\"\\n\\n**** All good! Teh file seemz 2 has been tranzlated correctly! (similarity = \" + str(similarity) + \")\")\n",
    "else:\n",
    "    raise Exception(\"**** Oops! Teh file doesn't seem 2 has been translatd correctly! Try 2 mak teh output vary similar 2 teh reference.txt file (similarity = \" + str(similarity) + \")\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6cab0bb8",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.10.6 64-bit",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.6"
  },
  "vscode": {
   "interpreter": {
    "hash": "40b70f523f94395ac61272c57f0d9feac5e18bd74bf54c8e741ccbdef25ac0c9"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
