# UI-Opencart-automated-tests
UI автотесты проекта Opencart с использованием pytest + selenium  
Подготовка тестового окружения под Windows:
1. Установить Docker Desktop  
2. Перейти в директорию opencart
3. Выполнить команду  
```$Env:OPENCART_PORT=8081; $Env:PHPADMIN_PORT=8888; $Env:LOCAL_IP=$(Get-NetIPAddress -AddressFamily IPv4 -InterfaceAlias 'Беспроводная сеть' | Where-Object {$_.AddressFamily -eq 'IPv4'}).IPAddress; docker-compose up -d```  
4. Убедиться в наличии значений в переменных окружения командой  
```$Env:OPENCART_PORT, $Env:PHPADMIN_PORT, $Env:LOCAL_IP```
5. Скопировать полученныe значения в переменных окружения LOCAL_IP, OPENCART_PORT  
Дополнительная информация:  
Остановить сервисы можно командой ```docker-compose down```  
Удалить данные сервисов можно командой ``` docker volume rm opencart_mariadb_data opencart_opencart_data opencart_opencart_storage_data```

Для локального запуска тестов:  
1. Cоздать виртуальное окружение
2. Установить зависимости командой  
```pip install -r requirements.txt```
3. Выполнить команду подставив ранее скопированные значения переменных окружения  
```pytest --url LOCAL_IP:OPENCART_PORT```
4. Дождаться окончания выполнения тестов

Для генерации и просмотра отчетности через Allure:  
1. Установить и настроить согласно официальной документации: https://allurereport.org/docs/gettingstarted/installation/  
2. После прохождения тестов выполнить команду ```allure generate allure-results -c```  
3. Для просмотра отчета выполнить команду ```allure open .\allure-report\```  

Для запуска тестов с использованием Selenoid:  
1. Проверить, что установлен Docker Desktop
2. Проверить, что запущен Opencart
3. Установить и запустить Selenoid согласно официальной документации: https://aerokube.com/selenoid/latest/  
4. Выполнить команду ```pytest --remote```  
5. Дождаться окончания выполнения тестов  
6. Генерация отчетности через Allure выполняется аналогично 

Для запуска тестов с использованием Jenkins:
1. Проверить, что установлен Docker Desktop
2. Проверить, что запущен Opencart  
3. Проверить, что запущен Selenoid  
4. Выполнить команду  
```docker run -d -p 8082:8080 -p 50000:50000 --restart=on-failure --name jenkins --network=selenoid jenkins/jenkins:lts-jdk17```  
5. Дополнительно установить необходимые пакеты в контейнер jenkins, выполнив последовательно команды  
```
docker exec -it -u 0 jenkins /bin/bash
apt-get update
apt-get install -y docker-compose
apt-get install python3
apt-get install python3-venv
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install allure
```  
6. В UI Jenkins (http://localhost:8082/) создать и настроить Pipeline, скопировав в Script содержимое из Jenkinsfile  
7. Запустить Pipeline, при этом отчетность Allure сгенерируется автоматически  
