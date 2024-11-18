from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom

with Diagram("",
             show=False,
             direction="LR",
             outformat="png",
             filename="diagrams/webex_sdk_custom_ui_architecture"):

    # Define icon paths
    user_icon = "../assets/icons/user.png"
    nexus_app_icon = "../assets/icons/cyracom_nexus.png"
    custom_ui_icon = "../assets/icons/custom_web_ui.png"
    cisco_cloud_icon = "../assets/icons/webex_cloud.png"
    interpreter_icon = "../assets/icons/interpreter.png"
    ucce_icon = "../assets/icons/cisco_ucce.png"
    cyracom_api_icon = "../assets/icons/cyracom_direct_api.png"

    # Nodes
    user = Custom("User\n(Doctor/Nurse)", user_icon)
    nexus_app = Custom("CyraCom Nexus", nexus_app_icon)
    custom_ui = Custom("Custom UI\nwith Webex SDK", custom_ui_icon)
    cisco_cloud = Custom("Webex Cloud", cisco_cloud_icon)
    interpreter = Custom("Interpreter", interpreter_icon)
    ucce = Custom("Cisco UCCE", ucce_icon)
    cyracom_api = Custom("CyraCom Direct API", cyracom_api_icon)

    # Diagram structure
    with Cluster("User Device"):
        user >> Edge(label="Uses") >> nexus_app >> Edge(label="Implements") >> custom_ui

    # Connections
    custom_ui >> Edge(label="Connects to") >> cisco_cloud
    cisco_cloud >> Edge(label="Routes Call") >> interpreter
    interpreter >> Edge(label="Operates through") >> ucce

    # Nexus app communicates with CyraCom API
    nexus_app << Edge(label="Session Data") >> cyracom_api

    # Data flows
    user >> Edge(label="Initiate Call") >> nexus_app
    interpreter >> Edge(label="Video Stream") << custom_ui
