<!-- https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax -->
# ProjetoPTI-PTR
Projeto das cadeiras de PTI/PTR. Grupo 10

# Correr o projeto
1. `py -m venv VirtualEnv`
2. `VirtualEnv\Scripts\activate.bat`
3. Criar um novo terminal e verificar se -> (VirtualEnv) C:\Users\...
4. `cd .\Django\`
5. `py manage.py runserver`
6. Aceder ao [site](127.0.0.1:8000)

# Objetivos

## Design
- [x] 1. Especificação API usando o padrão OpenAPI, em formato YAML ou JSON
- [x] 2. Especificar requisitos NF - escalabilidade
- [x] 3. Especificar requisitos NF - segurança
- [x] 4. Especificar requisitos NF - tolerância a faltas
- [x] 5. Design da arquitetura distribuída </br>
  - [ ] 5.1. Aplicação do conceito em relação aos load balancers </br>
  - [ ] 5.2. Aplicação do conceito em relação aos web servers </br>
  - [ ] 5.3. Aplicação do conceito em relação às bases de dados
- [x] 6. [GitHub](https://github.com/jotanmiguel/ProjetoPTI-PTR) - uso com branches individuais e releases

## Arquitetura distribuída e tolerância a faltas
- [ ] 7. Implementação da arquitetura distribuída (implementação de instâncias e configuração de redes) </br>
  - [ ] 7.1. Implementação dos balanceadores de carga </br>
  - [ ] 7.2. Implementação dos servers </br>
  - [ ] 7.3. Implementação das bases de dados
- [ ] 8. Configuração dos balanceadores de carga e mecanismos de escalabilidade
- [ ] 9. Configuração de mecanismos de tolerância a faltas e verificação de saúde </br>
  - [ ] 9.1.. Teste de tolerância a faltas nos balanceadores de carga </br>
  - [ ] 9.2. Teste de tolerância a faltas nos webservers </br>
  - [ ] 9.3. Teste de tolerância a faltas nas bases de dados
	
## Segurança
- [ ] 10. Implementação de mecanismo de Autenticação e autorização (Auth0)
- [ ] 11. Canais seguros, DNS e configuração de firewall</br>
	- [ ] 11.1. Uso de TLS com certificado assinado por uma </br>Autoridade Certificadora (AC)
  - [ ] 11.2. Nome de domínio registado e associado ao IP estático </br>
	- [ ] 11.3. Configurações de firewall
- [ ] 12. Configurar uso de APIs externas
- [ ] 13. Gestão de credenciais e IPs na instalação

## Automação e testes
- [ ] 14. Automação e scripts para construção e lançamento da aplicação
- [ ] 15. Inclusão de testes unitários integrados ao processo de construção da aplicação (Github)
- [ ] 16. Testes de aceitação com a API
- [ ] 17. Testes de carga
- [ ] 18. Testes de vulnerabilidades

# Bases de dados
Ideia para a base de dados (incompleto):
- **Categoria** (Id, nome, categoria pai)
- **Produto** (Id, nome, preco, categoria)
- **Fornecedor** (Supplier Id)
- **Cliente** (Cliente Id, morada)
- **Utilizador** (Id, nome, nif, telefone, tipo)
- **Encomenda** (Id, Cliente id, fornecedor, morada, quantidade, preco, data)

- [ ] diagrama da base de dados;

Conceitos:
- 2 bases de dados, 1 principal, outra secundária;

# API (João Oliveira)
Versão mais recente da [API](https://app.swaggerhub.com/apis/PTR010/MercadoOnline/0.2.0#/)
O que é preciso Fazer? :
- [ ] Continuar o desenvolvimento da API;
- [ ] Hierarquia de categorias (Incompleto; não funciona, mas já está iniciado);
- [ ] Remover "tabela" tags do Swagger, e outras que não façam sentido;
- [ ] Adicionar a cada endpoint mais atributos, e corrigir os que já existem;
- [ ] Adicionar os metodos Delete e Put;
- [ ] Atualizar a api com novos endpoints;

Bugs:
- Pagina admin não funciona para tabelas com chaves estrangeiras (ex: Categoria);

# Front-End (Daniela)

# Back-End (João Oliveira e Diogo)
- [ ] Diagrama de classes;

# Balenceadores de Carga (Miguel)
- [ ] Identificar protocolos a usar (mais do que um a identificar);
- [x] Trocar o http por https;
- [ ] Fazer o guião sobre balenciadores de carga;

# Servidor
Conceitos:
- Máximo de 2 instâncias
- Réplicas podem ser escaladas
- Monitorização dos níveis de carga ativamente
- Mínimo 2 servidores

# Redes
Conceitos:
- Existência de Sub-Redes, para dividir tráfego interno e externo e aumentar a segurança
- Cada balanceador deve estar conectado a uma sub-rede interna e a uma externa

# Serviços Cloud
- Escolher um destes serviços permitidos:
  - [ ] Google Cloud Platform
  - [ ] Amazon Web Services
  - [ ] Microsoft Azure

# Firewalls
Conceitos:
- [ ] Firewalls para cada rede e máquina virtual usada

# Escalabilidade
- [ ] Mecanismos de escalabilidade;

# Links uteis
- [Orientações gerais](https://12factor.net)
- [GitHub Hello World](https://docs.github.com/en/get-started/quickstart/hello-world)
- [GitHub Actions Hello World](https://lab.github.com/githubtraining/github-actions:-hello-world)
- [OpenAPI](https://swagger.io/specification/)
- [OpenAPI Tutorial](https://support.smartbear.com/swaggerhub/docs/tutorials/openapi-3-tutorial.html)
- [Cliente para testes da API](https://www.postman.com/)
- [OpenAPI editor especificação](https://editor.swagger.io/)
- [Load Balancer - HAProxy](http://cbonte.github.io/haproxy-dconv/2.5/intro.html)
- [Monitorização](https://www.netdata.cloud/)
- [Segurança](https://owasp.org/)
- [Top 10 OWASP](https://owasp.org/www-project-top-ten/)
- [Autenticação](https://auth0.com/)
- [Reserva de nome de domínio gratuito](https://my.dominios.pt)
- [Certificados SSL](https://letsencrypt.org/)
- [Testes unitários](https://docs.python.org/3/library/unittest.html)
- [Testes de carga](https://locust.io/)
- [Testes de vulnerabilidade](https://w3af.org)

# Github
Procedimentos:
1. Criar projeto privado no GitHub
2. Editar configurações do projeto e adicionar como colaboradores os elementos do grupo e os
docentes de PTR
3. Todos os elementos do grupo devem contribuir para o repositório. Nenhum elemento do grupo
trabalha diretamente sobre o main Branch
4. Cada contribuição é adicionada a um Branch específico criado para o efeito. Quando a
contribuição estiver preparada para ser avaliada pelos outros elementos é criado um Pull
Request. Quando o Pull Request for aprovado o Branch é eliminado. Não misturar
contribuições não relacionadas no mesmo branch. Documentar cada Branch e Pull Request.
5. Quando um Commit cria uma versão que está pronta para execução deve ser criada uma Tag
(Create a New Release) que vai criar uma nova Release permitindo usá-la em qualquer altura
para demonstrar esse estado do projeto.
