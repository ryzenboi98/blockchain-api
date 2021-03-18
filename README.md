# blockchain-api
This project represents a Blockchain simulation using Flask to host and create the API.

## What is a Blockchain?
A Blockchain is a descrentralized system with blocks linked through hashes.

Each block contains, in a generalized view, the following data:
* __Transactions__
* An integer value of 32-bits aka __nonce__
* The __timestamp__ when the block was added to the chain
* The __hash of the previous block__
* The __hash__ of the block itself calculated by the data mentioned above

## API

The API has two functionalities which are the following:
* Checkout the chain
* Mine a block

For each of this functionalities you may want to test out the following endpoints:
```http
GET localhost:5000/get_chain
```
```http
GET localhost:5000/mine_block
```

## Setup
To setup the project use [Docker](https://www.docker.com) to build up an Image to execute our Flask API locally. The default port configured is the port 5000, so make sure you don't have any other service already running in that port.

### Steps
1. Download the source code and move to it's main folder inside a terminal.
2. Open the [Docker](https://www.docker.com) desktop application.
3. Execute `docker-compose up` inside the terminal.
4. Open Postman or even browser on this [link](http://localhost:5000/get_chain) to check the genesis block
5. Mine a block using this [link](http://localhost:5000/mine_block)


