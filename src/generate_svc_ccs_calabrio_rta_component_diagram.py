from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom

OUTPUT_FORMATS = ["svg", "png"]
ICON_PATH = "../assets/icons/"

for out_format in OUTPUT_FORMATS:
    with Diagram(
        "svc-ccs-calabrio-rta Architecture",
        show=False,
        direction="TB",
        outformat=out_format,
        filename="diagrams/generate_svc_ccs_calabrio_rta_component_diagram",
    ):
        with Cluster("svc-ccs-calabrio-rta"):
            main = Custom("main", ICON_PATH + "golang.png")
            service = Custom("Service", ICON_PATH + "golang.png")
            api = Custom("Api", ICON_PATH + "api.png")
            http_server = Custom("HttpServer", ICON_PATH + "microservices.png")
            plugin_ccs_api = Custom("PluginCcsApi", ICON_PATH + "api.png")
            plugin_redis = Custom("PluginRedis", ICON_PATH + "database.png")
            helper = Custom("Helper", ICON_PATH + "placeholder.png")
            logger = Custom("Logger", ICON_PATH + "placeholder.png")
            tracer = Custom("Tracer", ICON_PATH + "placeholder.png")

        ccs_api = Custom("CCS API", ICON_PATH + "ccs_platform.png")
        redis = Custom("Redis", ICON_PATH + "database.png")
        otel = Custom("OTel Collector", ICON_PATH + "placeholder.png")

        main >> Edge(label="init") >> service
        service >> api
        api >> http_server
        service >> helper
        service >> logger
        service >> tracer
        http_server >> plugin_ccs_api >> ccs_api
        http_server >> plugin_redis >> redis
        tracer >> otel

