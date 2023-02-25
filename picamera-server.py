#!/usr/bin/env python3
import picamera_server

if __name__ == "__main__":
	app = picamera_server.PiCameraApp()
	app.run()