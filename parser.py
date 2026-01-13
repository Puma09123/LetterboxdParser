import json
import requests
from bs4 import BeautifulSoup


def get_user_ratings(username):
    """
    Получает имя пользователя Letterboxd и возвращает
    список фильмов с пользовательскими оценками.
    """
    url = f"https://letterboxd.com/{username}/films/"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Не удалось загрузить страницу пользователя")

    soup = BeautifulSoup(response.text, "html.parser")
    films = []

    posters = soup.find_all("li", class_="poster-container")

    for poster in posters:
        film_name = poster.get("data-film-name")
        rating = poster.get("data-user-rating")

        films.append({
            "title": film_name,
            "rating": rating
        })

    return films

def save_to_json(data, filename="results.json"):
    """
    Сохраняет результаты парсинга в JSON-файл.
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    username = "letterboxd_username"  # замените на реальное имя пользователя
    films = get_user_ratings(username)
    save_to_json(films)
    print("Данные сохранены в файл results.json")
