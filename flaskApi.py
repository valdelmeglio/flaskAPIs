#!flask/bin/python
from flask import Flask, jsonify, make_response
import re

app = Flask(__name__)
    
# The title() method for a string like "we're paolo's friends"
# would give back "We'Re Paolo'S Friends". This method, for 
# the same string returns "We're Paolo's Friends"
def titlecase(s):
    return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
                       lambda mo: mo.group(0)[0].upper() +
                              mo.group(0)[1:].lower(),
                s)
    
    
    
# First API. It takes a string and return it back in 
# Json format (using jsonify) with the first letter  
# of each word capitalized.
@app.route('/api/string/<string:api_string>', methods = ['GET'])
def get_string(api_string): 
     return jsonify( { 'api_string': titlecase(api_string) } )
     
     
# Second API. It takes two numbers, swap them
# and returns them swapped with their sum     
@app.route('/api/sum/<int:first>&<int:second>', methods = ['GET'])
def get_sum(first,second):
    (first,second) = (second,first)
    return jsonify( { 'sum': first+second, 'second':second, 'first':first } )       
    
# Error handler. This method will  
# be called for every API wrong call    
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)    

if __name__ == '__main__':
    app.run(debug = True)