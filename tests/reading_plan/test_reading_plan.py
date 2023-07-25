from tech_news.analyzer.reading_plan import ReadingPlanService  # noqa: F401, E261, E501
import pytest
from unittest.mock import Mock, patch


news_data = [
    {'title': 'Python', 'reading_time': 4},
    {'title': 'Pytest', 'reading_time': 3},
    {'title': 'Selenium', 'reading_time': 10},
    {'title': 'BeautifulSoup', 'reading_time': 15},
]


expected_result = {
    "readable": [
        {
            "unfilled_time": 3,
            "chosen_news": [("Python", 4), ("Pytest", 3)],
        },
        {
            "unfilled_time": 0,
            "chosen_news": [("Selenium", 10)],
        },
    ],
    "unreadable": [("BeautifulSoup", 15)],
}


def test_reading_plan_group_news():
    pass

    mock_find_news = Mock(return_value=news_data)

    with pytest.raises(ValueError):
        ReadingPlanService.group_news_for_available_time(0)

    with patch(
        "tech_news.analyzer.reading_plan.ReadingPlanService._db_news_proxy",
        mock_find_news,
    ):
        result = ReadingPlanService.group_news_for_available_time(10)

    assert result == expected_result
