from flask import Blueprint
from sqlalchemy import or_

from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.assignments import Assignment, AssignmentStateEnum, Teacher

from .schema import AssignmentGradeSchema, AssignmentSchema, TeacherListSchema

principal_assignments_resources = Blueprint('principal_assignments_resources', __name__)



@principal_assignments_resources.route('/assignments', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_assignments(p):
    """Returns all submitted and graded assignments"""
    list_of_submitted_and_graded_assignments = Assignment.filter(or_(Assignment.state == AssignmentStateEnum.SUBMITTED, Assignment.state == AssignmentStateEnum.GRADED)).all()
    principal_assignments_dump = AssignmentSchema().dump(list_of_submitted_and_graded_assignments, many=True)
    return APIResponse.respond(data=principal_assignments_dump)

@principal_assignments_resources.route('/teachers', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_teachers(p):
    """List all the teachers"""
    list_of_all_teachers = Teacher.query.all()
    principal_teachers_dump = TeacherListSchema().dump(list_of_all_teachers, many=True)
    return APIResponse.respond(data=principal_teachers_dump)


@principal_assignments_resources.route('/assignments/grade', methods=['POST'], strict_slashes=False)
@decorators.accept_payload
@decorators.authenticate_principal
def grade_assignment(p, incoming_payload):
    """Grade an assignment"""
    grade_assignment_payload = AssignmentGradeSchema().load(incoming_payload)

    graded_assignment = Assignment.mark_grade(
        _id=grade_assignment_payload.id,
        grade=grade_assignment_payload.grade,
        auth_principal=p
    )
    db.session.commit()
    graded_assignment_dump = AssignmentSchema().dump(graded_assignment)
    return APIResponse.respond(data=graded_assignment_dump)