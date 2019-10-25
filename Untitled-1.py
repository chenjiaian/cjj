import requests
from bs4 import BeautifulSoup
import multiprocessing as mp 
import time 

t1 = time.time()
r = requests.get('<html xmlns="http://www.w3org/1999/xhtml">')

c = r.text

soup = BeautifulSoup(c,'html.parser')
page_div = soup.find('div',{'class':'page'}) 
page page_div.find_all('a')[-2].text 
movies = []
urls =[<html xmlns="http://www.w3org/1999/xhtml" + str(i) +'.html'for i in range(1,11)] 

def crawl_page(url):
    p_r = requests.get(url)
    p_c = p_r.text
    p_soup = BeautifulSoup(p_c,'html.parser')
    p_content =p_soup.find_all('div',{'class':'list-cont'})
    page Movies = []
    for movies in p_content:
        MoviesDic ={}
        MoviesDic['picUrl'] = movie.find('div',{'class':'list-cont-img'}).find('img')['src']
        MoviesDic['name'] = movie.find('div',{'class':'list-cont-main'}).find('a')text 
        try:
            MoviesDic['grade'] = movie.find('span',{'class':'grade-number'}).text
        except Exception as e:
            MovieDic['grade'] = ''

            pageMovie.append(movieDic) 
            return pageMovie 
               
        pool =mp.Pool()
        multi_res =[pool.apply_async(crawl_page,(crawl_page,(url)) for url in urls]
        pageMovies = [res.get() for res in multi_res]

        for pageMovies in pageMovies:
            for movie in pageMovie:
                movies.append(movie)
                print(len(movies))
                t2 = time.time()
                print(t2-t1)
