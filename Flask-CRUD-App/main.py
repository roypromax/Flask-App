from flask import Flask, jsonify, request
import json

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home_route():
    return jsonify("Welcome to the menu app.")


@app.route("/create", methods=["POST"])
def create_route():
    new_menu_item = request.get_json()

    if "name" not in new_menu_item or "price" not in new_menu_item:
        return jsonify({"error": "Invalid menu item data"}), 400

    with open("menu_items.json", "r") as file:
        menu = json.load(file)

    for item in menu:
        if item["name"] == new_menu_item["name"]:
            return {"error": "Item already exists in the menu"}, 400

    menu.append(new_menu_item)

    with open("menu_items.json", "w") as file:
        json.dump(menu, file)

    return jsonify({"message": "Menu item created successfully"}), 201


@app.route("/read", methods=["GET"])
def read_route():
    with open("menu_items.json", "r") as file:
        menu = json.load(file)

    return jsonify(menu), 200


@app.route("/update", methods=["PATCH"])
def update_route():
    menu_item = request.get_json()

    if "name" not in menu_item or "price" not in menu_item:
        return jsonify({"error": "Invalid menu item data"}), 400

    with open("menu_items.json", "r") as file:
        menu = json.load(file)

    item_exists = False
    for item in menu:
        if item["name"] == menu_item["name"]:
            item_exists = True
            item["price"] = menu_item["price"]
            break

    if item_exists == False:
        return jsonify({"error": "Menu item not found"}), 404

    with open("menu_items.json", "w") as file:
        json.dump(menu, file)

    return jsonify({"message": "Price of item has been updated"}), 200


@app.route("/delete", methods=["DELETE"])
def delete_route():
    menu_item = request.get_json()

    if "name" not in menu_item:
        return jsonify({"error": "Invalid menu item data"}), 400

    with open("menu_items.json", "r") as file:
        menu = json.load(file)

    item_exists = False
    for item in menu:
        if item["name"] == menu_item["name"]:
            item_exists = True
            menu.remove(item)
            break

    if item_exists == False:
        return jsonify({"error": "Menu item not found"}), 404

    with open("menu_items.json", "w") as file:
        json.dump(menu, file)

    return jsonify({"message": f"{menu_item['name']} has been deleted from the menu"}), 201


if __name__ == "__main__":
    app.run(port=8080)
