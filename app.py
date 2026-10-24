
from flask import Flask , render_template, send_from_directory
import os

app = Flask(__name__)

RESUME_FOLDER = os.path.join(app.root_path,"static")
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/download")
def download():
    return send_from_directory(RESUME_FOLDER,"Aishwarya_Jalgi_CV.pdf", as_attachment =True)

if __name__=="__main__":
    app.run(debug=True)
   

