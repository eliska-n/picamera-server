import logging
import aiohttp.web
import jinja2

#

L = logging.getLogger(__name__)

#


class PiCamHandler:

	def __init__(self, app, svc):
		web_app = app.WebContainer.WebApp
		self.App = app

		# Setup Jinja
		self.Jinja2Env = jinja2.Environment(
			loader=jinja2.FileSystemLoader("templates"),
		)

		web_app.router.add_get('/', self.index)
		web_app.router.add_get('/capture', self.capture)

	async def index(self, request):
		template = self.Jinja2Env.get_template("index.html")
		return aiohttp.web.Response(
			body=template.render(),
			content_type="text/html"
		)

	async def capture(self, request):
		image_name = self.App.CaptureService.capture()
		return aiohttp.web.Response(json={"image_name": image_name})
