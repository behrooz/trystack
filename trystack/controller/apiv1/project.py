from flask import request

from trystack.decorator import json_required
from trystack.model import Project
from trystack.util import jsonify
from trystack.scehma.apiv1 import ProjectSchema

class ProjectController():
    @json_required
    def get_projects():
        projects = Project.query.all()
        projects_schema = ProjectSchema(many=True)
        return jsonify(
            {"projects": projects_schema.dump(projects)}
        )

    @json_required
    def get_project(project_id):
        return jsonify(status=501)        
    @json_required
    def create_project():
        return jsonify(status=501)
    @json_required
    def update_project(project_id):
        return jsonify(status=501)
    @json_required
    def delete_project(project_id):
        return jsonify(status=501)
        