import scrapy

class CapitalltSpider(scrapy.Spider):
    name = 'capitallt_nuoma'
    start_urls=['https://www.capital.lt/lt/nekilnojamas-turtas/nuomuoti/kaunas/butai']

    def parse(self,response):
        for flats in  response.xpath('//a[re:test(@class,"realty-item.realty-status-*")]'):
            dummy1 = flats.css('div.rid-place::text').get()
            dummy3 = dummy1.split(',')
            if len(dummy3)>3:
                street = dummy3[3]
            else:
                street = 'NaN'
            
            dummy4 = flats.css('div.rid-additional::text').get().split(',')
            if len(dummy4)>1:
                size=dummy4[1].replace(' m','')
                rooms=dummy4[0].replace(' Kamb.','')
            elif dummy4[0].find(' m')>-1:
                size=dummy4[0].replace(' m','')
                rooms='NaN'
            else:
                size='NaN'
                rooms='NaN'

            if len(flats.css('div.rid-additional::text').getall())==1:
                year = 'NaN'
                floor= 'NaN'
            else:
                dummy5 = flats.css('div.rid-additional::text').getall()[1].split(',')
                if len(dummy5)>2:
                    year = dummy5[2].strip()
                    floor = dummy5[1].replace(' Aukšt.','').strip()
                elif dummy5[1].find('Auk')>-1:
                    floor = dummy5[1].replace(' Aukšt.','').strip()
                    year = NaN
                else:
                    year=dummy5[1].strip()
                    floor='NaN'

                

            yield{
                'Pavadinimas': dummy1,
                'Rajonas': dummy3[2],
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
