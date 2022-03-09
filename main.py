import machine, time, esp32, http1

# uncomment and enter credentials to use with website, and put url to send data to in 'post_request' below.
# http1.connect_router(user_name1='<enter_wifi_username1>', password1='<enter_wifi_password1>',
#               			  user_name2='<enter_wifi_username2>', password2='<enter_wifi_password2>')

def magnet():
	for i in range(1000):
		magnet_read = esp32.hall_sensor() - 30
		print(magnet_read)
		if magnet_read < -10:
			#http1.http_post_request('door_open')
			print('opened')
			sound()
		elif magnet_read >= -10:
			#http1.http_post_request('door_closed')
			print('closed')
		time.sleep(0.5)

def sound():
	p23 = machine.Pin(23, machine.Pin.OUT)
	speaker = machine.PWM(p23)
	speaker.freq(350)
	# volume, max 512
	speaker.duty(400)
	time.sleep(0.8)
	# disconnects speaker
	speaker.deinit()

magnet()
