from ai.recommender import recommend_places


def test_recommendations():
    result = recommend_places(["mountains"])

    assert len(result) > 0
    assert "Шымбулак" in result