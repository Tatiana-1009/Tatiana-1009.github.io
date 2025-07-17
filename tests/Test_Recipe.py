from selenium import webdriver
from selenium.webdriver.common.by import By

def test_recipe01():
    driver = webdriver.Chrome()
    driver.get("https://tatiana-1009.github.io/Recipe.html")
    # Название блюда (тег h1), текст: "Простой бутерброд с сыром":
    assert driver.find_element(By.TAG_NAME, "h1").text == "Простой бутерброд с сыром"
    driver.quit()

def test_recipe02():
    driver = webdriver.Chrome()
    driver.get("https://tatiana-1009.github.io/Recipe.html")
    # Раздел "Что нужно":
    assert driver.find_element(By.TAG_NAME, "h2").text == "Что нужно"
    driver.quit()

def test_recipe03():
    driver = webdriver.Chrome()
    driver.get("https://tatiana-1009.github.io/Recipe.html")
    # В абзаце (тег p) перечислите ингредиенты через запятую
    # "Хлеб, сливочное масло, сыр, зелень (по желанию)":
    assert driver.find_element(By.TAG_NAME, "p").text == "Хлеб, сливочное масло, сыр, зелень (по желанию)"
    driver.quit()

def test_recipe04():
    driver = webdriver.Chrome()
    driver.get("https://tatiana-1009.github.io/Recipe.html")
    # Раздел "Как приготовить" (тег h2):
    assert driver.find_element(By.CSS_SELECTOR, "body > h2:nth-child(4)").text == "Как приготовить"
    driver.quit()

def test_recipe05():
    driver = webdriver.Chrome()
    driver.get("https://tatiana-1009.github.io/Recipe.html")
    # Разбейте инструкцию на отдельные шаги, каждый в своём абзаце (p):
    # "Намажьте хлеб маслом"
    # "Положите сверху ломтик сыра"
    # "Добавьте зелень, если хотите"
    # "Бутерброд готов!"
    assert driver.find_element(By.CSS_SELECTOR, "body > p:nth-child(5)").text == "Намажьте хлеб маслом"
    assert driver.find_element(By.CSS_SELECTOR, "body > p:nth-child(6)").text == "Положите сверху ломтик сыра"
    assert driver.find_element(By.CSS_SELECTOR, "body > p:nth-child(7)").text == "Добавьте зелень, если хотите"
    assert driver.find_element(By.CSS_SELECTOR, "body > p:nth-child(8)").text == "Бутерброд готов!"
    driver.quit()
