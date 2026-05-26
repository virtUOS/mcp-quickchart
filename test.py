import requests
import json

QUICKCHART_URL = "https://quickchart.io/chart"


def chart(type: str, datasets: list[list[int]], labels: list[str] = []):
    data = {"type": type, "data": {}}
    if labels:
        data["data"]["labels"] = labels
    data["data"]["datasets"] = [{"data": dataset} for dataset in datasets]
    print(json.dumps(data))
    params = {"c": json.dumps(data)}
    response = requests.get(QUICKCHART_URL, params=params)

    response.raise_for_status()

    with open("chart.png", "wb") as f:
        f.write(response.content)
    print("Image downloaded successfully!")


if __name__ == "__main__":
    chart(type="bar", labels=["Jan", "Feb", "Mar"], datasets=[[10, 20, 15]])
