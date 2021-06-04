import json
import random
import unittest


def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

# Un test unitaire pour la demo
class RandomTest(unittest.TestCase):

    def test_choice(self):
        liste = list(range(10))
        elt = random.choice(liste)
        self.assertIn(elt, liste)

