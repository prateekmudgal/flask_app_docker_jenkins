[Unit]
Description=Jenkins Agent

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu
ExecStart=/usr/bin/java -jar /home/ubuntu/agent.jar -url http://3.15.9.194:8080/ -secret 7acc512dbb34dec0e7d5641ad8a725dd226cc220e8bbefc51150996d91804d94 -name dockerengine -workDir "/home/ubuntu"
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target