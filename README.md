# Scrapy scripts for flat data extraction

Scripts for extracting information about existing flat offers in Kaunas from two websites:

https://www.aruodas.lt/

and

https://www.capital.lt/lt/nekilnojamas-turtas/


## Description

I want to have an idea what is flat situation in Kaunas. Specifically, I am interested in flat's:
1. Location (Rajonas)
2. Street (Gatve)
3. Price (Kaina)
4. Size (Dydis)
5. Number of rooms (Kambariai)
6. Year (Metai)
7. Floor/How many floors (Aukstas/is)
8*. (Just in case) I will be saving URL of each add (Nuoroda) 

This information should be put in a csv table, that can be later cleaned, merged, analyzed and plotted (I will be using R for this and these scripts are not added here so far)

## Examples of extracted tables

![Alt text](/Screenshot_of_table.png?raw=true "Screenshot of extracted table")

Current examples of extracted tables are 
-capitallt/capitalltbutai.csv 
-aruodas/aruodasbutai.csv


## Location of main Python scripts for extraction

In case different table structure is needed, these are the files that need to be changed:

-aroudas/spiders/aruodascrawl.py 
-capitallt/spiders/capitallt_scraper.py

## Run scripts/extract tables

Type in the terminal:

scrapy crawl capitallt -O <Name_of_the_saved_table>.csv

or 

scrapy crawl aruodascrawl -O <Name_of_the_saved_table>.csv


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)