import argparse
from endpoints import get_github_user_events
from display import display_events
import json

parser = argparse.ArgumentParser(description="Fetch GitHub user activity.")
parser.add_argument("username", help="GitHub username to fetch events for")
args = parser.parse_args()

events = get_github_user_events(args.username)

with open("data.json", "w") as data:
    json.dump(events, data, indent=4)

if events:
    print(f"Recent events for {args.username}:")
    display_events(events)