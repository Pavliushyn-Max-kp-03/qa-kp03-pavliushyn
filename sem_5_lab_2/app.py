from flask import Flask
from flask import jsonify, request, abort
from binaryFile import BinaryFile
from bufferFile import BufferFile
from directory import Directory
from logTextFile import LogTextFile
import json
app = Flask(__name__)
binaryFile1 = BinaryFile(1, 'binFile1', 'info1')
bufferFile1 = BufferFile('bufFile1', 5)
root = Directory('root', 100)
logTextFile1 = LogTextFile('logtext1', 'jibiub', root)
binFiles = [
    {
        'id': 1,
        'fileName': u'binFile1',
        'info': u'info1',
        'father': None
    },
    {
        'id': 2,
        'title': u'binFile2',
        'description': u'info2',
        'father': 'root'
    }
]

@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'This is lab2'
    a = response.status_code
    print(a)
@app.route('/binaryFile')
def hello_bin():
    return 'This is binary files pages'
@app.route('/binaryFiles', methods=['GET'])
def get_tasks():
    return jsonify({'binFiles': binFiles})
@app.route('/binaryFile_read/<int:file_id>', methods=['GET'])
def get_task(file_id):
    file = list(filter(lambda t: t['id'] == file_id, binFiles))
    if len(file) == 0:
        abort(404)
    return jsonify({'task': file[0]})
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404
@app.route('/binaryFile_delete/<int:file_id>', methods=['DELETE'])
def delete_task(task_id):
    file = list(filter(lambda t: t['id'] == task_id, binFiles))
    if len(file) == 0:
        abort(404)
    binFiles.remove(file[0])
    return jsonify({'result': True})
@app.route('/binaryFile_del')
def delete_bin():
    binaryFile1.__delete__()
    return jsonify({'result': True})

@app.route('/binaryFile_create/binaryFiles', methods=['POST'])
def create_task():
    if not request.json or not 'fileName' in request.json:
        abort(400)
    file = {
        'id': binFiles[-1]['id'] + 1,
        'fileName': request.json['fileName'],
        'info': request.json.get('info', ""),
        'father': None
    }
    binFiles.append(file)
    return jsonify({'task': file}), 201
@app.route('/binaryFile_move/<int:file_id>', methods=['PUT'])
def update_task(file_id):
    file = list(filter(lambda t: t['id'] == file_id, binFiles))
    if len(file) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    file[0]['fileName'] = request.json.get('fileName', file[0]['fileName'])
    file[0]['info'] = request.json.get('info', file[0]['info'])
    file[0]['father'] = request.json.get('father', file[0]['father'])
    return jsonify({'file': file[0]})

if __name__ == '__main__':
    app.run(debug=True)