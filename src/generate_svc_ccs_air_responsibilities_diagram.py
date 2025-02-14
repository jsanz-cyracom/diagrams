from diagrams import Diagram, Cluster
from diagrams.custom import Custom

# Define output file format
output_formats = ["svg", "png"]

# Define icon paths
icons_path = "../assets/icons/"
rabbitmq_icon = f"{icons_path}rabbitmq.png"
redis_icon = f"{icons_path}database.png"
cisco_ucce_icon = f"{icons_path}cisco_ucce.png"
svc_ccs_agents_icon = f"{icons_path}golang.png"
svc_ccs_air_icon = f"{icons_path}golang.png"
ccs_icon = f"{icons_path}ccs_platform.png"

# Generate diagrams in both SVG and PNG formats
for out_format in output_formats:
    with Diagram(
        "svc-ccs-agents & svc-ccs-air Responsibilities",
        show=False,
        direction="LR",  # Left to Right for better clarity
        outformat=out_format,
        filename=f"diagrams/generate_svc_ccs_air_responsibilities",
    ):

        # UCCE CTI System
        with Cluster("Cisco UCCE CTI System"):
            ucce_cti_server = Custom("UCCE CTI Server", cisco_ucce_icon)

        # Microservices
        with Cluster("Messaging & Processing"):
            with Cluster("svc-ccs-agents (TCP Listener & AMQP Publisher)"):
                svc_ccs_agents = Custom("svc-ccs-agents", svc_ccs_agents_icon)

            with Cluster("RabbitMQ Messaging Queue"):
                rabbitmq = Custom("RabbitMQ", rabbitmq_icon)

            with Cluster("svc-ccs-air (AMQP Consumer & CCS Syncer)"):
                svc_ccs_air = Custom("svc-ccs-air", svc_ccs_air_icon)

        # Data Stores
        with Cluster("Data Stores"):
            ha_redis = Custom("HA Redis (Distributed Cache)", redis_icon)

        # CCS System
        with Cluster("CCS System"):
            ccs = Custom("CCS Platform", ccs_icon)

        # Define interactions
        ucce_cti_server >> svc_ccs_agents  # UCCE CTI sends TCP events to svc-ccs-agents
        svc_ccs_agents >> rabbitmq  # svc-ccs-agents publishes messages to RabbitMQ
        svc_ccs_air << rabbitmq  # svc-ccs-air consumes messages from RabbitMQ
        svc_ccs_air >> ccs  # svc-ccs-air sends SOAP updates to CCS
        svc_ccs_agents >> ha_redis  # svc-ccs-agents updates Redis with latest agent state
        svc_ccs_air << ha_redis  # svc-ccs-air checks Redis before sending updates
