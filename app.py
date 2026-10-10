from flask import Flask, Response, request
from  flask_sqlalchemy import SQLAlchemy
import  mysql.connector
import json

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://root:@localhost/database'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(120))

    def to_json(self):
        return {'id': id,
                'name': name,
                'email': email}
# db.create_all() melhor usar no terminal, na cli escreva python e cole esse trecho e rode

# Selecionar tudo
@app.route('/user', methods=['GET'])
def select_user():
    users_object = User.query.all()
    user_json = [user.to_json() for user in users_object]

    return generete_response(200, 'users', user_json, 'Ok')

# Selecionar um
@app.route('/user/<id>', methods=['GET'])
def select_user_id(id):
    user_object = User.query.filter_by(id=id).first()
    user_json = user_object.to_json()

    return generete_response(200, 'user', user_json)

# Cadastrar
@app.route('/user/', methods=['POST'])
def make_user():
    body = request.get_json()
    #para validar se veio parametros, vou usar um try catch para gerar erro
    try:
        user = User(name=body['name']), email = body['email'])
        db.session.add(user)
        db.session.commit()
        return generete_response(201, 'user', user.to_json(), 'Criado com sucesso')
    except Exception as e:
        print(e)
        return generete_response(400, 'user', {}, 'Erro ao se cadastrar')

# Atualizar
@app.route('/user/<id>', methods=['PUT'])
def update_user(id):
    #para pegar o usuario
    user_object = User.query.filter_by(id=id).first()
    #para pegar as modificacoes
    body = request.get_json()
    try:
        if('name' in body):
            user_object.name = body['name']
        if ('email' in body):
            user_object.email = body['email']

        db.session.add(user_object)
        db.session.commit()
        return generete_response(200, 'user', user.to_json(), 'Atualizado com sucesso')
    except Exception as e:
        print(e)
        return generete_response(400, 'user', {}, 'Erro ao se atualizar')


# Deletar
@app.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
    user_object = User.query.filter_by(id=id).first()

    try:
        db.session.delete(user_object)
        db.commit()
        return generete_response(200, 'user', user.to_json(), 'Deletado com sucesso')
    except Exception as e:
        print(e)
        return generete_response(400, 'user', {}, 'Erro ao se deletar')


def generete_response(status, content_name, content, message=False):
    body = {}
    body[content_name] = message

    if(message):
        body['message'] = message
        return Response(json.dumps(body), status=status, minetype='application/json')




app.run()