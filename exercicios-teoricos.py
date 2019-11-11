"""

58.

{
  [
   "planta" : {

      "nome" : "Anis",
      "nome cientifico" : "Pimpinella anisum",
      "tamanho folha" : "Média",
      "periodo poda" : "90 dias",

   }

   "jardim" : {

       "local" : "IFC"

   }


   "plantadojardim" : {

       "data plantio" : "11/11/2019",

   }


   "planta" : {

         "nome" : "Hortelã",
         "nome cientifico" : "Mentha spicata",
         "tamanho folha" : "Pequena",
         "periodo poda" : "90 dias",

      }

      "jardim" : {

         "local" : "Jardim da Prefeitura"

      }


      "plantadojardim" : {

          "data plantio" : "11/11/2019",

      }
  ]
}



59. Associe as colunas que descrevem funcionalidades de acordo com os códigos disponíveis a
seguir:

(a) $('#tabela_pessoas').append(cabecalho);
(b) $var nome = $("#nome").val();
(c) var dados = JSON.stringify({ nome: nome, endereco: end, telefone: tel })-
(d) $("#success").fadeIn(1000);-
(e) var eu = $(this).attr('id');-
(f) var deu_certo = resultado.message == "ok"-

(b) obtém o identificador de um componente que foi acionado por um evento, atribuindo
essa identificação a uma variável.
(e) localiza um componente que tabula pessoas e adiciona o conteúdo de uma variável ao
interior desse componente.
(c) atribui o conteúdo de variáveis e seus respectivos valores a outra variável, fazendo uso
de um formato específico de dados em modo texto.
(f) atribui o resultado de uma expressão lógica a uma variável.
(d) faz um componente tornar-se visível na tela paulatinamente.
(a) atribui o conteúdo de um componente a uma variável.

60. Descreva qual é o objetivo do comando abaixo. A seguir, numere em que sequência ocorrem
as ações realizadas pelos comandos existentes nessa linha.
pessoas = list(map(model_to_dict, Pessoa.select()))

O objetivo do comando é captar as ocorrências do banco de dados, mudar seu valor de model para dictionary e aplicar esse tratamento para todas as ocorrências. Depois, com o list, organizar os dados.

(3) A lista é percorrida e um procedimento específico é aplicado a cada objeto da classe
Pessoa. Esse procedimento se chama: mapeamento.
(2) O resultado da aplicação do procedimento específico na lista de objetos é convertido
para uma lista.
(1) Obtém-se uma lista de objetos da classe Pessoa. Tal lista é obtida por meio de um
método chamado select.

61. A ação do backend que altera os dados de uma pessoa realiza uma sequência de passos bem
definida. Enumere as ações descritas a seguir:

(4) Executa o comando para atualizar efetivamente o objeto no banco de dados.
(1) Recebe os dados da requisição, convertendo-os a partir do formato de envio (no caso,
json).
(3) Define para o objeto os novos valores (com exceção do identificador), recebidos da
requisição.
(5) Retorna para o emissor da requisição a resposta da requisição.
(2) Obtém o objeto a ser modificado, a partir do identificador do mesmo.""