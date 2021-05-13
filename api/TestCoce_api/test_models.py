from django.test import TestCase
from api.api_models import Room, generate_unique_code


class RoomModelsTest(TestCase):

     def setUp(self):
        self.test1 = Room.objects.create(
            code=generate_unique_code(),
            host = "I am the host",
            guest_can_pause = True,
            votes_to_skip = 4
        )

    
    
     def test_code_length(self):
        self.assertLessEqual(len(self.test1.code),8)
