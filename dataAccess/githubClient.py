import os
import requests

def scanGithubIssues(repoUrl):
    debtedItems = []

    parts = repoUrl.rstrip("/").split("/")

    if len(parts) < 2:
        return debtedItems
    owner, repo = parts[-2], parts[-1]

    url = f"https://api.github.com/repos/{owner}/{repo}/issues?state=all&per_page=100"

    token = os.getenv("GITHUB_TOKEN")
    headers = {'Accept': 'application/vnd.github.v3+json'}
    if token:
        headers['Authorization'] = f"token {token}"

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            for issue in response.json():
                if 'pull_request' in issue:
                    continue
                title = issue.get('title', '')
                body = issue.get('body') or ''

                # Indented correctly inside the for loop!
                if any(kw in title.lower() or kw in body.lower() for kw in ['todo', 'fixme', 'workaround', 'debt']):
                    debtedItems.append({
                        'source': 'Issue Tracker',
                        'id': f"#{issue.get('number')}",
                        'title': title,
                        'state': issue.get('state')
                    })

    except Exception as e:
        print(f"Github API Error: {e}")

    return debtedItems