import os 
import requests
from dotenv import load_dotenv
from pexels_api import API

class pexel:
    def __init__(self, results_per_page=5, start_page=1):
        load_dotenv()

        self.apikey = os.getenv('API-KEY')
        self.results_per_page=results_per_page
        self.start_page=start_page
        self.size="small"

    def search_api_new(self, search, type):
        response=None
        results=None
        headers = {
        'Authorization': self.apikey
        }
        params = {
            'query': search,
            'page': self.start_page,
            'per_page': self.results_per_page
            #'orientation': orientation,
            #'color': color,
            # Size is not a documented filter for Pexels API; included for demonstration
        }
        if type=="image":
            response = requests.get('https://api.pexels.com/v1/search', headers=headers, params=params)
            results=response.json()['photos']
        elif type=="video":
            response = requests.get('https://api.pexels.com/videos/search', headers=headers, params=params)   
            results=response.json()['videos']     
        return results
    
    def search_api(self, search, color=None, orientation=None):
        api = API(self.apikey)
        print("color=["+color+"]")
        print(orientation)
        if color =="" and orientation =="":
            api.search(search, page=self.start_page, results_per_page=self.results_per_page)    
        if color !="" and orientation =="":
            api.search(search, page=1, results_per_page=5, color=color)
        if color =="" and orientation !="":         
            api.search(search, page=1, results_per_page=5, orientation=orientation) 
        if color !="" and orientation !="":         
            api.search(search, page=1, results_per_page=5, color=color, orientation=orientation)
        
        photos = api.get_entries()
        return photos