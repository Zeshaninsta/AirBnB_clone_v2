#!/usr/bin/env bash
# sets up web servers for the deployment of web_static
sudo apt-get update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/shared
sudo mkdir -p /data/web_static/releases/test
echo "<html> 
      <head> 
      </head>
      <body> 
        Hello World!
      </body>
     </html>" >> /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sudo sed -i "261 \\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" etc /nginx/sites-available/default
sudo service nginx restart
