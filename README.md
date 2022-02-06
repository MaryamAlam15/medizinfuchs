# Medizinfuchs

This is an app to extract data from [medizinfuchs.de](https://www.medizinfuchs.de/)
It is split into 2 apps:
1. **app** that scrap and extract data from the site and store it in Sqlite DB.
2. **api** that provides endpoints to get that data.
   1. The Following endpoints are implemented:
      1. GET /products: return data from the database.
      2. GET /products/scrape : scrape list of products, put into DB, and return data.
      3. GET /products/:product : return data of given product.
      4. GET /products/:product/scrape : scrape data for given product, put into DB, and return the data.

### Pre-Req:
 - Python 3.8
 - Docker

### How to run:

1. Build docker container with the command:
    > $ docker build -t mf-scraper .

2. Run the container:
    > $ docker run -d -p 9999:9999 --rm --name medizinfuchs-scraper -v /$(pwd)/db:/data/db/ --env SQLITE_PATH=/data/db/medizinfuchs.sqlite mf-scraper:latest