from scraper import *
from notion import *

site_url = input("Web adresini girin")

site_adi = get_site_name(site_url)
icon_url = get_icon(site_url)

data= {
    "Site URL": {"url": site_url},
    "Name": {"title": [{"text": { "content": site_adi}}]}
}

print(site_adi, site_url)

# print(create_notion_data(data,icon_url))


