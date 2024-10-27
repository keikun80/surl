freeze command : pip list --format=freeze > requirements.txt  
docker image build : docker image build -t surl-image .
docker run : docker run -d --name surl-container -p 8080:80 surl-image
