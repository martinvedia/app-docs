from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def root():
    return 'root'

@app.route("/tasks/<task_id>")
def get_task(task_id):
    tasks = {'task_id': task_id, 'descrip': 'Una descripción de una task'}
    query = request.args.get("query")

    if query:
        tasks["query"] = query

    return jsonify(tasks), 200

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    data["status"] = "Task created"
    return jsonify(data), 201
        
if __name__ == '__main__':
    app.run(debug = True)