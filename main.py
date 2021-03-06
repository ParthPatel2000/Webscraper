import requests
from bs4 import BeautifulSoup
import os
from download import download
import configloader as conf

download_path = conf.getpath()

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

start_category,start_page = conf.getlink()
# print(start_category)
for category_no in range(start_category,len(category_URL)):
    conf.update_category(category_no)                           # Updating the category for resume function to work

    category = category_URL[category_no]
    main_page = requests.get(category)

    dir_name = category.split('/')[-1]
    print('Category:', dir_name)
    category_path = os.path.join(download_path, dir_name)

    os.makedirs(category_path, exist_ok=True)

    soup = BeautifulSoup(main_page.content, 'html.parser')
    total_pages = soup.find_all('a', attrs={'class': 'page-numbers'})
    total_pages = int(total_pages[1].text)

    start_page = conf.getlink()[1]
    for page_no in range(start_page, total_pages + 1):                  # iterating each page for links
        conf.update_pageno(page_no)
        print('PageNO ', page_no)
        main_page = requests.get(category+'/page/'+str(page_no)).text
        soup = BeautifulSoup(main_page, 'html.parser')
        lines_with_urls = soup.find_all('h2', attrs={'class': 'entry-title'})
        urls = list()
        for line in lines_with_urls:
            urls.append(line.find('a').attrs['href'])

        for url in urls:                                                # Getting the file urls
            download_page = requests.get(url)
            download_page_soup = BeautifulSoup(download_page.content, 'html.parser')
            raw_download_link = download_page_soup.findAll('div', attrs={'class': 'entry-content'})
            download_links = raw_download_link[0].find_all('a')

            if len(download_links) == 0:
                print("No links found on page:", url)

            for download_link in download_links:
                download_link = download_link.attrs['href']

                if download_link.startswith('http://download.ps3-themes.com/'):
                    download(download_link, category_path)                       # Downloading the files
                else:
                    print("Not a valid download link:", download_link)
    conf.update_pageno(1)
