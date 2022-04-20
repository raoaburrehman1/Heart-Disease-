from Flask import Flask, render_template, request
import pickle
import numpy as np
#from sklearn.ensemble.forest import RandomForestClassifier

app= Flask(__name__)

svc_model = pickle.load(open('svc_trained_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
   inputs = []
   inputs.append(request.form['age'])
   inputs.append(request.form['sex'])    
   inputs.append(request.form['cp'])
   inputs.append(request.form['chol'])
   
   age = request.form['age']
   sex = request.form['sex'] 
   cp = request.form['cp']
   chol = request.form['chol']
   
   
   final_inputs = [np.array(inputs)]
   prediction = svc_model.predict(final_inputs)
    #unseen_feature_vectors = request.form.values()
   
   if prediction[0] == 1:
        categorical_array = "Have Disease"
   if prediction[0] == 0:
        categorical_array = "Not Have Disease"
    
   result= categorical_array
   if age=="1":
       age = "Old"
   if age=="2":
       age = "Mature"
       
   if sex=="0":
       sex = "Female"
   if sex=="1":
       sex = "Male"
     
   if cp=="0":
        cp = "Zero"
   if cp=="1":
       cp = "One"
   if cp=="2":
       cp = "Two"
   if cp=="3":
       cp = "Three"
       
   if chol=="0":
       chol = "Zero"
   if chol=="1":
       chol = "One"
       
   return render_template('predict.html', prediction_text1 = request.args['result'], age1 = request.args['age'], sex1 = request.args['sex'], cp1 = request.args['cp'], chol1 = request.args['chol'])


if __name__ == "__main__":
    app.run(debug=True)