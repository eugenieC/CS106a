# this imports the SimpleServer library
import SimpleServer
# This imports the functions you defined in searchengine.py
from searchengine import create_index, search, textfiles_in_dir
# has the json.dumps function. So useful
import json
import os

"""
File: extension_server.py
---------------------
This starts a server! Go to http://localhost:8000 to enjoy it. Currently
the server only serves up the HTML. It does not search. Implement code in
the TODO parts of this file to make it work.
"""

# the directory of files to search over
DIRECTORY = 'bbcnews'
# perhaps you want to limit to only 10 responses per search..
MAX_RESPONSES_PER_REQUEST = 10

class SearchServer:
    def __init__(self):
        """
        load the data that we need to run the search engine. This happens
        once when the server is first created.
        """
        self.html = open('extension_client.html').read()

        # TODO: Your code here. Change this code to load any data you want to use!
        if os.path.exists(DIRECTORY):
            # Build index from files in the given directory
            files = textfiles_in_dir(DIRECTORY)
            self.index = {}          # index is empty to start
            self.file_titles = {}    # mapping of file names to article titles is empty to start
            create_index(files, self.index, self.file_titles)
            print("successful index file")


    # this is the server request callback function. You can't change its name or params!!!
    def handle_request(self, request):
        """
        This function gets called every time someone makes a request to our
        server. To handle a search, look for the query parameter with key "query"
        """
        # it is helpful to print out each request you receive!
        print("request:",request)
        # link="http://localhost:8000/search?query="+request.params['query']
        # os.system("open \"\" "+link)

        # if the command is empty, return the html for the search page
        if request.command == '':
            return self.html

        # if the command is search, the client wants you to perform a search!
        if request.command == 'search':
            # right now we respond to a search request with an empty string.
            # TODO: Your code here. change this code to return the string version 
            # of a list of dicts. Use json.dumps(collection) to turn a list into a string

            results=search(self.index, request.params['query'])

            if results:                             # check for non-empty results list
                return json.dumps([{"title": self.file_titles[filename]} for filename in search(self.index, request.params["query"])])

            else:
                return json.dumps([{"title":"No results match that query."}])


def main():
    # make an instance of your Server
    handler = SearchServer()
    # start the server to handle internet requests!
    SimpleServer.run_server(handler, 8000) # make the server

if __name__ == '__main__':
    main()