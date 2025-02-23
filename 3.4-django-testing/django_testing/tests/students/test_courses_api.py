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
    course_name = courses[0].name

    response = client.get('/api/v1/courses/', {'id': course_id})

    assert response.status_code == 200
    data = response.json()
    assert data[0]['id'] == course_id
    assert data[0]['name'] == course_name


@pytest.mark.django_db
def test_filter_courses_by_id(client, student_factory, course_factory):
    students = student_factory(_quantity=5)
    courses = course_factory(_quantity=3, students=students)
    course1_id = courses[0].id
    course2_id = courses[1].id
    course1_name = courses[0].name
    course2_name = courses[1].name

    response = client.get('/api/v1/courses/', {'id': [course1_id, course2_id]})

    assert response.status_code == 200
    data = response.json()
    assert data[0]['name'] == course1_name
    assert data[1]['name'] == course2_name


@pytest.mark.django_db
def test_filter_courses_by_name(client, student_factory, course_factory):
    students = student_factory(_quantity=5)
    courses = course_factory(_quantity=3, students=students)
    course1_id = courses[0].id
    course2_id = courses[1].id
    course1_name = courses[0].name
    course2_name = courses[1].name

    response = client.get('/api/v1/courses/', {'name': [course1_name, course2_name]})

    assert response.status_code == 200
    data = response.json()
    assert data[0]['id'] == course1_id
    assert data[1]['id'] == course2_id


@pytest.mark.django_db
def test_create_course(client):
    course_data = {
        'name': 'Теоретическая механика',
        'students': [
            {
                'name': 'Даша',
                'birth_date': '2002-06-03'
            },
            {
                'name': 'Наташа',
                'birth_date': '2002-07-22'
            }
        ]
    }

    response = client.post('/api/v1/courses/', course_data, format='json')

    assert response.status_code == 201


@pytest.mark.django_db
def test_update_course(client, student_factory, course_factory):
    students = student_factory(_quantity=5)
    courses = course_factory(_quantity=3, students=students)
    course_id = courses[0].id
    new_data = {
        'name': 'Теоретическая механика',
    }

    response = client.patch(f'/api/v1/courses/{course_id}/', new_data, format='json')

    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_course(client, student_factory, course_factory):
    students = student_factory(_quantity=5)
    courses = course_factory(_quantity=3, students=students)
    course_id = courses[0].id

    response = client.delete(f'/api/v1/courses/{course_id}/', format='json')

    assert response.status_code == 204