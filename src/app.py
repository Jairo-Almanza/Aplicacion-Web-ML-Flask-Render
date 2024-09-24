
# your code here
from flask import Flask, request, render_template
from pickle import load
import pandas as pd

app = Flask(__name__)
model = load(open("/workspaces/Aplicacion-Web-ML-Flask-Render/models/model_xgbregressor_42_studentperformance.sav", "rb"))
prediction=0

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        
        val1 = float(request.form["Attendance"])
        val2 = float(request.form["Hours_studied"])
        val3 = float(request.form["Access_to_Resources_encoded"])
        val4 = float(request.form["Parental_Involvement_encoded"])
        
        data = [[val1, val2, val3, val4]]
        prediction = model.predict(data)[0]
        pred_class = prediction
    else:
        pred_class = None
    
    return render_template("index.html", prediction = pred_class)


# Habilitar el modo de depuración y ejecutar la aplicación
if __name__ == "__main__":
    app.debug = True
    app.run()

