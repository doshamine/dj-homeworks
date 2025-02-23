from rest_framework import serializers

from students.models import Course, Student


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ("id", "name", "birth_date")

class CourseSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True)

    class Meta:
        model = Course
        fields = ("id", "name", "students")

    def create(self, validated_data):
        students_data = validated_data.pop('students')

        course = Course.objects.create(**validated_data)

        for student_data in students_data:
            student_json = {**student_data, 'course': course}
            Student.objects.create(**student_json)

        return course
