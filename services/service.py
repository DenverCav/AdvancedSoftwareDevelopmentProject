import tempfile
import git
from dataAccess.scanner import scanCodeComments
from dataAccess.gitClient import scanGitCommits
from dataAccess.githubClient import scanGithubIssues

def repoAnalysis(repo_url):
    dashboardData = {
        'comment_count': 0,
        'commit_count': 0,
        'issue_count': 0,
        'total_debt': 0,
        'items': [],
        'url_scanned': repo_url
    }

    with tempfile.TemporaryDirectory() as tempDir:
        try:
            git.Repo.clone_from(repo_url, tempDir, depth=100)

            comments = scanCodeComments(tempDir)
            commits = scanGitCommits(tempDir)
            issues = scanGithubIssues(repo_url)

            dashboardData['comment_count'] = len(comments)
            dashboardData['commit_count'] = len(commits)
            dashboardData['issue_count'] = len(issues)
            dashboardData['total_debt'] = len(commits) + len(issues) + len(comments)
            dashboardData['items'] = commits + issues + comments

        except Exception as e:
            print(f"Servicing Error during analysis: {e}")

    return dashboardData