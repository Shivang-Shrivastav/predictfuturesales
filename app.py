from flask import Flask, render_template,request
import data_process

app = Flask(__name__)



@app.route('/', methods =['POST','GET'])
def index():

	try:
		if request.method == 'POST':

			item_id = int(request.form.get('item_id'))
			shop_id = int(request.form.get('shop_id'))

			units_sold = data_process.forecast(item_id,shop_id)

			display_msg = 'The forecast for units sold for item id ' + str(item_id) + ' &' +  ' shop id ' + str(shop_id) + ' is:- ' + str(units_sold)

			return render_template('index.html', message = display_msg)

	except:
		return 'Not able to process the data...Check from your end'

	return render_template('index.html')


if __name__ == '__main__':
    app.run(debug = False)
