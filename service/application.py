from flask import Flask, request, make_response
from service.db.db_session import global_init
from service.app.item_finder import get_item_by_id
from service.app.item_adder import import_items
from service.app.item_deletter import delete_item_by_id
import os

app = Flask(__name__)


def bad_answer(code: int, message: str):
    return {
               "code": code,
               "message": message
           }, str(code)


@app.route('/nodes/<string:id>', methods=["GET"])
def get_node(id: str):
    res = get_item_by_id(id)
    if not res:
        return bad_answer(404, "Item not found")
    else:
        return res, "200"


@app.route('/imports', methods=["POST"])
def import_nodes():
    if not request.json:
        return bad_answer(400, "Validation Failed")
    content = request.json
    res = import_items(content)
    if res:
        return "200"
    else:
        return bad_answer(400, "Validation Failed")


@app.route("/delete/<string:id>", methods=["DELETE"])
def delete_node(id):
    res = delete_item_by_id(id)
    if not res:
        return bad_answer(404, "Item not found")
    return "200"


if __name__ == '__main__':
    global_init("db\\nodes.sqlite3")
    app.run()
