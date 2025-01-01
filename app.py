import os   # Import the os module, jo system related functionalities ko access karne ke liye use hota hai
from flask import Flask, render_template, request, jsonify 
import openai #openai library ko import kiya gaya hai

app = Flask(__name__) #Flask class ka object banaya gaya hai jo batata hai ki app kahan se run ho raha hai

openai.api_key = os.getenv("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")

@app.route('/') 
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']   #the message from user is stored in user_input
    try:                                   #in try  block we will call the openai api to get the response
        response = openai.completions.create(            #generate the response using the openai api 
            model = "gpt-3.5-turbo",
            prompt=user_input,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.8
        )

        reply = response.choices[0].text.strip()    #the response is stored in reply    
        return jsonify({'reply': reply})
    except Exception as e:
        return jsonify({'error':str(e)})
    
if __name__ == '__main__':
    app.run(debug=True)  #app ko run karne ke liye