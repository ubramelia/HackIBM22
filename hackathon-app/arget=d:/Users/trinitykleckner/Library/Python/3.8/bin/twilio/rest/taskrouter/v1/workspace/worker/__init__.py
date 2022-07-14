# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page
from twilio.rest.taskrouter.v1.workspace.worker.reservation import ReservationList
from twilio.rest.taskrouter.v1.workspace.worker.worker_channel import WorkerChannelList
from twilio.rest.taskrouter.v1.workspace.worker.worker_statistics import WorkerStatisticsList
from twilio.rest.taskrouter.v1.workspace.worker.workers_cumulative_statistics import WorkersCumulativeStatisticsList
from twilio.rest.taskrouter.v1.workspace.worker.workers_real_time_statistics import WorkersRealTimeStatisticsList
from twilio.rest.taskrouter.v1.workspace.worker.workers_statistics import WorkersStatisticsList


class WorkerList(ListResource):

    def __init__(self, version, workspace_sid):
        """
        Initialize the WorkerList

        :param Version version: Version that contains the resource
        :param workspace_sid: The SID of the Workspace that contains the Worker

        :returns: twilio.rest.taskrouter.v1.workspace.worker.WorkerList
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.WorkerList
        """
        super(WorkerList, self).__init__(version)

        # Path Solution
        self._solution = {'workspace_sid': workspace_sid, }
        self._uri = '/Workspaces/{workspace_sid}/Workers'.format(**self._solution)

        # Components
        self._statistics = None

    def stream(self, activity_name=values.unset, activity_sid=values.unset,
               available=values.unset, friendly_name=values.unset,
               target_workers_expression=values.unset, task_queue_name=values.unset,
               task_queue_sid=values.unset, limit=None, page_size=None):
        """
        Streams WorkerInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param unicode activity_name: The activity_name of the Worker resources to read
        :param unicode activity_sid: The activity_sid of the Worker resources to read
        :param unicode available: Whether to return Worker resources that are available or unavailable
        :param unicode friendly_name: The friendly_name of the Worker resources to read
        :param unicode target_workers_expression: Filter by Workers that would match an expression on a TaskQueue
        :param unicode task_queue_name: The friendly_name of the TaskQueue that the Workers to read are eligible for
        :param unicode task_queue_sid: The SID of the TaskQueue that the Workers to read are eligible for
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.taskrouter.v1.workspace.worker.WorkerInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(
            activity_name=activity_name,
            activity_sid=activity_sid,
            available=available,
            friendly_name=friendly_name,
            target_workers_expression=target_workers_expression,
            task_queue_name=task_queue_name,
            task_queue_sid=task_queue_sid,
            page_size=limits['page_size'],
        )

        return self._version.stream(page, limits['limit'])

    def list(self, activity_name=values.unset, activity_sid=values.unset,
             available=values.unset, friendly_name=values.unset,
             target_workers_expression=values.unset, task_queue_name=values.unset,
             task_queue_sid=values.unset, limit=None, page_size=None):
        """
        Lists WorkerInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param unicode activity_name: The activity_name of the Worker resources to read
        :param unicode activity_sid: The activity_sid of the Worker resources to read
        :param unicode available: Whether to return Worker resources that are available or unavailable
        :param unicode friendly_name: The friendly_name of the Worker resources to read
        :param unicode target_workers_expression: Filter by Workers that would match an expression on a TaskQueue
        :param unicode task_queue_name: The friendly_name of the TaskQueue that the Workers to read are eligible for
        :param unicode task_queue_sid: The SID of the TaskQueue that the Workers to read are eligible for
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.taskrouter.v1.workspace.worker.WorkerInstance]
        """
        return list(self.stream(
            activity_name=activity_name,
            activity_sid=activity_sid,
            available=available,
            friendly_name=friendly_name,
            target_workers_expression=target_workers_expression,
            task_queue_name=task_queue_name,
            task_queue_sid=task_queue_sid,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, activity_name=values.unset, activity_sid=values.unset,
             available=values.unset, friendly_name=values.unset,
             target_workers_expression=values.unset, task_queue_name=values.unset,
             task_queue_sid=values.unset, page_token=values.unset,
             page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of WorkerInstance records from the API.
        Request is executed immediately

        :param unicode activity_name: The activity_name of the Worker resources to read
        :param unicode activity_sid: The activity_sid of the Worker resources to read
        :param unicode available: Whether to return Worker resources that are available or unavailable
        :param unicode friendly_name: The friendly_name of the Worker resources to read
        :param unicode target_workers_expression: Filter by Workers that would match an expression on a TaskQueue
        :param unicode task_queue_name: The friendly_name of the TaskQueue that the Workers to read are eligible for
        :param unicode task_queue_sid: The SID of the TaskQueue that the Workers to read are eligible for
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of WorkerInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.WorkerPage
        """
        data = values.of({
            'ActivityName': activity_name,
            'ActivitySid': activity_sid,
            'Available': available,
            'FriendlyName': friendly_name,
            'TargetWorkersExpression': target_workers_expression,
            'TaskQueueName': task_queue_name,
            'TaskQueueSid': task_queue_sid,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data, )

        return WorkerPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of WorkerInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of WorkerInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.WorkerPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return WorkerPage(self._version, response, self._solution)

    def create(self, friendly_name, activity_sid=values.unset,
               attributes=values.unset):
        """
        Create the WorkerInstance

        :param unicode friendly_name: A string to describe the resource
        :param unicode activity_sid: The SID of a valid Activity that describes the new Worker's initial state
        :param unicode attributes: A valid JSON string that describes the new Worker

        :returns: The created WorkerInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.WorkerInstance
        """
        data = values.of({
            'FriendlyName': friendly_name,
            'ActivitySid': activity_sid,
            'Attributes': attributes,
        })

        payload = self._version.create(method='POST', uri=self._uri, data=data, )

        return WorkerInstance(self._version, payload, workspace_sid=self._solution['workspace_sid'], )

    @property
    def statistics(self):
        """
        Access the statistics

        :returns: twilio.rest.taskrouter.v1.workspace.worker.workers_statistics.WorkersStatisticsList
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.workers_statistics.WorkersStatisticsList
        """
        if self._statistics is None:
            self._statistics = WorkersStatisticsList(
                self._version,
                workspace_sid=self._solution['workspace_sid'],
            )
        return self._statistics

    def get(self, sid):
        """
        Constructs a WorkerContext

        :param sid: The SID of the resource to fetch

        :returns: twilio.rest.taskrouter.v1.workspace.worker.WorkerContext
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.WorkerContext
        """
        return WorkerContext(self._version, workspace_sid=self._solution['workspace_sid'], sid=sid, )

    def __call__(self, sid):
        """
        Constructs a WorkerContext

        :param sid: The SID of the resource to fetch

        :returns: twilio.rest.taskrouter.v1.workspace.worker.WorkerContext
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.WorkerContext
        """
        return WorkerContext(self._version, workspace_sid=self._solution['workspace_sid'], sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.WorkerList>'


class WorkerPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the WorkerPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param workspace_sid: The SID of the Workspace that contains the Worker

        :returns: twilio.rest.taskrouter.v1.workspace.worker.WorkerPage
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.WorkerPage
        """
        super(WorkerPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of WorkerInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.taskrouter.v1.workspace.worker.WorkerInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.WorkerInstance
        """
        return WorkerInstance(self._version, payload, workspace_sid=self._solution['workspace_sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.WorkerPage>'


class WorkerContext(InstanceContext):

    def __init__(self, version, workspace_sid, sid):
        """
        Initialize the WorkerContext

        :param Version version: Version that contains the resource
        :param workspace_sid: The SID of the Workspace with the Worker to fetch
        :param sid: The SID of the resource to fetch

        :returns: twilio.rest.taskrouter.v1.workspace.worker.WorkerContext
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.WorkerContext
        """
        super(WorkerContext, self).__init__(version)

        # Path Solution
        self._solution = {'workspace_sid': workspace_sid, 'sid': sid, }
        self._uri = '/Workspaces/{workspace_sid}/Workers/{sid}'.format(**self._solution)

        # Dependents
        self._real_time_statistics = None
        self._cumulative_statistics = None
        self._statistics = None
        self._reservations = None
        self._worker_channels = None

    def fetch(self):
        """
        Fetch the WorkerInstance

        :returns: The fetched WorkerInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.WorkerInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return WorkerInstance(
            self._version,
            payload,
            workspace_sid=self._solution['workspace_sid'],
            sid=self._solution['sid'],
        )

    def update(self, activity_sid=values.unset, attributes=values.unset,
               friendly_name=values.unset, reject_pending_reservations=values.unset,
               if_match=values.unset):
        """
        Update the WorkerInstance

        :param unicode activity_sid: The SID of the Activity that describes the Worker's initial state
        :param unicode attributes: The JSON string that describes the Worker
        :param unicode friendly_name: A string to describe the Worker
        :param bool reject_pending_reservations: Whether to reject the Worker's pending reservations
        :param unicode if_match: The If-Match HTTP request header

        :returns: The updated WorkerInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.WorkerInstance
        """
        data = values.of({
            'ActivitySid': activity_sid,
            'Attributes': attributes,
            'FriendlyName': friendly_name,
            'RejectPendingReservations': reject_pending_reservations,
        })
        headers = values.of({'If-Match': if_match, })

        payload = self._version.update(method='POST', uri=self._uri, data=data, headers=headers, )

        return WorkerInstance(
            self._version,
            payload,
            workspace_sid=self._solution['workspace_sid'],
            sid=self._solution['sid'],
        )

    def delete(self, if_match=values.unset):
        """
        Deletes the WorkerInstance

        :param unicode if_match: The If-Match HTTP request header

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        headers = values.of({'If-Match': if_match, })

        return self._version.delete(method='DELETE', uri=self._uri, headers=headers, )

    @property
    def real_time_statistics(self):
        """
        Access the real_time_statistics

        :returns: twilio.rest.taskrouter.v1.workspace.worker.workers_real_time_statistics.WorkersRealTimeStatisticsList
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.workers_real_time_statistics.WorkersRealTimeStatisticsList
        """
        if self._real_time_statistics is None:
            self._real_time_statistics = WorkersRealTimeStatisticsList(
                self._version,
                workspace_sid=self._solution['workspace_sid'],
            )
        return self._real_time_statistics

    @property
    def cumulative_statistics(self):
        """
        Access the cumulative_statistics

        :returns: twilio.rest.taskrouter.v1.workspace.worker.workers_cumulative_statistics.WorkersCumulativeStatisticsList
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.workers_cumulative_statistics.WorkersCumulativeStatisticsList
        """
        if self._cumulative_statistics is None:
            self._cumulative_statistics = WorkersCumulativeStatisticsList(
                self._version,
                workspace_sid=self._solution['workspace_sid'],
            )
        return self._cumulative_statistics

    @property
    def statistics(self):
        """
        Access the statistics

        :returns: twilio.rest.taskrouter.v1.workspace.worker.worker_statistics.WorkerStatisticsList
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.worker_statistics.WorkerStatisticsList
        """
        if self._statistics is None:
            self._statistics = WorkerStatisticsList(
                self._version,
                workspace_sid=self._solution['workspace_sid'],
                worker_sid=self._solution['sid'],
            )
        return self._statistics

    @property
    def reservations(self):
        """
        Access the reservations

        :returns: twilio.rest.taskrouter.v1.workspace.worker.reservation.ReservationList
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.reservation.ReservationList
        """
        if self._reservations is None:
            self._reservations = ReservationList(
                self._version,
                workspace_sid=self._solution['workspace_sid'],
                worker_sid=self._solution['sid'],
            )
        return self._reservations

    @property
    def worker_channels(self):
        """
        Access the worker_channels

        :returns: twilio.rest.taskrouter.v1.workspace.worker.worker_channel.WorkerChannelList
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.worker_channel.WorkerChannelList
        """
        if self._worker_channels is None:
            self._worker_channels = WorkerChannelList(
                self._version,
                workspace_sid=self._solution['workspace_sid'],
                worker_sid=self._solution['sid'],
            )
        return self._worker_channels

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Taskrouter.V1.WorkerContext {}>'.format(context)


class WorkerInstance(InstanceResource):

    def __init__(self, version, payload, workspace_sid, sid=None):
        """
        Initialize the WorkerInstance

        :returns: twilio.rest.taskrouter.v1.workspace.worker.WorkerInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.WorkerInstance
        """
        super(WorkerInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload.get('account_sid'),
            'activity_name': payload.get('activity_name'),
            'activity_sid': payload.get('activity_sid'),
            'attributes': payload.get('attributes'),
            'available': payload.get('available'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_status_changed': deserialize.iso8601_datetime(payload.get('date_status_changed')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'friendly_name': payload.get('friendly_name'),
            'sid': payload.get('sid'),
            'workspace_sid': payload.get('workspace_sid'),
            'url': payload.get('url'),
            'links': payload.get('links'),
        }

        # Context
        self._context = None
        self._solution = {'workspace_sid': workspace_sid, 'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: WorkerContext for this WorkerInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.WorkerContext
        """
        if self._context is None:
            self._context = WorkerContext(
                self._version,
                workspace_sid=self._solution['workspace_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The SID of the Account that created the resource
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def activity_name(self):
        """
        :returns: The friendly_name of the Worker's current Activity
        :rtype: unicode
        """
        return self._properties['activity_name']

    @property
    def activity_sid(self):
        """
        :returns: The SID of the Worker's current Activity
        :rtype: unicode
        """
        return self._properties['activity_sid']

    @property
    def attributes(self):
        """
        :returns: The JSON string that describes the Worker
        :rtype: unicode
        """
        return self._properties['attributes']

    @property
    def available(self):
        """
        :returns: Whether the Worker is available to perform tasks
        :rtype: bool
        """
        return self._properties['available']

    @property
    def date_created(self):
        """
        :returns: The ISO 8601 date and time in GMT when the resource was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_status_changed(self):
        """
        :returns: The date and time in GMT of the last change to the Worker's activity
        :rtype: datetime
        """
        return self._properties['date_status_changed']

    @property
    def date_updated(self):
        """
        :returns: The ISO 8601 date and time in GMT when the resource was last updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def friendly_name(self):
        """
        :returns: The string that you assigned to describe the resource
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def sid(self):
        """
        :returns: The unique string that identifies the resource
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def workspace_sid(self):
        """
        :returns: The SID of the Workspace that contains the Worker
        :rtype: unicode
        """
        return self._properties['workspace_sid']

    @property
    def url(self):
        """
        :returns: The absolute URL of the Worker resource
        :rtype: unicode
        """
        return self._properties['url']

    @property
    def links(self):
        """
        :returns: The URLs of related resources
        :rtype: unicode
        """
        return self._properties['links']

    def fetch(self):
        """
        Fetch the WorkerInstance

        :returns: The fetched WorkerInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.WorkerInstance
        """
        return self._proxy.fetch()

    def update(self, activity_sid=values.unset, attributes=values.unset,
               friendly_name=values.unset, reject_pending_reservations=values.unset,
               if_match=values.unset):
        """
        Update the WorkerInstance

        :param unicode activity_sid: The SID of the Activity that describes the Worker's initial state
        :param unicode attributes: The JSON string that describes the Worker
        :param unicode friendly_name: A string to describe the Worker
        :param bool reject_pending_reservations: Whether to reject the Worker's pending reservations
        :param unicode if_match: The If-Match HTTP request header

        :returns: The updated WorkerInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.WorkerInstance
        """
        return self._proxy.update(
            activity_sid=activity_sid,
            attributes=attributes,
            friendly_name=friendly_name,
            reject_pending_reservations=reject_pending_reservations,
            if_match=if_match,
        )

    def delete(self, if_match=values.unset):
        """
        Deletes the WorkerInstance

        :param unicode if_match: The If-Match HTTP request header

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete(if_match=if_match, )

    @property
    def real_time_statistics(self):
        """
        Access the real_time_statistics

        :returns: twilio.rest.taskrouter.v1.workspace.worker.workers_real_time_statistics.WorkersRealTimeStatisticsList
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.workers_real_time_statistics.WorkersRealTimeStatisticsList
        """
        return self._proxy.real_time_statistics

    @property
    def cumulative_statistics(self):
        """
        Access the cumulative_statistics

        :returns: twilio.rest.taskrouter.v1.workspace.worker.workers_cumulative_statistics.WorkersCumulativeStatisticsList
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.workers_cumulative_statistics.WorkersCumulativeStatisticsList
        """
        return self._proxy.cumulative_statistics

    @property
    def statistics(self):
        """
        Access the statistics

        :returns: twilio.rest.taskrouter.v1.workspace.worker.worker_statistics.WorkerStatisticsList
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.worker_statistics.WorkerStatisticsList
        """
        return self._proxy.statistics

    @property
    def reservations(self):
        """
        Access the reservations

        :returns: twilio.rest.taskrouter.v1.workspace.worker.reservation.ReservationList
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.reservation.ReservationList
        """
        return self._proxy.reservations

    @property
    def worker_channels(self):
        """
        Access the worker_channels

        :returns: twilio.rest.taskrouter.v1.workspace.worker.worker_channel.WorkerChannelList
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.worker_channel.WorkerChannelList
        """
        return self._proxy.worker_channels

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Taskrouter.V1.WorkerInstance {}>'.format(context)
