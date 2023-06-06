# Análise comparativa de ferramentas GPT

Neste projeto realizamos uma comparação entre o ChatGPT e o Auto-GPT na realização de alguma tarefas triviais. O Objetivo desta comparação é identificar as vnatagens e desvantagens de cada ferramenta.

Mais informações sobre o a análise podem ser vistas neste [artigo](www.globo.com).

O Auto-GPT é disponibilizado em https://github.com/Significant-Gravitas/Auto-GPT. Neste endereço também é disponibilizado a documentação necessária para instalação e configuração do projeto. Ao final deste documento serão disponibilizadas as instruções de instalação em Portugês.

## Caso de Teste Básico
Na execução do primeiro caso, o Auto-GPT gerou dois arquivos:
 * [graph_generator.py](src/basico/graph_generator.py): arquivo com o script para a geração do gráfico solicitado;
 * [install_matplotlib.py](src/basico/install_matplotlib.py): arquivo gerado pelo Auto-GPT para a instalação da biblioteca MatPlotLib.

## Caso de Teste Avançado
Na execução do caso avançado, o Auto-GPT gerou dois arquivos:
 * [flight_search.py](src/avancado/flight_search.py): script contínuo para localização de passagens com preços mais baixos;
 * [flight_search_test.py](src/avancado/flight_search_tests.py): arquivo com testes unitários para validação do script.

## Execução do Teste Avançado

Link para uma execução de um teste do Cenário Avançado: https://www.loom.com/share/84e3120a155049b382a468be19507a20

# Instalando e configurando o AutoGPT

## 📋 Requisitos

Escolha o ambiente para rodar o Auto-GPT:

  - [Docker](https://docs.docker.com/get-docker/) (*Recomendado*)
  - Python 3.10 or later (Instruções: [para Windows](https://www.tutorialspoint.com/how-to-install-python-in-windows))
  - [VSCode + devcontainer](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)


## 🗝️ Obtendo a chave a API

A chave da API da OpenAI pode ser acessada em: [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys).

!!! Atenção
    Para usar a API da OpenAI API com Auto-GPT, recomenda-se **setting up billing**
    (AKA paid account). A conta free é [limitada][openai/limites api] a 3 chamadas na API por minuto, que pode fazer a aplicação quebrar.

   Você pode setar a configurações de pagamento em [Manage account > Billing > Overview](https://platform.openai.com/account/billing/overview).

## Configurando Auto-GPT

### Configurando com docker Docker

1. Certifique-se que o Docker está instalado, veja em [Requisitos](#Requisitos)
2. Crie um projeto diretório par o Auto-GPT

        :::shell
        mkdir Auto-GPT
        cd Auto-GPT

3. No projeto diretório, crie um arquivo chamado `docker-compose.yml` com o seguinte conteúdo:

        :::yaml
        version: "3.9"
        services:
          auto-gpt:
            image: significantgravitas/auto-gpt
            depends_on:
              - redis
            env_file:
              - .env
            environment:
              MEMORY_BACKEND: ${MEMORY_BACKEND:-redis}
              REDIS_HOST: ${REDIS_HOST:-redis}
            profiles: ["exclude-from-up"]
            volumes:
              - ./auto_gpt_workspace:/app/autogpt/auto_gpt_workspace
              - ./data:/app/data
              ## allow auto-gpt to write logs to disk
              - ./logs:/app/logs
              ## uncomment following lines if you want to make use of these files
              ## you must have them existing in the same folder as this docker-compose.yml
              #- type: bind
              #  source: ./azure.yaml
              #  target: /app/azure.yaml
              #- type: bind
              #  source: ./ai_settings.yaml
              #  target: /app/ai_settings.yaml
          redis:
            image: "redis/redis-stack-server:latest"

4. Crie a configuração necessária [configuração](#configuração) de arquivos. Se necessário você pode encontrar templates no [repository].
5. Pull a última imagem do [Docker Hub]

        :::shell
        docker pull significantgravitas/auto-gpt

6. Continue com [Run with Docker](#run-with-docker)

[Docker Hub]: https://hub.docker.com/r/significantgravitas/auto-gpt
[repository]: https://github.com/Significant-Gravitas/Auto-GPT


### Configure com Git

!!! Importante
    Certifique-se que tem o [Git](https://git-scm.com/downloads) instalado no seu SO.

!!! Informação "Comando de execução"
    Para executar os comandos, abra o CMD, Bash, or Powershell window.  
    No Windows: pressione ++win+x++ and pick *Terminal*, or ++win+r++ and enter `cmd`

1. Clone o repositório

        :::shell
        git clone -b stable https://github.com/Significant-Gravitas/Auto-GPT.git

2. Navegue para o diretório onde você baixou o repositório

        :::shell
        cd Auto-GPT

### Configuração sem o Git/Docker

1. Baixe o `Código fonte (zip)` da [latest stable release](https://github.com/Significant-Gravitas/Auto-GPT/releases/latest)
2. Extraia o arquivo zipado em uma pasta.


### Configuração

1. Encontre o arquivo de nome `.env.template` na pasta principal do `Auto-GPT`.
    be hidden by default in some operating systems due to the dot prefix. To reveal
2. Crie uma cópia do `.env.template` e chame de `.env`;
3. Abra o arquivo `.env` no editor de texto.
4. Encontre a linha com descrição `OPENAI_API_KEY=`.
5. Depois de `=`, adicione a chave da API da OpenAI.
6. Salve e feche o arquivo `.env`.

## Executando Auto-GPT

### Executando com Docker

O caminha mais fácil é usando o `docker-compose`. 

Importante: Docker Compose versão 1.29.0 ou posterior é necessário usar a versão 3.9 do Compose file format.
Você pode checar a versão do docker compose instalado no seu sistema executando o seguinte comando:

	docker-compose version

Isto irá exibir a versão do Docker Compose que é corrente instalada no seu sistema.

Caso seja necessário atualizar o Docker Compose para uma nova versão, siga as instruções de instalação em: https://docs.docker.com/compose/install/

Uma vez que se tenha a versão mais recente do docker-compose, execute os seguintes comandos na pasta Auto_GPT.

1. Construa a imagem.

        :::shell
        docker-compose build auto-gpt

2. Execute o Auto-GPT

        :::shell
        docker-compose run --rm auto-gpt

[docker-compose file]: https://github.com/Significant-Gravitas/Auto-GPT/blob/stable/docker-compose.yml


### Executando com o Dev Container

1. Instale o [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extensão em VS Code.

2. Abra a paleta de comando executando ++f1++ e digite `Dev Containers: Open Folder in Container`.

3. Run `./run.sh`.
