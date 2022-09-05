from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Project, TimeLog


class TestCreateUserAPIView(APITestCase):
    def test_with_post_method_with_correct_arguments(self):
        payload = {
            "username": "testuser",
            "password": "pass",
        }
        response = self.client.post("/user/register/", data=payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["data"].get("username"), "testuser")

    def test_with_post_method_with_only_username(self):
        payload = {"username": "testuser"}
        response = self.client.post("/user/register/", data=payload)
        self.assertEqual(response.data.get("password")[0].code, "required")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_with_post_method_without_arguments(self):
        response = self.client.post("/user/register/")
        self.assertEqual(response.data.get("password")[0].code, "required")
        self.assertEqual(response.data.get("username")[0].code, "required")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TestUserRetrieveUpdateDestroyAPIView(APITestCase):
    user = None

    def setUp(self):
        self.user = User.objects.create_user("testuser", "pass")

    def test_with_unauthenticated_get_method(self):
        response = self.client.get(f"/user/retrieve_update_destroy/{self.user.id}/")
        self.assertEqual(response.data.get("detail").code, "not_authenticated")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_with_get_method(self):
        self.client.force_authenticate(self.user)
        response = self.client.get(f"/user/retrieve_update_destroy/{self.user.id}/")
        self.assertEqual(response.data.get("username"), "testuser")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_with_patch_method_with_correct_arguments(self):
        self.client.force_authenticate(self.user)
        payload = {
            "first_name": "Changed FirstName",
            "last_name": "Changed LastName",
        }
        response = self.client.patch(
            f"/user/retrieve_update_destroy/{self.user.id}/", data=payload
        )
        self.assertEqual(response.data.get("first_name"), "Changed FirstName")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_with_delete_method_with_correct_arguments(self):
        self.client.force_authenticate(self.user)
        response = self.client.delete(f"/user/retrieve_update_destroy/{self.user.id}/")
        self.assertEqual(response.data, None)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class TestProjectAPIView(APITestCase):
    user = None
    project = None

    def setUp(self):
        self.user = User.objects.create_user("testuser", "pass")
        self.project = Project.objects.create(
            title="Test Title", description="Test Description"
        )

    def test_project_with_unauthenticated_get_method(self):
        response = self.client.get("/project/")
        self.assertEqual(response.data.get("detail").code, "not_authenticated")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_project_with_post_method(self):
        self.client.force_authenticate(self.user)
        payload = {
            "title": "Test Title",
            "description": "Test Description",
        }
        response = self.client.post("/project/", data=payload)
        self.assertEqual(response.data.get("data")["title"], "Test Title")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_project_with_authenticated_get_method(self):
        self.client.force_authenticate(self.user)
        response = self.client.get(f"/project/{self.project.id}/")
        self.assertEqual(response.data.get("description"), "Test Description")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestTimelogsAPIView(APITestCase):
    user = None
    project = None

    def setUp(self):
        self.user = User.objects.create_user("testuser", "pass")
        self.project = Project.objects.create(
            title="Test Title", description="Test Description"
        )
        self.timelog = TimeLog.objects.create(
            user=self.user,
            project=self.project,
            work_description="Test Desc",
            date="2022-08-02",
            hours=2.30,
        )

    def test_timelog_with_unauthenticated_get_method(self):
        response = self.client.get("/timelog/")
        self.assertEqual(response.data.get("detail").code, "not_authenticated")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_timelog_with_post_method(self):
        self.client.force_authenticate(self.user)
        payload = {
            "project": self.project.id,
            "work_description": "Test Desc",
            "date": "2022-08-03",
            "hours": 2.30,
            "status": "in_progress",
        }
        response = self.client.post("/timelog/", data=payload)
        self.assertEqual(response.data.get("message"), "Timelog Created Successfully")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_timelog_with_authenticated_get_method(self):
        self.client.force_authenticate(self.user)
        response = self.client.get(f"/timelog/{self.timelog.id}/")
        self.assertEqual(response.data.get("work_description"), "Test Desc")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
