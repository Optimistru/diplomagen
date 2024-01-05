### Генератор дипломов для соревнований по программированию ulivt ###

input: формат данных s4ris  
output: формат docx для печати дипломов

Для настройки необходимо переопределить поля 
SEASON, D1, D2, D3 в файле common/settings.py

Для запуска в полном режиме необходим доступ в базу данных, 
в корень проекта положите файл secdist.json с форматом
`{
  "host": <host>,
  "port": <port>,
  "db_name": <db_name>,
  "user": <user>,
  "password": <password>
}`