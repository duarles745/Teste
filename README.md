# Testando git adsadasdasdas modificando texto asdasdaw 

# Salvando modificações no Git, com teste prático

# Para iniciar um novo repositório Git, é necessário criar uma pasta com um controle de associação do Git. Para fazer isso, basta digitar o seguinte comando dentro da pasta na qual deseja salvar os arquivos que serão versionados pelo Git: "git init". Isso criará um ponto de controle para que o GitHub (ou outro repositório) possa rastrear os arquivos e, assim, permitirá o controle de versão.

# O comando "git add" é usado para adicionar arquivos ao espaço de preparação (staging area) para os arquivos que sofreram alguma modificação (changes) após o último commit. Você pode usar "git add ." para adicionar todos os arquivos modificados ou "git add nome_do_arquivo.extensão" para adicionar arquivos específicos.

# Se o desenvolvedor desejar restaurar um arquivo ao seu estado anterior à modificação, ele pode usar o comando "git restore nome_do_arquivo.extensão". Se o arquivo já estiver na área de preparação (staging area) após um "git add", é possível reverter apenas essa etapa com o comando "git restore --staged nome_do_arquivo.extensão".

# Após atribuir o arquivo modificado à área de preparação, é necessário enviar as modificações para o repositório. Para fazer isso, use o comando "git commit -m 'Adicionar novo título'". O argumento "-m" permite adicionar uma breve descrição da modificação feita no commit.

# Caso o desenvolvedor queira ver todas as modificações feitas no código, pode usar o comando "git log". Isso mostrará todas as modificações feitas, com informações como o autor, data e hora de cada commit. Cada commit é identificado por um hash único, que pode ser usado para referenciar commits específicos.

# Para restaurar um arquivo a partir de um commit anterior, você pode usar o comando "git checkout" ou "git restore" com o hash do commit desejado. Por exemplo, "git checkout hash_do_commit nome_do_arquivo.extensão" restauraria o arquivo para o estado no commit referenciado.

# Após fazer o commit das modificações no código, o usuário pode enviar o código para um repositório remoto na nuvem. Primeiro, você pode verificar os repositórios remotos associados ao seu repositório local usando o comando "git remote". Isso mostrará uma lista de remotos configurados.

# Para enviar suas alterações para um repositório remoto na nuvem, você pode usar o comando "git push". A sintaxe típica é "git push nome_do_remote nome_da_branch". Por exemplo, se você deseja enviar suas alterações para um repositório chamado "origin" na branch principal (geralmente chamada "main" ou "master"), você usaria o comando "git push origin main" ou "git push origin master", dependendo da configuração do repositório.

# Lembre-se de que você deve ter permissões adequadas no repositório remoto para realizar o push das modificações.

# Se você está enviando pela primeira vez para um repositório remoto, pode ser necessário configurar o repositório remoto com o comando "git remote add nome_do_remote URL_do_repositório". Isso cria uma conexão entre o repositório local e o repositório remoto para que você possa fazer push e pull das alterações.
 
 
# O comando git pull é usado para recuperar as últimas alterações do repositório remoto e mesclá-las automaticamente em sua branch local. Isso significa que ele executa dois passos em um: primeiro, ele faz um git fetch para buscar as atualizações do repositório remoto, e depois, ele faz um git merge (ou um git rebase, dependendo da configuração) para incorporar as alterações locais.

# É útil quando você deseja trazer as atualizações do repositório remoto e mesclá-las automaticamente em sua branch local

 # O comando git fetch é usado para buscar as atualizações do repositório remoto, mas ele não mescla automaticamente as alterações em sua branch local. Ele apenas atualiza as referências remotas e baixa as informações sobre as mudanças no repositório remoto, permitindo que você veja o que foi alterado antes de decidir como incorporar as atualizações em sua branch local.
# É útil quando você deseja verificar as atualizações antes de mesclá-las manualmente, o que lhe dá mais controle sobre o processo.

# caso o desenvolvedor queira compartilhar seu codigo apartir de uma branch que nao seja a main ou a master ele pode criar uma nova branch utilizando o codigo " git branch (nome de branch que queira) " e para selecionar a branch criada pode ser usado o codigo " git checkout (nome da branch criada). Para verificar a branch selecionada o usuario pode usar o codigo " git branch " assim o vscode marca a branch selecionada.

# Criar uma nova branch:

# Para criar uma nova branch, você pode usar o comando git branch. No entanto, geralmente é acompanhado pelo nome da nova branch que você deseja criar. Por exemplo:


# git branch nome_da_nova_branch

# Selecionar uma branch:

# Para mudar para a nova branch que você acabou de criar, você pode usar o comando git checkout. Isso permite alternar entre diferentes branches no Git. Por exemplo:

# git checkout nome_da_nova_branch

# Uma forma mais recente e recomendada de criar e mudar para uma nova branch ao mesmo tempo é usar o comando git switch:

# git switch -c nome_da_nova_branch

# Verificar branches:

# Para listar todas as branches presentes no seu repositório Git e destacar a branch atual, você pode usar o comando git branch. A branch atual estará marcada com um asterisco (*). Por exemplo: git branch 

# O comando git merge é usado para mesclar as alterações de uma branch em outra. Você normalmente mescla uma branch secundária (como uma feature branch) na branch principal (como main ou master).

# Primeiro, certifique-se de estar na branch na qual deseja incorporar as alterações. Em seguida, execute o comando git merge seguido do nome da branch que deseja mesclar.

# O comando git rebase é outra opção para unir branches, mas ele reorganiza o histórico de commits de uma forma linear. Isso pode ser útil para manter um histórico mais limpo e linear.

# Para usar o git rebase, primeiro, certifique-se de estar na branch na qual deseja incorporar as alterações. Em seguida, execute o comando git rebase seguido do nome da branch que deseja mesclar.