import requests
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('hn', type=int, help='The hall ticket number (1-60)')


args = parser.parse_args()

hn = str(args.hn)

if len(hn) != 2:
    hn = str(0) + hn

hn = str(1005207330) + hn


url = 'http://127.0.0.1:5000/result'


payload = {
    'hn': hn
}

response = requests.post(url, json=payload)

if response.status_code == 200:
    result = response.json()
    print(result['name'] + " : " + str(result['sgpa']))
else:
    print(f"Error: {response.status_code}")
    print(response.text)
