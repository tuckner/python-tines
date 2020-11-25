#!/usr/bin/env python

import requests
import json

class TinesAPI:
    
    def __init__(self, email="", tenant="", token="", session=None):
        """Create a new Tines instance to talk to the API."""
        self.token = token
        self.tenant = tenant
        self.email = email
        self.headers = {
            "content-type": "application/json",
            "x-user-email": self.email,
            "x-user-token": self.token
        }
        self.params = {}

    def call_api(self, url, method=None, params=None, data=None, **kwargs):
        if method.lower() == "get":
            resp = requests.get(url, params=self.params, headers=self.headers)
        elif method.lower() == "post":
            resp = requests.post(url, params=params, headers=self.headers, data=data)
        elif method.lower() == "put":
            resp = requests.put(url, params=params, headers=self.headers, data=data)
        elif method.lower() == "delete":
            resp = requests.delete(url, params=params, headers=self.headers)        
        if resp.status_code == 200:
            return resp
    
    def list_events(self, **kwargs):
        url = '{}{}'.format(self.tenant, '/api/v1/events')
        resp = self.call_api(url, method='get', params=kwargs)
        return resp

    def get_event(self, id=None):
        url = '{}{}{}'.format(self.tenant, '/api/v1/events/', id)
        resp = self.call_api(url, method='get')
        return resp

    def list_stories(self):
        url = '{}{}'.format(self.tenant, '/api/v1/stories')
        resp = self.call_api(url, method='get')
        return resp

    def get_story(self, id=None):
        url = '{}{}{}'.format(self.tenant, '/api/v1/stories/', id)
        resp = self.call_api(url, method='get')
        return resp

    def export_story(self, id=None):
        url = '{}{}{}{}'.format(self.tenant, '/api/v1/stories/', id, '/export')
        resp = self.call_api(url, method='get')
        return resp

    def list_agents(self, verbose=False):
        if verbose:
            params = {'per_page': '200'}
        else:
            params = {}
        url = '{}{}'.format(self.tenant, '/api/v1/agents')
        resp = self.call_api(url, method='get', params=params)
        return resp

    def get_agent(self, id=None):
        url = '{}{}{}'.format(self.tenant, '/api/v1/agents/', id)
        resp = self.call_api(url, method='get')
        return resp

    def list_events_by_agent(self, id=None, **kwargs):
        url = '{}{}{}{}'.format(self.tenant, '/api/v1/agents/', id, '/events')
        resp = self.call_api(url, method='get', params=params)
        return resp

    def create_agent(self, data=None):
        url = '{}{}'.format(self.tenant, '/api/v1/agents/')
        resp = self.call_api(url, method='post', data=data)
        return resp
    
    def update_agent(self, id=None, data=None):
        url = '{}{}{}'.format(self.tenant, '/api/v1/agents/', id)
        resp = self.call_api(url, method='put', data=data)
        return resp

    def run_agent(self, id=None):
        url = '{}{}{}{}'.format(self.tenant, '/api/v1/agents/', id, '/run')
        resp = self.call_api(url, method='post')
        return resp

    def delete_agent(self, id=None):
        url = '{}{}{}'.format(self.tenant, '/api/v1/agents/', id)
        resp = self.call_api(url, method='delete')
        return resp

    def list_global_resources(self):
        url = '{}{}'.format(self.tenant, '/api/v1/global_resources')
        resp = self.call_api(url, method='get')
        return resp

    def create_global_resource(self, data=None):
        url = '{}{}'.format(self.tenant, '/api/v1/global_resources')
        resp = self.call_api(url, method='post', data=data)
        return resp

    def append_global_resource(self, id=None, data=None):
        url = '{}{}{}{}'.format(self.tenant, '/api/v1/global_resources/', id, '/append')
        resp = self.call_api(url, method='put', data=data)
        return resp

    def delete_global_resource(self, id=None):
        url = '{}{}{}{}'.format(self.tenant, '/api/v1/global_resources/', id)
        resp = self.call_api(url, method='delete')
        return resp
