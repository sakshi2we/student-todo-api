from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []
task_id = 1

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    global task_id
    data = request.json
    task = {
        "id": task_id,
        "title": data.get("title"),
        "priority": data.get("priority", "medium"),
        "completed": False
    }
    tasks.append(task)
    task_id += 1
    return jsonify(task)

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    for task in tasks:
        if task["id"] == id:
            task["completed"] = True
            return jsonify(task)
    return {"error": "Task not found"}, 404

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    global tasks
    tasks = [t for t in tasks if t["id"] != id]
    return {"message": "Deleted"}

if __name__ == '__main__':
    app.run(debug=True)