# bancoDioVivo

Sistema Bancário
Este é um sistema bancário simples implementado em Python. Ele permite operações básicas como depósitos, saques, consulta de extrato, cadastro de clientes e contas, além de funcionalidades avançadas como alteração de limites de saque, cadastro e gerenciamento de chaves Pix, e controle de acesso por computadores autorizados.

Funcionalidades
Operações Básicas
Depósito: Permite ao cliente depositar um valor em sua conta.
Saque: Permite ao cliente sacar um valor de sua conta, respeitando o limite de saque e o número máximo de saques diários.
Extrato: Exibe o saldo atual da conta do cliente.
Cadastrar Cliente: Permite cadastrar um novo cliente no sistema.
Cadastrar Conta: Permite cadastrar uma nova conta para um cliente existente.
Limites de Saque
Alterar Limite de Saque: Permite alterar o limite de valor que pode ser sacado em uma única transação.
Alterar Limite de Saques Diários: Permite alterar o número máximo de saques que um cliente pode realizar por dia. Três saques são gratuitos, e há planos mensais pagos para aumentar esse limite:
10 saques por R$ 29,90/mês
20 saques por R$ 39,90/mês
50 saques por R$ 49,90/mês
Chaves Pix
Cadastro de Chave Pix: Permite cadastrar diferentes tipos de chaves Pix para a conta do cliente:
Email
Telefone
CPF
Chave Aleatória
Controle de Acesso
Cadastrar Computador: Ao cadastrar um computador, o sistema captura automaticamente o MAC Address da máquina e registra como um dispositivo autorizado a realizar transações.
Autorizar Computador: Permite que o computador principal autorize outros computadores a realizar operações, inserindo manualmente o MAC Address.
Segurança
Verificação de Autorização: Todas as operações de saque verificam se o computador executante está autorizado, garantindo que apenas dispositivos autorizados possam realizar transações.
Como Usar
Menu de Operações
plaintext
Copiar código
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
[c] Cadastrar Cliente
[a] Cadastrar Conta
[l] Alterar Limite de Saque
[p] Cadastro de Chave Pix
[m] Cadastrar Computador
[u] Autorizar Computador
=> 
Exemplos de Uso
Cadastrar um Cliente:

Selecione a opção c.
Insira o nome e sobrenome do cliente.
Cadastrar uma Conta:

Selecione a opção a.
Insira o nome e sobrenome do cliente.
Insira o saldo inicial da conta.
Depositar:

Selecione a opção d.
Insira o nome e sobrenome do cliente.
Insira o valor a ser depositado.
Sacar:

Selecione a opção s.
Insira o nome e sobrenome do cliente.
Insira o valor a ser sacado.
A verificação de autorização do computador será realizada automaticamente.
Consultar Extrato:

Selecione a opção e.
Insira o nome e sobrenome do cliente.
O saldo atual será exibido.
Alterar Limite de Saque:

Selecione a opção l.
Insira o nome e sobrenome do cliente.
Insira o novo limite de saque.
Escolha um plano de saques diários se desejar alterar o limite.
Cadastrar Chave Pix:

Selecione a opção p.
Insira o nome e sobrenome do cliente.
Insira o tipo de chave Pix e o valor da chave.
Cadastrar Computador:

Selecione a opção m.
Insira o nome e sobrenome do cliente.
O MAC Address do computador será capturado automaticamente e cadastrado.
Autorizar Computador:

Selecione a opção u.
Insira o nome e sobrenome do cliente.
Insira o MAC Address do computador a ser autorizado.
Sair:

Selecione a opção q para sair do sistema.
Requisitos
Python 3.6 ou superior
Biblioteca getmac: Instale usando pip install getmac
Instalação
Clone o repositório:

bash
Copiar código
git clone https://github.com/seu-usuario/seu-repositorio.git
Instale as dependências:

bash
Copiar código
pip install getmac
Execute o script:

bash
Copiar código
python nome_do_script.py
Contribuição
Sinta-se à vontade para contribuir com melhorias para este projeto. Para contribuir:

Fork o repositório.
Crie uma branch para sua funcionalidade (git checkout -b funcionalidade-xyz).
Commit suas mudanças (git commit -m 'Adiciona funcionalidade xyz').
Push para a branch (git push origin funcionalidade-xyz).
Abra um Pull Request.
Licença
Este projeto está licenciado sob a licença MIT.
