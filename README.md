# Scrapy scripts for flat data extraction

Scripts for extracting information about existing flat offers in Kaunas from two websites:

https://www.aruodas.lt/

and

https://www.capital.lt/lt/nekilnojamas-turtas/


## Description

We want to have an idea what is flat situation in Kaunas. Specifically, we are interested in flat's:
1.  Location (Rajonas)
2.  Street (Gatve)
3.  Price (Kaina)
4.  Size (Dydis)
5.  Number of rooms (Kambariai)
6.  Year (Metai)
7.  Floor/How many floors (Aukstas/is)
8.  (Just in case) I will be saving URL of each ad (Nuoroda) 

This information should be put in a csv table, that can be later cleaned, merged, analyzed and plotted.

The first line of the csv table contains the names of the fields. Size of the table depends on the number of ads on the website (During the testing time there were 800 ads in aruodas.lt and 200 ads in capital.lt. Script was running for couple of minutes)

## Examples of extracted tables

![picture alt](/images/Screenshot_of_table.png?raw=true "Screenshot of extracted table")


## Usage

In case different table structure is needed, these files from the Spider_scripts need to be altered:

* aruodas_scraper.py
* capitallt_scraper.py

## Run scripts and save data in local files

In order to generate automatically generated scripts needed for the crawling, run 

`start.py`

When all needed files are in place, type in the terminal:

`scrapy crawl capitallt -O <Name_of_the_saved_table>.csv`

and

`scrapy crawl aruodas -O <Name_of_the_saved_table>.csv`

to scrape the other website.

P.S. In case HTTP error 403 appears, settings.py files may need to be altered accordingly. 

## Instalation

* To install required packages, type in the terminal:

`pip install -r requirements.txt`

Alternatively, for conda users, try to run:

`conda install --file requirements.txt`

* To clone this repository, type in the terminal:

`git clone https://github.com/A-Tilunaite/Learn_scrape_tests.git`

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)


## TO DO:
* Add exact run script times