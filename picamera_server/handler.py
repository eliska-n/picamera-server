import logging
import aiohttp.web
import jinja2
import os

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
		web_app.router.add_get('/image/{image_name}', self.get_image)

	async def index(self, request):
		template = self.Jinja2Env.get_template("index.html")
		return aiohttp.web.Response(
			body=template.render(),
			content_type="text/html"
		)

	async def capture(self, request):
		image_name = self.App.CaptureService.capture()
		print(image_name)
		return aiohttp.web.json_response({"image_name": image_name})

	async def get_image(self, request):
		image_name = request.match_info["image_name"]
		abs_path = os.path.abspath("./data/{}".format(image_name))
		template = self.Jinja2Env.get_template("show_image.html")
		return aiohttp.web.Response(
			body=template.render({"image_path": "file://{}".format(abs_path)}),
			content_type="text/html"
		)
