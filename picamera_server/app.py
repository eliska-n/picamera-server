import asab
import asab.web

from .stream_service import StreamService
from .handler import PiCamHandler


class PiCameraApp(asab.Application):
	def __init__(self):
		super().__init__()
		self.add_module(asab.web.Module)

		self.WebService = self.get_service("asab.WebService")
		self.WebContainer = asab.web.WebContainer(
                        self.WebService, "web"
                )
		
		self.StreamService = StreamService(self)
		self.Handler = PiCamHandler(self, self.StreamService)