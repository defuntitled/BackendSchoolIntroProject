import flask
from flask import Flask, request, make_response
from service.db.db_session import global_init
from service.app.item_finder import get_item_by_id
from service.app.item_adder import import_items
from service.app.item_deletter import delete_item_by_id
import sys

sys.path.append('path')

app = Flask(__name__)
database_loaded = False


def bad_answer(code: int, message: str):
    return {
               "code": code,
               "message": message
           }, str(code)


@app.route('/nodes/<string:id>', methods=["GET"])
def get_node(id: str):
    global database_loaded
    if not database_loaded:
        global_init("db\\nodes.sqlite3")
        database_loaded = True
    res = get_item_by_id(id)
    if not res:
        flask.abort(404)
    else:
        return res, "200"


@app.route('/imports', methods=["POST"])
def import_nodes():
    global database_loaded
    if not database_loaded:
        global_init("db\\nodes.sqlite3")
        database_loaded = True
    if not request.json:
        flask.abort(400)
    try:
        content = request.json
    except:
        flask.abort(400)
    res = import_items(content)
    if res:
        return "200"
    else:
        flask.abort(400)


@app.route("/delete/<string:id>", methods=["DELETE"])
def delete_node(id):
    global database_loaded
    if not database_loaded:
        global_init("db\\nodes.sqlite3")
        database_loaded = True
    res = delete_item_by_id(id)
    if not res:
        flask.abort(404)
    return "200"


@app.errorhandler(400)
def ret_val_err():
    return bad_answer(400, "Validation Failed")


@app.errorhandler(404)
def ret_val_err():
    return bad_answer(404, "Item not found")


if __name__ == '__main__':
    if not database_loaded:
        global_init("db\\nodes.sqlite3")
        database_loaded = True
    app.run()
