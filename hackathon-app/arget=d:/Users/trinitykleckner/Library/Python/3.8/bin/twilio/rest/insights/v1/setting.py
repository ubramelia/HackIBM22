# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class SettingList(ListResource):

    def __init__(self, version):
        """
        Initialize the SettingList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.insights.v1.setting.SettingList
        :rtype: twilio.rest.insights.v1.setting.SettingList
        """
        super(SettingList, self).__init__(version)

        # Path Solution
        self._solution = {}

    def get(self):
        """
        Constructs a SettingContext

        :returns: twilio.rest.insights.v1.setting.SettingContext
        :rtype: twilio.rest.insights.v1.setting.SettingContext
        """
        return SettingContext(self._version, )

    def __call__(self):
        """
        Constructs a SettingContext

        :returns: twilio.rest.insights.v1.setting.SettingContext
        :rtype: twilio.rest.insights.v1.setting.SettingContext
        """
        return SettingContext(self._version, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Insights.V1.SettingList>'


class SettingPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the SettingPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.insights.v1.setting.SettingPage
        :rtype: twilio.rest.insights.v1.setting.SettingPage
        """
        super(SettingPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of SettingInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.insights.v1.setting.SettingInstance
        :rtype: twilio.rest.insights.v1.setting.SettingInstance
        """
        return SettingInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Insights.V1.SettingPage>'


class SettingContext(InstanceContext):

    def __init__(self, version):
        """
        Initialize the SettingContext

        :param Version version: Version that contains the resource

        :returns: twilio.rest.insights.v1.setting.SettingContext
        :rtype: twilio.rest.insights.v1.setting.SettingContext
        """
        super(SettingContext, self).__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = '/Voice/Settings'.format(**self._solution)

    def fetch(self, subaccount_sid=values.unset):
        """
        Fetch the SettingInstance

        :param unicode subaccount_sid: The subaccount_sid

        :returns: The fetched SettingInstance
        :rtype: twilio.rest.insights.v1.setting.SettingInstance
        """
        data = values.of({'SubaccountSid': subaccount_sid, })

        payload = self._version.fetch(method='GET', uri=self._uri, params=data, )

        return SettingInstance(self._version, payload, )

    def update(self, advanced_features=values.unset, voice_trace=values.unset,
               subaccount_sid=values.unset):
        """
        Update the SettingInstance

        :param bool advanced_features: The advanced_features
        :param bool voice_trace: The voice_trace
        :param unicode subaccount_sid: The subaccount_sid

        :returns: The updated SettingInstance
        :rtype: twilio.rest.insights.v1.setting.SettingInstance
        """
        data = values.of({
            'AdvancedFeatures': advanced_features,
            'VoiceTrace': voice_trace,
            'SubaccountSid': subaccount_sid,
        })

        payload = self._version.update(method='POST', uri=self._uri, data=data, )

        return SettingInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Insights.V1.SettingContext {}>'.format(context)


class SettingInstance(InstanceResource):

    def __init__(self, version, payload):
        """
        Initialize the SettingInstance

        :returns: twilio.rest.insights.v1.setting.SettingInstance
        :rtype: twilio.rest.insights.v1.setting.SettingInstance
        """
        super(SettingInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload.get('account_sid'),
            'advanced_features': payload.get('advanced_features'),
            'voice_trace': payload.get('voice_trace'),
            'url': payload.get('url'),
        }

        # Context
        self._context = None
        self._solution = {}

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: SettingContext for this SettingInstance
        :rtype: twilio.rest.insights.v1.setting.SettingContext
        """
        if self._context is None:
            self._context = SettingContext(self._version, )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The account_sid
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def advanced_features(self):
        """
        :returns: The advanced_features
        :rtype: bool
        """
        return self._properties['advanced_features']

    @property
    def voice_trace(self):
        """
        :returns: The voice_trace
        :rtype: bool
        """
        return self._properties['voice_trace']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self, subaccount_sid=values.unset):
        """
        Fetch the SettingInstance

        :param unicode subaccount_sid: The subaccount_sid

        :returns: The fetched SettingInstance
        :rtype: twilio.rest.insights.v1.setting.SettingInstance
        """
        return self._proxy.fetch(subaccount_sid=subaccount_sid, )

    def update(self, advanced_features=values.unset, voice_trace=values.unset,
               subaccount_sid=values.unset):
        """
        Update the SettingInstance

        :param bool advanced_features: The advanced_features
        :param bool voice_trace: The voice_trace
        :param unicode subaccount_sid: The subaccount_sid

        :returns: The updated SettingInstance
        :rtype: twilio.rest.insights.v1.setting.SettingInstance
        """
        return self._proxy.update(
            advanced_features=advanced_features,
            voice_trace=voice_trace,
            subaccount_sid=subaccount_sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Insights.V1.SettingInstance {}>'.format(context)
