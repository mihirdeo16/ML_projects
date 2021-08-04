# Recommendation System for Movies
## *Deploy using Docker container and access through API requests:*

**Pull the container from Docker-Hub**
```shell
docker pull asdfg8m8d/simple_recommendation_system_movies
```
Or build and run the container using following steps
```
cd RecomdSys/
docker build -t recommandationsystem .
docker run -d -p 1000:80 recommandationsystem
```
To check the container is running correctly you can use curl utility
```
curl http://localhost:1000/isAlive
>> true
```
ALso in browser you can check: http://localhost:1000/isAlive

If you get **true** in return, Recommandation system is working and can be access throught *curl or web browser*:
>http://localhost:1000/prediction/?f=Transformers:%20War%20For%20Cybertron%20Trilogy
>>Transformers: War for Cybertron: Earthrise


![Terminal Output](https://github.com/mihir-workspace/ML_projects/blob/main/RecomdSys/images/Screenshot%20from%202021-02-17%2000-22-02.png)

#### Or in Brower:
![](https://github.com/mihir-workspace/ML_projects/blob/main/RecomdSys/images/Screenshot%20from%202021-02-17%2000-22-37.png)
