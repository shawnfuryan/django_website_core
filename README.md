## Django 1.8

A base for Django web projects that takes care of many of the boilerplate tasks that every website needs to have done, but which vary little among them.

#### Environment Variables
This project is configured to rely on certain environment variables being set appropriately. These include:

* DJANGO_SECRET_KEY - The secret key that Django uses to lock down many of its security features. You shouldn't really ever need to type this in, so a long randomly generated string is in order.
