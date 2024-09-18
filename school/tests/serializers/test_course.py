from django.test import TestCase
from rest_framework.utils.serializer_helpers import ReturnDict

from school.models.course import CourseModel
from school.serializers.course import CourseSerializer


class CourseSerializerTestCase(TestCase):

    def setUp(self) -> None:
        self.course_model = CourseModel(
            code="Python",
            description="Python course",
            level="B",
        )

        self.course_serializer = CourseSerializer(instance=self.course_model)

    @property
    def data(self):
        data = self.course_serializer.data
        assert isinstance(data, ReturnDict)
        return data

    def test_course_serializer_keys(self):
        """
        Test that checks course serializer attributes.
        """

        expected_keys = {"id", "code", "description", "level"}
        self.assertEqual(self.data.keys(), expected_keys)

    def test_course_serializer_values(self):
        """
        Test that checks course serializer values.
        """

        assert isinstance(self.data, ReturnDict)

        self.assertEqual(self.data["code"], self.course_model.code)
        self.assertEqual(self.data["description"], self.course_model.description)
        self.assertEqual(self.data["level"], self.course_model.level)
