#Search Data Module
#Kevin Lai 101288231
import crawler
import os

#Function rerieves the outgoing links for the given url and returns a list of the outgoing links
#Parameter: url: the given url to retrieve outgoing links for
#Return: list_of_outgoing_url: list of outgoing urls for the given url
def get_outgoing_links(url):
    list_of_outgoing_url = []

    if url in crawler.url_to_num:
        file_path = os.path.join("crawl_data",str(crawler.url_to_num[url]))
        file = os.path.join(file_path, "outgoing_links.txt")
        if os.path.isfile(file):
            filein = open(file, "r")

            for x in filein:
                list_of_outgoing_url.append(x.strip())
    else:
        return None

    filein.close()
    return list_of_outgoing_url

#Function rerieves the incoming links for the given url and returns a list of the incoming links
#Parameter: url: the given url to retrieve incoming links for
#Return: list_of_incoming_url: list of incoming urls for the given url
def get_incoming_links(url):
    list_of_incoming_url = []

    if url in crawler.url_to_num:
        file_path = os.path.join("crawl_data",str(crawler.url_to_num[url]))
        file = os.path.join(file_path, "incoming_links.txt")
        if os.path.isfile(file):
            filein = open(file, "r")

            for x in filein:
                list_of_incoming_url.append(x.strip())
    else:
        return None

    filein.close()
    return list_of_incoming_url

#Function navigates to the index directory that corresponds to the URL given and retrieves 
#the data from a text file named page_rank
#Parameter: url: the url to retrieve page_rank for
#Return: page_rank: the page rank for the url given: -1: if the given url is not found
def get_page_rank(url):
     if url in crawler.url_to_num:
        file_path = os.path.join("crawl_data",str(crawler.url_to_num[url]))
        file = os.path.join(file_path, "page_rank.txt")
        if os.path.isfile(file):
            filein = open(file, "r")
            page_rank = float(filein.readline())
            filein.close()
            return page_rank       
     else:
         return -1

#Function retrieves the data for the inverse document frequency of a given word. The idf directory 
#is in the crawler_data directory and the data to be returned is in a text file where the name of 
#the file is the word given as a parameter.
#Parameter: word: the word to fetch idf
#Return: idf: idf value for the given word : 0: if no idf is found for word
def get_idf(word):
    file_path = os.path.join("crawl_data","idf")
    file = os.path.join(file_path, word+".txt")
    if os.path.isfile(file):
            filein = open(file, "r")
            idf = float(filein.readline())
            filein.close()
            return idf
    return 0

#Function fetch the data by accessing the directories corresponding to the URL and then access the tf directory. The function then retrieves the data 
#from a text file where the name of the file is the word given as a parameter.
#Parameter: url: url to fetch td: word: word to get term frequency
#Return tf: the term frequency for the word on the current url webpage: 0: if the url or tf file is not found
def get_tf(url,word):
    if url in crawler.url_to_num:
        file_path = os.path.join("crawl_data",str(crawler.url_to_num[url]))
        tf_path = os.path.join(file_path, "tf")
        file = os.path.join(tf_path, word+".txt")

        if os.path.isfile(file):
            filein = open(file, "r")
            tf = float(filein.readline())
            filein.close()
            return tf
    return 0

#Function fetch the data by accessing the directories corresponding to the URL and then access the tf_idf directory. The function then retrieves the data 
#from a text file where the name of the file is the word given as a parameter.
#Parameter: url: url to fetch tf_idf: word: word to get tf_idf
#Return tf_idf: the tf_idf for the word on the current url webpage: 0: if the url or tf_idf file is not found
def get_tf_idf(url,word):
    if url in crawler.url_to_num:
        file_path = os.path.join("crawl_data",str(crawler.url_to_num[url]))
        tf_idf_path = os.path.join(file_path, "tf_idf")
        file = os.path.join(tf_idf_path, word+".txt")

        if os.path.isfile(file):
            filein = open(file, "r")
            tf_idf = float(filein.readline())
            filein.close()
            return tf_idf
    return 0

