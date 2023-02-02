# Cloud-Computing-HW1-microservices
a web application to find the weather of a given city


This repository contains two microservices and a client script to demonstrate how to build and call microservices using Flask, Docker, and Python.

## Microservices

The two microservices are defined in `app.py`:

- A `city_to_zip` microservice that takes a city name as input and returns the corresponding zipcode.
- A `zip_to_weather` microservice that takes a zipcode as input and returns the corresponding weather information.


## Running the Microservices

To run the microservices, you need to have Docker installed. Then, follow these steps:

1. Build the Docker image using the Dockerfile:

    ```
    docker build -t microservice_city2zip .
    docker build -t microservice_zip2weather .
    ```

2. Run the Docker container:

    ```
    docker run -d -p 8000:5000 microservice_city2zip
    docker run -d -p 8001:5000 microservice_zip2weather
    ```

## Running the Client

To run the client, you need to have Python 3 and the `requests` library installed. Then, run the following command:


## Running the Integration

To run the integration, you need to have Python 3 and the `requests` library installed. Then, run the following command:

    python3 integration.py
