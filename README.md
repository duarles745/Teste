# Testando git adsadasdasdas modificando texto asdasdaw 

# Salvando modificações no Git, com teste prático

# Para iniciar um novo repositório Git, é necessário criar uma pasta com um controle de associação do Git. Para fazer isso, basta digitar o seguinte comando dentro da pasta na qual deseja salvar os arquivos que serão versionados pelo Git: "git init". Isso criará um ponto de controle para que o GitHub (ou outro repositório) possa rastrear os arquivos e, assim, permitirá o controle de versão.

# O comando "git add" é usado para adicionar arquivos ao espaço de preparação (staging area) para os arquivos que sofreram alguma modificação (changes) após o último commit. Você pode usar "git add ." para adicionar todos os arquivos modificados ou "git add nome_do_arquivo.extensão" para adicionar arquivos específicos.

# Se o desenvolvedor desejar restaurar um arquivo ao seu estado anterior à modificação, ele pode usar o comando "git restore nome_do_arquivo.extensão". Se o arquivo já estiver na área de preparação (staging area) após um "git add", é possível reverter apenas essa etapa com o comando "git restore --staged nome_do_arquivo.extensão".

# Após atribuir o arquivo modificado à área de preparação, é necessário enviar as modificações para o repositório. Para fazer isso, use o comando "git commit -m 'Adicionar novo título'". O argumento "-m" permite adicionar uma breve descrição da modificação feita no commit.

# Caso o desenvolvedor queira ver todas as modificações feitas no código, pode usar o comando "git log". Isso mostrará todas as modificações feitas, com informações como o autor, data e hora de cada commit. Cada commit é identificado por um hash único, que pode ser usado para referenciar commits específicos.

# Para restaurar um arquivo a partir de um commit anterior, você pode usar o comando "git checkout" ou "git restore" com o hash do commit desejado. Por exemplo, "git checkout hash_do_commit nome_do_arquivo.extensão" restauraria o arquivo para o estado no commit referenciado.