from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

#Fake Restaurants
restaurant = {'name': 'The CRUDdy Crab', 'id': '1'}
restaurants = [{'name': 'The CRUDdy Crab', 'id': '1'}, {'name':'Blue Burgers', 'id':'2'},{'name':'Taco Hut', 'id':'3'}]

#Fake Menu Items
items = [ {'name':'Cheese Pizza', 'description':'made with fresh cheese', 'price':'$5.99','course' :'Entree', 'id':'1'}, {'name':'Chocolate Cake','description':'made with Dutch Chocolate', 'price':'$3.99', 'course':'Dessert','id':'2'},{'name':'Caesar Salad', 'description':'with fresh organic vegetables','price':'$5.99', 'course':'Entree','id':'3'},{'name':'Iced Tea', 'description':'with lemon','price':'$.99', 'course':'Beverage','id':'4'},{'name':'Spinach Dip', 'description':'creamy dip with fresh spinach','price':'$1.99', 'course':'Appetizer','id':'5'} ]
item =  {'name':'Cheese Pizza','description':'made with fresh cheese','price':'$5.99','course' :'Entree', 'id':'1'}

'''
RESTAURANTS
'''
@app.route('/')
@app.route('/restaurants')
def show_all_restaurants():
	#DATABASE CHANGES
	return render_template('all_restaurants.html', restaurants=restaurants)

@app.route('/restaurant/new', methods=['GET','POST'])
def create_restaurant():
	if request.method == 'POST':
		#DATABASE CHANGES
		return redirect(url_for('show_all_restaurants'))
	else:
		return render_template('new_restaurant.html')

@app.route('/restaurant/<int:restaurant_id>/edit', methods=['GET','POST'])
def edit_restaurant(restaurant_id):
	if request.method == 'POST':
		#DATABASE CHANGES
		return redirect(url_for('show_all_restaurants'))
	else:
		return render_template('edit_restaurant.html', restaurant=restaurant)

@app.route('/restaurant/<int:restaurant_id>/delete', methods=['GET','POST'])
def delete_restaurant(restaurant_id):
	if request.method == 'POST':
		#DATABASE CHANGES
		return redirect(url_for('show_all_restaurants'))
	else:
		return render_template('delete_restaurant.html', restaurant=restaurant)

'''
MENU ITEMS
'''
@app.route('/restaurant/<int:restaurant_id>')
@app.route('/restaurant/<int:restaurant_id>/menu')
def show_menu_items(restaurant_id):
	#DATABASE CHANGES
	return render_template('all_menu.html', restaurant_id=restaurant_id, items=items)

@app.route('/restaurant/<int:restaurant_id>/menu/new', methods=['GET','POST'])
def create_menu_item(restaurant_id):
	if request.method == 'POST':
		#DATABASE CHANGES
		return redirect(url_for('show_menu_items', restaurant_id=restaurant_id))
	else:
		return render_template('new_menu_item.html', restaurant_id=restaurant_id)

@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit', methods=['GET','POST'])
def edit_menu_item(restaurant_id, menu_id):
	if request.method == 'POST':
		#DATABASE CHANGES
		return redirect(url_for('show_menu_items', restaurant_id=restaurant_id))
	else:
		return render_template('edit_menu_item.html', restaurant_id=restaurant_id, item=item)

@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete', methods=['GET','POST'])
def delete_menu_item(restaurant_id, menu_id):
	if request.method == 'POST':
		#DATABASE CHANGES
		return redirect(url_for('show_menu_items', restaurant_id=restaurant_id))
	else:
		return render_template('delete_menu_item.html', restaurant_id=restaurant_id, item=item)

if __name__=='__main__':
	app.run(debug=True, host='0.0.0.0', port=5000)
