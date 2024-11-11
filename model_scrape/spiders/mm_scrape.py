import scrapy
import json

class MmScrapeSpider(scrapy.Spider):
    name = "mm_scrape"

    URLS = "https://www.modelmanagement.com/backend/api/models/search"
    AGE_MIN = 60
    AGE_MAX = 61

    def start_requests(self):
        # Write the opening bracket for the JSON array
        with open(f'Models({self.AGE_MIN}-{self.AGE_MAX}).json', 'w') as f:
            f.write("[\n")
        
        payload = {
            "page": 1,
            "limit": 20,
            "age-min": self.AGE_MIN,
            "age-max": self.AGE_MAX,       
        }

        yield scrapy.Request(
            url=self.URLS,
            method='POST',
            body=json.dumps(payload), 
            headers={'Content-Type': 'application/json'}, 
            callback=self.parse,
            meta={'page': 1}
        )

    def parse(self, response):
        try:
            data = response.json()
        except AttributeError:
            data = json.loads(response.text)

        current_page = response.meta['page']
        models_data = [entry["model"] for entry in data.get("data", [])]

        # Append model data to JSON file
        with open(f'Models({self.AGE_MIN}-{self.AGE_MAX}).json', 'a') as f:
            for i, model in enumerate(models_data):
                # Check if it's the last model of the last page to avoid adding a comma
                if current_page == data.get("meta", {}).get("last_page", 1) and i == len(models_data) - 1:
                    f.write(json.dumps(model) + "\n")
                else:
                    f.write(json.dumps(model) + ",\n")

        # Get the last page from the meta data
        last_page = data.get("meta", {}).get("last_page", 1)
        self.log(f"Processing page: {current_page} / Last page: {last_page}")
        next_page = current_page + 1

        # Continue to the next page if it exists
        if next_page <= last_page:
            payload = {
                'page': next_page,
                'limit': 20,
                'age-min': self.AGE_MIN,
                'age-max': self.AGE_MAX,
            }

            yield scrapy.Request(
                url=self.URLS,
                method='POST',
                body=json.dumps(payload),
                headers={'Content-Type': 'application/json'},
                callback=self.parse,
                meta={'page': next_page}
            )
        else:
            # Close the JSON array after the last page is processed
            with open(f'Models({self.AGE_MIN}-{self.AGE_MAX}).json', 'a') as f:
                f.write("]\n")
            self.log("Completed writing JSON array to file.")
