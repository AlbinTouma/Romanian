import json
import pandas as pd
from resources import *


for  verb in RomanianDictionary['Verbs']:
    if (verb['Infinitive'] == input(str)): #input infinitive of verb you want to search
        verb = verb['Infinitive'], verb['Definition'], verb['Simple Present']
        print(json.dumps(verb, indent=4))
    else:
        if not(verb['Infinitive'] == input(str)):
            print('error')
            exit()

