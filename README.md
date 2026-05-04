# 📝 League Notes - API

> **O LeagueNotes nasce como uma solução simples para jogadores de League of Legends que desejam melhorar no jogo.** 
> 
> Ele permite que o jogador possa criar o seu usuário e cadastrar quantas contas de LoL quiser. Nelas, ele poderá criar as suas
> notas personalizadas para cada matchup que jogar, permitindo também que possa consultá-las futuramente para rever
> ponto que precisa melhorar ou o que deve continuar fazendo para vencer.

---
## 🚀 Tecnologias Utilizadas
* 🐍 **_Python >= 3.13_**
* :zap: **_FastAPI_** (Web Framework)
* 🐘 **_PostgreSQL_** (Banco de dados)
* ⚗️ **_SQLAlchemy_** (ORM)
* 📦 **_Poetry_** (Gerenciamento de dependências)
* 🐳 **_Docker & Docker Compose_** (Containerização)
* 🧪 **_Pytest_** (Testes automatizados)
* 🛡️ **_Pydantic_** (Validação de dados)
* 🎟️ **_PyJWT_** (Autenticação)
* 🔒 **_Bcrypt_** (Hashing de senhas)
---
## 🛠️ Como rodar o projeto

### Pré-requisitos
* **_Docker_** instalado
* **_Docker Compose_** instalado

### Passo a passo
1. No terminal, clonar o repositório:
   ```bash
   git clone https://github.com/dev-alba/api-league-notes.git
   ```
   
2. Ainda no terminal, abrir o diretório do LeagueNotes:
   ```bash
   cd api-league-notes
   ```
   
3. (Opcional) Caso deseje rodar o **_Black_** ou o **_Pytest_** fora do **_Docker_**, você
precisará instalar as dependências do **_Poetry_**:
   ```bash
   poetry install
   ```
   
4. Copiar o arquivo **_.env.example_** para a pasta raiz do projeto e alterar as variáveis de ambiente:
   ```bash
   cp .env.example .env
   ```
   
- Para as configurações do **_.env_**, preencha o arquivo da maneira a seguir:
   ```bash
   DB_HOST=db
   DB_NAME=api-league-notes
   DB_USER=seu_usuario_aqui   # seu usuário do banco
   DB_PASSWORD=sua_senha_aqui   # sua senha para o usuário do banco
   DB_PORT=5432
   DATABASE_URL=sua_url_do_banco_aqui   # preenche caso possua alguma URL externa do postgres, 
                                        # caso não, deixe em branco 
  
   ACCESS_TOKEN_EXPIRE_MINUTES=60   # o tempo, em minutos, que seu token deve ser válido
   SECRET_KEY=sua_senha_secreta_aqui   # insira a sua chave secreta para o jwt
   ALGORITHM=HS256
   ```
  
> Para a criação da sua senha secreta, é aconselhável que a gere pelo próprio terminal:
>   ```bash
>  openssl rand -base64 32
>   ```
    
- O valor retornado pelo terminal poderá ser utilizado no **_.env_**.

5. Montar e imagem e subir o container do **_Docker_**:
   ```bash
   docker-compose up --build
   ```
   
Com isso, o seu LeagueNotes já deve rodar normalmente.

Basta acessar a documentação do **_Swagger_** (localhost:8000/docs).

> Vale lembrar que será necessário fazer login para se autenticar e poder acessar todas as rotas.
As únicas rotas públicas da API serão o cadastro de usuários e login.
---
## 🧪 Testes automatizados

### Como executar os testes
É necessário que o usuário tenha seguido o passo 3. da instalação do LeagueNotes. Caso
já tenha sido feito, basta rodar o comando no terminal:
   ```bash
   poetry run pytest 
   ```

- Dessa forma, todos testes do diretório **_tests_** serão executados para confirmar se
obtiveram sucesso.
---
## ✨ Padronização de código
Se, por ventura, o usuário tenha feito alguma alteração no código do projeto e deseja
manter a sintaxe do código no padrão escrito originalmente **(PEP8)**, pode-se
utilizar o **_Black_**.

Para isso, deve-se, assim como na execução dos testes, ter seguido o passo 3. da 
instalação do LeagueNotes. 

Após isso, pode rodar o comando no terminal:
   ```bash
   poetry run black .
   ```
> Para que o **_Black_** varra todo o projeto, certifique-se de que está com o terminal aberto no diretório raiz do projeto.
---
## ❤️ Agradecimentos

*   **À minha família**, por serem minha maior fonte de apoio, inspiração e por 
acreditarem na minha jornada na tecnologia.
*   **À FATEC Ribeirão Preto**, pelo ensino de qualidade e por proporcionar 
o ambiente necessário para o meu crescimento como desenvolvedor.