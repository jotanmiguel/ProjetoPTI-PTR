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
