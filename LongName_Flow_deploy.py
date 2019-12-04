from LongName_Flow import LongName_Flow

LongName_Flow.deploy(
    "Flow Schematics", 
    base_image="python:3.7",
    python_dependencies=[],
    registry_url="znicholasbrown",
    image_name="prefect_flow",
    image_tag="displacement-flow",
)