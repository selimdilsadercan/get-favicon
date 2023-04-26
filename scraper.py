from bs4 import BeautifulSoup
import requests

def get_icon(site_url):
    request = requests.get(site_url).text
    soup = BeautifulSoup(request, "lxml")
    head = soup.head
    
    link = head.find("link", rel="icon")
    adres : str = link["href"] 

    if adres.startswith("http"):
        icon_url = adres
    else: 
        icon_url = site_url + adres

    return icon_url


def get_site_name(site_url: str):
    site_name = site_url.split("://")[1]

    site_name = site_name.split("www.")[1] if site_name.count("www") != 0 else site_name

    site_name = site_name.split(".")[0]
    site_name = site_name.title()

    return site_name


icon = get_icon(input()) 
print(icon)
