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
nexus_icon = f"{icons_path}cyracom_nexus.png"  # New icon for Nexus

# Generate diagrams in both SVG and PNG formats
for out_format in output_formats:
    with Diagram(
        "svc-ccs-air Component Architecture",
        show=False,
        direction="TB",
        outformat=out_format,
        filename=f"diagrams/generate_svc_ccs_air_component",
    ):

        # Define major clusters with spacing
        with Cluster("Cisco"):
            ucce_cti_server = Custom("UCCE CTI Server", cisco_ucce_icon)

        with Cluster("Messaging & Processing"):
            with Cluster("(TCP Listener & AMQP Publisher)"):
                svc_ccs_agents = Custom("svc-ccs-agents", svc_ccs_agents_icon)

            with Cluster("RabbitMQ Messaging Queue"):
                rabbitmq = Custom("RabbitMQ", rabbitmq_icon)

            with Cluster("(AMQP Consumer & CCS Syncer)"):
                svc_ccs_air = Custom("svc-ccs-air", svc_ccs_air_icon)

        with Cluster("Data Stores"):
            ha_redis = Custom("Redis (Distributed Cache)", redis_icon)

        with Cluster("CCS System"):
            ccs = Custom("CCS Platform", ccs_icon)

        with Cluster("Other Consumers"):
            nexus = Custom("Nexus", nexus_icon)

        # Define interactions with better separation
        ucce_cti_server >> svc_ccs_agents  # UCCE CTI sends TCP events to svc-ccs-agents
        svc_ccs_agents >> rabbitmq  # svc-ccs-agents publishes messages to RabbitMQ
        svc_ccs_air << rabbitmq  # svc-ccs-air consumes messages from RabbitMQ
        svc_ccs_air >> ccs  # svc-ccs-air sends SOAP updates to CCS
        svc_ccs_agents >> ha_redis  # svc-ccs-agents updates Redis with latest agent state
        svc_ccs_air << ha_redis  # svc-ccs-air checks Redis before sending updates
        
        # Nexus consuming real-time messages and agent state
        nexus << rabbitmq  # Nexus listens for real-time messages
        nexus << ha_redis  # Nexus retrieves agent states from Redis
