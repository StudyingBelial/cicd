from flask import Flask, jsonify
from main import Add, Subtract, CallHello

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
    app.run()