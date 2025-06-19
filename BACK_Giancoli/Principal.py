from BancoDados import BancoDeDados

pst = BancoDeDados("PetStreet.db")

pst.criar_tabela_usuario()

pst.criar_tabela_status_animal()

pst.criar_tabela_animal()

pst.criar_tabela_publicacao()

pst.criar_tabela_saude_animal()

pst.inserir_usuario("Diogo Henrique", "165.098.356-25", 'pessoa_fisica', "dioguinho123@email.com", "22052006", "(11)99874-5642", "Rua juvencio pinhalzinho", "Extrema", "MG", "37640-000", "https://www.culturamix.com/wp-content/uploads/2009/02/Will-Smith.jpg")
pst.inserir_usuario("Ronaldinho Gaucho", "165.108.466-25", 'pessoa_fisica', "Ronaldinho123@email.com", "15091000", "(35)93874-9036", "Avenida Brasil", "Copacapana", "RJ", "39350-000", "https://i.pinimg.com/originals/68/82/a3/6882a3da8991bf4dcd0430dfb43792dd.jpg")
pst.inserir_usuario('João Silva', '12345678900', 'pessoa_fisica', 'joao@email.com', 'senha123', '35999990000', 'Rua A, 123', 'Pouso Alegre', 'MG', '37550-000', 'https://images4.fanpop.com/image/photos/19300000/Leonardo-Dicaprio-leonardo-dicaprio-19374229-900-902.jpg')
pst.inserir_usuario('ONG Patinhas Felizes', '12345678000199', 'instituicao', 'contato@patinhas.org', 'ongsecure', '35999991111', 'Av. Central, 500', 'Extrema', 'MG', '37640-000', 'https://res.cloudinary.com/worldpackers/image/upload/c_limit,f_auto,q_auto,w_1140/jylajpy28o0z8f4n4pdn')
pst.inserir_usuario('Carlos Andrade', '98765432100', 'pessoa_fisica', 'carlos@email.com', 'senha456', '35999992222', 'Rua B, 456', 'Itajubá', 'MG', '37500-000', 'https://tse3.mm.bing.net/th?id=OIP.X-0DAa-umK-6bkYwvUtXfgHaEc&pid=Api&P=0&h=180')
pst.inserir_usuario('Instituto Amigos dos Animais', '23456789000188', 'instituicao', 'contato@amigos.org', 'amigos123', '35999993333', 'Rua Verde, 89', 'Santa Rita', 'MG', '37510-000', 'https://oimparcial.com.br/app/uploads/2019/12/iStock_000018342486_Medium-1-630x420-1.jpg')
pst.listar_usuario()

pst.inserir_StatusAnimal('Disponível', 'Pronto para adoção')
pst.inserir_StatusAnimal('Adotado', 'Animal já adotado')
pst.inserir_StatusAnimal('Em tratamento', 'Animal está em tratamento veterinário')
pst.listar_StatusAnimal()

pst.inserir_animal('Rex', 'Cachorro', 'Vira-lata', 'macho', '2 anos', 'Cachorro dócil e brincalhão.', 'Pouso Alegre', 'MG', 2, 1, 'https://fotos.amomeupet.org/uploads/fotos/0x800_1568662224_5d7fe2d09bccd_hd.jpeg')
pst.inserir_animal('Mimi', 'Gato', 'Siamês', 'femea', '1 ano e meio', 'Gata tranquila, castrada.', 'Extrema', 'MG', 4, 1, 'https://gatos.plus/wp-content/uploads/2020/05/gato-siames-bebe-puro.jpg')
pst.inserir_animal('Nina', 'Gato', 'Siamês', 'femea', '2 anos', 'Gata bagunceira, castrada.', 'São Paulo', 'SP', 3, 2, 'https://todosobregatos.org/wp-content/uploads/2021/12/gato-siames-oscuro.jpeg')
pst.inserir_animal('Bolinha', 'Cachorro', 'Poodle', 'macho', '3 anos', 'Muito animado e amigável.', 'Itajubá', 'MG', 1, 1, 'https://talktodogs.com/wp-content/uploads/2021/01/Adorable-Poodle-Pup.jpg')
pst.inserir_animal('Luna', 'Gato', 'Persa', 'femea', '2 anos', 'Carinhosa e dorminhoca.', 'Santa Rita', 'MG', 5, 1, 'https://www.dci.com.br/wp-content/uploads/2020/09/Design-sem-nome-8.jpg')
pst.inserir_animal('Thor', 'Cachorro', 'Labrador', 'macho', '4 anos', 'Grande e protetor.', 'Extrema', 'MG', 6, 3, 'https://tse1.mm.bing.net/th?id=OIP.3gxyH87lFoAuvruYSu0hiAHaLH&pid=Api&P=0&h=180')
pst.listar_Animal()

