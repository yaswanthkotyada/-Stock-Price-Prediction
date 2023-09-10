from flask import Flask,render_template,request
import pickle 
import numpy as np
app=Flask(__name__)
method=pickle.load(open("stockprice.pkl","rb"))
@app.route("/")
def home():
    return render_template('dastock.html')
@app.route("/prediction", methods=["GET","POST"])
def prediction():
    if request.method=="POST":
        int_features=[float(x) for x in request.form.values()]
        final_features=[np.array(int_features)]
        prediction=method.predict(final_features)
        output=prediction[0]
        return render_template('dastock.html',prediction_text="closed_value is {}".format(output))
if __name__=="__main__":
    app.run(debug=True)
