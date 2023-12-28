from __init__ import app
from flask import render_template
from models import User,Categoria,Post,PostCategoria,Tag,TipoPostagem

@app.route('/')
def page_home():
    teste = User.query.all()
    return render_template("index.html", teste=teste)

@app.route('/telaeditor')
def tela_editor():
    categorias = Categoria.query.all()
    return render_template("telaeditor.html", categorias=categorias)

@app.route('/tela_editor/processar_edicao', methods =['POST'])
def processar_edição():
    return print(f'ok')

@app.route('/login', methods=['POST'])
def login():
    teste = forms.request
    return render_template('login.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')