from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    matches = []
    error = None
    regex_pattern = ''
    test_string = ''
    match_count = 0

    if request.method == 'POST':
        regex_pattern = request.form.get('regex', '')
        test_string = request.form.get('test_string', '')

        if regex_pattern and test_string:
            try:
                iterator = re.finditer(regex_pattern, test_string)
                for match in iterator:
                    matches.append(match.group(0))
                
                match_count = len(matches)
                
            except re.error as e:
                error = f"Invalid Regular Expression: {e}"

    return render_template(
        'index.html', 
        matches=matches, 
        match_count=match_count,
        error=error, 
        regex=regex_pattern, 
        test_string=test_string
    )

if __name__ == '__main__':
    app.run(debug=True)