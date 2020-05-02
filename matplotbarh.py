#barh chart - Horizontal
import csv # to read csv file
from matplotlib import pyplot as plt
import numpy as np
from collections import Counter

#print(plt.style.available) # gives all available styles
plt.style.use('ggplot') #use this style

with open('data.csv') as csv_file: # open file
    csv_reader=csv.DictReader(csv_file) # convert to dict

    lan_counter=Counter()
    for row in csv_reader:
        lan_counter.update(row['LanguagesWorkedWith'].split(';'))
languages=[]
popularity=[]

for item in lan_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])
languages.reverse()
popularity.reverse()

#print(languages)
#print(popularity)
plt.barh(languages,popularity)
plt.title('Pop Lans')
plt.ylabel('languges')
plt.xlabel('users')
plt.show()
plt.savefig('barh.png')


   # row=next(csv_reader) # first row
   # print(row['LanguagesWorkedWith'].split(';'))#access key and split with ;



