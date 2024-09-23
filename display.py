def display_events(events):
    for event in events:
        match event['type']:
            case 'PushEvent':
                repo = event['repo']['name']
                commits = len(event['payload']['commits'])
                print(f"- Pushed {commits} commits to {repo}")
            case 'IssuesEvent':
                repo = event['repo']['name']
                print(f"- Pushed {commits} commits to {repo}")
            case 'WatchEvent':
                repo = event['repo']['name']
                print(f"- Starred {repo}")
    return None