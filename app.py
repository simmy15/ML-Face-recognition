from flask import Flask,  render_template 
from flask import Response
from camera import Video
import time
app=Flask(__name__)
pred="sad"
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/')
def gen(camera):
	for i in range(1,16):
		frame=camera.get_frame(i)
		yield(b'--frame\r\n'
		b'Content-Type:  image/jpeg\r\n\r\n' + frame +
		 b'\r\n\r\n')
		time.sleep(3) 
		
	camera.closing()	
	return render_template('index.html', output=pred)

@app.route('/after')
def after():
	return render_template('after.html', output=pred)	
		



@app.route('/video')
def video():
	return Response(gen(Video()),
	mimetype='multipart/x-mixed-replace; boundary=frame')


     


app.run(debug = True)
