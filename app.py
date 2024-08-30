from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    name = request.args.get('name', 'World!')

    # ... (rest of your code in index)

    return render_template('index.html', name=name)

@app.route('/get_data')
def get_data():
    # Option 1: Pass the name as a query parameter
    # name = request.args.get('name')  # Uncomment if using this option
    # data = {'message': f"Hello, {name}!"}  # Uncomment this line

    # Option 2: Access the name from a session variable (if applicable)
    # name = session.get('name')  # Uncomment this line, and set up session management if needed
    # data = {'message': f"Hello, {name}!"}  # Uncomment this line

    # Choose the appropriate option based on how you want to handle the name
    data = {'message': 'Hello from the server!'}  # Placeholder message for now

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
