<!DOCTYPE html>
<html>
<head>
<title>Curso</title>
</head>
<body>


#ABRIR PÁGINA PARA ESCOLHER CURSO - eletro ou info

{% for pessoa in lista : %}
{{ pessoa.nome }} | {{ pessoa.endereco }} | {{ pessoa. telefone }}
<a href=/ excluir pessoa ?nome={{ pessoa.nome }}>Excluir</a><br>
{% endfor %}



</body>
</html>