# *SGE - Sistema de Gestão de Estoque 🗳️ ☛ 🏭* 

Este é um sistema de gerenciamento de estoque para ajudar a gerenciar as entradas, saídas e níveis de estoque de produtos em uma empresa. Um sistema de gestão de estoque é uma solução tecnológica utilizada para controlar e gerenciar o estoque de um negócio ou organização. Ele permite que a empresa acompanhe a quantidade de itens em estoque, sua localização, data de validade e outros fatores importantes. Além disso, os sistemas de gestão de estoque também permitem que a empresa monitore a entrada e saída de itens, gerencie pedidos e compras de estoque, e forneça relatórios e insights sobre a performance do estoque.

Os sistemas de gestão de estoque também são projetados para ser integrados com outros sistemas e processos da empresa, como o sistema de gerenciamento de vendas ou o sistema de gerenciamento financeiro. Isso permite uma visão mais completa da performance do estoque e ajuda a prevenir problemas como falta ou excesso de estoque.

Os sistemas de gestão de estoque são uma parte importante da operação de muitas empresas e podem ajudar a melhorar a eficiência, aumentar a precisão e reduzir custos. Eles também ajudam a garantir a disponibilidade dos itens certos no momento certo, o que é crucial para atender às necessidades dos clientes e manterem a satisfação do cliente.

## Funcionalidades 📦✔️

- **Permitir o cadastro de uma matriz e filial (Inclusão, Exclusão e Edição)**
- **Inserir dados sobre uma matriz e filial como: nome, endereço, tipo**
- **Permitir o cadastro de um produto (Inclusão, Exclusão e Edição)**
- **Inserir dados sobre um produto como: nome, quantidade, valor e destino**
- **Permitir a transferência de um produto entre filiais, bem como entre filial e matriz;**

## Instalação 🚀🐍
1. Clone ou faça o download deste repositório  `https://github.com/kamipip/projeto01`

2. Instale as dependências necessárias listadas no arquivo `requirements.txt`

3. Execute o arquivo `alternative.py` para iniciar o sistema

## Comandos de Instalação 🖥️👩‍💻

```
git clone https://github.com/kamipip/projeto01
```

```
cd projeto01
```

```
pip install -r requirements.txt
```

```
python alternative.py
```



## Uso 🐧🗔
1. Adicione produtos ao estoque fornecendo seus detalhes, como nome, descrição, preço e quantidade inicial.
2. Atualize as informações dos produtos existentes quando necessário.
3. Registre as entradas e saídas de estoque para atualizar o nível de estoque.
4. Faça a transferência de um produto de uma matriz para uma filial

## Contribuição ⚙️🔝 
Contribuições são sempre bem-vindas! Para contribuir, basta abrir uma issue ou criar um pull request com suas sugestões ou correções.

## Licença ©️ ⚖️
Este software está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Estrutura de Diretorios 📁

    📁Aquiles/
        📁animations/  # Pasta com as animações da Stack de Teste Aquiles.
            🐍loading.py

        📁coding_test/ # Ambiente de testes de código
            🐍class_coding_test.py

        📁function_test/ # Ambiente com testes de função
            🐍class_test.py

    📁GUI/ # Diretorio Principal
        📁assets/ # imagens utilizadas na GUI
            🖼️icon.png
            🖼️product.png
            🖼️ industry.png
            🖼️exclude.png

        📁build/ # pasta onde está localizada o executável do beta do programa
            📁MyApplication/
                🗔MyApplication.exe

        📁sistema_estoque # Model e Controller da aplicação
            🐍crud_operation.py
            🐍db_operation.py
            🖹edit_filial.txt
            🖹edit_matriz.txt
            🖹edit_pdt.txt
            🐍produto.py
            🐍matriz.py
            🐍filial.py

        🐍alternative.py # Arquivo principal da primeira interface
        🐍alternative2.py # Arquivo secundário da primeira interface

    📁sql_scripts/ # Scripts do banco de dados
        🗄️filial.sql
        🗄️matriz.sql
        🗄️produto.sql

     🖹requirements.txt # Arquivos com as dependências necessárias




