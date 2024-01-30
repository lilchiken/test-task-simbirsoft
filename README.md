# test-task-simbirsoft

## quick start:
1. sudo docker compose -f docker-compose.yml up -d
2. python3 -m venv venv
3. source venv/bin/activate
4. pip install -r requirements.txt
5. pip install ./lib
6. cd src
7. mkdir allure
8. pytest --alluredir=allure/
9. Посмотреть вывод allure  
    Либо allure serve allure (предпочтительный)  
    Либо sudo bash ./send_results.sh и заходим на http://localhost:5252  
