# djcommerce
djcommerce is an E-commerce website made with django


### Setup
```bash
 git clone [repo-url]
 pip install requirements.txt
```
Delete the sqlite3.db and migrations folder( if present )

Make sure that you are inside the virtual environment. You can use pycharm ide for the same.

Once all the pip requirements are satisfies, run the following commands
```bash
 python manage.py createsuperuser #( this creates a super user that can login to the admin dashboard )
 python manage.py makemigrations
 python manage.py migrate
 python manage.py runserver
```
Now visit http://localhost:8000 and your djcommerce app will just work fine!

## Features and Functionalities

- Homepage showing list of products
- Add to product to cart
- Checkout page displaying the order details
- Apply coupon codes at the time of checkout
- Add Shipping and Billing address ( also save for future use )
- Add payment details with stripe ( also save card for future use )

More functionalities will be added in the later commits!!!

Guide to deploy the application on pythonanywhere for free : [visit here](https://shreyapohekar.com/blogs/deploy-a-django-web-application-on-pythonanywhere-for-free/)
