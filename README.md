# spider_world
In this project, I used scrapy to scrape population and country data from https://www.worldometers.info/world-population/population-by-country/ url. 
To do that firstly I create spider worldscrapers. In this spider I define start_request method to make request, in this request I use callback attribute to 
parse method. In this method I parse the this request to get table content after that I get all tr attributes from it then iterate them in for loop to get 
country data and population. Finally, yield them to population.json file.
