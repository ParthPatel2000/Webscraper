import requests
from bs4 import BeautifulSoup
import os
from download import download

download_path = "D:/PS3" # change this to what you want your directory to be, or this directory will be created

category_URL = ["http://www.ps3-themes.com/x/dynamic-themes",
                "http://www.ps3-themes.com/x/slideshow-themes",
                "http://www.ps3-themes.com/x/animals-nature",
                "http://www.ps3-themes.com/x/art-graphics",
                "http://www.ps3-themes.com/x/babes",
                "http://www.ps3-themes.com/x/cars-transportation",
                "http://www.ps3-themes.com/x/people",
                "http://www.ps3-themes.com/x/comics-anime",
                "http://www.ps3-themes.com/x/gaming",
                "http://www.ps3-themes.com/x/holiday-seasonal",
                "http://www.ps3-themes.com/x/misc",
                "http://www.ps3-themes.com/x/movies-tv",
                "http://www.ps3-themes.com/x/music",
                "http://www.ps3-themes.com/x/sports",
                "http://www.ps3-themes.com/x/tech"]


for category in category_URL:
    # Finding the no of pages.
    main_page = requests.get(category)

    dir_name = category.split('/')[-1]
    print('Category:', dir_name)
    download_path = os.path.join(download_path, dir_name)

    os.makedirs(download_path, exist_ok=True)

    soup = BeautifulSoup(main_page.content, 'html.parser')
    total_pages = soup.find_all('a', attrs={'class': 'page-numbers'})
    total_pages = int(total_pages[1].text)

    # Iterating the no of pages starting from 1

    for page_no in range(1, total_pages + 1):
        print('PageNO ', page_no)
        main_page = requests.get(category+'/page/'+str(page_no)).text
        soup = BeautifulSoup(main_page, 'html.parser')
        lines_with_urls = soup.find_all('h2', attrs={'class': 'entry-title'})
        urls = list()
        for line in lines_with_urls:
            urls.append(line.find('a').attrs['href'])

        for url in urls:
            download_page = requests.get(url)
            download_page_soup = BeautifulSoup(download_page.content, 'html.parser')
            raw_download_link = download_page_soup.findAll('div', attrs={'class': 'entry-content'})
            download_link = raw_download_link[0].find('a').attrs['href']
            # print(download_link)
            download(download_link, download_path)
