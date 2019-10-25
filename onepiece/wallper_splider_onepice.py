import requests
import re
from bs4 import BeautifulSoup
import time

def banner():
    print ()
    print (' ██████╗ ███╗   ██╗███████╗██████╗ ██╗███████╗ ██████╗███████╗ ')
    print ('██╔═══██╗████╗  ██║██╔════╝██╔══██╗██║██╔════╝██╔════╝██╔════╝ ')
    print ('██║   ██║██╔██╗ ██║█████╗  ██████╔╝██║█████╗  ██║     █████╗   ')
    print ('██║   ██║██║╚██╗██║██╔══╝  ██╔═══╝ ██║██╔══╝  ██║     ██╔══╝   ')
    print ('╚██████╔╝██║ ╚████║███████╗██║     ██║███████╗╚██████╗███████╗ ')
    print (' ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝     ╚═╝╚══════╝ ╚═════╝╚══════╝ ')
    print ()
def get_img_url():
    img_urls = []
    for pagenum in range(1,13):
        base_url = "https://wall.alphacoders.com/by_sub_category.php?id=173190&name=%E6%B5%B7%E8%B4%BC%E7%8E%8B+%E5%A3%81%E7%BA%B8&filter=4K+Ultra+HD&lang=Chinese&page={}".format(pagenum)
        index_text = requests.get(base_url).text
        index_soup = BeautifulSoup(index_text,'html5lib')
        img_infos = index_soup.select('img')
        for img_info in img_infos:
            try:
                img_url = img_info['data-src']
                if "avatars" not in img_url:
                    img_urls.append(img_info['data-src'].replace('thumb-350-','thumb-1920-'))
            except :
                continue
    return img_urls
def download_img(img_urls):
    for img_url in img_urls:
        try:
            img_name = re.search(r'(thumb-.*?g)',img_url).group(1)
            img = requests.get(img_url)
            img_save = open("img/{}".format(img_name),'wb')
            img_save.write(img.content)
            print ('{}下载完成'.format(img_name))
            img_save.close()
        except :
            continue
def main():
    banner()
    img_urls = get_img_url()
    download_img(img_urls)
if __name__ == "__main__":
    main()