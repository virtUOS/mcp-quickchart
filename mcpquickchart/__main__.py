from mcpquickchart.server import server
import os

if __name__ == "__main__":
    port = os.getenv("QUICKCHART_MCP_SERVER_PORT")
    host = os.getenv("QUICKCHART_MCP_SERVER_HOST", "127.0.0.1")
    if port:
        server.run(transport="http", host=host, port=int(port))
    else:
        server.run()
