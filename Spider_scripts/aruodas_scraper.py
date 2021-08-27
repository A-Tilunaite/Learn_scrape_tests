import scrapy

class aruodascrawl(scrapy.Spider):
    name='aruodas'
    start_urls=['https://m.en.aruodas.lt/butai/kaune/puslapis/1/?obj=1&FRegion=43&FDistrict=6']

    def parse(self,response):
        for flats in response.css('a.result-item-info-container-v3'):
            region_street=flats.css('span.item-address-v3::text').get().strip().split(',')
            all_info=flats.css('span.item-description-v3::text').get()
            s1 = all_info.find('rooms')
            s2 = all_info.find('m²')
            s3 = all_info.find('floor')
            s4 = all_info.find('year')
            yield {
                #'Pavadinimas': flats.css('span.item-address-v3::text').get().strip(),
                'Rajonas':  region_street[0],
                'Gatve' :  region_street[1],
                'Kaina': flats.css('span.item-price-main-v3').xpath('span/text()').get().replace('€',''),
                #'Visa_info': all_info,
                'Dydis': all_info[(s1+6):(s2)].replace(',','.'), 
                'Kambariai':  all_info[0:(s1)].strip(),
                'Metai': all_info[(s3+6):(s4)],
                'Aukstas/is': all_info[(s2+3):(s3)], 
                'Nuoroda': flats.attrib['href'],
            }
        next_page = response.css('div.button-next-v2').css('a').attrib['href']
        first_url=response.request.url
        if next_page is not None and first_url.find(next_page)==-1:
                yield response.follow(next_page ,callback=self.parse)
                
