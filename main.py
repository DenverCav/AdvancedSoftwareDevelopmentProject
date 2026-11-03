from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

from services.service import repoAnalysis


@app.route('/', methods=['GET', 'POST'])
def index():
    results = None
    repo_url = ""

    if request.method == 'POST':
        repo_url = request.form.get('repo_url')
        if repo_url:
            rawData = repoAnalysis(repo_url)

            results = {
                'total': rawData.get('total_debt', 0),
                'comments': rawData.get('comment_count', 0),
                'commits': rawData.get('commit_count', 0),
                'issues': rawData.get('issue_count', 0),
                'items': []
            }

            for item in rawData.get('items', []):
                item_copy = item.copy()
                if 'hexsha' in item_copy and 'hash' not in item_copy:
                    item_copy['hash'] = item_copy['hexsha']
                results['items'].append(item_copy)

    return render_template('dashboard.html', results=results, repo_url=repo_url)


if __name__ == '__main__':
    app.run(debug=True)