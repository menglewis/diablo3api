# -*- coding: utf-8 -*-
import requests

from diablo3api.resources import Profile, Item, Follower, Artisan


class Diablo3API(object):
    """
    Wrapper Class for the Diablo 3 API
    """

    API_HOST = "https://us.battle.net/api/d3"

    def __init__(self, api_host=API_HOST):
        """
        :param api_host: The location of the Diablo 3 API
        """
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': 'Diablo 3 Python API Wrapper', 'Accept': 'application/json'})
        self.api_host = api_host

        self.profile = self._register(Profile)
        self.item = self._register(Item)
        self.follower = self._register(Follower)
        self.artisan = self._register(Artisan)

    def _register(self, resource):
        """
        Initializes the Resource with the Wrapper classes API Host and Requests Session
        :param resource:
        :return:
        """
        return resource(self.api_host, self.session)
