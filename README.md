# cat_feeder_demo

In order to request data from the microservice, a URL is sent and requests.get() call is made. Here is an example
call: requests.get("https://en.wikipedia.org/wiki/Pinot_noir#Description"). The URL is received and the appropriate
information from the page is scraped, turned into a JSON object and then returned.
