# Sistema de Viagem

###### Obs: Os dados precisarão ser persistidos em arquivo físico JSON

A aplicação se divide em três partes na qual cada uma irá ter uma responsabilidade específica, estas três partes são divididas em:

- **Model** (Irá escrever e modificar os dados persistidos no arquivo JSON).
- **View** (Exibição dos dados, para o usuário).
- **Controller** (Manipular a entrada de dados do usuario, será responsável por interligar o view e model).

##### Estrutura de pasta

```
projeto/
    data/
        motoristas.json
        veiculos.json
        viagem.json
    README.md
    src/
        controller.py
        model.py
        views/
            view.py
            motoristaView.py
            veiculoView.py
            viagemView.py
```

## Views

###### Nome do arquivo: view.py

- O view terá um **menu principal** no qual irá exibir todas as funcionalidades que a aplicação possui.
- Para cada funcionalidade um menu especifíco para ela será criado, são eles o menu de **motorista**, **veículo** e **viagem**.

O menu de principal deverá exibir as seguintes funcionalidades:

1. **Menu de Motorista**
1. **Menu de Veículo**
1. **Menu de Viagem**

#### Menu paciente

###### nome do arquivo: motoristaView.py

O menu de paciente deverá exibir as seguintes funcionalidades:

1. Cadastrar motorista
1. Buscar motorista por CPF
1. Editar nome do motorista (Somente quando, após a busca e seleção do mesmo)
1. Remover motorista (Somente quando, após a busca e seleção do mesmo)
1. Listar todos os motorista por tipo da carteira (Perguntar antes qual tipo da carteira 'A' - 'B' - 'AB')
1. Listar todos os motorista
1. Sair

#### Menu veículo

###### nome do arquivo: veículoView.py

O menu de consulta deverá exibir as seguintes funcionalidades:

1. Cadastrar veículo
1. Buscar veículo por placa
1. Adicionar motorista ao veículo
1. Remover motorista do veículo
1. Listar veículos com motoristas
1. Listar veículos sem motoristas
1. Remover veículo
1. Sair

#### Menu viagem

###### nome do arquivo: viagemView.py

O menu de médico deverá exibir as seguintes funcionalidades:

1. Criar viagem
1. Finalizar viagem por placa (Aqui muda somente o status de True para False)
1. Viagens ativas
1. Veículos que estão em viagem
1. Veículos que estão Disponíveis para viagem
1. Listar todas as viagens
1. Listar todas as viagens por período (data inicial e final, todas as viagens deste período)
1. Sair

## Model

###### nome do arquivo: model.py

- Os dados irão ser armazenados em arquivos **JSON**, no qual serão lidos e escritos.
- Este arquivo só poderá ser acessado pelo **controller.py**.
- Não permitir duplicidade de dados.
- Exigir confirmação de exclusão de dados.

##### loadData(fileName)

Esta função é responsável por ler os dados dos arquivos **JSON** e retorna-los em forma de um **dicionário** no qual serão armazenados na variável global **tmpDict**, usando como base o **nome do arquivo**, passado como argumento. Essa função será invocada toda vez que um menu for selecionado e a variável **tmpDic** resetada, para realocar um novo dado.

_**Argumentos Permitidos**_

- motorista
- veículo
- viagem

##### loadDataById(id)

Esta função é responsável por ler dados específicos com base no seu **id**, armazenados temporariamente na variável global **tmpDict**. e armenar esse **id** em um variável temporária **tmpID**.

##### updateData(data)

Esta função é responsável por alterar dados específicos de um **id** usando a variável temporaria **tmpID** que será usada como consulta para modificar a variável global **tmpDict** e escrever os dados dessa variável no arquivo **JSON**, esta função terá como objetivo atualizador dados.

##### writeData(data)

Esta função é responsável por adicionar dados à variável global **tmpDict** e escreve-los no arquivo **JSON**, esta função terá como objetivo adicionar novos dados.

#### removeData()

Esta função é responsável por remover um dado específicos de um **id** usando a variável temporaria **tmpID** que será usada como consulta para modificar a variável global **tmpDict** e escrever os dados dessa variável no arquivo **JSON**, esta função terá como objetivo remover dados.

### Arquivos json

###### motorista.json

```
{
  "data": [
    {
      "id": "12345",
      "cpf": "12345",
      "nome": "O pirigoso",
      "carteira": "AB"
    }
  ]
}
```

###### veiculo.json

```
{
  "data": [
    {
      "id": "12345",
      "placa": "12345",
      "tipo": "CARRO",
      "motorista": "O pirigoso"
    }
  ]
}
```

###### viagem.json

```
{
  "data": [
    {
      "id": "12345",
      "veiculo": "12345",
      "rota": "66",
      "status": false,
      "data": "20/20/20"
    }
  ]
}
```

## Controller

###### Nome do arquivo: controller.py

- Irá exibir o **menu principal**.
- Receber entrada de dados do usuário e exibir novos menus com base nesses dados.
- Manipular a exibição e escrita/leitura dos dados.

