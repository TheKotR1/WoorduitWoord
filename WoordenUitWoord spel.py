#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
goedWords = 0
goedScore = 0
foutScore=0
wordList = [0,0]
wordListBeta = []
correctList = [0,0]
wrongList = [0,0]
guess = "herstart"

#  Input
word = input("Kies het te spelen woord: " )
length = input("Kies de minimale woordlengte (4 is normaal): ")
minLen = int(length)
# Look up words from word (webscrape)

import requests
from bs4 import BeautifulSoup
wordListBeta = []

URL = "https://scrabblemania.nl/" + word
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")


results = soup.find_all("div", class_="wyniki")
test = soup.find_all("p")

for i in range (len(test)):
    words1 = test[i].text.strip().split(", ")
    for i in range (0,len(words1)):
        b = ''.join(x for x in words1[i] if x.isalpha())
        if len(b) >= minLen:
            wordListBeta.append(b)

wordList = [[x,0] for x in wordListBeta]

# Prompt for user input (words)
while guess != "xxx":
    guess = input("Vul een nieuw woord in (xxx om op te geven): ")
    if guess == "xxx":
        print("\n Bedankt voor het spelen!")
    elif len(guess) < minLen:
        print(f"De minimale lengte voor een gok is {minLen} letters")
    else:
        goed = 0
        fout = 0
        dubbel = 0
        for i in range (0,len(wordList)):
            if guess == wordList[i][0]:
                goed = 1
                if wordList[i][1] != 1:
                    wordList[i][1] = 1
                else:
                    dubbel = 1
                    print("Dit woord heeft u al gehad")
        if goed == 0:
            print("Dit woord staat niet in de lijst. -1 punt")
            foutScore += 1
            # Add word to list wrongList
        elif goed == 1 and dubbel != 1:
            points = len(guess)-minLen+1
            print(f"Goed woord! {points} punt(en)")
            goedWords += 1
            goedScore += points
            #add word to list correctList            
                
            
print(f"U heeft {goedWords} woorden juist ingevuld met totaal {goedScore} punten en {foutScore} woorden onjuist.\n")
print(f"Dit geeft u een totaalscore van {goedScore-foutScore}. Gefeliciteerd!")
print("Dit waren alle mogelijke woorden:")
print(wordListBeta)


# In[333]:


# Recalibrate list & Scores
import numpy as np
goedWords = 0
goedScore = 0
foutScore=0
wordList = [0,0]
wordListBeta = []
correctList = [0,0]
wrongList = [0,0]
guess = "herstart"


# In[334]:


#  Input
word = input("Kies het te spelen woord: " )
length = input("Kies de minimale woordlengte (4 is normaal): ")
minLen = int(length)


# In[335]:


# Look up words from word (webscrape)

import requests
from bs4 import BeautifulSoup
wordListBeta = []

#String concatenate with correct word
URL = "https://scrabblemania.nl/" + word
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
# print (soup)


results = soup.find_all("div", class_="wyniki")
# print(results)
test = soup.find_all("p")
# print(test)

for i in range (len(test)):
#     print(test[i])
    words1 = test[i].text.strip().split(", ")
#     print(words1)
    for i in range (0,len(words1)):
        b = ''.join(x for x in words1[i] if x.isalpha())
        if len(b) >= minLen:
            wordListBeta.append(b)
            
# print(wordListBeta)

# bonus = np.zeros((len(wordListBeta),1))
# wordList = np.append(wordListBeta,bonus)

wordList = [[x,0] for x in wordListBeta]
print(wordList)
#     if (test[i].startswith("<p>")):
#         print(test[i])
#         test1[i]=test[3:]
#         print(test1[i])
#     wordsgroup = results[i].find("p")
#     words = wordsgroup.text.strip().split(", ")
#     #print(words)
#     for i in range (0,len(words)):
#         b = ''.join(x for x in words[i] if x.isalpha())
#         wordListBeta.append(b)
#print(wordListBeta)

# wordList = [[x,0] for x in wordListBeta]
#print(wordList)


# In[336]:


# Prompt for user input (words)
while guess != "xxx":
    guess = input("Vul een nieuw woord in (xxx om op te geven): ")
    if guess == "xxx":
        print("\n Bedankt voor het spelen!")
    elif len(guess) < minLen:
        print(f"De minimale lengte voor een gok is {minLen} letters")
    else:
        goed = 0
        fout = 0
        dubbel = 0
        for i in range (0,len(wordList)):
            if guess == wordList[i][0]:
                goed = 1
                if wordList[i][1] != 1:
                    wordList[i][1] = 1
                else:
                    dubbel = 1
                    print("Dit woord heeft u al gehad")
        if goed == 0:
            print("Dit woord staat niet in de lijst. -1 punt")
            foutScore += 1
            # Add word to list wrongList
        elif goed == 1 and dubbel != 1:
            points = len(guess)-minLen+1
            print(f"Goed woord! {points} punt(en)")
            goedWords += 1
            goedScore += points
            #add word to list correctList            
                
            
print(f"U heeft {goedWords} woorden juist ingevuld met totaal {goedScore} punten en {foutScore} woorden onjuist.\n")
print(f"Dit geeft u een totaalscore van {goedScore-foutScore}. Gefeliciteerd!")
print("Dit waren alle mogelijke woorden:")
print(wordListBeta)


# In[31]:





# In[ ]:


get_ipython().set_next_input('Database highscore words');get_ipython().run_line_magic('pinfo', 'words')


# In[ ]:





# In[ ]:





# In[100]:


import requests
import lxml.html as lh
from bs4 import BeautifulSoup

#String concatenate with correct word
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

#print(soup)
results = soup.find(id = "ResultsContainer")
#print(results.prettify())
job_elements = results.find_all("div", class_="card-content")
#print(job_elements)

for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
#     print(title_element)
#     print(company_element)
#    print(location_element)
#wordsInWord = results.find_all("div", class_="results")
#print(wordsInWord)

