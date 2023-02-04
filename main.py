from flask import Flask, request
from paragraph_parser import ParagraphParser
import json

app = Flask(__name__)


@app.route('/word_frequency',methods=['GET'])
def get_word_frequency():
    if request.method == 'GET':
        data = json.loads(request.data)
        paragraph = data['paragraph']
        parser  = ParagraphParser(paragraph)
        response = parser.get_word_frequency()
        print(response)
        return response

  
if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8000,debug = True)