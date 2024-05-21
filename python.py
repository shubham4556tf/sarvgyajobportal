from flask import Flask,render_template
app = Flask(__name__)


JOBS=[
    {
        'id':1,
        'title':'Data Science',
        'location':'Bengalur , India',
        'salary':'Rs 1,00,000'
        
        
    },
    {
        'id':2,
        'title':'Data Analyst',
        'location':'Delhi NCR , India',
        'salary':'Rs 1,00,000'
        
        
    },
    {
        'id':3,
        'title':'Web Developer',
        'location':'Noida , India',
        'salary':'Rs 12,00,000'
        
        
    },
    {
        'id':4,
        'title':'Backend Engineer',
        'location':'US san , India',
        'salary':'Rs 11,00,000'
        
        
    },
     {
        'id':5,
        'title':'Frontend Engineer',
        'location':'Bengalur , India',
        'salary':'Rs 11,00,000'
        
        
    }
     
]
@app.route("/")
def hello_world():  
    return render_template("index.html",jobs=JOBS,company_name='Sarvgya')
if __name__=="__main__":
    app.run(host="0.0.0.0",port=50100,debug=True)