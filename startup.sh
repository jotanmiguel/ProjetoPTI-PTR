#Clone repository to webserver
git clone https://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@github.com/jotanmiguel/ProjetoPTI-PTR.git

# source ProjetoPTI-PTR/VirtualEnv/Scripts/activate

# sudo apt install python3-pip

# pip3 install Django

# pip3 install djangorestframework

# pip3 install drf_yasg

# pip3 install djongo

# sudo apt-get install libjpeg-dev zlib1g-dev libtiff5-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python3-tk

# pip3 install pillow

# pip3 install "pymongo[srv]"

# Automatically run server on every startup
echo '@reboot /bin/bash -c "source /home/pgpddjjm/ProjetoPTI-PTR/VirtualEnv/Scripts/activate && /usr/bin/python3 /home/pgpddjjm/ProjetoPTI-PTR/Django/manage.py runserver 0.0.0.0:8000"' | crontab -

# Run server
/bin/bash -c "source /home/pgpddjjm/ProjetoPTI-PTR/VirtualEnv/Scripts/activate && /usr/bin/python3 /home/pgpddjjm/ProjetoPTI-PTR/Django/manage.py runserver 0.0.0.0:8000"