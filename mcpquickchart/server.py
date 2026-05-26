from mcpquickchart.chart import get_chart_bytes
from mcpquickchart.dataset import Dataset
from fastmcp import FastMCP
from fastmcp.utilities.types import Image

server = FastMCP("quickchart")


@server.tool()
def render_chart(
    labels: list[str],
    datasets: list[Dataset],
    type: str = "bar",
) -> Image:
    """Render a chart image using QuickChart.io API.

    Args:
        labels: List of labels for the chart
        datasets: List of dataset objects with label and data
        type: Chart type (default: "bar")

    Returns:
        Image object containing the chart PNG
    """
    chart_bytes = get_chart_bytes(
        type=type,
        labels=labels,
        datasets=[{"label": ds.label, "data": ds.data} for ds in datasets],
    )
    return Image(data=chart_bytes, format="png")
