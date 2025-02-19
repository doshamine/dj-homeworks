import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Student, Course


@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.prepare(Student, *args, **kwargs)
    return factory

@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, make_m2m=True, *args, **kwargs)
    return factory


@pytest.mark.django_db
def test_list_courses(client, student_factory, course_factory):
    students = student_factory(_quantity=5)
    courses = course_factory(_quantity=3, students=students)

    response = client.get('/api/v1/courses/')

    assert response.status_code == 200
    data = response.json()
    assert len(courses) == len(data)


@pytest.mark.django_db
def test_retrieve_courses(client, student_factory, course_factory):
    students = student_factory(_quantity=5)
    courses = course_factory(_quantity=3, students=students)
    course_id = courses[0].id

    response = client.get('/api/v1/courses/', {'id': course_id})

    assert response.status_code == 200
    data = response.json()


