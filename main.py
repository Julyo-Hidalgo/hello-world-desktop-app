import eel

eel.init('web', allowed_extensions=['.html'])

@eel.expose
def say_hello_py(x):
	print('Hello from %s' % x)

eel.say_hello_js('PYTHON World!')

eel.start('index.html')
