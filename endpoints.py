import urllib.request #libreria propia de python para manejar peticiones HTTP
import json

def get_github_user_events(username):
    url = f"https://api.github.com/users/{username}/events"
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read().decode('utf-8')
            events = json.loads(data)
            return events
    except urllib.error.HTTPError as e:
        print(f"Error fetching events for {username}. Status code: {e.code}")
        return None