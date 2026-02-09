freeze command
 - pip list --format=freeze > requirements.txt  
docker image build  
- move working directory to "deploy"
- docker image build -t surl-gen -f ./Dockerfile .
run docker container
 - docker run -d --name surl-container -p 8080:8080 surl-gen
