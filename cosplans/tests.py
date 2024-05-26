from django.contrib.auth.models import User
from .models import CosPlan, Cosplay
from rest_framework import status
from rest_framework.test import APITestCase


class CosPlanListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username="emmy", password="pw")
        self.cosplay = Cosplay.objects.create(cosplay_name="Test Cosplay")
    
    def test_can_list_cosplans(self):
        emmy = User.objects.get(username="emmy")
        cosplay = Cosplay.objects.get(cosplay_name="Test Cosplay")
        
        CosPlan.objects.create(
            cosplayer=emmy, 
            cosplay_task="stuff", 
            due_date="2024-05-26", 
            cosplay=self.cosplay 
        )
        response = self.client.get("/cosplans/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_logged_in_user_can_create_cosplan(self):
        self.client.login(username="emmy", password="pw")

        # Create a Cosplay object first for associating the CosPlan
        cosplay = Cosplay.objects.create(cosplay_name="Test Cosplay")
        
        # Include all the fields for creating a CosPlan
        data = {
            "cosplay_task": "a task",
            "due_date": "2024-05-26",
            "cosplay_notes": "Some notes",
            "cosplay": cosplay.id,
        } 

        response = self.client.post("/cosplans/", data, format="json")

        count = CosPlan.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_logged_out_user_cant_create_cosplan(self):
        
        cosplay = Cosplay.objects.create(cosplay_name="Test Cosplay")
        
        data = {
            "cosplay_task": "a task",
            "due_date": "2024-05-26",
            "cosplay_notes": "some notes",
            "cosplay": cosplay.id
        }
        response = self.client.post("/cosplans/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)