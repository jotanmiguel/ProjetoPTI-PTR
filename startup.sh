#Clone repository to webserver
git clone https://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@github.com/jotanmiguel/ProjetoPTI-PTR.git

source ProjetoPTI-PTR/VirtualEnv/Scripts/activate

sudo apt install python3-pip

pip3 install Django

pip3 install djangorestframework

pip3 install drf_yasg

pip3 install djongo

sudo apt-get install libjpeg-dev zlib1g-dev libtiff5-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python3-tk

pip3 install pillow

pip3 install "pymongo[srv]"

#run the django server
python3 ProjetoPTI-PTR/Django/manage.py runserver