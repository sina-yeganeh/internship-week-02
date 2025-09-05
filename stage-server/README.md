# Internship in APA - Week 01
### Learning Topic
- [Linux Command Line](https://www.udemy.com/course/the-linux-command-line-bootcamp/)
- [Python](https://www.youtube.com/watch?v=_uQrJ0TkZlc&list=PLTjRvDozrdlxj5wgH4qkvwSOdHLOCx10f&index=1)
- [Git](https://www.youtube.com/watch?v=8JJ101D3knE)

### Project
- Create a project in github
- Develop a flask server with three API endpoints:
  - /my-ip: returns client ip
  - /weather: takes location as input and reports the temperature, humidity in response
  - /quote: returns a random quote
  - Flask server should log every request and response
- Deploy flask server using NGINX
- Implement periodic web server log rotation using logrotate.
- Set up a cron job to back up the application’s database daily to a secure location.

## Write-up
In addition to the log rotation I add JSON logging for better analyse. Here is the output of API endpoints:
- `/my-ip`
```json
{
  "ip": "127.0.0.1"
}
```

- `/weather`
```json
{
  "humidity": 10,
  "status": "clear sky",
  "temperature": {
    "feels_like": 30.28,
    "temp": 32.62,
    "temp_kf": null,
    "temp_max": 32.99,
    "temp_min": 32.62
  }
}
```

- `/quote`
```json
{
  "quote": "You make the world a better place by making yourself a better person."
}
```

### Setup NGINX Server
We need a WSGI (**W**eb **S**erver **G**etway **I**nterface) for deploy a Flask app. In this case I use *Gunicorn*. After installation (`sudo apt install gunicorn`), run the service with:
```bash
gunicorn -w 4 -b 127.0.0.1:5000 app:app
```
- `-w`: handel multi requests.
- `-b`: bind to localhost.

Note that if you are using a virutalenv like me, you should install Gunicorn for your virutalenv, else you will get dependency error.

After Gunicorn, I setup Nginx. I grab this ready-to-use config from Chatgpt (creat a file at `/etc/nginx/sites-available/internship-week-01` and copy the config):
```nginx
server {
    listen 80;
    server_name localhost;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

And enable the site:
```bash
sudo ln -s /etc/nginx/sites-available/internship-week-01 /etc/nginx/sites-enabled/
sudo nginx -t # test config
sudo systemctl restart nginx
```
Do not forget to remove the defualt config of Nginx.

Finally I curl the localhost to see if my API works:
```bash
$ curl -i http://127.0.0.1/quote

HTTP/1.1 200 OK
Server: nginx/1.22.1
Date: Tue, 02 Sep 2025 18:00:41 GMT
Content-Type: application/json
Content-Length: 45
Connection: keep-alive

{"quote":"The only easy day was yesterday."}
```

### Corn Job Backup
For secuirty reason, backups can not be in the project folder. Usually we put them in /opt/backups/ directory and change the access (700, or only sudo users). In this project we do not have database, so I am going to backup from logs folder only (just practicing).

I coded a tiny bash [script](./backup.sh) for backuping:
```bash
#!/bin/bash

if [ "$EUID" -ne 0 ]; then
  echo "Please run script as root."
  exit 1
fi

DATE=$(date +%F_%H-%M-%S)
FILENAME="log_backup_$DATE.zip"

zip -r $FILENAME ./logs

if [ ! -d "/opt/backups/" ]; then
  sudo mkdir /opt/backups
fi
sudo mv $FILENAME /opt/backups
sudo chmod 700 /opt/backups

echo "Backup logs successfully"
```

So the next step is to add this script to cron job (cron is a service in linux to run program or script in a specific time). `Crontab` is like a time table for cron. You can add new program to it by:
```bash
sudo crontab -e # -e: edit
```
Every line has this structure (minute, hour, day of month, the month and day of the week):
```
m h  dom mon dow   command
```
So if i want to add a cron to run every day in midnight, It would be like this:

```bash
0 0 * * * /opt/backup/backup.sh
```
