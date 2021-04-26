# Webscraper
webscraper made for www.ps3-themes.com

the config file
has 3 fields that can be tweaked for ux

Category field:
  Takes category no (range 0 - 14)
  the category field takes numbers 0 to 14
  also the categories are in same sequence as with the ones on the website.
  so the category 0 means 1'st category and 1 means 2nd category and so on till 14.
  Anything above that and there can be errors or unexpexted results.

PAGE field:
  Takes webpage no (range 1 - can be anything)
  this takes numbers from 1 and there is no upper limit because all the categories have different total pages.
  this is used just to have a reference so that when the process stops the code knows from which page to resume downloading.

category and page no can be set manually according to need

Path field:
  The path where you want to download the files.
  all the subfolders named after categories will be created automatically don't worry.
  Just show it where to put the main folder.

Example config file

storagepath:
  path: "D:/PS3"

# the download path change to where-ever you want it
# category folders will be created automatically

link:
  category: '0'
  page: '1'

# Categories are numbered from 0
# in case of stopping you can restart from a particular category and it's page_no to save time.
# category no for respective cateogries

#    0    dynamic-themes",
#    1    slideshow-themes",
#    2    animals-nature",
#    3    art-graphics",
#    4    babes",
#    5    cars-transportation",
#    6    people",
#    7    comics-anime",
#    8    gaming",
#    9    holiday-seasonal",
#    10   misc",
#    11   movies-tv",
#    12   music",
#    13   sports",
#    14   tech"
