from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom

# Output file formats
output_formats = ["svg", "png"]

# Icon paths
icons_path = "../assets/icons/"
service_icon = f"{icons_path}microservices.png"
config_icon = f"{icons_path}config.png"
secret_icon = f"{icons_path}authentication.png"
placeholder_icon = f"{icons_path}placeholder.png"
api_icon = f"{icons_path}api.png"
redis_icon = f"{icons_path}redis.png"
otel_icon = f"{icons_path}otel.png"
sidecar_icon = f"{icons_path}k8s_sidecar.png"

for out_format in output_formats:
    with Diagram(
        "svc-ccs-calabrio-rta Deployment",
        show=False,
        direction="TB",
        outformat=out_format,
        filename="diagrams/generate_svc_ccs_calabrio_rta_deployment_diagram",
    ):
        with Cluster("Kubernetes Cluster"):
            with Cluster("Pod: svc-ccs-calabrio-rta"):
                rta_service = Custom("svc-ccs-calabrio-rta", service_icon)
                otel_sidecar = Custom("OpenTelemetry Sidecar", sidecar_icon)

            config_map = Custom("ConfigMap", config_icon)
            secret = Custom("Secret", secret_icon)

            config_map >> Edge(label="Env Vars") >> rta_service
            secret >> Edge(label="Secrets") >> rta_service
            config_map >> Edge(style="dashed") >> otel_sidecar

        redis = Custom("Redis", redis_icon)
        info_manager = Custom("CCS Info Manager API", api_icon)
        calabrio_rta = Custom("Calabrio RTA API", api_icon)
        otel_collector = Custom("OpenTelemetry Collector", otel_icon)

        rta_service >> redis
        rta_service >> info_manager
        rta_service >> calabrio_rta
        otel_sidecar >> otel_collector
