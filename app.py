from flask import Flask,request

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
    return r"""

    <div></div>
    <input> 
    <button onclick="sendMessage()">send </button>
    <script>
  const username = prompt("what is your user name?")

  const output = document.querySelector("div")


    async function sendMessage(){
    const message = document.querySelector("input")

  const rawResponse = await fetch('api/chat', {
    method: 'POST',
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({username,message:message.value})
  });
  const content = await rawResponse.json();
    output.textContent = ""
  console.log(content);
    for (const message of content.messages){
      output.innerHTML += `<div>${message.username}s-${message.message}</div>`
    }
    }

    setInterval(async() => {
    const response = await fetch("/api/messages")
    const content = await response.json()
     output.textContent = ""
      console.log(content);
        for (const message of content.messages){
          output.innerHTML += `<div>${message.username}-${message.message}</div>`
        }
    }, 1000)

    </script>
    """
if __name__ == "__main__": 
    app.run(port = 5001, debug = True)