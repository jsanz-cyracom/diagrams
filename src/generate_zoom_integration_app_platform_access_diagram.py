# src/generate_zoom_integration_app_platform_access_diagram.py

from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom

# Common graph attributes
graph_attr = {
    "fontsize": "16",
    "fontname": "Arial",
    "dpi": "300",
    "bgcolor": "white"  # Changed from "transparent" to "white"
}

# Node and edge attributes
node_attr = {
    "fontsize": "16",
    "fontname": "Arial"
}
edge_attr = {
    "fontsize": "14",
    "fontname": "Arial"
}

# Generate both SVG and PNG outputs
for out_format in ["svg", "png"]:
    with Diagram("Access to Zoom Integration App from Various Platforms",
                 show=False,
                 direction="TB",
                 outformat=out_format,
                 filename=f"diagrams/zoom_integration_app_platform_access",
                 graph_attr=graph_attr):

        # Icon paths
        user_icon = "../assets/icons/user.png"
        desktop_icon = "../assets/icons/desktop.png"
        web_browser_icon = "../assets/icons/web_browser.png"
        mobile_device_icon = "../assets/icons/mobile_devices.png"
        zoom_client_icon = "../assets/icons/zoom_client.png"
        zoom_integration_app_icon = "../assets/icons/zoom_integration_app.png"
        cyracom_direct_api_icon = "../assets/icons/cyracom_direct_api.png"

        # Users on different platforms
        with Cluster("Users"):
            desktop_user = Custom("Desktop User", user_icon)
            web_user = Custom("Web Browser User", user_icon)
            mobile_user = Custom("Mobile User", user_icon)

        # Platforms
        desktop = Custom("Desktop App", desktop_icon)
        web_browser = Custom("Web Browser", web_browser_icon)
        mobile_device = Custom("Mobile App", mobile_device_icon)

        # Define Zoom Client and Zoom Integration App
        zoom_client = Custom("Zoom Client", zoom_client_icon)
        zoom_integration_app = Custom("Zoom Integration App", zoom_integration_app_icon)
        cyracom_direct_api = Custom("CyraCom Direct API", cyracom_direct_api_icon)

        # Connections to Zoom Client
        desktop_user >> Edge(**edge_attr) >> desktop >> Edge(**edge_attr) >> zoom_client
        web_user >> Edge(**edge_attr) >> web_browser >> Edge(**edge_attr) >> zoom_client
        mobile_user >> Edge(**edge_attr) >> mobile_device >> Edge(**edge_attr) >> zoom_client

        # Zoom Integration App
        zoom_client >> Edge(label="Accesses", **edge_attr) >> zoom_integration_app

        # Indicate interaction with CyraCom Direct API
        zoom_integration_app >> Edge(label="Uses", style="dashed", **edge_attr) >> cyracom_direct_api
