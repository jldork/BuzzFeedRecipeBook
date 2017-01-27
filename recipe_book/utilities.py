from bs4 import BeautifulSoup
from urllib import request

def make_soup(url):
    r = request.urlopen(url).read()
    soup = BeautifulSoup(r, 'html.parser')
    return soup

def strip_list(my_list):
    return list(map(str.strip, my_list))