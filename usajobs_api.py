import requests
from utils.config import USAJOBS_API_KEY 

def fetch_usajobs(Keyword,location="remote",results_per_page='5'):
    headers={
        "Host":"data.usajobs.gov",
        "User-Agent":"mandananurag@gmail.com",
        "Authorization-Key":USAJOBS_API_KEY
     
    }
    params={
        "keyword":Keyword,
        "LocationName":location,
        "ResultsPerPage":results_per_page
    }
    url=f"https://data.usajobs.gov/api/search"
    response=requests.get(url,headers=headers,params=params)
    if response.status_code==200:
        return response.json().get('SearchResult',{}).get("SearchResultItems",[])
        
    else:
        print(f"Error connecting to API. Status Code: {response.status_code}")
        return []    
