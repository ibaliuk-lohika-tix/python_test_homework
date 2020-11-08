import json
from models.models import Context, ContextProfile
import os
import pytest


class Facade:
    def __init__(self):
        self.context = Context()
        self.context.root_path = os.path.abspath(os.path.dirname(__file__))
        with open(f"{self.context.root_path}/test_profile.json") as test_profile:
            self.context.profile = ContextProfile(**json.load(test_profile))


facade = Facade()
