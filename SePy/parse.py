from bs4 import BeautifulSoup
 
with open("SePy.html", "r") as f:
    
    contents = f.read()
 
    soup = BeautifulSoup(contents, 'lxml')
 
    print("title: " + str(soup.title))
    print("H1:" + str(soup.h1))
    print("paragraphs: " + str(soup.p))