pst.inserir_publicacao('Adote o Rex - Companheiro Leal', 'Rex é um cão dócil, brincalhão e vacinado. Ideal para quem busca um amigo fiel!', 2, 1, 'todos', 'https://fotos.amomeupet.org/uploads/fotos/0x800_1568662224_5d7fe2d09bccd_hd.jpeg')
pst.inserir_publicacao('Conheça a Mimi - Uma gata encantadora', 'Mimi é tranquila, castrada e carinhosa. Pronta para encontrar um novo lar!', 2, 2, 'todos', 'https://gatos.plus/wp-content/uploads/2020/05/gato-siames-bebe-puro.jpg')
pst.inserir_publicacao('Bolinha está esperando por você!',  'Poodle animado, sociável e ótimo para conviver com crianças. Adote já!', 1, 4, 'todos', 'https://talktodogs.com/wp-content/uploads/2021/01/Adorable-Poodle-Pup.jpg')
pst.inserir_publicacao( 'Luna quer um lar cheio de carinho!', 'Gatinha persa, muito carinhosa e dorminhoca. Dê uma chance à Luna!', 2, 5, 'todos', 'https://www.dci.com.br/wp-content/uploads/2020/09/Design-sem-nome-8.jpg')
pst.inserir_publicacao('Adoção Responsável - Faça a diferença','Adotar é um ato de amor, mas é importante se preparar para dar o cuidado necessário ao seu novo amigo. Saiba tudo sobre adoção responsável!',1,3,'todos','https://tse3.mm.bing.net/th?id=OIP.gttOckea63OvQINOBprIcQHaEF&pid=Api&P=0&h=180')
pst.inserir_publicacao('Participe da nossa Campanha de Castração!','Estamos promovendo uma castração gratuita para animais em situação de risco. Agende a sua participação!',3,1,'instituicoes','https://tse4.mm.bing.net/th?id=OIP.3aM5SkkMkdgk8SOhnNVsSQHaEg&pid=Api&P=0&h=180')
pst.inserir_publicacao('Feira de Adoção no Parque Municipal!','Neste sábado, teremos uma feira de adoção no Parque Municipal. Venha conhecer diversos animais à procura de um lar.',2,6,'todos','https://midias.gazetaonline.com.br/_midias/jpg/2019/02/06/feira_de_adocao-5990916.jpg')
pst.listar_Publicacao()

pst.inserir_Saude_Animal(1, '2025-05-01', 'vacina', 'Saudável', 'Vacinação antirrábica aplicada.', 'Dr. Marcos', 'vacina_rex.pdf', 'TRUE', 'FALSE', 'TRUE', 'Ótimo', 'Revisão em 6 meses')
pst.inserir_Saude_Animal(2, '2025-05-03', 'castracao', 'Castrada', 'Castrada com sucesso.', 'Dra. Ana', 'castracao_mimi.pdf', 'TRUE', 'TRUE', 'TRUE', 'Excelente', 'Recuperação perfeita')
pst.inserir_Saude_Animal(3, '2025-04-15', 'vermifugacao', 'Vermifugado', 'Vermífugo oral administrado.', 'Dr. Jorge', 'NULL', 'TRUE', 'FALSE', 'TRUE', 'Bom', 'Repetir após 3 meses')
pst.inserir_Saude_Animal(4, '2025-05-10', 'avaliacao', 'Check-up', 'Avaliação geral realizada.', 'Dra. Carla', 'NULL', 'TRUE', 'TRUE', 'TRUE', 'Saudável', 'Sem observações')
pst.inserir_Saude_Animal(5, '2025-05-15', 'tratamento', 'Tratamento em andamento', 'Tratamento contra sarna.', 'Dr. Luiz', 'NULL', 'FALSE', 'FALSE', 'FALSE', 'Regular', 'Retorno em 10 dias')
pst.listar_SaudeAnimal()

pst.exportar_usuarios_para_json('usuarios.json')
pst.exportar_animais_para_json('animais.json')
pst.exportar_publicacoes_para_json('publicacoes.json')
pst.exportar_SaudeAnimal_para_json('SaudeAnimal.json')
pst.exportar_StatusAnimal_para_json('StatusAnimal.json')

