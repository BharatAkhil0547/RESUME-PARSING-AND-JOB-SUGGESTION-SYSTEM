from flask import Flask,url_for,redirect,render_template,request
from werkzeug.utils import secure_filename
from check import *
import os
app=Flask(__name__)
upload_folder = "uploads/"
if not os.path.exists(upload_folder):
   os.mkdir(upload_folder)

app.config['UPLOAD_FOLDER'] = upload_folder
@app.route('/')
def welcome():
    return render_template("file.html")
path_name=""
result={}
@app.route('/upload',methods=["GET","POST"])
def upload():
    if request.method == 'POST': # check if the method is post
      f = request.files['file'] # get the file from the files object
      # Saving the file in the required destination
      f.save(os.path.join(app.config['UPLOAD_FOLDER'] ,secure_filename(f.filename))) # this will secure the file
      path_name=os.path.join(app.config['UPLOAD_FOLDER'] ,secure_filename(f.filename))
      data=Resume_Parser(path_name)
      return render_template("hello.html",items=data)
@app.route('/submit',methods=["GET","POST"])
def submit():
   if request.method=="POST":
        dict=request.form['result']
        result=eval(dict)
        dropdown=request.form['slct']
        dropdown=dropdown+".csv"
        naukri=os.path.join("C:\\Users\\chaitu\\Desktop\\WebScraping\\Naukri\\",dropdown)
        monster=os.path.join("C:\\Users\\chaitu\\Desktop\\WebScraping\\Monster\\",dropdown)
        #path="C:\Users\chaitu\Desktop\WebScraping\Naukri\IT Infrastructure Services.csv"
        #df=pd.read_csv("C:\\Users\\chaitu\\Desktop\\WebScraping\\Naukri\\IT Infrastructure Services.csv")
        #df=df.head(10)
        # years1=request.form["Experience"]

        ## Experience
        years=0
        if "Experience1" in request.form:
            years=0
        elif "Experience" in request.form:
            years=request.form["Experience"]
            years=int(years)


        mf=pd.read_csv(monster)
        nf=pd.read_csv(naukri)
        nf['Skill-Match'] = nf.apply(lambda row : check(row['KeySkills'],result["Skills"]), axis = 1)
        nf['Percentage']=nf.apply(lambda row:percentage(row['KeySkills'],row['Skill-Match']),axis=1)
        mf['Skill-Match'] = mf.apply(lambda row : check(row['KeySkills'],result["Skills"]), axis = 1)
        mf['Percentage']=mf.apply(lambda row:percentage(row['KeySkills'],row['Skill-Match']),axis=1)
        m_dict=mf.to_dict(orient="records")
        n_dict=nf.to_dict(orient="records")
        n_dict=[i for i in n_dict if float(i['Percentage'])>0.2]
        m_dict=[i for i in m_dict if float(i['Percentage'])>0.2]
        if len(n_dict)>=len(m_dict):
            c=['-' for i in range(len(n_dict)-len(m_dict))]
            m_dict=m_dict+c
            d={i:"" for i in range(len(n_dict))}
            i=0
            count=0
            while i<len(n_dict):
                d[count]=n_dict[i]
                count=count+1
                d[count]=m_dict[i]
                count=count+1
                i=i+1
            return render_template("job_details.html",item=d)
        else:
            c=['-' for i in range(len(m_dict)-len(n_dict))]
            n_dict=n_dict+c
            d={i:"" for i in range(len(n_dict))}
            i=0
            count=0
            while i<len(n_dict):
                d[count]=n_dict[i]
                count=count+1
                d[count]=m_dict[i]
                count=count+1
                i=i+1
            return render_template("job_details.html",item=d)

   

if __name__=='__main__':
    app.run(debug=True)