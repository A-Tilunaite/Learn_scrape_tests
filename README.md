# Flat_scrape_tests
Extract data about existing flat offers

Some notes:
1. I just need to use Python to extract data about flats price/size/location/... into a nice table. Data merging/cleaning/analysis/plots will be done later with R (not sure why I ended up with this option precisely)

2. Flat selling and rent crawlers are identical more or less. So main files that would be of some interest are        -aruodas/aroudas/spiders/aruodascrawl.py
-capitallt/capitallt/spiders/capitallt_scraper.py

3. To run scripts I used command in terminal, e.g.:
scrapy crawl capitallt -O capitalltbutai.csv

4. Current examples of extracted tables are 
-capitallt/capitalltbutai.csv
-aruodas/aruodasbutai.csv
