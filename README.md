# flask_app_docker_jenkins_sonarqube
# Dockerize the sample python application

Build the image using the following command

```bash
$ docker build -t simple-flask-app:latest .
```

Run the Docker container using the command shown below.

```bash
$ docker run -d -p 5000:5000 simple-flask-app
```

The application will be accessible at the ip `http://<host_ip>:5000`
