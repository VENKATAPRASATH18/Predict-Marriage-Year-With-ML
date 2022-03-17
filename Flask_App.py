import flask
import flask_cors
from flask import request,render_template
import joblib

F_app = flask.Flask(__name__,template_folder='Template')
F_app.config["DEBUG"] = True

from flask_cors import CORS
CORS(F_app)

@F_app.route('/')
def home():
   return render_template('Structure.html')

@F_app.route('/predict',methods=['GET'])
def predict():
    
    model = joblib.load('age_prediction.ml')
    predicted_age_of_marriage = model.predict([[int(request.args['gender']),
                            int(request.args['religion']),
                            int(request.args['caste']),
                            int(request.args['mother_tongue']),
                            int(request.args['country']),
                            int(request.args['height_cms']),
                           ]])
    return str(round(predicted_age_of_marriage[0],2))
if __name__ == "__main__":
    F_app.run(debug=True)
