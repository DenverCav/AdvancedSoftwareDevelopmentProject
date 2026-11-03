import os
import re

def scanCodeComments(repo_path):
    debtedItems = []
    pattern = re.compile(r'(//|/\*)\s*(TODO|FIXME):\s*(.*)', re.IGNORECASE)

    for root, dirs, files in os.walk(repo_path):
        if '.git' in root:
            continue
        for file in files:
            if file.endswith(('.c', '.cpp', '.h', '.py', '.js', '.java')):
                filePath = os.path.join(root, file)
                try:
                    with open(filePath, 'r', encoding='utf-8', errors='ignore') as f:
                        for lineNumber, line in enumerate(f, 1):
                            matches = pattern.search(line)
                            if matches:
                                debtedItems.append({
                                    'source': 'Code Comments',
                                    'file': os.path.relpath(filePath, repo_path),
                                    'line': lineNumber,
                                    'text': matches.group(3).strip()
                                })
                except Exception as e:
                    continue
    return debtedItems