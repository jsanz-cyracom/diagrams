from diagrams import Diagram, Cluster
from diagrams.custom import Custom

# Define output file formats
output_formats = ["svg", "png"]

# Icon paths
icons_path = "../assets/icons/"

golang_icon = f"{icons_path}golang.png"
api_icon = f"{icons_path}api.png"
database_icon = f"{icons_path}database.png"
component_icon = f"{icons_path}component.png"
placeholder_icon = f"{icons_path}placeholder.png"

# Generate diagrams in both SVG and PNG formats
for out_format in output_formats:
    with Diagram(
        "svc-ccs-calabrio-rta Architecture",
        show=False,
        direction="TB",
        outformat=out_format,
        filename="diagrams/generate_svc_ccs_calabrio_rta_component_diagram",
    ):
        # Application components
        main = Custom("main", golang_icon)
        service = Custom("Service", golang_icon)
        api = Custom("Api", api_icon)
        http_server = Custom("HttpServer", golang_icon)
        scheduler = Custom("Scheduler", component_icon)
        state_processor = Custom("StateProcessor", component_icon)
        helper = Custom("Helper", component_icon)
        logger = Custom("Logger", placeholder_icon)
        tracer = Custom("Tracer", placeholder_icon)

        # Plugins
        with Cluster("Plugins"):
            plugin_ccs_api = Custom("PluginCcsApi", api_icon)
            plugin_redis = Custom("PluginRedis", database_icon)
            plugin_calabrio = Custom("PluginCalabrioRta", placeholder_icon)

        # External systems
        with Cluster("External Systems"):
            ccs_manager_api = Custom("CCS Info Manager API", api_icon)
            calabrio_rta = Custom("Calabrio RTA", placeholder_icon)
            redis = Custom("Redis", database_icon)
            otel_collector = Custom("OTel Collector", placeholder_icon)

        # Initialization flow
        main >> service >> http_server >> api

        # Service interactions
        service >> scheduler
        service >> state_processor
        service >> helper
        service >> logger
        service >> tracer
        service >> plugin_ccs_api
        service >> plugin_redis
        service >> plugin_calabrio

        # Plugin communications
        plugin_ccs_api >> ccs_manager_api
        plugin_redis >> redis
        plugin_calabrio >> calabrio_rta
        tracer >> otel_collector
