from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom

# Define output formats
output_formats = ["png", "svg"]

for out_format in output_formats:
    with Diagram("",
                 show=False,
                 direction="LR",
                 outformat=out_format,
                 filename=f"diagrams/webex_widget_architecture"):
        
        # Define icon paths
        user_icon = "../assets/icons/user.png"
        nexus_app_icon = "../assets/icons/cyracom_nexus.png"
        widget_icon = "../assets/icons/webex_meetings_widget.png"
        cisco_cloud_icon = "../assets/icons/webex_cloud.png"
        interpreter_icon = "../assets/icons/interpreter.png"
        ucce_icon = "../assets/icons/cisco_ucce.png"
        cyracom_api_icon = "../assets/icons/cyracom_direct_api.png"

        # Nodes
        user = Custom("User\n(Doctor/Nurse)", user_icon)
        nexus_app = Custom("CyraCom Nexus", nexus_app_icon)
        widget = Custom("Webex Meetings Widget", widget_icon)
        cisco_cloud = Custom("Webex Cloud", cisco_cloud_icon)
        interpreter = Custom("Interpreter", interpreter_icon)
        ucce = Custom("Cisco UCCE", ucce_icon)
        cyracom_api = Custom("CyraCom Direct API", cyracom_api_icon)

        # Diagram structure
        with Cluster("User Device"):
            user >> Edge(xlabel="Uses", tailport="s") >> nexus_app >> Edge(label="Embeds") >> widget

        # Connections
        widget >> Edge(label="Connects to") >> cisco_cloud
        cisco_cloud >> Edge(label="Routes Call") >> interpreter
        interpreter >> Edge(label="Operates through") >> ucce

        # Nexus app communicates with CyraCom API
        nexus_app << Edge(label="Session Data") >> cyracom_api

        # Data flows
        user >> Edge(label="Initiate Call", labeldistance="2") >> nexus_app
        interpreter >> Edge(label="Video Stream") << widget
