<!DOCTYPE html>
<html>
<head>
	<title>Listar Pessoas</title>
</head>
<body background="/static/background.gif">
<button><a href="/inserirpessoa">Inserir Pessoa</a></button>

<center><p>----------------------------------------</p>
<h3>Listagem de pessoas:</h3>
<p>----------------------------------------</p></center>
<br>
<p>----------x----------x----------x----------</p>

{%for i in geral:%}
	{{i.nome}}
{%endfor%}


<p>Bruna Marcelinha</p>
<form action="/exibirmensagem"><input type="submit" value="Deletar">
</form> 
<form action="/alterarpessoa"><input type="submit" value="Alterar">
</form> 
<p>----------x----------x----------x----------</p>
<p>Múcio Afofadinho</p>
<form action="/exibirmensagem"><input type="submit" value="Deletar">
</form> 
<form action="/alterarpessoa"><input type="submit" value="Alterar">
</form> 
<p>----------x----------x----------x----------</p>
<p>Tiago Lindinho</p>
<form action="/exibirmensagem"><input type="submit" value="Deletar">
</form> 
<form action="/alterarpessoa"><input type="submit" value="Alterar">
</form> 
<p>----------x----------x----------x----------</p>

</body>
</html>