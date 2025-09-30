"""
"""


import logging
from fastmcp import FastMCP, Client
from fastmcp.server.middleware.timing import DetailedTimingMiddleware

# -----------------------------------------------------------------------------------------

# Global logging configuration
logging.basicConfig(
	level=logging.INFO,
	format='%(levelname)s: %(asctime)s   -   %(name)s   -   %(message)s'
)

# -----------------------------------------------------------------------------------------

# # Importar el codigo de los servidores
# from mcp_geo_http import mcp as geo_mcp
# from mcp_weather_http import mcp as weather_mcp

# Crear proxies para los servidores remotos
geo_remote = FastMCP.as_proxy(Client("https://geohttp.fastmcp.app/mcp"))
weather_remote = FastMCP.as_proxy(Client("https://weatherhttp.fastmcp.app/mcp"))

# -----------------------------------------------------------------------------------------

# Crear el servidor principal
main_mcp = FastMCP(name="RemoteProxyMountDemo",)

# -----------------------------------------------------------------------------------------

# Basic timing for all requests
main_mcp.add_middleware(DetailedTimingMiddleware())

# -----------------------------------------------------------------------------------------

# Mount the remote MCP servers into the main MCP server
main_mcp.mount(geo_remote, prefix="geo")
main_mcp.mount(weather_remote, prefix="weather")

# -----------------------------------------------------------------------------------------

# Run the main MCP server with HTTP transport
if __name__ == "__main__":
    main_mcp.run(transport="http", host="0.0.0.0", port=5000)   # Accesible via http://localhost:8003/mcp

# Example client configuration for connecting to this server:
# "weather-htttp-mcp-server": {
#     "url": "http://localhost:8001/mcp",
#     "type": "http"

# -----------------------------------------------------------------------------------------
