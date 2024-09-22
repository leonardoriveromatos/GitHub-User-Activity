import argparse
from endpoints import get_github_user_events
from display import display_events

parser = argparse.ArgumentParser(description="Fetch GitHub user activity.")
parser.add_argument("username", help="GitHub username to fetch events for")
args = parser.parse_args()

events = get_github_user_events(args.username)

if events:
    print(f"Recent events for {args.username}:")
    display_events(events)