from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom

with Diagram("Access to Zoom Integration App from Various Platforms",
             show=False,
             direction="TB",
             outformat="png",
             filename="diagrams/zoom_integration_app_platform_access"):

    # Icon paths
    user_icon = "../assets/icons/user.png"
    desktop_icon = "../assets/icons/desktop.png"  # New icon needed
    web_browser_icon = "../assets/icons/web_browser.png"  # New icon needed
    mobile_device_icon = "../assets/icons/mobile_device.png"  # New icon needed
    zoom_client_icon = "../assets/icons/zoom_client.png"
    zoom_integration_app_icon = "../assets/icons/zoom_integration_app.png"

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

    # Connections to Zoom Client
    desktop_user >> desktop >> zoom_client
    web_user >> web_browser >> zoom_client
    mobile_user >> mobile_device >> zoom_client

    # Zoom Integration App
    zoom_client >> Edge(label="Accesses") >> zoom_integration_app
