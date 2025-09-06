# Internship in APA - Week 02
### Learning Topics:
- SSH
  - Local Port Forwarding
  - Remote Port Forwarding
  - SSH Tunneling
  - SOCKS Proxy via SSH
  - Passwordless Authentication
  - File Transfer using scp
  - SSH Agent Forwarding
- Docker Topics:
  - [Docker](https://www.youtube.com/watch?v=SXwC9fSwct8)
  - [Docker Compose](https://www.youtube.com/watch?v=SXwC9fSwct8)

### Project:
- Create 4 Docker containers:
  - Developer 1
  - Developer 2
  - Stage Server
  - Jump Server
- Create a project in github
- Stage Server: Add project from last week into this container
- Developer 1: Create a python script that connects to Jump Server using SSH agent forwarding and keeps trying if fails or disconnected
- Developer 2: Create a python script that connects to Jump Server using passwordless authentication and keeps trying if fails or disconnected
- Developer 2 ➜ Add functionality to the script that forwards Stage Server’s API server port into developer2 container


## Write-up
```bash
# To-do
```