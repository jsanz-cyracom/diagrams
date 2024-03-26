from diagrams import Diagram, Cluster
from diagrams.custom import Custom
from diagrams.onprem.network import Internet
from diagrams.programming.language import Python
from diagrams.onprem.client import User

with Diagram(show=False,
             direction="TB",
             outformat="svg", filename="docs/diagrams/generate_tab_extension_integration") as diagram:
    
    with Cluster(label=""):
        interpreter = Custom("Interpreter", "../icons/interpreter.png")
        teams_int = Custom("Microsoft Teams", "../icons/teams.png")
        tab_extension_int = Custom("Tab Extension", "../icons/teams_extension.png")
        authentication_int = Custom("Auth", "../icons/authentication.png")
        waiting_int = Custom("Waiting", "../icons/waiting.png")
        join_call_int = Custom("Join Call", "../icons/join.png")
        interpretation_int = Custom("Conference", "../icons/conference.png")
        
        interpreter >> teams_int >> tab_extension_int >> authentication_int >> waiting_int >> join_call_int >> interpretation_int

    with Cluster(label=""):
        patient = Custom("Patient", "../icons/patient.png")
        teams_pat = Custom("Microsoft Teams", "../icons/teams.png")
        tab_extension_pat = Custom("Tab Extension", "../icons/teams_extension.png")
        authentication_pat = Custom("Auth", "../icons/authentication.png")
        join_call_pat = Custom("Join Call", "../icons/join.png")
        interpreter_join_pat = Custom("Interpreter Joins", "../icons/interpreter.png")
        consultation_pat = Custom("Conference", "../icons/conference.png")
        
        patient >> teams_pat >> tab_extension_pat >> authentication_pat >> join_call_pat >> interpreter_join_pat >> consultation_pat

    with Cluster(label=""):
        doctor = Custom("Doctor", "../icons/doctor.png")
        teams_doc = Custom("Microsoft Teams", "../icons/teams.png")
        tab_extension_doc = Custom("Tab Extension", "../icons/teams_extension.png")
        authentication_doc = Custom("Auth", "../icons/authentication.png")
        patient_join_doc = Custom("Patient Joins", "../icons/patient.png")
        interpreter_request_doc = Custom("Interpreter\r\nRequest", "../icons/request.png")
        rtc_bridge_doc = Custom("RTC Bridge", "../icons/golang.png")
        interpreter_join_doc = Custom("Interpreter Joins", "../icons/interpreter.png")
        consultation_doc = Custom("Conference", "../icons/conference.png")
        
        doctor >> teams_doc >> tab_extension_doc >> authentication_doc >> patient_join_doc >> interpreter_request_doc
        interpreter_request_doc >> rtc_bridge_doc >> interpreter_join_doc >> consultation_doc

diagram
