# 🎓 Get_Count_Students

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-4.0+-43B02A?style=for-the-badge&logo=selenium&logoColor=white)](https://www.selenium.dev/)

Автоматизированный скрипт тестирования веб-страницы для получения данных о количестве поступающих студентов по выбранной специальности.

---

## Описание проекта

Данный проект представляет собой UI-тест, написанный на **Python** с использованием фреймворка **Selenium WebDriver**. Скрипт осуществляет переход на целевой ресурс и извлекает информацию о количестве поступающих из таблицы данных.

Проект включает в себя:
* **Позитивный тест (`test_get_count_students`)** — валидация извлечения данных по существующей строке таблицы.
* **Негативный тест (`test_get_count_negative`)** — проверка поведения при обращении к несуществующим/некорректным элементам.

---

## Tехнологический стек

* **Язык программирования:** Python
* **Инструмент автоматизации:** Selenium WebDriver
* **Браузер:** Google Chrome

---

## Быстрый старт

### 1. Предварительные требования

Убедитесь, что у вас установлены:
* Python 3.8 или выше
* Браузер Google Chrome

### 2. Установка зависимостей

Клонируйте репозиторий и установите библиотеки:

```bash
# Клонирование репозитория
git clone [https://github.com/waneyok/Automation_Get_Count_Students.git](https://github.com/waneyok/Automation_Get_Count_Students.git)

# Переход в директорию проекта
cd Automation_Get_Count_Students

# Установка Selenium
pip install selenium

```

---

## Запуск тестов

Вы можете запустить тесты с помощью `pytest` или напрямую через Python:

### Запуск через pytest *(рекомендуется)*:

```bash
pytest script.py

```

### Прямой запуск:

```bash
python script.py

```

---

## Структура тестов

| Функция | Тип теста | Описание |
| --- | --- | --- |
| `test_get_count_students()` | **Позитивный** | Переходит в раздел «ИНФОРМАЦИЯ ДЛЯ ПОСТУПАЮЩИХ» и извлекает ячейку таблицы `tr:3, td:3`. |
| `test_get_count_negative()` | **Негативный** | Проверяет обработку ошибок при обращении к некорректным ячейкам таблицы. |

---

## Автор

* **Проект:** Automation_Get_Count_Students
* **Цель:** Отработка навыков UI-автоматизации на Python + Selenium.

```
