# MyEnterprise


Protegido por a CC License (ver ficheiro 'LICENCE')

Este software está protegido com a Creative Commons Licence, e poderá ser usado, editado e alterado por qualquer individuo ou organização desde que os direitos sejam sempre atribuidos ao autor , e qualquer mudança ou alteração deverá sempre fazer referencia ao mesmo.

Dou assim permissão a qualquer endividuo ou organização o uso e alteração deste sofware com base na licença mencionada em cima.

Esta aplicação tem como função armazenadar no seu dispositovo um registo de contactos (pessoas) , trabalhadores da empresa, novos candidatos a postos de trabalho na empresa, e pessoas que ocupam cargos de chefia na empresa. Tem a funçao que guardar curriculos de trabalhadores, managers, e candidatos (deverão ser guardados numa pasta á sua escolha e carregar na aplicação) como tambem de abri-los diretamente da aplicação.


Campos de cada classe de registo :

Pessoas:

- Nome - tipo texto
- Idade - tipo numérico
- Morada - tipo texto
- telefone/telemvel - tipo numérico
- Email - tipo texto
- Rede Social - tipo texto
- País - tipo texto
- Nacionalidade - tipo texto
- Documento identificação - tipo numerico
- Numero Fiscal - tipo numérico


Manager:

- (os mesmos que pessoa)
- Trabalho - tipo texto
- Salário - tipo decimal
- Data Inicio - tipo texto
- Data Fim - tipo texto
- Curriculum Vitae - exclisivamente .pdf

Empregado:

- (os mesmos que Manager)

Candidatos:

- (os mesmos que Pessoas)
- Data atual
- Posto de trabalho a que se aplica
- Curriculum Vitae
- Estado da candidatura

Icons:

- https://www.flaticon.com

- https://icons8.com

Intruções:

- O campo 'key' deverá ser intruduzido em texto e deverá estar entre aspas, este campo é o valor associado a cada registo e deverá ser diferente para cada um dos registos:
    - exemplo:
        - se quiser defenir o campo 'key' para nome deverá intruduzir: 'nome'

- Todos os campos restantes têm o seu tipo defenido e poderá adicionar os valores que quiser sem usar as aspas.

- Os curriculos devem estar no formato .pdf

- Deve (não obrigatorio) criar uma pasta onde guarda todos os curriculos, o programa encarrega-se 
de criar uma ligação para os mesmos, se o curriculo for apagado a plicação irá informar um erro, deve fornecer um curriculo novo usando o botão 'Selecionar Curriculo'.

