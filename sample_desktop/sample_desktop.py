import requests
import re
from urllib.parse import urljoin
from bs4 import BeautifulSoup
def get_img_list():
    url_list = []
    for page_num in range(1,2):
        base_url = 'http://simpledesktops.com/browse/{}/'.format(page_num)
        index_text = requests.get(base_url).text
        index_soup = BeautifulSoup(index_text,'html5lib')
        srcs = index_soup.select('.desktop')
        for src in srcs:
            url = urljoin('http://simpledesktops.com',src.find('a')['href'])
            url_list.append(url)
    return url_list
def download_img(url_list):
    for url in url_list:
        index_text = requests.get(url).text
        index_soup = BeautifulSoup(index_text,'html5lib')
        srcs = index_soup.find('img')['src']
        del_str = re.search(r'g(.*?g)',srcs).group(1)
        name = re.search(r'([a-zA-Z0-9_.]*?g)',srcs).group(1)
        src = srcs.replace(del_str,'')
        print ("开始下载：{}".format(name))
        img = open('img/{}'.format(name),'wb')
        img.write(requests.get(src).content)
        img.close()
        print ("下载完成：{}".format(name))
def main():
    url_list = get_img_list()
    download_img(url_list)
if __name__ == "__main__":
    main()