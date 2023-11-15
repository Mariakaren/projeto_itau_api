from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

usuarios = []
user_id = 1
class Pessoa:
    def __init__(self, id, nome_completo, data_nascimento, endereco, cpf, estado_civil):
        self.id = id
        self.nome_completo = nome_completo
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        self.cpf = cpf
        self.estado_civil = estado_civil

    def __str__(self):
        return f"Nome: {self.nome_completo}\nData de Nascimento: {self.data_nascimento}\nEndereço: {self.endereco}\nCPF: {self.cpf}\nEstado Civil: {self.estado_civil}"

@app.route('/', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        global user_id
        nome_completo = request.form['nome_completo']
        data_nascimento = request.form['data_nascimento']
        endereco = request.form['endereco']
        cpf = request.form['cpf']
        estado_civil = request.form['estado_civil']

        usuario = Pessoa(user_id, nome_completo, data_nascimento, endereco, cpf, estado_civil)
        user_id += 1 
        usuarios.append(usuario)

    return render_template('template.html')

@app.route('/atualizar/<int:user_id>', methods=['GET', 'POST'])
def atualizar_usuario(user_id):
    if request.method == 'POST':
        
        nome_completo = request.form['nome_completo']
        data_nascimento = request.form['data_nascimento']
        endereco = request.form['endereco']
        cpf = request.form['cpf']
        estado_civil = request.form['estado_civil']

        for usuario in usuarios:
            if usuario.id == user_id:
                usuario.nome_completo = nome_completo
                usuario.data_nascimento = data_nascimento
                usuario.endereco = endereco
                usuario.cpf = cpf
                usuario.estado_civil = estado_civil
                break

        return redirect(url_for('lista_usuarios'))

    user_to_modify = next((user for user in usuarios if user.id == user_id), None)
    if user_to_modify:
        return render_template('atualizar.html', usuario=user_to_modify)
    else:
        return "Usuário não encontrado."


@app.route('/excluir/<int:user_id>', methods=['GET'])
def excluir_usuario(user_id):
    global usuarios  
    usuarios = [usuario for usuario in usuarios if usuario.id != user_id]
    return redirect(url_for('lista_usuarios'))


@app.route('/lista')
def lista_usuarios():
    return render_template('lista.html', usuarios=usuarios)

if __name__ == "__main__":
    app.run(debug=True)