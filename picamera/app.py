import asab
import asab.web


class PiCameraApp(asab.Application):
	def __init__(self):
		super().__init__()
		self.add_module(asab.web.Module)
