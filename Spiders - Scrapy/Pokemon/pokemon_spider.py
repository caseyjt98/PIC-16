import scrapy

class PokemonSpider(scrapy.Spider):
    name = "pokemon"
    def start_requests(self):
        urls = [
                'https://pokemondb.net/pokedex/national'
                ]
        for url in urls:
            yield scrapy.Request(url=url, callback = self.parse)



    def parse(self,response):
        list_of_pokemon = response.css('span.infocard-tall')
        
        for pokemon in list_of_pokemon:
            d = {
                'name':pokemon.css('a.ent-name::text').extract_first(),
                'number':pokemon.css('small::text').extract_first()
            }

            pokemon_url = pokemon.css('a::attr(href)').extract_first()
            full_url = response.urljoin(pokemon_url) # get full url using urljoin()
            r = scrapy.Request(full_url,self.parse2)
            r.meta["item"] = d
            yield r
            #yield scrapy.Request(url= pokemon_url, callback = self.parse)


    def parse2(self,response):
        d = response.meta["item"]
        pokedex_entries = response.css("article >  table.vitals-table  td::text").extract()
        first_entry = pokedex_entries[0]
        d["first_entry"] = first_entry
        yield d



