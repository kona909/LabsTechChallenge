from flask import Flask, render_template

app = Flask(__name__)
app.config['DEBUG']= True 

@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/gc2677', methods = ['GET'])
def test():
	return render_template('tutorial2.html')

if __name__ == '__main__':
    app.run()
