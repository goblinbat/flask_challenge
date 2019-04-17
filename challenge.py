from flask import Flask

app = Flask(__name__)

@app.route('/<int:far>')
def convert(far):
    cel = (far - 32) / 1.8
    return f'{cel}'


if __name__=='__main__':
    app.run(debug=True)