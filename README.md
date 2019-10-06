# Marvel Crawler

Download all Marvel API data to a Mongodb with this project



## Installation

Clone this repository

    $ git clone git@github.com:Guilehm/marvel-crawler.git

Enter directory

    $ cd marvel-crawler
    
Copy the sample file `env.sample` to `.env`

    $ cp env.sample .env
    
Use some text editor to change your credentials*

    $ vim .env
    
*<small>*to get the credentials sign-up [here](https://developer.marvel.com/account).*</small>
    
### Installation with Docker

You must have Docker and Docker Compose installed on your machine

After completing the previous steps and having the Docker service running, run:

    $ docker-compose build

## Use guide

Spider is configured to download information from the following endpoints:
- characters
- series
- comics
- stories
- events
- creators

Start the spiders with the following command:

    $ docker-compose run crawler scrapy crawl characters

Change `characters` to one of the desired endpoints above.

Logs will be printed to the terminal and a report will be generated at the end of requests.
Should any request fail, Scrapy will be responsible for retrying and ensuring that no information is lost.

The documents will be saved to mongodb in a database called `marvelCrawler`.
To access them, I recommend using [Robo 3T](https://robomongo.org/download). 


I set a delay of 2s for each request and a maximum of 5 concurrent requests, so as not to overload the API.

Change this data as desired, but try not to overload the server.

<strong>Be nice to the API.</strong>


## Recommendations

- Stay tuned to the limit of 3000 daily requests.
- Each endpoint can bring up to 100 results per pagination *
- The endpoints `events` and` creators` are very heavy and I had bad results over 25 items per pagination, I recommend not changing the code.

*<small>* *Change the amount of pagination results in the `.env` file in the `LIMIT` variable.</small>
*<small>By default I set 50 items for reasonable performance and not overloading the server.*</small>


## Contribution
If you want to contribute, just open an issue.
Fork the repository and change whatever you'd like.

Pull requests are always welcome.
