from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

from services.service import repoAnalysis


@app.route('/', methods=['GET', 'POST'])
def index():
    dashboard_data = None

    if request.method == 'POST':
        repo_url = request.form.get('repo_url')
        if repo_url:
            dashboard_data = repoAnalysis(repo_url)

    return render_template('dashboard.html', data=dashboard_data)


if __name__ == '__main__':
    app.run(debug=True)