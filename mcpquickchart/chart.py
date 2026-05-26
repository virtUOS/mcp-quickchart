from typing import dataclass_transform
import json
import requests

QUICKCHART_URL = "https://quickchart.io/chart"


def get_chart_bytes(type: str, labels: list[str], datasets: list[dict]) -> bytes:
    """Fetch chart image bytes from QuickChart.io API.

    Args:
        type: Chart type (e.g., "bar", "line", "pie")
        labels: List of labels for the chart
        datasets: List of dataset dictionaries

    Returns:
        Raw bytes of the PNG image
    """
    data = {"type": type, "data": {}}
    data["data"]["labels"] = labels
    data["data"]["datasets"] = datasets
    params = {"c": json.dumps(data)}
    response = requests.get(QUICKCHART_URL, params=params)
    response.raise_for_status()
    return response.content
