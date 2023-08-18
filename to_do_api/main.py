from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def root():
    return 'root'

@app.route("/tasks/<task_id>")
def get_task(task_id):
    tasks = {'task_id': task_id, 'descrip': 'Una descripción de una task'}
    return jsonify(tasks), 200

@app.route('/tasks', methods=['POST'])
def create_task(descrip):
    data = request.get_json()
    return jsonify(data), 200
        
    
    

if __name__ == '__main__':
    app.run(debug = True)