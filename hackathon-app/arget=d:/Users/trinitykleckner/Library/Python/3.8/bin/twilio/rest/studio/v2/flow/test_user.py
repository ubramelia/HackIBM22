# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class FlowTestUserList(ListResource):

    def __init__(self, version, sid):
        """
        Initialize the FlowTestUserList

        :param Version version: Version that contains the resource
        :param sid: Unique identifier of the flow.

        :returns: twilio.rest.studio.v2.flow.test_user.FlowTestUserList
        :rtype: twilio.rest.studio.v2.flow.test_user.FlowTestUserList
        """
        super(FlowTestUserList, self).__init__(version)

        # Path Solution
        self._solution = {'sid': sid, }

    def get(self):
        """
        Constructs a FlowTestUserContext

        :returns: twilio.rest.studio.v2.flow.test_user.FlowTestUserContext
        :rtype: twilio.rest.studio.v2.flow.test_user.FlowTestUserContext
        """
        return FlowTestUserContext(self._version, sid=self._solution['sid'], )

    def __call__(self):
        """
        Constructs a FlowTestUserContext

        :returns: twilio.rest.studio.v2.flow.test_user.FlowTestUserContext
        :rtype: twilio.rest.studio.v2.flow.test_user.FlowTestUserContext
        """
        return FlowTestUserContext(self._version, sid=self._solution['sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Studio.V2.FlowTestUserList>'


class FlowTestUserPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the FlowTestUserPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param sid: Unique identifier of the flow.

        :returns: twilio.rest.studio.v2.flow.test_user.FlowTestUserPage
        :rtype: twilio.rest.studio.v2.flow.test_user.FlowTestUserPage
        """
        super(FlowTestUserPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of FlowTestUserInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.studio.v2.flow.test_user.FlowTestUserInstance
        :rtype: twilio.rest.studio.v2.flow.test_user.FlowTestUserInstance
        """
        return FlowTestUserInstance(self._version, payload, sid=self._solution['sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Studio.V2.FlowTestUserPage>'


class FlowTestUserContext(InstanceContext):

    def __init__(self, version, sid):
        """
        Initialize the FlowTestUserContext

        :param Version version: Version that contains the resource
        :param sid: Unique identifier of the flow.

        :returns: twilio.rest.studio.v2.flow.test_user.FlowTestUserContext
        :rtype: twilio.rest.studio.v2.flow.test_user.FlowTestUserContext
        """
        super(FlowTestUserContext, self).__init__(version)

        # Path Solution
        self._solution = {'sid': sid, }
        self._uri = '/Flows/{sid}/TestUsers'.format(**self._solution)

    def fetch(self):
        """
        Fetch the FlowTestUserInstance

        :returns: The fetched FlowTestUserInstance
        :rtype: twilio.rest.studio.v2.flow.test_user.FlowTestUserInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return FlowTestUserInstance(self._version, payload, sid=self._solution['sid'], )

    def update(self, test_users):
        """
        Update the FlowTestUserInstance

        :param list[unicode] test_users: List of test user identities that can test draft versions of the flow.

        :returns: The updated FlowTestUserInstance
        :rtype: twilio.rest.studio.v2.flow.test_user.FlowTestUserInstance
        """
        data = values.of({'TestUsers': serialize.map(test_users, lambda e: e), })

        payload = self._version.update(method='POST', uri=self._uri, data=data, )

        return FlowTestUserInstance(self._version, payload, sid=self._solution['sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Studio.V2.FlowTestUserContext {}>'.format(context)


class FlowTestUserInstance(InstanceResource):

    def __init__(self, version, payload, sid):
        """
        Initialize the FlowTestUserInstance

        :returns: twilio.rest.studio.v2.flow.test_user.FlowTestUserInstance
        :rtype: twilio.rest.studio.v2.flow.test_user.FlowTestUserInstance
        """
        super(FlowTestUserInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload.get('sid'),
            'test_users': payload.get('test_users'),
            'url': payload.get('url'),
        }

        # Context
        self._context = None
        self._solution = {'sid': sid, }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: FlowTestUserContext for this FlowTestUserInstance
        :rtype: twilio.rest.studio.v2.flow.test_user.FlowTestUserContext
        """
        if self._context is None:
            self._context = FlowTestUserContext(self._version, sid=self._solution['sid'], )
        return self._context

    @property
    def sid(self):
        """
        :returns: Unique identifier of the flow.
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def test_users(self):
        """
        :returns: List of test user identities that can test draft versions of the flow.
        :rtype: list[unicode]
        """
        return self._properties['test_users']

    @property
    def url(self):
        """
        :returns: The URL of this resource.
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self):
        """
        Fetch the FlowTestUserInstance

        :returns: The fetched FlowTestUserInstance
        :rtype: twilio.rest.studio.v2.flow.test_user.FlowTestUserInstance
        """
        return self._proxy.fetch()

    def update(self, test_users):
        """
        Update the FlowTestUserInstance

        :param list[unicode] test_users: List of test user identities that can test draft versions of the flow.

        :returns: The updated FlowTestUserInstance
        :rtype: twilio.rest.studio.v2.flow.test_user.FlowTestUserInstance
        """
        return self._proxy.update(test_users, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Studio.V2.FlowTestUserInstance {}>'.format(context)
