import requests
from bs4 import BeautifulSoup
import json

url = ["https://tex.stackexchange.com/?tab=active",
       "https://tex.stackexchange.com/?tab=bounties",
       "https://tex.stackexchange.com/?tab=hot",
       "https://tex.stackexchange.com/?tab=week",
       "https://tex.stackexchange.com/?tab=month"]
       
Final_Result = []
for link in url:
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'lxml')
    Category = link.rsplit('=', 1)[-1]

    Question_list = soup.find(id="question-mini-list")
    Questions= Question_list.find_all(class_="question-summary")

    for qt in Questions:

        t = qt.find(class_="question-hyperlink")    
        Qsn = t.get_text()
        link = t['href'] 
        
        v = qt.find(class_="mini-counts")
        vote = v.get_text()
        
        s = qt.find(class_="status")
        s1 = s.find(class_="mini-counts")
        num_ans = s1.get_text()
        
        vi = qt.find(class_="views")
        vi1 = vi.find(class_="mini-counts")
        view = vi1.get_text()
        
        tag = qt.find(class_="tags")
        post_tag=tag.find(class_="post-tag")
        pt= post_tag.get_text()
        
        start = qt.find(class_="started")  
        rt = start.find(class_="relativetime")
        time = rt.get_text()
        
        Au  = start.get_text()
        Au1 = Au.rsplit('\n')[-2]
        Author = Au1.rsplit(' ')[-2]
        
        rs = start.find(class_="reputation-score")
        R_Score = rs.get_text()
        record = {
            'Question':Qsn,
            'Votes':vote,
            'number of answers':num_ans,
            'Views':view,
            'Tags':pt,
            'Category':Category,
            "Time": time,
            "Author Name": Author,
            "Reputation Score": R_Score,
            }
        Final_Result.append(record)
   

#Lets write these to a JSON file for now. 
with open('LaTex.json', 'w') as outfile:
    json.dump(Final_Result, outfile, indent=4)