from flask import Flask, request, jsonify

app = Flask(__name__)

users = [
    {"id": 1, "name": "Kim"},
    {"id": 2, "name": "Lee"}
]

# GET: 전체 사용자 조회
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

# GET: 특정 사용자 조회
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# POST: 사용자 생성
@app.route("/users", methods=["POST"])
def create_user():
    new_user = request.json
    users.append(new_user)
    return jsonify(new_user), 201

# PUT: 전체 사용자 수정
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    new_data = request.json
    for i, user in enumerate(users):
        if user["id"] == user_id:
            users[i] = {"id": user_id, **new_data}
            return jsonify(users[i])
    return jsonify({"error": "User not found"}), 404

# DELETE: 사용자 삭제
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    global users
    users = [u for u in users if u["id"] != user_id]
    return jsonify({"message": "Deleted"})

if __name__ == "__main__":
    app.run(debug=True)