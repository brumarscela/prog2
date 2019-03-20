from flask import Flask , render_template

app = Flask(__name__) #, static_url_path = '/ static')

@app.route("/")
def inicio():
    return render_template ("Inicio.html")

@app.route("/listarpessoa")
def listarPessoas():
    lista = ["a","b"]
    return render_template ("ListarPessoa.html", geral=lista)
    
@app.route("/inserirpessoa")
def inserirPessoas():
    return render_template ("InserirPessoa.html")

@app.route("/alterarpessoa")
def alterarPessoa():
    return render_template ("AlterarPessoa.html")

@app.route("/exibirmensagem")
def exibirMensagem():
    return render_template ("ExibirMensagem.html")

app.run(debug=True)