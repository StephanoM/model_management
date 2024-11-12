import scrapy
import json

class ModelSpider(scrapy.Spider):
    name = "model_scrape"
    start_index = 20100  
    end_index = 20200  

    def __init__(self, *args, **kwargs):
        super(ModelSpider, self).__init__(*args, **kwargs)
        self.output_filename = f"intagram_({self.start_index}-{self.end_index}).json"
        self.results = []

    def start_requests(self):
        try:
            with open('entries_full.json', 'r') as file:
                data = json.load(file)
            
            proxy_url = self.settings.get('PROXY')  # Retrieve the proxy URL from settings
            for entry in data[self.start_index:self.end_index]:
                slug = entry['slug']
                url = f"https://www.modelmanagement.com/backend/api/profile/model/{slug}?extra_data=true"
                
                # Log the proxy being used
                self.logger.info(f"Using proxy: {proxy_url} for URL: {url}")
                
                yield scrapy.Request(
                    url,
                    callback=self.parse,
                    meta={'proxy': proxy_url, 'slug': slug}
                )
        except FileNotFoundError:
            self.logger.error("The JSON file was not found.")

    def parse(self, response):
        try:
            json_response = response.json()
            data = json_response.get("data", {})

            result = {
                'slug': data.get('slug'),
                'country_name': data.get('location', {}).get('country_name'),
                'is_premium': data.get('is_premium'),
                'has_instagram_username': data.get('has_instagram_username')
            }
            
            # Log the proxy used for the response
            self.logger.info(f"Received response for {response.meta['slug']} using proxy: {response.meta.get('proxy')}")
            
            self.results.append(result)
        except json.JSONDecodeError:
            self.logger.error("Failed to decode JSON response.")

    def closed(self, reason):
        with open(self.output_filename, 'w') as f:
            json.dump(self.results, f, indent=4)
