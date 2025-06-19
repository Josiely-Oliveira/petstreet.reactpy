import sqlite3
import json

class BancoDeDados:
    def __init__(self, nome_banco):
        self.nome_banco = nome_banco
        self.conexao = sqlite3.connect(self.nome_banco)
        # Essa linha faz com os resultados retornados se comportem como dicionários
        # Isto aconte no método exportar_usuarios_para_json()
        self.conexao.row_factory = sqlite3.Row
        self.cursor = self.conexao.cursor()

    def criar_tabela_usuario(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuario (
                 id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
                 nome VARCHAR(100) NOT NULL,
                 cpf_ou_cnpj VARCHAR(20) NOT NULL UNIQUE,
                 tipo_usuario CHECK( tipo_usuario IN ('pessoa_fisica', 'instituicao')) NOT NULL,
                 email VARCHAR(100) NOT NULL UNIQUE,
                 senha VARCHAR(255) NOT NULL,
                 telefone VARCHAR(20),
                 endereco VARCHAR(255),
                 cidade VARCHAR(100),
                 estado CHAR(2),
                 cep CHAR(9),
                 foto_perfil VARCHAR(255),
                 data_cadastro DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.conexao.commit()
    
    def criar_tabela_status_animal(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS StatusAnimal (
                  id_status INTEGER PRIMARY KEY AUTOINCREMENT,
                  nome_status VARCHAR(50) NOT NULL UNIQUE,
                  descricao TEXT
            )
        ''')
        self.conexao.commit()

    def criar_tabela_animal(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS animal (
                  id_animal INTEGER PRIMARY KEY AUTOINCREMENT,
                  nome VARCHAR(100),
                  especie VARCHAR(50) NOT NULL,
                  raca VARCHAR(50),
                  sexo CHECK(SEXO IN ('macho', 'femea')) NOT NULL,
                  idade_aproximada VARCHAR(50),
                  descricao TEXT,
                  cidade VARCHAR(100),
                  estado CHAR(2),
                  data_publicacao DATETIME DEFAULT CURRENT_TIMESTAMP,
                  id_usuario_dono INT NOT NULL,
                  id_status INT NOT NULL,
                  imagem_animal VARCHAR(255),
                  FOREIGN KEY (id_usuario_dono) REFERENCES usuario(id_usuario),
                  FOREIGN KEY (id_status) REFERENCES StatusAnimal(id_status)
            )
        ''')
        self.conexao.commit()

    def criar_tabela_publicacao(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS publicacao (
                  id_publicacao INTEGER PRIMARY KEY AUTOINCREMENT,
                  titulo VARCHAR(255) NOT NULL,
                  conteudo TEXT NOT NULL,
                  data_publicacao DATETIME DEFAULT CURRENT_TIMESTAMP,
                  id_autor INT NOT NULL,
                  id_animal_pub INT NOT NULL,
                  visibilidade CHECK ( visibilidade IN('todos', 'usuarios_autenticados', 'instituicoes')) DEFAULT 'todos',
                  imagem_destacada VARCHAR(255),
                  FOREIGN KEY (id_autor) REFERENCES usuario(id_usuario),
                  FOREIGN KEY (id_animal_pub) REFERENCES animal(id_animal)
            )
        ''')
        self.conexao.commit()

    def criar_tabela_saude_animal(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS SaudeAnimal (
                 id_registro INTEGER PRIMARY KEY AUTOINCREMENT,
                 id_animal INT NOT NULL,
                 data_registro DATE NOT NULL,
                 tipo_registro CHECK( tipo_registro IN('avaliacao', 'tratamento', 'vacina', 'castracao', 'vermifugacao', 'exame', 'estado_atual', 'outro')) NOT NULL,
                 condicao VARCHAR(100),
                 descricao TEXT,
                 veterinario_nome VARCHAR(100),
                 documento_anexo VARCHAR(255),
                 vacinado BOOLEAN,
                 castrado BOOLEAN,
                 vermifugado BOOLEAN,
                 estado_saude VARCHAR(100),
                 observacoes TEXT,
                 FOREIGN KEY (id_animal) REFERENCES Animal(id_animal)
            )
        ''')
        self.conexao.commit()

    def inserir_usuario(self, nome, cpf_ou_cnpj, tipo_usuario, email, senha, telefone, endereco, cidade, estado, cep, foto_perfil):
        self.cursor.execute('''
            INSERT INTO usuario (nome, cpf_ou_cnpj, tipo_usuario, email, senha, telefone, endereco, cidade, estado, cep, foto_perfil)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (nome, cpf_ou_cnpj, tipo_usuario, email, senha, telefone, endereco, cidade, estado, cep, foto_perfil))
        self.conexao.commit()

    def inserir_animal(self, nome, especie, raca, sexo, idade_aproximada, descricao, cidade, estado, id_usuario_dono, id_status, imagem_animal):
        self.cursor.execute('''
            INSERT INTO animal (nome, especie, raca, sexo, idade_aproximada, descricao, cidade, estado, id_usuario_dono, id_status, imagem_animal)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (nome, especie, raca, sexo, idade_aproximada, descricao, cidade, estado, id_usuario_dono, id_status, imagem_animal))
        self.conexao.commit()

    def inserir_StatusAnimal(self, nome_status, descricao):
        self.cursor.execute('''
            INSERT INTO StatusAnimal (nome_status, descricao)
            VALUES (?, ?)
            ''', (nome_status, descricao))
        self.conexao.commit()

    def inserir_publicacao(self, titulo, conteudo, id_autor, id_animal_pub, visibilidade, imagem_destacada):
        self.cursor.execute('''
            INSERT INTO publicacao (titulo, conteudo, id_autor, id_animal_pub, visibilidade, imagem_destacada)
            VALUES (?, ?, ?, ?, ?, ?)
            ''', (titulo, conteudo, id_autor, id_animal_pub, visibilidade, imagem_destacada))
        self.conexao.commit()

    def inserir_Saude_Animal(self, id_animal, data_registro, tipo_registro, condicao, descricao, veterinario_nome, documento_anexo, vacinado, castrado, vermifugado, estado_saude, observacoes):
        self.cursor.execute('''
            INSERT INTO SaudeAnimal (id_animal, data_registro, tipo_registro, condicao, descricao, veterinario_nome, documento_anexo, vacinado, castrado, vermifugado, estado_saude, observacoes)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (id_animal, data_registro, tipo_registro, condicao, descricao, veterinario_nome, documento_anexo, vacinado, castrado, vermifugado, estado_saude, observacoes))
        self.conexao.commit()
    
    def listar_usuario(self):
        self.cursor.execute("SELECT * FROM usuario")
        resultado = self.cursor.fetchall()
        if resultado:
             for row in resultado:
                print(dict(row))
        else:
            return None

    def listar_StatusAnimal(self):
        self.cursor.execute("SELECT * FROM StatusAnimal")
        resultado = self.cursor.fetchall()
        if resultado:
             for row in resultado:
                print(dict(row))
        else:
            return None   

    def listar_Animal(self):
        self.cursor.execute("SELECT * FROM animal")
        resultado = self.cursor.fetchall()
        if resultado:
             for row in resultado:
                print(dict(row))
        else:
            return None  

    def listar_Publicacao(self):
        self.cursor.execute("SELECT * FROM publicacao")
        resultado = self.cursor.fetchall()
        if resultado:
             for row in resultado:
                print(dict(row))
        else:
            return None   

    def listar_SaudeAnimal(self):
        self.cursor.execute("SELECT * FROM SaudeAnimal")
        resultado = self.cursor.fetchall()
        if resultado:
             for row in resultado:
                print(dict(row))
        else:
            return None   

    def selecionar_usuario_por_nome(self, nome):
        self.cursor.execute("SELECT * FROM usuario WHERE nome = ?", (nome,))
        resultado = self.cursor.fetchall()
        if resultado:
             for row in resultado:
                print(dict(row))
        else:
            return None

    def atualizar_usuario(self, id_usuario, novo_nome, novo_cpf_ou_cnpj, novo_tipo_usuario,  novo_email, novo_senha, novo_telefone, novo_endereco, novo_cidade, novo_estado, novo_cep, novo_foto_perfil):
        try:
            self.cursor.execute('''
                UPDATE usuario
                SET nome = ?, cpf_ou_cnpj = ?, tipo_usuario = ?, email = ?, senha = ?, telefone = ?, endereco = ?, cidade = ?, estado = ?, cep = ?, foto_perfil = ?
                WHERE id_usuario = ?
            ''', (self, id_usuario, novo_nome, novo_cpf_ou_cnpj, novo_tipo_usuario,  novo_email, novo_senha, novo_telefone, novo_endereco, novo_cidade, novo_estado, novo_cep, novo_foto_perfil))
            self.conexao.commit()
            
            if self.cursor.rowcount == 0:
                print("Usuário não encontrado.")
            else:
                print("Dados atualizados com sucesso!")
        except sqlite3.IntegrityError as e:
            print("Erro ao atualizar: email ou telefone já existem.")
            print("Detalhes:", e)


    def excluir_usuario(self, id_usuario):
        self.cursor.execute('''
        DELETE FROM usuario
        WHERE id_usuario = ?
        ''', (id_usuario,))
        self.conexao.commit()

    def exportar_usuarios_para_json(self, caminho_arquivo):
        # Executa uma consulta SQL para buscar todos os registros da tabela "usuario"
        self.cursor.execute("SELECT * FROM usuario")
        
        # Recupera todos os resultados da consulta e armazena numa lista
        resultados = self.cursor.fetchall()

        # Converte cada linha do resultado (que é um objeto tipo Row) para um dicionário
        # Assim, cada usuário será representado como um dict com chaves correspondendo aos nomes das colunas
        usuario_lista = [dict(linha) for linha in resultados]

        # Abre (ou cria) o arquivo no caminho informado para escrita em modo texto com codificação UTF-8
        with open(caminho_arquivo, 'w', encoding='utf-8') as f:
            # Escreve a lista de usuários convertida para JSON no arquivo, com formatação legível (indent=4)
            # ensure_ascii=False permite que caracteres especiais apareçam normalmente no arquivo JSON
            json.dump(usuario_lista, f, ensure_ascii=False, indent=4)

        # Exibe no console uma mensagem indicando quantos usuários foram exportados e para qual arquivo
        print(f"{len(usuario_lista)} usuários exportados para {caminho_arquivo}")

    def exportar_animais_para_json(self, caminho_arquivo):
        # Executa uma consulta SQL para buscar todos os registros da tabela "animal"
        self.cursor.execute("SELECT * FROM animal")
        
        # Recupera todos os resultados da consulta e armazena numa lista
        resultados = self.cursor.fetchall()

        # Converte cada linha do resultado (que é um objeto tipo Row) para um dicionário
        # Assim, cada animal será representado como um dict com chaves correspondendo aos nomes das colunas
        animal_lista = [dict(linha) for linha in resultados]

        # Abre (ou cria) o arquivo no caminho informado para escrita em modo texto com codificação UTF-8
        with open(caminho_arquivo, 'w', encoding='utf-8') as f:
            # Escreve a lista de usuários convertida para JSON no arquivo, com formatação legível (indent=4)
            # ensure_ascii=False permite que caracteres especiais apareçam normalmente no arquivo JSON
            json.dump(animal_lista, f, ensure_ascii=False, indent=4)

        # Exibe no console uma mensagem indicando quantos animais foram exportados e para qual arquivo
        print(f"{len(animal_lista)} animais exportados para {caminho_arquivo}")

    def exportar_publicacoes_para_json(self, caminho_arquivo):
        # Executa uma consulta SQL para buscar todos os registros da tabela "publicacao"
        self.cursor.execute("SELECT * FROM publicacao")
        
        # Recupera todos os resultados da consulta e armazena numa lista
        resultados = self.cursor.fetchall()

        # Converte cada linha do resultado (que é um objeto tipo Row) para um dicionário
        # Assim, cada publicacao será representada como um dict com chaves correspondendo aos nomes das colunas
        publicacao_lista = [dict(linha) for linha in resultados]

        # Abre (ou cria) o arquivo no caminho informado para escrita em modo texto com codificação UTF-8
        with open(caminho_arquivo, 'w', encoding='utf-8') as f:
            # Escreve a lista de usuários convertida para JSON no arquivo, com formatação legível (indent=4)
            # ensure_ascii=False permite que caracteres especiais apareçam normalmente no arquivo JSON
            json.dump(publicacao_lista, f, ensure_ascii=False, indent=4)

        # Exibe no console uma mensagem indicando quantas publicacoes foram exportados e para qual arquivo
        print(f"{len(publicacao_lista)} publicacoes exportadas para {caminho_arquivo}")
    
    def exportar_SaudeAnimal_para_json(self, caminho_arquivo):
        # Executa uma consulta SQL para buscar todos os registros da tabela "SaudeAnimal"
        self.cursor.execute("SELECT * FROM SaudeAnimal")
        
        # Recupera todos os resultados da consulta e armazena numa lista
        resultados = self.cursor.fetchall()

        # Converte cada linha do resultado (que é um objeto tipo Row) para um dicionário
        # Assim, cada usuário será representado como um dict com chaves correspondendo aos nomes das colunas
        SaudeAnimal_lista = [dict(linha) for linha in resultados]

        # Abre (ou cria) o arquivo no caminho informado para escrita em modo texto com codificação UTF-8
        with open(caminho_arquivo, 'w', encoding='utf-8') as f:
            # Escreve a lista de usuários convertida para JSON no arquivo, com formatação legível (indent=4)
            # ensure_ascii=False permite que caracteres especiais apareçam normalmente no arquivo JSON
            json.dump(SaudeAnimal_lista, f, ensure_ascii=False, indent=4)

        # Exibe no console uma mensagem indicando quantos usuários foram exportados e para qual arquivo
        print(f"{len(SaudeAnimal_lista)} SaudeAnimal exportados para {caminho_arquivo}")

    def exportar_StatusAnimal_para_json(self, caminho_arquivo):
        # Executa uma consulta SQL para buscar todos os registros da tabela "StatusAnimal"
        self.cursor.execute("SELECT * FROM StatusAnimal")
        
        # Recupera todos os resultados da consulta e armazena numa lista
        resultados = self.cursor.fetchall()

        # Converte cada linha do resultado (que é um objeto tipo Row) para um dicionário
        # Assim, cada usuário será representado como um dict com chaves correspondendo aos nomes das colunas
        StatusAnimal_lista = [dict(linha) for linha in resultados]

        # Abre (ou cria) o arquivo no caminho informado para escrita em modo texto com codificação UTF-8
        with open(caminho_arquivo, 'w', encoding='utf-8') as f:
            # Escreve a lista de usuários convertida para JSON no arquivo, com formatação legível (indent=4)
            # ensure_ascii=False permite que caracteres especiais apareçam normalmente no arquivo JSON
            json.dump(StatusAnimal_lista, f, ensure_ascii=False, indent=4)

        # Exibe no console uma mensagem indicando quantos usuários foram exportados e para qual arquivo
        print(f"{len(StatusAnimal_lista)} usuários exportados para {caminho_arquivo}")

    def importar_usuarios_de_json(self, caminho_arquivo):
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            usuario_lista = json.load(f)

        for usuario in usuario_lista:
            try:
                self.cursor.execute('''
                    INSERT INTO usuarios (nome, email, telefone) VALUES (?, ?, ?)
                ''', (usuario['nome'], usuario['email'], usuario['telefone']))
            except sqlite3.IntegrityError:
                print(f"Usuário {usuario['nome']} já existe. Ignorando.")
        self.conexao.commit()

        print(f"{len(usuario_lista)} usuários importados de {caminho_arquivo}")


    def fechar(self):
        self.conexao.close()
