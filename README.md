# Web Crawler in Python
Course Project for COMP 1405Z Fall 2022.

# Description
This project’s goal is to determine the top ten pages found during a crawl related to the user’s search query. The focus was to decrease time complexity and therefore increase the efficiency of the project. More on this matter can be found in the report included in the project. The project is divided into three parts: crawler, searchdata, and search

# Crawler 
Main function: extract, manipulate, and save data from HTML strings.
The crawler accepts a seed URL to parse. It will then parse the URLs embedded in the seed URL (determined by <a> tags) and continue to do so for each page it finds until the program has parsed every page. For each page, the crawler will extract the inner HTML content of the <p> tags to determine TF, IDF, and TF-IDF values for words on the page. The crawler is also in charge of extracting outgoing and incoming links to determine the page’s page rank. The crawler will save all this information in respective files for later use.

# Search Data
Main function: extract the correct data from files created in the crawler.

The searchdata file simply retrieves any information required while running the search.

# Search 
Main function: accept a search query and outputs the top ten pages
The search file will determine the TF-IDF of the inputted query to calculate the cosine similarity of all pages found during the crawl. If the user chooses to “boost” these values, the cosine similarity score will be multiplied by the page’s page rank for the final score. The program will take those values and sort them using an efficient sorting algorithm to output the ten pages with the highest scores.

# Running the Project
The included python files are modules. To watch them in action, refer to the test files. Make sure that the test files are in the same directory as the project files. Note that this project’s focus was not HTML/web development and is therefore designed to run on specific websites such as http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html
