# VideoGames-API
Simple API service to query a games database, the source of truth for our API
is the [GiantBomb API](https://www.giantbomb.com/api/documentation/#toc-0-41).
For this simple service , we are only going to expose two endpoints in our API.

Get Video Games endpoint (Provides us with 10 Video games matching the search query)

Get All Video Games endpoint (Provides all the data for Video games matching the search query limited to 100 objects)

You can visit the deployed API end point [here](https://2gsqwm.deta.dev/docs#/)

Feel free to make curl calls as below:

`curl -X 'GET' \
  'https://2gsqwm.deta.dev/games/{search_query}?page=0' \
  -H 'accept: application/json`
  
Eg:
`curl -X 'GET' \
  'https://2gsqwm.deta.dev/games/pokemon?page=0' \
  -H 'accept: application/json`
  
## Tech Stack

- Python
- FastAPI - A python framework to build APIs
- Docker - To containerize the application
- [Deta](https://www.deta.sh/) - To deploy the app for easy sharing


## Overview

The API key needs to be got from GiantBomb API if you want to be 
able to test the application locally.

The Docker and Docker-compose files are available for easy local setup and testing
The API key is set by setting the variable `GIANTBOMB_API_KEY`. You need
to pass this value in from the `.env` file.

### Local setup 

1. Clone the repository

`git clone git@github.com:saisha92/giantbomb-api.git`

2. Sign Up with GiantBomb API and request an API key, once you have the key
create a file called `.env` at the root level of the git directory
and add the value in the file like below:

`GIANTBOMB_API_KEY='YOUR_KEY'`

3. The Docker desktop service must be running on your local machine,
once you can confirm the service is running. Execute the below command

`docker-compose up --build`

This builds and sets up your API and it runs at localhost:8000
You can use postman / make Curl requests locally,

`curl -X 'GET' \
  'http://localhost:8000/games/{search_query}?page=0' \
  -H 'accept: application/json`

You can modify the code and restart the server and test any local changes you have made

### Deta deployed endpoint

The app is deployed at deta, it is a minimalistic cloud service that 
allows for deploying small python and Node applications

You can navigate to the UI [here](https://2gsqwm.deta.dev/docs#/)

<img width="1223" alt="try_it_out" src="https://user-images.githubusercontent.com/8673979/116015252-95e8ab00-a606-11eb-9823-59ad3e4aac01.png">

From the UI you can expand the end point, hit the "try it out" button 
and pass in values you want to query and see the response

Response will look like as below

<img width="1093" alt="Screen Shot 2021-04-25 at 8 41 46 PM" src="https://user-images.githubusercontent.com/8673979/116015322-ca5c6700-a606-11eb-8889-acec9b043576.png">


## Things for improvement / deploy at scale

This is just a simple API service , we need to take few things into 
consideration if we would want to scale this API service

1. Load Balancer -> We would need to have a load balancer to be able 
to distribute the requests and be more efficient

2. Cache Layer -> We could have a cache layer that caches the original API call
we make the GiantBomb API and eturns the data from cache for the same request

3. Business and Disaster recovery and Security are important things to consider

### Code improvement thought

1. Have an API testing framework in place for effective test process
2. Reduce # lines of code for Json Parsing
