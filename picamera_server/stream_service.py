import asab
import logging
import picamera

L = logging.getLogger(__name__)


class StreamService(asab.Service):

	def __init__(self, app, service_name='StreamService'):
		super().__init__(app, service_name)



