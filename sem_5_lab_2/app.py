from flask import Flask
from flask import jsonify, request, abort
from binaryFile import BinaryFile, InvalidPathError
from bufferFile import BufferFile, InvalidPathError
from directory import Directory, InvalidPathError
from logTextFile import LogTextFile, InvalidPathError
import json
app = Flask(__name__)
binaryFile1 = BinaryFile('binFile1', 'info1')
bufferFile1 = BufferFile('bufFile1', 5)
root = Directory('root', 100)
logTextFile1 = LogTextFile('logtext1', 'jibiub', root)

@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'This is lab2'
    a = response.status_code
    print(a)
@app.route('/binaryFile')
def hello_bin():
    return 'This is binary files pages'
@app.route('/binaryFile_read/<string:fileName>', methods=['GET'])
def get_bin_file():
    a = binaryFile1.read()
    try:
        return jsonify({'info': a})
    except InvalidPathError as err:
        abort(400, err)
@app.route('/binaryFile_delete/<string:name>', methods=['DELETE'])
def delete_bin_file():
    try:
        binaryFile1.__delete__()
        return jsonify({'result': True})
    except InvalidPathError as err:
        abort(400, err)
@app.route('/binaryFile_create', methods=['POST'])
def create_bin_file():
    binaryFile2 = BinaryFile.__init__('binary2', 'info')
    return jsonify({'result': True})
@app.route('/binaryFile_move/<string:name>', methods=['PUT'])
def move_bin_file(path):
    pass
@app.route('/bufferFile')
def hello_buf():
    return 'This is buffer files pages'
@app.route('/bufferFile_read/<string:fileName>', methods=['GET'])
def get_buffer_file():
    pass
@app.route('/bufferFile_delete/<string:name>', methods=['DELETE'])
def delete_buffer_file():
    pass
@app.route('/bufferFile_create', methods=['POST'])
def create_buffer_file():
    bufferFile2 = BufferFile.__init__('binary2', 5)
    return jsonify({'result': True})
@app.route('/bufferFile_move/<string:name>', methods=['PUT'])
def move_buf(path):
    pass
@app.route('/bufferFile_push/<string:name>')
def push():
    pass
@app.route('/bufferFile_consume/<string:name>')
def consume():
    pass
@app.route('/durectory')
def hello_dir():
    return 'This is directory pages'
@app.route('/directory_list_el/', methods=['GET'])
def get_list_el():
    pass
@app.route('/directory_delete/<string:name>', methods=['DELETE'])
def delete_dir():
    pass
@app.route('/directory_create', methods=['POST'])
def create_dir():
    directory2 = Directory.__init__('binary2', 50, root)
    return jsonify({'result': True})
@app.route('/directory_move/<string:name>', methods=['PUT'])
def move_dir(path):
    pass
@app.route('/logtextFile')
def hello_log():
    return 'This is logtext files pages'
@app.route('/logTextFile_read/<string:fileName>', methods=['GET'])
def get_logtext_file():
    pass
@app.route('/logTextFile_delete/<string:name>', methods=['DELETE'])
def delete_logtext_file():
    pass
@app.route('/logtextFile_create', methods=['POST'])
def create_logtext_file():
    logTextFile2 = LogTextFile.__init__('lgtxt2', 'kfncn')
    return jsonify({'result': True})
@app.route('/logtextFile_append/<string:name>', methods=['PUT'])
def append(newLine):
    pass



if __name__ == '__main__':
    app.run(debug=True)