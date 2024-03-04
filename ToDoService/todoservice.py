import os
from flask import Flask, jsonify, request
from sqlalchemy import create_engine

app = Flask(__name__)

# In-memory data store for todo items
'''
todos = [
    {"id": 1, "title": "Learn Flask", "completed": False},
    {"id": 2, "title": "Build Todo App", "completed": True}
]
'''
# Get database connection details from environment variables
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_NAME = os.environ.get('DB_NAME')

# Create database connection
db_url = f'mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
engine = create_engine(db_url)

# Route to get all todo items
@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

# Route to get a specific todo item by ID
@app.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = next((todo for todo in todos if todo['id'] == todo_id), None)
    if todo:
        return jsonify(todo)
    else:
        return jsonify({"error": "Todo not found"}), 404

# Route to create a new todo item
@app.route('/todos', methods=['POST'])
def create_todo():
    data = request.json
    if 'title' in data:
        todo = {
            "id": len(todos) + 1,
            "title": data['title'],
            "completed": True
        }
        todos.append(todo)
        return jsonify(todo), 201
    else:
        return jsonify({"error": "Title is required"}), 400

# Route to update an existing todo item
@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = next((todo for todo in todos if todo['id'] == todo_id), None)
    if todo:
        data = request.json
        todo['title'] = data.get('title', todo['title'])
        todo['completed'] = data.get('completed', todo['completed'])
        return jsonify(todo)
    else:
        return jsonify({"error": "Todo not found"}), 404

# Route to delete an existing todo item
@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todos = [todo for todo in todos if todo['id'] != todo_id]
    return jsonify({"message": "Todo deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)