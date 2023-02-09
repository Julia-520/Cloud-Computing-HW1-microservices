docker network create --subnet=172.18.0.0/16 mynetwork

cd microservice_city2zip
docker build -t city2zip:latest .
docker run -p 8000:5000 -d --name city2zip --network mynetwork --hostname city2zip --ip 172.18.0.2 city2zip

cd ../microservice_zip2weather
docker build -t zip2weather:latest .
docker run -p 8001:5000 -d --name zip2weather --network mynetwork --hostname zip2weather --ip 172.18.0.3 zip2weather

