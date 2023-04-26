import requests
import json

NOTION_TOKEN = "secret_0cN8GmB27WhsD2aYr9zVYRaJX1UASk7ivV3B5IkajOu"
DATABASE_ID = "d25b65fcd7ac4c3d9a2a8ef28cea33ef"
    
headers = {
    "Authorization": "Bearer " + NOTION_TOKEN,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

def get_pages():
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"

    payload = {"page_size": 100}
    response = requests.post(url, json=payload, headers=headers)

    data = response.json()  

    with open('db.json', "w", encoding='utf8') as f:
       json.dump(data, f, ensure_ascii=False, indent=4)

    results = data["results"]

    return results


def create_notion_data(properties, icon_url):
    icon =  {
        "type": "external", 
        "external": {
            "url": icon_url
        }
    }

    create_url = "https://api.notion.com/v1/pages"

    payload = {"parent": {"database_id": DATABASE_ID}, "properties": properties, "icon": icon}

    res = requests.post(create_url, headers=headers, json=payload)
    return res


