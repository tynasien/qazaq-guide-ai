def recommend_places(interests):
    places = {
        "nature": [
            "Чарынский каньон",
            "Бозжыра",
            "Кольсайские озёра"
        ],
        "mountains": [
            "Шымбулак",
            "Медеу",
            "Кольсайские озёра"
        ],
        "history": [
            "Мавзолей Ходжи Ахмеда Ясави",
            "Отрар",
            "Тамгалы"
        ],
        "city": [
            "Бәйтерек",
            "Кок-Тобе",
            "EXPO"
        ]
    }

    recommendations = []

    for interest in interests:
        if interest in places:
            recommendations.extend(places[interest])

    return list(dict.fromkeys(recommendations))