# mcp-quickchart

An MCP server for rendering chart images using QuickChart.io API.

## Installation

### From PyPI

```bash
pip install mcp-quickchart
```

### From Source

```bash
pip install -e .
```

### Using Docker

```bash
docker build -t mcp-quickchart .
docker run -p 8000:8000 mcp-quickchart
```

## Usage

### As MCP Server

Run the server using `stdio` transport:

```bash
python -m mcpquickchart
```

or after installation:
```bash
mcp-quickchart
```

Or with custom host/port and `streamablehttp` transport:

```bash
export QUICKCHART_MCP_SERVER_HOST=0.0.0.0
export QUICKCHART_MCP_SERVER_PORT=8000
mcp-quickchart
```

### Available Tool

The server provides a `render_chart` tool with the following parameters:

- `labels`: List of labels for the chart
- `datasets`: List of dataset objects with `label` and `data` fields
- `type`: Chart type (default: `"bar"`, supports `"line"`, `"pie"`, etc.)

Returns a PNG image of the rendered chart.

## Configuration

| Environment Variable | Default | Description |
|---------------------|---------|-------------|
| `QUICKCHART_MCP_SERVER_HOST` | `127.0.0.1` | Server bind address |
| `QUICKCHART_MCP_SERVER_PORT` | - | HTTP transport port |

## License

MIT
