from flask import Flask, request
from paragraph_parser import ParagraphParser
import json

app = Flask(__name__)

def handle_paragraph():
    try:
        data = json.loads(request.data)
        paragraph = str(data['paragraph'])
    except:
        message = """
            Error parsing paragraph from request body. body should be of the form:
            {"paragraph": "your_paragraph_here"}
        """
        return message, 400
    return paragraph,200


@app.route('/word_frequency',methods=['GET'])
def get_word_frequency():        
    paragraph,code = handle_paragraph()
    if code != 200:
        return paragraph,code
    parser  = ParagraphParser(paragraph)
    response = parser.get_word_frequency()
    return response

  
if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8000,debug = True)