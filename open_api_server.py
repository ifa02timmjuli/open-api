
"""
OPEN-API Julian Timmer

Requirements:
* flask
"""

import uuid 

from flask import Flask, request, jsonify, abort


# initialize Flask server
app = Flask(__name__)

# create unique id for lists, users, entries
user_id_bob = uuid.uuid4()
user_id_alice = uuid.uuid4()
user_id_eve = uuid.uuid4()
todo_list_1_id = '1318d3d1-d979-47e1-a225-dab1751dbe75'
todo_list_2_id = '3062dc25-6b80-4315-bb1d-a7c86b014c65'
todo_list_3_id = '44b02e00-03bc-451d-8d01-0c67ea866fee'
entry_1_id = uuid.uuid4()
entry_2_id = uuid.uuid4()
entry_3_id = uuid.uuid4()
entry_4_id = uuid.uuid4()

# define internal data structures with example data
user_list = [
    {'id': user_id_bob, 'name': 'Bob'},
    {'id': user_id_alice, 'name': 'Alice'},
    {'id': user_id_eve, 'name': 'Eve'},
]
todo_lists = [
    {'id': todo_list_1_id, 'name': 'Einkaufsliste'},
    {'id': todo_list_2_id, 'name': 'Arbeit'},
    {'id': todo_list_3_id, 'name': 'Privat'},
]
entries = [
    {'id': entry_1_id, 'name': 'Milch', 'description': '', 'list': todo_list_1_id, 'user': user_id_bob},
    {'id': entry_2_id, 'name': 'Arbeitsblätter ausdrucken', 'description': '', 'list': todo_list_2_id, 'user': user_id_alice},
    {'id': entry_3_id, 'name': 'Kinokarten kaufen', 'description': '', 'list': todo_list_3_id, 'user': user_id_eve},
    {'id': entry_4_id, 'name': 'Eier', 'description': '', 'list': todo_list_1_id, 'user': user_id_eve},
]

# add some headers to allow cross origin access to the API on this server, necessary for using preview in Swagger Editor!
@app.after_request
def apply_cors_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST,DELETE'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

# define endpoint for getting and deleting existing todo lists
@app.route('/todo-list/<list_id>', methods=['GET', 'DELETE'])
def handle_list(list_id):
    # find todo list depending on given list id
    list_item = None
    for l in todo_lists:
        if l['id'] == list_id:
            list_item = l
            break
    # if the given list id is invalid, return status code 404
    if not list_item:
        abort(404)
    if request.method == 'GET':
        # find all todo entries for the todo list with the given id
        print('Returning todo list...')
        return jsonify([i for i in todos if i['list'] == list_id])
    elif request.method == 'DELETE':
        # delete list with given id
        print('Deleting todo list...')
        todo_lists.remove(list_item)
        return '', 200

# define endpoint for adding a new list
@app.route('/todo-list', methods=['POST'])
def add_new_list():
    # make JSON from POST data (even if content type is not set correctly)
    new_list = request.get_json(force=True)
    print('Got new list to be added: {}'.format(new_list))
    # create id for new list, save it and return the list with id
    new_list['id'] = uuid.uuid4()
    todo_lists.append(new_list)
    return jsonify(new_list), 200

# define endpoint for adding entry to list
@app.route('/todo-list/<list_id>/entry', methods=['POST'])
def add_new_entry(list_id):
    # make JSON from POST data (even if content type is not set correctly)
    new_entry = request.get_json(force=True)
    print('Got new entry to be added: {}'.format(new_entry))
    # create id for new entry, save it and return the list with the new entry with id
    new_entry['id'] = uuid.uuid4()
    # append to list
    new_entry['list'] = list_id
    entries.append(new_entry)
    return '', 200

# define endpoint to manipulate entry
@app.route('/todo-list/<list_id>/entry/<entry_id>', methods=['PUT', 'DELETE'])
def manipulate_entry(list_id, entry_id):
    entry_item = None
        for l in entries:
            if l['id'] == entry_id:
                entry_item = l
                break
    if request.method == 'PUT':
        new_entry_data = request.get_json(force=True)
        entry_item['name'] = new_entry_data['entry']['name']
        entry_item['description'] = new_entry_data['entry']['description']
        return '', 200
    elif request.method == 'DELETE':
        entries.remove(entry_item)
        return '', 200

# define endpoint for adding user and getting list of users
@app.route('/user', methods=['GET', 'POST'])
def handle_user():
    # make JSON from POST data (even if content type is not set correctly)
    new_user = request.get_json(force=True)
    if request.method == 'POST':
        print('Got new user to be added: {}'.format(new_user))
        new_user['id'] = uuid.uuid4()
        user_list.append(new_user)
        return jsonify(new_user), 200
    elif request.method == 'GET':
        return jsonify(user_list)
        
# define endpoint for adding and getting user
@app.route('/user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user_item = None
    for l in user_list:
        if l['id'] == user_id:
            user_item = l
            break
    print('Deleting user...')
    user.remove(user_item)
    return '', 200

if __name__ == '__main__':
    # start Flask server
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
