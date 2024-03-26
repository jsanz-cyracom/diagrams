from diagrams import Diagram, Cluster
from diagrams.custom import Custom

with Diagram(show=False,
             direction="TB",
             outformat="svg",
             filename="docs/diagrams/generate_in_meeting_extension_integration") as diagram:
    
    with Cluster(label=""):
        interpreter = Custom("Interpreter", "../icons/interpreter.png")
        waiting_int = Custom("Waiting", "../icons/waiting.png")
        teams_int = Custom("Microsoft Teams\r\nLink", "../icons/teams.png")
        join_call_int = Custom("Join Call", "../icons/join.png")
        interpretation_int = Custom("Conference", "../icons/conference.png")
        
        interpreter >> waiting_int >> teams_int >> join_call_int >> interpretation_int

    with Cluster(label=""):
        patient = Custom("Patient", "../icons/patient.png")
        teams_pat = Custom("Microsoft Teams", "../icons/teams.png")
        join_call_pat = Custom("Join Call", "../icons/join.png")
        interpreter_join_pat = Custom("Interpreter Joins", "../icons/interpreter.png")
        consultation_pat = Custom("Conference", "../icons/conference.png")
        
        patient >> teams_pat >> join_call_pat >> interpreter_join_pat >> consultation_pat

    with Cluster(label=""):
        doctor = Custom("Doctor", "../icons/doctor.png")
        teams_doc = Custom("Microsoft Teams", "../icons/teams.png")
        in_meeting_ext_doc = Custom("In-Meeting\r\nExtension", "../icons/teams_extension.png")
        authentication_doc = Custom("Auth", "../icons/authentication.png")
        interpreter_request_doc = Custom("Interpreter\r\nRequest", "../icons/request.png")
        cyracom_api_doc = Custom("CyraCom API", "../icons/golang.png")
        interpreter_join_doc = Custom("Interpreter Joins", "../icons/interpreter.png")
        consultation_doc = Custom("Conference", "../icons/conference.png")
        
        doctor >> teams_doc >> in_meeting_ext_doc >> authentication_doc >> interpreter_request_doc
        interpreter_request_doc >> cyracom_api_doc >> interpreter_join_doc >> consultation_doc

diagram