from flask import Flask, request, render_template
import requests

app = Flask(__name__)

# List to store todo items
todo_items = []

# Define route to serve HTML page
@app.route('/')
def index():
    # Fetch todo items from Todo Service API
    todo_items = fetch_todo_items()
    # Render HTML template with todo items
    return render_template('index.html', todo_items=todo_items)

# Function to fetch todo items from Todo Service API
def fetch_todo_items():
    # Make HTTP request to Todo Service API
    response = requests.get('http://localhost:5000/todos')

    # Parse JSON response and extract todo items
    if response.status_code == 200:
        return response.json()
    else:
        return []
    
@app.route('/add_task', methods=['POST'])
def add_task():
    task_title = request.form.get('task_title')
    if task_title:
        # Add the task to the todo list
        todo_items.append({'title': task_title})
    return render_template('index.html', todo_items=todo_items)
    

if __name__ == '__main__':
    app.run(debug=True, port=5002)  # Run on port 5001 instead of the default 5000
