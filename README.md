# scraper_microservice_demo

In order to request data from the microservice, a URL is sent and a requests.get() call is made. Here is an example
call: requests.get("https://en.wikipedia.org/wiki/Pinot_noir#Description"). The URL is received and the appropriate
information from the page is scraped, turned into a JSON object and then returned.


<img width="400" alt="UML" src="https://user-images.githubusercontent.com/11323552/236707908-222e5cd6-3e95-4409-8471-62cfe1424bed.png">
