E commerce Django app

Welcome to the ecomm app!

To open this application created using the Django framework you have to first open CMD and navigate to the foler that 
contains the app. Then you type in >python manage.py runserver. After that , the app is available by typing in localhost:8000 
in any browser. The first page it opens is a list of all products in database, ordered from cheapest to most expensive.

To add a new product you type the following address in the browser: localhost:8000/addProduct.There you can enter 
a new product as a .json file.

To add a new user you type the following address in the browser: localhost:8000/addUser.There you can enter 
a new user, by entering the required fields as a .json file.

To delete a user or a product, we use the <slug> field. You can sumply type in localhost:8000/<product_slug>/delete
to delete a product or localhost:8000/<user_slug>/delete to delete a user.

This app has been created using Python version 3.8.8 using the Django framework version 4.0.3
