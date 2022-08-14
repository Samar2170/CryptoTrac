### INSTRUCTIONS

``` bash
docker-compose up
```
This will start the docker containers. You can access the web interface at http://0.0.0.0:1337/ 

### SOME INFO 

1. The docker-compose.yml file is located at the root of the project
2. The .env file will be sent separately to you
3. This project uses a Remotely self hosted Postgresql database instead of sqllite. (Specifically created for this project)
4. The price update script is being run via celery-beat at 30 secs interval.
5. The price alert system is being triggered via post save signals and run as celery tasks. 