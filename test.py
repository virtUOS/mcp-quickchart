from typing import dataclass_transform
import requests
import json

QUICKCHART_URL = "https://quickchart.io/chart"


def chart(type: str, datasets: list[dict], labels: list[str]):
    data = {"type": type, "data": {}}
    data["data"]["labels"] = labels
    data["data"]["datasets"] = datasets
    print(json.dumps(data))
    params = {"c": json.dumps(data)}
    response = requests.get(QUICKCHART_URL, params=params)

    response.raise_for_status()

    with open("chart.png", "wb") as f:
        f.write(response.content)
    print("Image downloaded successfully!")


if __name__ == "__main__":
    chart(
        type="bar",
        labels=["Jan", "Feb", "Mar"],
        datasets=[
            {"label": "Test", "data": [10, 20, 15]},
            {"label": "Second", "data": [1, 2, 3]},
        ],
    )
