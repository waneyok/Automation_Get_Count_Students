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
        tables = browser.find_elements(By.CSS_SELECTOR, "table.MsoTableGrid")
        tb_element = tables[1].find_element(
            By.CSS_SELECTOR, "tr:nth-child(3) td:nth-child(3)"
        )
        print(f"Количество заявлений = {tb_element.text}")
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
        tables = browser.find_elements(By.CSS_SELECTOR, "table.MsoTableGrid")
        tb_element = tables[1].find_element(
            By.CSS_SELECTOR, "tr:nth-child(3.0) td:nth-child(13)"
        )
        print(f"Количество заявлений = {tb_element.text}")
    except Exception as e:
        print(f"Произошла ошибка при выполнении теста: {e}")
test_get_count_students()
test_get_count_negative()
