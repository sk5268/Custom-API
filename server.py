from flask import Flask, request, jsonify
import requests
import re

app = Flask(__name__)

@app.route('/result', methods=['POST'])
def get_result():
    # Extract the hall ticket number from the POST request
    hn = request.json.get('hn')

    # URL and payload setup
    url = 'REDACTED 😅'
    payload = {
        'htno': hn,
        'submit': 'SUBMIT'
    }

    # Make a POST request to the server
    s = requests.Session()
    response = s.post(url, data=payload).text

    # Extract the name and SGPA using regular expressions
    try:
        name = re.findall(r'&nbsp;(.*?)<', response)[2]
        sgpa_raw = re.findall(r'19">(.*?)<', response)[1]

        if sgpa_raw != '-':
            sgpa_temp = re.findall(r'"style19">&nbsp;(.*?)<', response)[0]
            sgpa = float("{:.2f}".format(float(sgpa_temp))) if sgpa_temp != '-' else 'fail'
        else:
            sgpa = 'withheld'
    except IndexError:
        return jsonify({'error': 'Unable to retrieve result. Please check the hall ticket number and try again.'}), 400

    # Return the result as a JSON object
    return jsonify({'name': name, 'sgpa': sgpa})

if __name__ == '__main__':
    app.run(debug=True)
