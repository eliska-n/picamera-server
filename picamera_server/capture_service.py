import asab
import logging
import picamera

L = logging.getLogger(__name__)


class CaptureService(asab.Service):

	def __init__(self, app, service_name='CaptureService'):
		super().__init__(app, service_name)

	def capture(self):
		image_name = "img_{}.jpeg".format(self.App.time())
		with picamera.PiCamera() as camera:
			camera.resolution = (640, 480)
			camera.capture("./data/" + image_name)
		return image_name
