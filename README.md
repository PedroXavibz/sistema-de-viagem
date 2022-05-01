# Sistema de Marcação de Consulta Médica


###### Obs: Os dados precisarão ser persistidos em arquivo físico JSON

A aplicação se divide em três partes na qual cada uma irá ter uma responsabilidade específica, estas três partes são divididas em:

- __Model__ (Irá escrever e modificar os dados persistidos no arquivo JSON).
- __View__ (Exibição dos dados, para o usuário).
- __Controller__ (Manipular a entrada de dados do usuario, será responsável por interligar o view e model).

##### Estrutura de pasta
```
projeto/
    model.py
    controller.py
    data/
        paciente.json
        consulta.json
        medico.json
        funcionario.json
        clinica.json
    views/
        view.py
        pacienteView.py
        clinicaView.py
        funcionarioView.py
        medicoView.py
        consultaView.py
```

## Views


###### Nome do arquivo: view.py


* O view terá um **menu principal** no qual irá exibir todas as funcionalidades que a aplicação possui.
* Para cada funcionalidade um menu especifíco para ela será criado, são eles o menu de __paciente__, __marcação de consulta__, __médico__, __funcionário__ e __clínica__.

O menu de principal deverá exibir as seguintes funcionalidades:

1. __Menu de Paciente__
1. __Menu de Marcação de Consulta__
1. __Menu de Médico__
1. __Menu de Funcionário__
1. __Menu de Clínica__

#### Menu paciente

###### nome do arquivo: pacienteView.py

O menu de paciente deverá exibir as seguintes funcionalidades:

1. Cadastrar paciente
1. Buscar paciente por CPF
1. Editar dados do paciente (Somente quando, após a busca e seleção do mesmo)
1. Remover paciente (Somente quando, após a busca e seleção do mesmo)
1. Listar todos os pacientes
1. Sair

#### Menu consulta

###### nome do arquivo: consultaView.py

O menu de consulta deverá exibir as seguintes funcionalidades:

1. Marcar consulta
1. Buscar consulta por paciente
1. Editar consulta (Somente quando, após a busca e seleção do mesmo)
1. Remover consulta (Somente quando, após a busca e seleção do mesmo)
1. Listar consultas
1. Listar consultas por retorno
1. Listar consultas por intervalo de data
1. Sair

#### Menu médico

###### nome do arquivo: medicoView.py

O menu de médico deverá exibir as seguintes funcionalidades:

1. Marcar consulta
1. Cadastrar médico
1. Buscar médico por CRM
1. Editar médico (Somente quando, após a busca e seleção por CRM)
1. Remover médico
1. Listar todos os médicos
1. Pesquisar médico por especialidade
1. Sair

#### Menu funcionário

###### nome do arquivo: funcionarioView.py

O menu de funcionário deverá exibir as seguintes funcionalidades:

1. Cadastrar funcionário
1. Buscar funcionário por matrícula
1. Editar funcionário (Somente quando, após a busca e seleção por matrícula)
1. Remover funcionário
1. Listar todos os funcionários
1. Sair

#### Menu clínica

###### nome do arquivo: funcionarioView.py

O menu de clínica deverá exibir as seguintes funcionalidades:

1. Cadastrar clínica
1. Buscar clínica por CNPJ
1. Editar clínica
1. Remover clínica
1. Listar todas as clínicas
1. Sair

## Model

###### nome do arquivo: model.py

* Os dados irão ser armazenados em arquivos __JSON__, no qual serão lidos e escritos.
* Este arquivo só poderá ser acessado pelo __controller.py__.
* Não permitir duplicidade de dados.
* Exigir confirmação de exclusão de dados.

##### loadData(fileName)
Esta função é responsável por ler os dados dos arquivos __JSON__ e retorna-los em forma de um __dicionário__ no qual serão armazenados na variável global __tmpDict__, usando como base o __nome do arquivo__, passado como argumento. Essa função será invocada toda vez que um menu for selecionado e a variável __tmpDic__ resetada, para realocar um novo dado.

*__Argumentos Permitidos__*
- paciente 
- consulta
- medico
- funcionario
- clinica

##### loadDataById(id)
Esta função é responsável por ler dados específicos com base no seu __id__, armazenados temporariamente na variável global __tmpDict__. e armenar esse __id__ em um variável temporária __tmpID__.


##### updateData(data)
Esta função é responsável por alterar dados específicos de um __id__ usando a variável temporaria __tmpID__ que será usada como consulta para modificar a variável global __tmpDict__ e escrever os dados dessa variável no arquivo __JSON__, esta função terá como objetivo atualizador dados.

##### writeData(data)
Esta função é responsável por adicionar dados à variável global __tmpDict__ e escreve-los no arquivo __JSON__, esta função terá como objetivo adicionar novos dados.

#### removeData()
Esta função é responsável por remover um dado específicos de um __id__ usando a variável temporaria __tmpID__ que será usada como consulta para modificar a variável global __tmpDict__ e escrever os dados dessa variável no arquivo __JSON__, esta função terá como objetivo remover dados.

### Arquivos json

###### paciente.json
```
{
    "data": [
        {
            "id": "12345",
            "cpf": "12345",
            "nome": "Joazin",
            "telefone": "123456789",
            "endereco": "Rua sei la tlgd?",
        },
    ].
}
```

###### consulta.json
```
{
    "data": [
        {
            "id": "12345",
            "codigo": "12345",
            "paciente": "É o tal do tralha",
            "medico": "Alceu Dispor",
            "data": "20/20/2020",
            "hora": "25HRs",
            "retorno": "26HRs",
            "observacao": "Paciente com casos de cabacice",
        },
    ].
}
```

###### medico.json
```
{
    "data": [
        {
            "id": "12345",
            "CRM": "12345",
            "nome": "Doutor Sono",
            "email": "baiano@gmail.com",
            "especialidade": "Gemer sem fazer barulho",
            "clinica": "B.O.G.A",
        },
    ].
}
```

###### funcionario.json
```
{
    "data": [
        {
            "id": "666",
            "matricula": "666",
            "cpf": "666",
            "nome": "Capeta",
            "email": "capeta666@gmail.com",
            "clinica": "B.O.G.A",
        },
    ].
}
```

###### clinica.json
```
{
    "data": [
        {
            "id": "12345",
            "cnpj": "12345",
            "nome": "B.O.G.A",
            "endereco": "Rua mal odores",
        },
    ].
}
```

## Controller

###### Nome do arquivo: controller.py

- Irá exibir o __menu principal__.
- Receber entrada de dados do usuário e exibir novos menus com base nesses dados.
- Manipular a exibição e escrita/leitura dos dados.

