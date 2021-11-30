# python_server_testing_florian_marques

## Author
- Florian Marques

# To install :
- `pip install pytest requests`

## To Do
You are to create a python website, using flask, that calculates the mean of GET requests containing a list of numbers. The website should be dockerized, and built using docker compose. Then you will create a testing file, using the python library pyunit, and these tests should cover: The site working: 
- a test that calls the website's url and confirms a code reply of 200. The site output is correct: 
- a test that sends a GET request to the website and confirms that the website returns the correct answer. 
- The site can handle stress: the average response time of the site should be below 100 ms per request, when 1000 requests are sent per second.

## Commands to launch the application :
- Build the application with docker (place you into the project directory) : `docker build -t docker_python_test -f Dockerfile.dockerfile .`
- To launch the application with docker : `docker run -p 5000:5000 docker_python_test`
- To launch it with docker compose : `docker-compose up`
- Try this link for the sum: `http://127.0.0.1:5000/means?int=1&int=2&int=5`