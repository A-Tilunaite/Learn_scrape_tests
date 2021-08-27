import scrapy

class CapitalltSpider(scrapy.Spider):
    name = 'capitallt'
    start_urls=['https://www.capital.lt/lt/nekilnojamas-turtas/pirkti/kaunas/butai']

    def parse(self,response):
        for flats in  response.xpath('//a[re:test(@class,"realty-item.realty-status-*")]'):
            title = flats.css('div.rid-place::text').get()
            sep_title = title.split(',')
            if len(sep_title)>3:
                street = sep_title[3]
            else:
                street = 'NaN'
            
            info_line1 = flats.css('div.rid-additional::text').get().split(',')
            if len(info_line1)>1:
                size=info_line1[1].replace(' m','')
                rooms=info_line1[0].replace(' Kamb.','')
            elif info_line1[0].find(' m')>-1:
                size=info_line1[0].replace(' m','')
                rooms='NaN'
            else:
                size='NaN'
                rooms='NaN'

            if len(flats.css('div.rid-additional::text').getall())==1:
                year = 'NaN'
                floor= 'NaN'
            else:
                info_line2 = flats.css('div.rid-additional::text').getall()[1].split(',')
                if len(info_line2)>2:
                    year = info_line2[2].strip()
                    floor = info_line2[1].replace(' Aukšt.','').strip()
                elif info_line2[1].find('Auk')>-1:
                    floor = info_line2[1].replace(' Aukšt.','').strip()
                    year = NaN
                else:
                    year=info_line2[1].strip()
                    floor='NaN'

                

            yield {
                #'Pavadinimas': title,
                'Rajonas': sep_title[2],
                'Gatve' : street,
                'Kaina': flats.css('div.realty-item-price').css('strong::text').get().replace('€',''),
                'Dydis': size,
                'Kambariai': rooms,
                'Metai': year,
                'Aukstas/is': floor,
                'Nuoroda': flats.attrib['href'],
            }
        next_page = response.css('div.right-side').css('a').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback =self.parse)
            
