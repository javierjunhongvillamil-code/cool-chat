from flask import Flask,request, render_template

app = Flask(__name__)
chat_messages = []



@app.route("/api/messages",methods = ["GET"])
def messages():
    return {"messages":chat_messages}

@app.route("/api/chat",methods = ["POST"])
def chat():

    username = request.json['username']
    message = request.json['message']
    chat_messages.append({"username" : username,
              "message" : message})
    return {"messages":chat_messages}

@app.route("/")
def hello_world():
    return render_template("index.html")

if __name__ == "__main__": 
    app.run(port = 5001, debug = True)