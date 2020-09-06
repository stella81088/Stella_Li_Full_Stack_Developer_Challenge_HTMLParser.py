import csv
from bs4 import BeautifulSoup
from urllib.request import urlopen
import random
import requests

url = "https://www.cheatsheet.com/gear-style/20-questions-to-ask-siri-for-a-hilarious-response.html/"

page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

csvFile = open('questions.csv', 'w+', newline='')

for h2 in soup.find_all('h2'):
    header = h2.string
    #print (header)
    
    writer = csv.writer(csvFile)
    writer.writerow([header])

csvFile.close()

with open('questions.csv') as f:
    reader = csv.reader(f)
    chosen_row = random.choice(list(reader))

def notification(message):
    report = {}
    report["value1"] = message

    requests.post(
        'https://maker.ifttt.com/trigger/challenge/with/key/dK76I0jFBeQzZrc6NqVjs3', data=report)

notification(chosen_row)
print("COMPLETED")
# print(article.prettify())




