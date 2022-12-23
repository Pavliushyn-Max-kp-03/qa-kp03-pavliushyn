from flask import Flask
from flask import jsonify, request, abort
from binaryFile import BinaryFile
from bufferFile import BufferFile
from directory import Directory
from logTextFile import LogTextFile
import json
app = Flask(__name__)
binaryFile1 = BinaryFile(5, 'binFile1', 'info1')
bufferFile1 = BufferFile(5, 'bufFile1', 5)
root = Directory(2, 'root', 100)
logTextFile1 = LogTextFile(5, 'logtext1', 'jibiub', root)
binFiles = [
    {
        'id': 1,
        'fileName': u'binFile1',
        'info': u'info1',
        'father': None
    },
    {
        'id': 2,
        'fileName': u'binFile2',
        'info': u'info2',
        'father': 'root'
    }
]
logFiles = [
    {
        'id': 1,
        'fileName': u'logFile1',
        'info': u'info1',
        'father': None
    },
    {
        'id': 2,
        'title': u'logFile2',
        'info': u'info2',
        'father': 'directory1'
    }
]
bufFiles = [
    {
        'id': 1,
        'fileName': u'bufFile1',
        'maxSize': 10,
        'father': None
    },
    {
        'id': 2,
        'fileName': u'bufFile2',
        'maxSize': 15,
        'father': 'root'
    }
]
directories = [
    {
        'id': 1,
        'dirName': u'directory1',
        'maxElements': 100,
        'father': 'root'
    },
    {
        'id': 2,
        'dirName': u'root',
        'maxElements': 150,
        'father': None
    }
]


@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'This is lab2'
    a = response.status_code
    print(a)
###########################################################
@app.route('/binaryFile')
def hello_bin():
    return 'This is binary files pages'
@app.route('/binaryFiles', methods=['GET'])
def get_bin():
    return jsonify({'binFiles': binFiles})
@app.route('/binaryFile_read/<int:file_id>', methods=['GET'])
def get_task(file_id):
    file = list(filter(lambda t: t['id'] == file_id, binFiles))
    if len(file) == 0:
        abort(404)
    return jsonify({'file': file[0]}), 302
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404
@app.route('/binaryFile_delete/<int:file_id>', methods=['GET', 'DELETE'])
def delete_bin(file_id):
    file = list(filter(lambda t: t['id'] == file_id, binFiles))
    if len(file) == 0:
        abort(404)
    binFiles.remove(file[0])
    return jsonify({'result': True})
@app.route('/binaryFile_del')
def del_bin():
    binaryFile1.__delete__()
    return jsonify({'result': True}), 201

@app.route('/binaryFile_create/binaryFiles', methods=['POST'])
def create_bin():
    if not request.json or not 'fileName' in request.json:
        abort(400)
    file = {
        'id': binFiles[-1]['id'] + 1,
        'fileName': request.json['fileName'],
        'info': request.json.get('info', ""),
        'father': None
    }
    binFiles.append(file)
    return jsonify({'file': file}), 201
@app.route('/binaryFile_move/<int:file_id>', methods=['PUT'])
def update_bin(file_id):
    file = list(filter(lambda t: t['id'] == file_id, binFiles))
    if len(file) == 0:
        abort(404)
    if not request.json:
        abort(400)
    file[0]['fileName'] = request.json.get('fileName', file[0]['fileName'])
    file[0]['info'] = request.json.get('info', file[0]['info'])
    file[0]['father'] = request.json.get('father', file[0]['father'])
    return jsonify({'file': file[0]})
#######################################################
@app.route('/logFile_create/logFiles', methods=['POST'])
def create_log():
    if not request.json or not 'fileName' in request.json:
        abort(400)
    file = {
        'id': logFiles[-1]['id'] + 1,
        'fileName': request.json['fileName'],
        'info': request.json.get('info', ""),
        'father': None
    }
    logFiles.append(file)
    return jsonify({'file': file}), 201
@app.route('/logFile_move/<int:file_id>', methods=['PUT'])
@app.route('/logFile_append/<int:file_id>', methods=['PUT'])
def update_log(file_id):
    file = list(filter(lambda t: t['id'] == file_id, logFiles))
    if len(file) == 0:
        abort(404)
    if not request.json:
        abort(400)
    file[0]['fileName'] = request.json.get('fileName', file[0]['fileName'])
    file[0]['info'] = request.json.get('info', file[0]['info'])
    file[0]['father'] = request.json.get('father', file[0]['father'])
    return jsonify({'file': file[0]})
@app.route('/logFile')
def hello_log():
    return 'This is log files pages'
@app.route('/logFiles', methods=['GET'])
def get_log_files():
    return jsonify({'logFiles': logFiles})
