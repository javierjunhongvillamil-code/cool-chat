from flask import Flask,request

app = Flask(__name__)
chat_messages = []



@app.route("/api/messages",methods = ["GET"])
def messages():
    return {"messages":chat_messages}

@app.route("/api/chat",methods = ["POST"])
def chat():
    message = request.json['message']
    chat_messages.append(message)
    return {"messages":chat_messages}

@app.route("/")
def hello_world():
    return r"""

    <div></div>
    <input> 
    <button onclick="sendMessage()">send </button>
    <script>

  const output = document.querySelector("div")


    async function sendMessage(){
    const message = document.querySelector("input")
      console.log("user input", message.value)
      



  const rawResponse = await fetch('api/chat', {
    method: 'POST',
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({message:message.value})
  });
  const content = await rawResponse.json();
    output.textContent = ""
  console.log(content);
    for (const message of content.messages){
      output.innerHTML += `<div>${message}</div>`
    }
    }

    setInterval(async() => {
    const response = await fetch("/api/messages")
    const content = await response.json()
     output.textContent = ""
      console.log(content);
        for (const message of content.messages){
          output.innerHTML += `<div>${message}</div>`
        }
    }, 1000)

    </script>
    """

app.run(port = 5001,debug = True)