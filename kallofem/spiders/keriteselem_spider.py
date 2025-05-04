import scrapy


class KeritesElemSpider(scrapy.Spider):
    name = "keriteselem"
    start_urls  = ["https://kallofem.hu/shop/group/keriteselemek?page=1"]
    #"/shop/group/keriteselemek?page=1" URL  "/shop/group/keriteselemek" helyett, mert eltérő eredményeket ad.


    def parse(self, response):
        # Szűkítjük a keresést a 'div.product-group-container'-en belülre,
        # hogy elkerüljük az ütközést a másik 'article.product-row' elemekkel
        for prod in response.css("div.product-group-container article.product-row"):
            yield {
                "name": prod.xpath(".//h4/text()").get(),
                "image": prod.xpath(".//img/@src").get(),
                "price": prod.css(".product-price::text").get(),
            }

            next_page =response.xpath('//a[@rel="next"]/@href').get()
            if next_page is not None:
                yield response.follow(next_page, callback=self.parse)