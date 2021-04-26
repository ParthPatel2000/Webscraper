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
