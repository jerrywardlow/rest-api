#!flask/bin/python
from flask import Flask, jsonify, abort

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'descripttion': u'Paper, paper products, staples, staplers, more paper',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Must read everything Miguel has written..',
        'done': False
    }
]

@app.route('/todo/api/v1/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/todo/api/v1/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})


if __name__ == '__main__':
    app.run(debug=True)
