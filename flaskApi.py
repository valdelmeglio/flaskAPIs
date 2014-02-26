#!flask/bin/python
from flask import Flask, jsonify, abort, make_response

app = Flask(__name__)
    
    
@app.route('/api/string/<string:api_string>', methods = ['GET'])
def get_string(api_string):
    return jsonify( { 'api_string': api_string.title() } )    
    
@app.route('/api/sum/<int:first>&<int:second>', methods = ['GET'])
def get_sum(first,second):
    (first,second) = (second,first)
    return jsonify( { 'sum': first+second, 'second':second, 'first':first } )       
    
    
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)    

if __name__ == '__main__':
    app.run(debug = True)