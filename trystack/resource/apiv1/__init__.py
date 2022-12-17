from trystack.trystack import apiv1 as api
from .project import ProjectRsource

api.add_resource(
    ProjectRsource,
    "/projects",
    methods=["GET", "POST"],
    endpoint="projects"
)

api.add_resource(
    ProjectRsource,
    "/project/<project_id>",
    methods=["GET", "PATCH", "DELETE"],
    endpoint="project"
)