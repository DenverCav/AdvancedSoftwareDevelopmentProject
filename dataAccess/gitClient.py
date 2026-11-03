import git
import re


def scanGitCommits(repo_path):
    debtedItems = []
    repo = None
    try:
        repo = git.Repo(repo_path)
        pattern = re.compile(r'\b(TODO|FIXME|workaround|tech debt|temporary)\b', re.IGNORECASE)

        for commit in repo.iter_commits(max_count=200):
            if pattern.search(commit.message):
                debtedItems.append({
                    'source': 'Git Commit',
                    'author': str(commit.author),
                    'hexsha': commit.hexsha[:7],
                    'message': commit.message.strip().split('\n')[0]
                })
    except Exception as e:
        print(f"Git Log Error: {e}")
    finally:
        if repo:
            repo.close()

    return debtedItems