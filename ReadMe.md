Commands: 
python3 -m venv venv 
source venv/bin/activate 
pip install -r requirements.txt

Скопирайте поля из .env.example Создайте папку .env
 вставте скопированые поля в .env и введите туда свои личные параметры 
 Пример: 
 SECRET_KEY='dwdpokpoklkkoqw' 
 DEBUG=True 
 ALLOWED_HOSTS='127.0.0.1 localhost'

удалите миграции, к сожелению не смог их засунуть в гитигнор, без понятия почему

напишите в командную строку 
python manage.py makemigrations 
python manage.py migrate 
python manage.py runserver