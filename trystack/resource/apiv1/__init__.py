from trystack.trystack import apiv1 as api
from .project import ProjectRsource
from .user import UserResource

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

auth_routes = ["/register", "/login"]
api.add_resource(UserResource, *auth_routes)

# api.add_resource(
#     UserResource,
#     "/register",
#     methods=["POST"],
#     endpoint="register"
# )

# api.add_resource(
#     UserResource,
#     "/login",
#     methods=["POST"],
#     endpoint="login"
# )