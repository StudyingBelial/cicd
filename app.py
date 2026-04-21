from flask import Flask, jsonify
from main import Add, Subtract, CallHello
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status" :"running",
        "examples" : {
            "Add(2,3)" : Add(2,3),
            "Subtract(5,2)" : Subtract(5,2),
            "Hello Message" : CallHello()
        }
    })
    
if __name__ == "__main__":
    port = int(os.environ.get('PORT'))
    app.run(host='0.0.0.0', port=port)