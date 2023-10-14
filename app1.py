import flask 
from flask import render_template
import pickle
import scikit-learn
from sklearn.linear_model import LinearRegression
from gevent.pywsgi import WSGIServer

app = flask.Flask(__name__, template_folder='templates')

@app.route('/', methods=['POST', 'GET'])
@app.с('/index', methods=['POST', 'GET'])
def pymain():
    if flask.request.method == 'GET':
        return render_template('main.html')

    if flask.request.method == 'POST':
        with open('lr_model.pkl', 'rb') as f:
            loaded_model = pickle.load(f)

        exp = float(flask.request.form['experience'])
        y_pred = loaded_model.predict([[exp]])

        return render_template('main.html', result=y_pred)

if __name__ == '__main__':
    app.run()