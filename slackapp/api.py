from flask import Flask, request
from agent import Agent

app = Flask(__name__)

agent = Agent()

@app.route('/agent', methods=['POST'])
def respond():
    email = request.json.get('email')
    message = request.json.get('message')
    user_input = email + " " + message

    # Pass user_input to the approve method
    approval_result = agent.callbacks[0].approve(user_input)

    # Use the approval_result in your logic as needed
    if approval_result:
        result = agent.run(user_input)
        return result
    else:
        return "Approval denied."

if __name__ == "__main__":
    app.run(port=5000)