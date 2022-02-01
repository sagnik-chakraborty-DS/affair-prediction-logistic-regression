from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import joblib
from src.utils.all_utils import log
log_file = open("Logs\logs.txt", 'a+')
app = Flask(__name__) # initializing a flask app

@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")


@app.route('/report.html',methods=['GET'])  # route to display the home page
@cross_origin()
def report():
    return render_template("report.html")


@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            Womans_age=float(request.form['Womans_age'])
            yrs_marriage= float(request.form['yrs_marriage'])
            number_of_children= int(request.form['number of children'])
            
            is_Rate_marriage = request.form['Rate_marriage']
            #(= 1 if tract bounds river; 0 otherwise)
            if(is_Rate_marriage=='1'):
                Rate_marriage=1
            elif(is_Rate_marriage=='2'):
                Rate_marriage=2
            elif(is_Rate_marriage=='3'):
                Rate_marriage=3    
            elif(is_Rate_marriage=='4'):
                Rate_marriage=4
            
            is_Religious = request.form['Religious']
            if(is_Religious=="1"):
                Religious=1
            elif(is_Religious=="2"):
                Religious=2    
            elif(is_Religious=="3"):
                Religious=3    
            elif(is_Religious=="4"):
                Religious=4
            
            is_Education=request.form['Education']
            if(is_Education=="9"):
                Education=9        
            elif(is_Education=="12"):
                Education=12
            elif(is_Education=="14"):
                Education=14
            elif(is_Education=="16"):
                Education=16
            elif(is_Education=="17"):
                Education=17
            elif(is_Education=="20"):
                Education=20
            
            is_Woman_occupation=request.form['Woman occupation']
            if(is_Woman_occupation=="1"):
                Woman_occupation=1
            elif(is_Woman_occupation=="2"):
                Woman_occupation=2                                
            elif(is_Woman_occupation=="3"):
                Woman_occupation=3
            elif(is_Woman_occupation=="4"):
                Woman_occupation=4
            elif(is_Woman_occupation=="5"):
                Woman_occupation=5    
            elif(is_Woman_occupation=="6"):
                Woman_occupation=6
            
            is_man_occupation=request.form['Man occupation']
            if(is_man_occupation=="1"):
                Man_occupation=1
            elif(is_man_occupation=="2"):
                Man_occupation=2                                
            elif(is_man_occupation=="3"):
                Man_occupation=3
            elif(is_man_occupation=="4"):
                Man_occupation=4
            elif(is_man_occupation=="5"):
                Man_occupation=5    
            elif(is_man_occupation=="6"):
                Man_occupation=6
            filename = 'artifacts\model_dir\logistic_regression.model'
            loaded_model = joblib.load(open(filename, 'rb')) # loading the model file from the storage
            # predictions using the loaded model file
            prediction=loaded_model.predict([[Womans_age,yrs_marriage,number_of_children,Rate_marriage,Religious,Education,Woman_occupation,Man_occupation]])
            print('prediction is', prediction)
            # showing the prediction results in a UI
            return render_template('result.html',prediction=prediction)
        except Exception as e:
            log(log_file, str(e))


if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001, debug=True)
	app.run(debug=True) # running the app