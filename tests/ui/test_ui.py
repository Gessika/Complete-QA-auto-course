import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

@pytest.mark.ui 
def test_check_incorrect_username():
    #Створення обьекту для керування бр
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    #Відкриваемо сторінку
    driver.get("https://github.com/login")
    
    #Знаходимо поле, в яке будемо вводити неправильне імя користувача або поштову адресу
    login_elem = driver.find_element(By.ID, "login_field")
    
    #Вводитмо неправильне імя користувача або поштову адресу
    login_elem.send_keys("sergiibutenko@mistakeinemail.com")
    
    #Знаходимо поле, в яке будемо вводити  неправильний пароль
    passw_elem = driver.find_element(By.ID, "password")

    #Вводитмо неправильний пароль
    passw_elem.send_keys("wrong password")
    
    #Знаходимо кнопку sign_in
    btn_elem = driver.find_element(By.NAME, "commit")
    
    #Емулюемо клік лівою кнопкою
    btn_elem.click()
    
    #Перевіряемо, що назва сторінки така, яку ми очікуемо
    assert driver.title == "Sign in to GitHub - GitHub" #атрибут title зберігае в собі заголовок сторінки
    time.sleep(3) #Після написання тесту треба видалити

    #Закриваемо бр
    driver.close()