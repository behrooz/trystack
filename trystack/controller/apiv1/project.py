from flask import request

from trystack.trystack import db
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
        project = Project.query.get(project_id)
        if project is None:
            return jsonify(status=404)
        project_schema = ProjectSchema()
        return jsonify(
            {"project":project_schema.dump(project)}
        )

    @json_required
    def create_project():
        project_schema = ProjectSchema(only=["name"])        
        request_data = project_schema.load(request.get_json())
        project = Project.query.filter_by(name=request_data["name"]).first()
        if project is not None:
            return jsonify(status=409)
        project = Project(name=request_data["name"])            
        db.session.add(project)
        db.session.commit()
        project_schema = ProjectSchema()
        return jsonify(
            state={"project": project_schema.dump(project)},
            status=201
        )


    @json_required
    def update_project(project_id):        
        project_schema = ProjectSchema(only=["status"])
        request_data = project_schema.load(request.get_json())
        project = Project.query.get(project_id)
        if project is None:
            return jsonify(status=404)
        project.status = request_data["status"]
        db.session.commit()
        project_schema = ProjectSchema()
        return jsonify(
            state=project_schema.dump(project),            
        )

    @json_required
    def delete_project(project_id):
        project = Project.query.get(project_id)
        if project is None:
            return jsonify(status=404)
        db.session.delete(project)
        db.session.commit()
        return jsonify(status=204)
        