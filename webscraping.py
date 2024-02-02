from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://islamqa.info/en/answers/128927/it-is-essential-to-acquire-and-take-possession-of-items-before-selling-them"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

title = soup.find(class_="title is-4 is-size-5-touch").text.strip()
print(title)

question = soup.find(class_="single_fatwa__question text-justified").text.strip().replace("Question\n\n","")
print(question)

answer = soup.find(class_="single_fatwa__answer").text.strip().replace("Answer\n\n\n\n\n\n\n","")
print(answer)

data = [[title, question, answer]]
df = pd.DataFrame(data, columns=["title", "question", "answer"])
print(f"jawwad print{df}")
print(df['question']) 
df.to_csv("islamqa_data.csv", index=False)
print("Data exported to islamqa_data.csv")
