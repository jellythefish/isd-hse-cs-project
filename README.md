# Txt-Convertify

Txt-Convertify - веб-сервис, выполняющий конвертацию текстового файла одной кодировки в текстовый файл другой выбранной кодировки.



## Установка:

#### 1. Скопируйте файлы проекта с помощью команды в консоли, если у вас Mac OS X или Linux:

   ```bash
git clone https://github.com/jellythefish/isd-hse-cs-project.git
   ```

   Если же у вас Windows, то скачайте zip-архив с проектом: 

   Ссылка: [Txt-Convertify](https://github.com/jellythefish/isd-hse-cs-project/archive/master.zip)

   

#### 2. Установите Python:

Если Вы пользуетесь Linux или Mac OS X, все уже готово в Вашей системе. Если Вы пользователь Windows, Вы можете скачать установочный файл с домашней страницы Python:

- Зайдите на [python.org](https://www.python.org/)

- В секции Downloads, выберите Download for xxx Python "3.xxx".

- После загрузки файла запустите его.

- На первой странице инсталлятора выберите чекбокс "Add Python 3.xxx to PATH".

- Нажмите *Install*, затем нажмите *Close* когда установка закончится.

  

#### 3. Перейдите в папку с проектом через командную строку с помощью команды (например, если папка с репозиторием в папке "Загрузки"):

   Если репозиторий загружен через **git clone**:

   ```bash
cd C:\Users\[Username]\Downloads\isd-hse-cs-project 
   ```

   Если репозиторий скачан как zip по ссылке и разархивирован в папку "Загрузки":

   ```bash
cd C:\Users\[Username]\Downloads\isd-hse-cs-project-master
   ```

#### 4.  Далее, установите зависимости с помощью команды:

```bash
pip install -r requirements.txt
```

#### 5. Затем в папке с проектом введите команду в консоли для запуска локального веб-сервера:

```bash
cd C:\Users\[Username]\Downloads\isd-hse-cs-project 
python run-server.py
```

   Это приведет к запуску локального веб-сервера по адресу http://127.0.0.1:5000.



## Использование:

Для использования конвертера нужно воспользоваться в консоли утилитой curl. Если ее у вас нет, то она также лежит в папке с проектом. Запустить ее можно из папки bin, то есть:

```bash
isd-hse-cs-project\curl\bin\curl.exe
```

Далее посылается POST-запрос на сервер в виде:

```bash
curl -F file=@<filename> http://127.0.0.1:5000/convert/<output-type> -o <output-filename>
```

Где

<**filename**>- абсолютный путь до текстового файла,

<**output-type**> - конечная кодировка файла,

<**output-filename**> - имя файла на выходе.

В итоге сконвертированный файл окажется в вашей текущей директории (директории на момент запуска команды curl) в виде **output-filename**.txt

 