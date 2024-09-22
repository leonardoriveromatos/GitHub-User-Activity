def display_events(events):
    for event in events[:10]:
        if event['type'] == 'PushEvent':
            repo = event['repo']['name']
            commits = len(event['payload']['commits'])
            print(f"- Pushed {commits} commits to {repo}")
        elif event['type'] == 'IssuesEvent':
            repo = event['repo']['name']
            print(f"- Opened a new issue in {repo}")
        elif event['type'] == 'WatchEvent':
            repo = event['repo']['name']
            print(f"- Starred {repo}")