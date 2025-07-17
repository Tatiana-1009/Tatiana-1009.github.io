from selenium import webdriver
from selenium.webdriver.common.by import By

def test_recipe():
    driver = webdriver.Chrome()
    driver.get("https://tatiana-1009.github.io/Recipe.html")

    # Название блюда (тег h1), текст: "Простой бутерброд с сыром":
    assert "Простой бутерброд с сыром" == driver.find_element(By.TAG_NAME, "h1").text

    # Раздел "Что нужно":
    assert "Что нужно" in driver.find_element(By.TAG_NAME, "h2").text

    # В абзаце (тег p) перечислите ингредиенты через запятую
    # "Хлеб, сливочное масло, сыр, зелень (по желанию)":
    assert ("Хлеб, сливочное масло, сыр, зелень (по желанию)"
            in driver.find_element(By.TAG_NAME, "body").text)

    # Раздел "Как приготовить" (тег h2):
    assert "Как приготовить" in driver.find_element(By.TAG_NAME, "body").text

    # Разбейте инструкцию на отдельные шаги, каждый в своём абзаце (p):
    # "Намажьте хлеб маслом."
    # "Положите сверху ломтик сыра."
    # "Добавьте зелень, если хотите."
    # "Бутерброд готов!"
    assert ("Намажьте хлеб маслом, Положите сверху ломтик сыра,"
            "Добавьте зелень, если хотите, Бутерброд готов!"
            in driver.find_element(By.TAG_NAME, "body").text)

    driver.quit()
