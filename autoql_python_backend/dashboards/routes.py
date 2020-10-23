from flask import request, jsonify

from autoql_python_backend import app, db
from autoql_python_backend.dashboards.models import Dashboard


@app.route('/dashboards', methods=['POST'])
def create_dashboard():

    try:
        json_data = request.get_json()
        dashboard = Dashboard(json_data['project_id'], json_data['user_id'], json_data['name'], json_data['data'])
    except (KeyError, TypeError):
        return 'Invalid request parameters', 400
    db.session.add(dashboard)
    db.session.commit()
    return jsonify(dashboard.to_dict()), 201


@app.route('/dashboards', methods=['GET'])
def get_dashboards():

    project_id = request.args.get('project_id')
    user_id = request.args.get('user_id')

    if not (project_id and user_id):
        return "project_id and user_id are required", 400

    dashboards = Dashboard.query.filter_by(project_id=project_id, user_id=user_id).all()
    return jsonify([dashboard.to_dict() for dashboard in dashboards]), 200


@app.route('/dashboards/<int:dashboard_id>', methods=['PUT'])
def update_dashboard(dashboard_id):

    dashboard = Dashboard.query.filter_by(id=dashboard_id).first()
    if not dashboard:
        return 'Dashboard not found', 404

    try:
        json_data = request.get_json()
        dashboard.name = json_data['name']
        dashboard.data = json_data['data']
    except (KeyError, TypeError):
        return 'Invalid request parameters', 400

    db.session.add(dashboard)
    db.session.commit()
    return jsonify(dashboard.to_dict()), 200
