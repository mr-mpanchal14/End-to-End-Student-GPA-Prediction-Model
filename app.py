from flask import Flask,request,render_template
from src.pipeline.predict_pipeline import CustomData,PredictPipeline
import numpy as np

application = Flask(__name__)

app = application

## Route for a home page

# @app.route('/')
# def index():
#     return render_template('index.html') 

# 2 methods, it is going to support GET and POST
@app.route('/', methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data = CustomData(
            age = int(request.form.get('age')),
            gender = request.form.get('gender'),
            race_ethnicity = request.form.get('race_ethnicity'),
            parental_education = request.form.get('parental_education'),
            study_time_weekly = float(request.form.get('study_time_weekly')),
            absent = int(request.form.get('absent')),
            tutor = request.form.get('tutor'),
            parental_supp = request.form.get('parental_supp'),
            extracurr = request.form.get('extracurr'),
            sports = request.form.get('sports'),
            music = request.form.get('music'),
            volunteer = request.form.get('volunteer')

        )
        pred_df = data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline=PredictPipeline()
        print("Mid Prediction")
        results=predict_pipeline.predict(pred_df)
        print("after Prediction")
        return render_template('home.html',results=np.round(results[0],2))
    

if __name__=="__main__":
    #app.run(host="0.0.0.0")
    app.run(host='0.0.0.0', port = 8080)