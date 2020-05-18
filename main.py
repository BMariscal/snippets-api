import logging

from flask import Flask, abort, jsonify, request, render_template

from controllers import create_snippet, get_snippet, update_snippet


app = Flask(__name__)

@app.route("/")
def index():
  return jsonify({"message": "Hello!"})

@app.route("/snippets" , methods=['POST'])
def create_snippet_entity():
  request_data = request.get_json()
  process_snippet = create_snippet.create(request_data)
  return jsonify(process_snippet)


@app.route("/snippets/like" , methods=['PUT'])
def update_snippet_entity():
  request_data = request.get_json()
  try:
    name = request_data["name"]
  except KeyError:
    abort(400)
    return

  process_snippet = update_snippet.update(name)
  return jsonify(process_snippet)

@app.route("/snippets/<string:name>" , methods=['GET'])
def get_snippet_entity(name):
  if not name:
    abort(400)
    return 

  try:
    logging.info("Fetching {}".format(name))
    fetch_snippet = get_snippet.fetch(name)
    print(fetch_snippet)
  except:
    abort(404)
    return
      
  return jsonify (fetch_snippet)


app.run(host='0.0.0.0', debug=True, port=8080)