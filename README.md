# flask_app_docker_jenkins_sonarqube
### Dockerize the sample python application

Build the image using the following command

```bash
$ docker build -t prateek0912/sample-python:latest .
```

Run the Docker container using the command shown below.

```bash
$ docker run -d -p 7077:5000 prateek0912/sample-python
```

The application will be accessible at the ip `http://<host_ip>:5000`
