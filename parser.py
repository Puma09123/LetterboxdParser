def get_user_ratings(username):
    """
    Получает имя пользователя Letterboxd и возвращает
    HTML-страницу с оценками пользователя.
    """
    url = f"https://letterboxd.com/{username}/films/"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Не удалось загрузить страницу пользователя")

    return response.text
