from bs4 import BeautifulSoup
import requests, openpyxl

excel=openpyxl.Workbook()
print(excel.sheetnames)
sheet=excel.active
sheet.title="top rated shows"
print(excel.sheetnames)
sheet.append(["movie name",'movie rank',"movie yar","IMDB rating"])
try:
    source = requests.get('https://www.imdb.com/chart/top/')
    source.raise_for_status()
    soup = BeautifulSoup(source.text, 'html.parser')

    movies = soup.find('tbody', class_="lister-list").find_all('tr')

    for movie in movies:
        name = movie.find('td', class_="titleColumn").a.text

        rank = movie.find('td', class_="titleColumn").get_text(strip=True).split('.')[0]

        year = movie.find('td', class_="titleColumn").span.text.strip('()')

        rating=movie.find('td', class_="ratingColumn imdbRating").strong.text

        print(name,rank,year,rating)
        sheet.append([name,rank,year,rating])



except Exception as e:
    print(e.args)

excel.save("top rated shows.xlsx")