@app.route('/logFile_read/<int:file_id>', methods=['GET'])
def get_log(file_id):
    file = list(filter(lambda t: t['id'] == file_id, logFiles))
    if len(file) == 0:
        abort(404)
    return jsonify({'file': file[0]})
@app.route('/logFile_delete/<int:file_id>', methods=['GET', 'DELETE'])
def delete_log(task_id):
    file = list(filter(lambda t: t['id'] == task_id, logFiles))
    if len(file) == 0:
        abort(404)
    logFiles.remove(file[0])
    return jsonify({'result': True})
@app.route('/logFile_del')
def del_log():
    logTextFile1.__delete__()
    return jsonify({'result': True})
###################################################
@app.route('/dir_create/directories', methods=['POST'])
def create_dir():
    if not request.json or not 'dirName' in request.json:
        abort(400)
    dir = {
        'id': directories[-1]['id'] + 1,
        'dirName': request.json['dirName'],
        'maxElements': bufFiles[-1]['id'] - 5,
        'father': None
    }
    directories.append(dir)
    return jsonify({'dir': dir}), 201
@app.route('/dir_move/<int:dir_id>', methods=['PUT'])
def update_dir(dir_id):
    dir = list(filter(lambda t: t['id'] == dir_id, directories))
    if len(dir) == 0:
        abort(404)
    if not request.json:
        abort(400)
    dir[0]['dirName'] = request.json.get('dirName', dir[0]['dirName'])
    dir[0]['maxElements'] = request.json.get('maxElements', dir[0]['maxElements'])
    dir[0]['father'] = request.json.get('father', dir[0]['father'])
    return jsonify({'dir': dir[0]})
@app.route('/directory')
def hello_dir():
    return 'This is directory pages'
@app.route('/directories', methods=['GET'])
def get_dirs():
    return jsonify({'directories': directories})
@app.route('/dir_read/<int:dir_id>', methods=['GET'])
def get_dir(dir_id):
    dir = list(filter(lambda t: t['id'] == dir_id, directories))
    if len(dir) == 0:
        abort(404)
    return jsonify({'task': dir[0]})
@app.route('/dir_delete/<int:dir_id>', methods=['GET', 'DELETE'])
def delete_dir(dir_id):
    dir = list(filter(lambda t: t['id'] == dir_id, directories))
    if len(dir) == 0:
        abort(404)
    directories.remove(dir[0])
    return jsonify({'result': True})
@app.route('/dir_del')
def del_dir():
    root.__delete__()
    return jsonify({'result': True})
########################################################
@app.route('/bufFile_create/bufFiles', methods=['POST'])
def create_buf():
    if not request.json or not 'fileName' in request.json:
        abort(400)
    file = {
        'id': bufFiles[-1]['id'] + 1,
        'fileName': request.json['fileName'],
        'maxSize': bufFiles[-1]['id'] + 5,
        'father': None
    }
    bufFiles.append(file)
    return jsonify({'task': file}), 201
@app.route('/bufFile_move/<int:file_id>', methods=['PUT'])
@app.route('/bufFile_push/<int:file_id>', methods=['PUT'])
@app.route('/bufFile_consume/<int:file_id>', methods=['PUT'])
def update_buf(file_id):
    file = list(filter(lambda t: t['id'] == file_id, bufFiles))
    if len(file) == 0:
        abort(404)
    if not request.json:
        abort(400)
    file[0]['fileName'] = request.json.get('fileName', file[0]['fileName'])
    file[0]['maxSize'] = request.json.get('maxSize', file[0]['maxSize'])
    file[0]['father'] = request.json.get('father', file[0]['father'])
    return jsonify({'file': file[0]})
@app.route('/bufFile')
def hello_buf():
    return 'This is buf files pages'
@app.route('/bufFiles', methods=['GET'])
def get_buf_files():
    return jsonify({'bufFiles': bufFiles})
@app.route('/bufFile_read/<int:file_id>', methods=['GET'])
def get_buf(file_id):
    file = list(filter(lambda t: t['id'] == file_id, bufFiles))
    if len(file) == 0:
        abort(404)
    return jsonify({'file': file[0]})
@app.route('/bufFile_delete/<int:task_id>', methods=['GET', 'DELETE'])
def delete_buf(task_id):
    file = list(filter(lambda t: t['id'] == task_id, bufFiles))
    if len(file) == 0:
        abort(404)
    bufFiles.remove(file[0])
    return jsonify({'result': True}), 302
@app.route('/bufFile_del')
def del_buf():
    bufferFile1.__delete__()
    return jsonify({'result': True}), 201
if __name__ == '__main__':
    app.run(debug=True)