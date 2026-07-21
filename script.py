from selenium import webdriver
from selenium.webdriver.common.by import By
#Позитивный тест(Данные валидны)
def test_get_count_students():
    # Подключение браузера и ссылки сайта
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get("https://psxt.ucoz.com/")
    # Поиск и проверка нужных элементов
    try:
        need_link = browser.find_element(
            By.LINK_TEXT, "ИНФОРМАЦИЯ ДЛЯ ПОСТУПАЮЩИХ"
        )
        need_link.click()
        tb_element = browser.find_element(
            By.CSS_SELECTOR, "table.MsoTableGrid tr:nth-child(3) td:nth-child(3)"
        )
        print(tb_element)
    except Exception as e:
        print(f"Произошла ошибка при выполнении теста: {e}")
def test_get_count_negative():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get("https://psxt.ucoz.com/")
    try:
        need_link = browser.find_element(
            By.LINK_TEXT, "ИНФОРМАЦИЯ ДЛЯ ПОСТУПАЮЩИХ"
        )
        need_link.click()
        tb_element = browser.find_element(
            By.CSS_SELECTOR, "table.MsoTableGrid tr:nth-child(9) td:nth-child(3)"
        )
        print(tb_element)
    except Exception as e:
        print(f"Произошла ошибка при выполнении теста: {e}")
