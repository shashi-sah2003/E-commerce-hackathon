from django import template
from django.shortcuts import render
from django.template import Template
from django.contrib.auth.models import User
from Product.models import Product , Cart

register = template.Library()

def idToUser(id):
    user = User.objects.get(id=int(id))
    return user

def idToProduct(id):
    product = Product.objects.get(id=id)
    return product.id

def add(carts):
    net = 0
    for cart in carts:
        net += cart.cost
    return net

register.filter('idToUser', idToUser)
register.filter('idToProduct', idToProduct)
register.filter('add', add)