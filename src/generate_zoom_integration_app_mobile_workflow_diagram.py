from diagrams import Diagram, Edge
from diagrams.custom import Custom

with Diagram("User Workflow on Mobile Devices",
             show=False,
             direction="LR",
             outformat="png",
             filename="diagrams/zoom_integration_app_mobile_workflow"):

    # Icon paths
    mobile_user_icon = "../assets/icons/mobile_user.png"  # New icon needed
    zoom_mobile_app_icon = "../assets/icons/zoom_mobile_app.png"  # New icon needed
    zoom_integration_app_icon = "../assets/icons/zoom_integration_app.png"
    wso2_icon = "../assets/icons/wso2.png"
    api_gateway_icon = "../assets/icons/api_gateway.png"
    microservices_icon = "../assets/icons/microservices.png"
    interpreter_icon = "../assets/icons/interpreter.png"

    # Nodes
    mobile_user = Custom("Mobile User", mobile_user_icon)
    zoom_mobile_app = Custom("Zoom Mobile App", zoom_mobile_app_icon)
    zoom_integration_app = Custom("Zoom Integration App\n(Next.js)", zoom_integration_app_icon)
    wso2 = Custom("WSO2 Identity Server", wso2_icon)
    api_gateway = Custom("API Gateway\n(Azure APIM)", api_gateway_icon)
    microservices = Custom("Microservices\n(Golang Services)", microservices_icon)
    interpreter = Custom("Interpreter", interpreter_icon)

    # Workflow
    mobile_user >> Edge(label="Opens") >> zoom_mobile_app >> Edge(label="Selects App") >> zoom_integration_app
    zoom_integration_app >> Edge(label="Auth Request") >> wso2
    mobile_user << Edge(label="Displays Interface") << zoom_integration_app
    mobile_user >> Edge(label="Submits Request") >> zoom_integration_app
    zoom_integration_app >> Edge(label="API Call") >> api_gateway >> microservices
    microservices >> Edge(label="Assigns") >> interpreter
    interpreter >> Edge(label="Joins Meeting") >> zoom_mobile_app
