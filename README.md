# Marvel Crawler

Baixe os todos os dados da API da Marvel para um banco de documentos com este projeto.



## Instalação

Clone este repositório

    $ git clone git@github.com:Guilehm/marvel-crawler.git

Entre no diretório

    $ cd marvel-crawler
    
Copie o arquivo `env.sample` para `.env`

    $ cp env.sample .env
    
Utilize algum editor para alterar suas credenciais*

    $ vim .env
    
*<small>*para obter as credenciais se cadastre [aqui](https://developer.marvel.com/account).*</small>
    
### Instalação com Docker

É necessário ter o Docker e o Docker-compose instalados em sua máquina.
Recomendo este tutorial de instalação para o Linux [https://www.digitalocean.com/community/tutorials/como-instalar-e-usar-o-docker-no-ubuntu-18-04-pt](https://www.digitalocean.com/community/tutorials/como-instalar-e-usar-o-docker-no-ubuntu-18-04-pt)

Após ter concluído as etapas anteriores e estar com o serviço do Docker rodando, execute:

    $ docker-compose build

## Utilização

O spider está configurado para baixar informações dos seguintes endpoints:
- characters
- series
- comics
- stories
- events
- creators

Inicie os spiders com o seguinte comando:

    $ docker-compose run crawler scrapy crawl characters

Altere `characters` por um dos endpoints desejados acima.

Os logs serão impressos no terminal e um relatório será gerado ao final das requests.
Caso alguma request falhe, o Scrapy será responsável por tentar novamente e garantir que nenhuma informação seja perdida.

Os documentos serão salvos no mongodb em um banco chamado `marvelCrawler`.
Para acessá-los, recomendo a utilização do *[Robo 3T](https://robomongo.org/download)*. 

Configurei um delay de 2s para cada request e no máximo 5 requests em concorrência, para não sobrecarregar a API.

Altere esses dados conforme desejar, mas tente não sobrecarregar o servidor.


## Recomendações

- Fique atento ao limite de 3000 requisições diárias.
- Cada endpoint pode trazer até 100 resultados por paginação*
- Os endpoints `events` e `creators` são muito pesados e tive resultados ruins acima de 25 itens por paginação, recomendo não alterar no código.

*<small>*Altere a quantidade de resultados por paginação no arquivo `.env` na variável `LIMIT`.*</small>
*<small>*Por padrão estabeleci a quantidade de 50 itens, para ter uma performance boa.*</small>
