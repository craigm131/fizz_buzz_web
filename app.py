#!venv/bin/python3.7

from flask import Flask,request

app = Flask(__name__)

@app.route('/fizzbuzz')
def calculate():
    for param in ['begin', 'end']:
        if param not in request.args:
            return 'Missing {}'.format(param)
    result = []
    for n in range(int(request.args.get('begin')), int(request.args.get('end'))+1):
        if n%3 == 0:
            result.append('fizz')
        elif n%5 == 0:
            result.append('buzz')
        else:
            result.append(n)
    return ','.join(str(item) for item in result)

if __name__ == '__main__':
    app.run(port=80)