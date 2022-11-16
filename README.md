# Shoppi mart E-Commerce Web Application
## Description
This is a Simple E-Commerce web application creadted with Django Using **MySQL** and **SQLite** as Primary Database.
## Project paths
- For Getting all products Data >  "**/products**"
- For Getting single product Data >  "**/products/:title**"
- For a Cart >  "**/order/cart**"
    - Send a post Rrequest,it will return a cart id.
    - go to **/cart/cart_id/items/**  to get the cart data. First Time it will return empty cart.But You can add products by send product id and quantity in body by post request.
    - To delete any product from cart send a delete request to **cart/:cart_id/items/:product_id**


