from shop import app as application
if __name__ == '__main__':
	application.run(debug=False, hosts='0.0.0.0', port='8080')