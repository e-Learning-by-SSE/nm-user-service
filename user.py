from models.UserRepo import UserRepo
from schemas.schemas import UserSchema
from flask import request

userRepo = UserRepo()
userSchema = UserSchema()
userListSchema = UserSchema(many=True)
USER_NOT_FOUND = "User not found for id: {}"


def get(id):
    user_data = userRepo.fetchById(id)
    if user_data:
        return userSchema.dump(user_data)
    return {'message': USER_NOT_FOUND.format(id)}, 404

def update(id):
    user_data = userRepo.fetchById(id)
    user_req_json = request.get_json()
    if user_data:
        user_data.name = user_req_json['name']
        userRepo.update(user_data)
        return userSchema.dump(user_data)
    return {'message': USER_NOT_FOUND.format(id)}, 404

def delete(id):
    user_data = userRepo.fetchById(id)
    if user_data:
        userRepo.delete(id)
        return {'message': 'Item deleted successfully'}, 200
    return {'message': USER_NOT_FOUND.format(id)}, 404

def create():
    user_req_json = request.get_json()
    user_data = userSchema.load(user_req_json)
    userRepo.create(user_data)
    return userSchema.dump(user_data),201

def getAll():
    return userListSchema.dump(userRepo.fetchAll()), 200
    