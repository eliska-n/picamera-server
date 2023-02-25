import logging
import aiohttp.web


L = logging.getLogger(__name__)

#


class PiCamHandler:

	def __init__(self, app, svc):
		web_app = app.WebContainer.WebApp
		self.StreamService = svc
		self.App = app

		web_app.router.add_get('/', self.stream_video)
		web_app.router.add_get('/shoot', self.shoot_a_photo)

	async def stream_video(self, request):
		pass

	async def shoot_a_photo(self, request):
		frame = self.StreamService.get_frame()
		return aiohttp.web.Response(text="shooting")
