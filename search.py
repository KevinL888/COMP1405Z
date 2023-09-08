#Search Module
#Kevin Lai 101288231

import os
import math
import crawler
import searchdata

#Function is responsible for answering search queries by utilizing the functions in the searchdata module in order to rank
#the top 10 searches based on the query from highest to lowest. I mainly worked on optimizing my search function to ensure
#that I minimized the time complexity. All the data that are used to calculate the top 10 most relevant pages are stored in
#files from the crawl process and retrieved from the searchdata module.
#Parameter: phrase: the search query: boost: if page rank should be used
#Return top_ten_pages: list of top 10 webpages based off cosine simularity score
def search(phrase,boost):
    list_of_documents = []
    top_ten_pages = []
    phrase_into_list = phrase.split()
    query_dict = {}
    numerator = 0
    left_denominator = 0
    right_denominator = 0

#create dictinary to store unique words for the search phrase
    for word in phrase_into_list:
        if word in query_dict:
            query_dict[word]["count"] +=1
        else:
            query_dict[word] = {"count" : 1}

#calculate query tf_idf for each word
    for word,value in query_dict.items():
        idf = searchdata.get_idf(word)

        query_td_idf = math.log2(1 + (value["count"]/len(phrase_into_list))) * idf

        value["query_tf_idf"] = query_td_idf
        #calculate left denominator which is query tf_idf multiplied by itself
        left_denominator+= (query_td_idf*query_td_idf)

    #loop through all the webpages(URLs) directories to get the tf_idf of the words from the query
    for i in range(len(crawler.url_to_num)):
        document_path = os.path.join("crawl_data", str(i))

        #loop through each of the unique words in the query(this loop will only run twice if example: the query was apple coconut apple)
        for word in query_dict.keys():
            tf_idf = searchdata.get_tf_idf(crawler.num_to_url[i],word)
            #calculate numerator by sum of each documents tf_idf multiplied by the query tf_idf for that word
            numerator += (query_dict[word]["query_tf_idf"]*tf_idf)
            #calculate right denominator which is the documents word tf_idf multiplied by itselfs
            right_denominator += (tf_idf * tf_idf)

        denominator = (math.sqrt(left_denominator)*math.sqrt(right_denominator))

        #create a dictionary with the format url,title,score
        document_dict = {}
        document_dict["url"] = crawler.num_to_url[int(i)]
        title_file = os.path.join(document_path,"title.txt")
        title = ""
        if os.path.isfile(title_file):
            filein = open(title_file, "r")
            title = filein.readline()
            filein.close()

        document_dict["title"] = title.strip()

        if(denominator != 0):
            document_dict["score"] = numerator/denominator
        else:
            document_dict["score"] = 0

        #if boost is true than multiply the cosine simularity with the page rank
        if boost:
            page_rank = searchdata.get_page_rank(crawler.num_to_url[i])
            document_dict["score"]*=page_rank

        #append the documents to a list as a dictionary with the format of url,title,score
        list_of_documents.append(document_dict)

        numerator = 0
        right_denominator = 0

    #sort the list of webpages by their consine simularity score from ascending to descending order
    list_of_documents = sorted(list_of_documents, key=lambda k: k['score'], reverse=True)

    #find the top 10 maximum scores and append to a top ten list to be displayed
    for index in range(10):
        top_ten_pages.append(list_of_documents[index])

    return top_ten_pages
