from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom

with Diagram("Zoom Integration App - High-Level Architecture",
             show=False,
             direction="LR",
             outformat="png",
             filename="diagrams/zoom_integration_app_high_level_architecture"):

    # Icon paths
    user_icon = "../assets/icons/user.png"
    zoom_client_icon = "../assets/icons/zoom_client.png"  # New icon needed
    zoom_integration_app_icon = "../assets/icons/zoom_integration_app.png"
    wso2_icon = "../assets/icons/wso2.png"  # New icon needed
    citrix_lb_icon = "../assets/icons/citrix_load_balancer.png"  # New icon needed
    kubernetes_icon = "../assets/icons/kubernetes.png"  # New icon needed
    api_gateway_icon = "../assets/icons/api_gateway.png"  # New icon needed
    microservices_icon = "../assets/icons/microservices.png"  # New icon needed
    interpreter_icon = "../assets/icons/interpreter.png"

    # Define nodes
    user = Custom("User", user_icon)
    zoom_client = Custom("Zoom Client", zoom_client_icon)
    zoom_integration_app = Custom("Zoom Integration App\n(Next.js)", zoom_integration_app_icon)
    wso2 = Custom("WSO2 Identity Server", wso2_icon)
    citrix_lb = Custom("Citrix Load Balancer", citrix_lb_icon)
    kubernetes = Custom("Kubernetes Cluster", kubernetes_icon)
    api_gateway = Custom("API Gateway\n(Azure APIM)", api_gateway_icon)
    microservices = Custom("Microservices\n(Golang Services)", microservices_icon)
    interpreter = Custom("Interpreter", interpreter_icon)

    # Diagram structure
    user >> Edge(label="Uses") >> zoom_client >> Edge(label="Selects App") >> zoom_integration_app
    zoom_integration_app >> Edge(label="Auth Request") >> wso2
    zoom_integration_app >> Edge(label="Routed Through") >> citrix_lb >> kubernetes
    zoom_integration_app >> Edge(label="API Calls") >> api_gateway >> microservices
    microservices >> Edge(label="Assigns") >> interpreter
