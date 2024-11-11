import scrapy
import json

class MmScrapeSpider(scrapy.Spider):
    name = "mm_scrape"

    URLS = "https://www.modelmanagement.com/backend/api/models/search"
    # age_ranges = [(16, 23), (23, 24), (24, 25), (25, 26), (26,27),(27,28),(28,29),(29,30),(30,31),(31,33),(33,36),(36,100)]  # Define age ranges here
    # age_ranges = [(23, 24), (24, 25), (25, 26), (26,27),(27,28),(28,29),(29,30),(30,31),(31,33),(33,36),(36,100)]  # Define age ranges here
    age_ranges = [(36,100)]  # Define age ranges here

    def start_requests(self):
        for age_min, age_max in self.age_ranges:
            # Write the opening bracket for each JSON array
            filename = f'Models({age_min}-{age_max}).json'
            with open(filename, 'w') as f:
                f.write("[\n")
            
            payload = {
                "page": 1,
                "limit": 20,
                "age-min": age_min,
                "age-max": age_max,
            }

            # Pass age_min and age_max in meta to use them later
            yield scrapy.Request(
                url=self.URLS,
                method='POST',
                body=json.dumps(payload), 
                headers={'Content-Type': 'application/json'}, 
                callback=self.parse,
                meta={'page': 1, 'age_min': age_min, 'age_max': age_max, 'filename': filename}
            )

    def parse(self, response):
        try:
            data = response.json()
        except AttributeError:
            data = json.loads(response.text)

        current_page = response.meta['page']
        age_min = response.meta['age_min']
        age_max = response.meta['age_max']
        filename = response.meta['filename']
        models_data = [entry["model"] for entry in data.get("data", [])]

        # Append model data to JSON file
        with open(filename, 'a') as f:
            for i, model in enumerate(models_data):
                # Check if it's the last model of the last page to avoid adding a comma
                if current_page == data.get("meta", {}).get("last_page", 1) and i == len(models_data) - 1:
                    f.write(json.dumps(model) + "\n")
                else:
                    f.write(json.dumps(model) + ",\n")

        # Get the last page from the meta data
        last_page = data.get("meta", {}).get("last_page", 1)
        self.log(f"Processing page: {current_page} / Last page: {last_page} for age range {age_min}-{age_max}")
        next_page = current_page + 1

        # Continue to the next page if it exists
        if next_page <= last_page:
            payload = {
                'page': next_page,
                'limit': 20,
                'age-min': age_min,
                'age-max': age_max,
            }

            yield scrapy.Request(
                url=self.URLS,
                method='POST',
                body=json.dumps(payload),
                headers={'Content-Type': 'application/json'},
                callback=self.parse,
                meta={'page': next_page, 'age_min': age_min, 'age_max': age_max, 'filename': filename}
            )
        else:
            # Close the JSON array after the last page is processed
            with open(filename, 'a') as f:
                f.write("]\n")
            self.log(f"Completed writing JSON array to file for age range {age_min}-{age_max}")
