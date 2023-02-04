
from flask import Flask , redirect , url_for , request # Importing the class flask
# app is the object or instance of Flask
app = Flask(__name__)
# app.route informs Flask about the URL to be used by function
@app.route('/api/parse_paragraph',methods=['GET'])
def parse_paragraph():
    if request.method == 'GET':
        data = request.data 
        print(data)
        
        return 'ok'

  
if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8000,debug = True)