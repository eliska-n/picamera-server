import asab
import logging
import picamera
import time

L = logging.getLogger(__name__)


class CaptureService(asab.Service):

	def __init__(self, app, service_name='CaptureService'):
		super().__init__(app, service_name)

	def capture(self):
		image_name = "img_{}.jpeg".format(self.App.time())
		with picamera.PiCamera() as camera:
			camera.resolution = (1024, 768)
			camera.rotation = 180
			camera.start_preview()
			time.sleep(1)
			camera.capture("./data/" + image_name)
		return image_name
