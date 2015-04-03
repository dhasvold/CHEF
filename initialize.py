#! usr/bin/env python3

#############################################################
# 
# Author: John Turner
# Version: 1.0
# Last Updated: 2/18/2015
# 
# This file contains the database initialization script for
# the Recruiter Connect Database. This file will drop, recreate
# and migrate the db, and then insert the data necessary to 
# start working, including:
#	- Creating a SuperUser
#	- Adding the Groups
#	- Adding Users to the Groups
# 
#############################################################

import random
import os
import datetime
import sys

# Initialize the django environment, import the models
os.environ['DJANGO_SETTINGS_MODULE'] = 'chef.settings'
import base_app.models as mod
import django
django.setup()

# grab models that I'll need 
from django.contrib.auth.models import Group, Permission, ContentType
from django.db import connection
import subprocess

# Drop database, recreate it, migrate it
cursor = connection.cursor()
#cursor.execute('DROP SCHEMA PUBLIC2 CASCADE')
#cursor.execute('CREATE SCHEMA PUBLIC')
subprocess.call([sys.executable, 'manage.py', 'migrate'])

#############################################################################
############################## GROUPS/USERS #################################
#############################################################################

Group.objects.all().delete()

############################# ADMINISTRATORS ################################

# Administrators - have full rights to all system
# 	- add superuser to this group
group     = Group()
group.name= "Administrator"
group.save()

# Add all permissions to Admin group
permissions = Permission.objects.all()

for permission in permissions:
	group.permissions.add(permission)

mod.User.objects.all().delete()

# Create superuser with the following credentials:
# 	- username = admin
# 	- password: password
# 	- email = john.duane.turner@gmail.com

# First create a new address and add it to the superuser
address         = mod.Address()
address.address1= '1100 BYU Lane'
address.city    = 'Provo'
address.state   = 'UT'
address.ZIP     = '84606'
address.save() 

user           = mod.User.objects.create_superuser( username='admin', email='test@fake.com', password='password' )
user.first_name= 'Admin'
user.address   = address
user.save()

group.user_set.add(user)

################################# MANAGERS ###################################

# Managers - can add/edit/delete the following:
#	- Events
#	- Areas
# 	- Inventory
#	- Transactions
group = Group()
group.name = 'Manager'
group.save()

# Add permissions for the Managers
# Get content types first
content_types = ContentType.objects.exclude(app_label='auth').exclude(app_label='admin')
content_types.exclude(app_label='base_app', model='User').exclude(app_label='contenttypes').exclude(app_label='sessions')

for content_type in content_types:
	permissions = Permission.objects.filter(content_type=content_type)

	for permission in permissions:
		group.permissions.add(permission)

################################## GUESTS ####################################

# Guests have no permissions, they are used in creating new users
group = Group()
group.name = 'Guest'
group.save()

address = mod.Address()
address.address1 = 'Nowhere'
address.address2 = 'Nowhere'
address.city = 'Nowhere'
address.state = 'UT'
address.ZIP = '84606'

address.save()

# Add a couple of guests
user = mod.User()

user.first_name = 'Joseph'
user.last_name = 'Townson'
user.email = 'fake@fake.com'
user.address = address
user.phone = '7134088245'
user.security_question = 'What is your name'
user.security_answer = 'You already know this, fool'
user.username = 'jobro1'

user.save()
group.user_set.add(user)

user.first_name = 'Sarah'
user.last_name = 'Samsonite'
user.email ='fake@fake.com'
user.address = address
user.phone = '2813308004'
user.security_question = 'What dat password be???'
user.security_answer = 'Haha, got em'
user.username = 'sarahbro1'

user.save()
group.user_set.add(user)

#############################################################################
################################ DUMMY DATA #################################
#############################################################################

################################ INVENTORY ##################################

# Bulk product - musket balls
photo              = mod.Photograph()
photo.place_taken  = "Colonial Heritage Fsetival"
photo.image        = "products/media/product_images/musket_balls.jpg"
photo.description  = "Musket balls for sale!"
photo.photographer = user

photo.save()

specs                 = mod.ProductSpecification()
specs.name            = 'Musket Balls'
specs.price           = 2.0
specs.description     = 'Made to the exact specifications to match what was shot during the Revolutionary War!'
specs.manufacturer    = 'Test manufacturer'
specs.average_cost    = 2.0
specs.sku             = '111'
specs.order_form_name = 'Test order form'
specs.production_time = 'Test production time'
specs.photograph      = photo

specs.save()

inventory                  = mod.Inventory()
inventory.quantity_on_hand = 1
inventory.shelf_location   = 'Corner'
inventory.order_file       = 'Test File'
inventory.condition        = 'Old'
inventory.specs            = specs

inventory.save()

############################ SERIALIZED PRODUCT #############################

# Broom
photo              = mod.Photograph()
photo.place_taken  = "Colonial Heritage Fsetival"
photo.image        = "products/media/product_images/broom.jpg"
photo.description  = "Broom made by one of our very own artisans!"
photo.photographer = user

photo.save()

specs                 = mod.ProductSpecification()
specs.name            = 'Broom'
specs.price           = 2.0
specs.description     = 'Bring a colonial flair to your normal chores!'
specs.manufacturer    = 'Artisan Allen'
specs.average_cost    = 2.0
specs.sku             = '111'
specs.order_form_name = 'Test order form'
specs.production_time = 'Test production time'
specs.photograph      = photo

specs.save()

product                  = mod.SerializedProduct()
product.quantity_on_hand = 1
product.shelf_location   = 'Back Corner'
product.order_file       = 'Test File'
product.condition        = 'Ancient'
product.specs            = specs

product.serial_number = '2222222'
product.cost          = 20.00
product.status        = 'Good'

product.save()

################################## ITEM #####################################

# Item for rent
photo              = mod.Photograph()
photo.place_taken  = "Colonial Heritage Fsetival"
photo.image        = "rentals/media/canon.jpg"
photo.description  = "A canon that really fires!"
photo.photographer = user

photo.save()

specs                 = mod.ProductSpecification()
specs.name            = 'Canon'
specs.price           = 2.0
specs.description     = 'Canon lent to us for rent by the Smithsonian'
specs.manufacturer    = 'Test manufacturer'
specs.average_cost    = 2.0
specs.sku             = '111'
specs.order_form_name = 'Test order form'
specs.production_time = 'Test production time'
specs.photograph      = photo

specs.save()

rental_item                 = mod.Item()
rental_item.quantity_on_hand= 1
rental_item.shelf_location  = 'Front Corner'
rental_item.order_file      = 'Test File'
rental_item.condition       = 'New'
rental_item.specs           = specs

rental_item.standard_rental_price= 2.00
rental_item.times_rented         = 2
rental_item.price_per_day        = 2.00
rental_item.replacement_price    = 2.00

rental_item.save()

# Item not for rent
specs                = mod.ProductSpecification()
specs.name           = 'Full-Sized Replica of the Liberty Bell'
specs.price          = 20000.0
specs.description    = 'Made to the exact dimensions as the actual Liberty Bell. For display only.'
specs.manufacturer   = 'Test manufacturer'
specs.average_cost   = 2.0
specs.sku            = '111'
specs.order_form_name= 'Test order form'
specs.production_time= 'Test production time'

specs.save()

item                 = mod.Item()
item.quantity_on_hand= 1
item.shelf_location  = 'Front Corner'
item.order_file      = 'Test File'
item.condition       = 'New'
item.specs           = specs

item.save()

############################## WARDROBE ITEM ################################

# Man's Jacket
photo              = mod.Photograph()
photo.place_taken  = "Colonial Heritage Fsetival"
photo.image        = "rentals/media/mans_jacket.jpg"
photo.description  = "Colonial era man's jacket!"
photo.photographer = user

photo.save()

specs                 = mod.ProductSpecification()
specs.name            = 'Jacket'
specs.price           = 2.0
specs.description     = "Man's jacket from the 1600's"
specs.manufacturer    = 'H&M'
specs.average_cost    = 2.0
specs.sku             = '111'
specs.order_form_name = 'Test order form'
specs.production_time = 'Test production time'
specs.photograph      = photo

specs.save()

wardrobe_item                 = mod.WardrobeItem()
wardrobe_item.quantity_on_hand= 1
wardrobe_item.shelf_location  = 'Front Right Corner'
wardrobe_item.order_file      = 'Test File'
wardrobe_item.condition       = 'Newest'
wardrobe_item.specs           = specs

wardrobe_item.standard_rental_price= 2.00
wardrobe_item.times_rented         = 2
wardrobe_item.price_per_day        = 2.00
wardrobe_item.replacement_price    = 2.00

wardrobe_item.size         = 38
wardrobe_item.size_modifier= 'S'
wardrobe_item.gender       = 'M'
wardrobe_item.color        = 'White'
wardrobe_item.pattern      = 'Paisely'
wardrobe_item.start_year   = '1677-1-1'
wardrobe_item.end_year     = '1678-1-1'

wardrobe_item.save()

# Man's shirt
photo              = mod.Photograph()
photo.place_taken  = "Colonial Heritage Fsetival"
photo.image        = "rentals/media/mans_shirt.jpg"
photo.description  = "Colonial era man's shirt!"
photo.photographer = user

photo.save()

specs                 = mod.ProductSpecification()
specs.name            = 'Shirt'
specs.price           = 2.0
specs.description     = "Man's dress shirt from the 1600's"
specs.manufacturer    = 'Banana Republic'
specs.average_cost    = 2.0
specs.sku             = '111'
specs.order_form_name = 'Test order form'
specs.production_time = 'Test production time'
specs.photograph      = photo

specs.save()

wardrobe_item                 = mod.WardrobeItem()
wardrobe_item.quantity_on_hand= 1
wardrobe_item.shelf_location  = 'Front Right Corner'
wardrobe_item.order_file      = 'Test File'
wardrobe_item.condition       = 'Newest'
wardrobe_item.specs           = specs

wardrobe_item.standard_rental_price= 3.00
wardrobe_item.times_rented         = 3
wardrobe_item.price_per_day        = 3.00
wardrobe_item.replacement_price    = 3.00

wardrobe_item.size         = 38
wardrobe_item.size_modifier= 'L'
wardrobe_item.gender       = 'M'
wardrobe_item.color        = 'White'
wardrobe_item.pattern      = 'Paisely'
wardrobe_item.start_year   = '1677-1-1'
wardrobe_item.end_year     = '1678-1-1'

wardrobe_item.save()

################################ ADDRESS ####################################

add = mod.Address()
add.address1 = '1000 State St'
add.city = 'Orem'
add.state = 'UT'
add.ZIP = '84606'

add.save()

ven = mod.Venue()
ven.name = 'Provo City Park'
ven.address = add

ven.save()

add = mod.Address()
add.address1 = '1000 University Av'
add.city = 'Provo'
add.state = 'UT'
add.ZIP = '84606'

add.save()

ven = mod.Venue()
ven.name = 'Orem City Park'
ven.address = add

ven.save()

add = mod.Address()
add.address1 = '1000 Brown St'
add.city = 'Park City'
add.state = 'UT'
add.ZIP = '84606'

add.save()

ven = mod.Venue()
ven.name = 'Park City Park'
ven.address = add

ven.save()


#############EVENTS###################################

ev = mod.Event()
ev.name = 'Revolutionary War Reenactment '
ev.related_image = 'events/media/event_photos/revolutionary_war.jpg'
ev.start_date = '2016-1-1'
ev.end_date = '2016-2-1'

ev.save()

#############area1#############################

ar = mod.Area()
ar.name = 'Musket Station'
ar.description = 'Here you can shoot some awesome, black-powder muskets'
ar.event = ev

ar.save()

es = mod.ExpectedSaleItem()
es.name = 'Muskets'
es.related_image = 'events/media/ei_photos/musket.jpg'
es.high_price = 50.00
es.low_price = 40.00
es.area = ar

es.save()

es = mod.ExpectedSaleItem()
es.name = 'Gun Powder'
es.related_image = 'events/media/ei_photos/gun_powder.jpg'
es.high_price = 10.00
es.low_price = 5.00
es.area = ar

es.save()

################AREA2#############################33

ar = mod.Area()
ar.name = 'Sack Race'
ar.description = 'For some reason we are going to have a sack race'
ar.event = ev

ar.save()

es = mod.ExpectedSaleItem()
es.name = 'Potato Sacks'
es.related_image = 'events/media/ei_photos/potato_sacks.jpg'
es.high_price = 3.00
es.low_price = 2.99
es.area = ar

es.save()

es = mod.ExpectedSaleItem()
es.name = 'Special Shoes'
es.related_image = 'events/media/ei_photos/special_shoes.jpg'
es.high_price = 20.00
es.low_price = 15.00
es.area = ar

es.save()

##############EVENT2############################

ev = mod.Event()
ev.name = 'Artisan Breadmaking'
ev.related_image = 'events/media/event_photos/artisan_breadmaking.jpg'
ev.start_date = '2016-2-1'
ev.end_date = '2016-3-1'

ev.save()

#############area1#############################

ar = mod.Area()
ar.name = 'Musket Station'
ar.description = 'Here you can shoot some awesome, black-powder muskets'
ar.event = ev

ar.save()

es = mod.ExpectedSaleItem()
es.name = 'Muskets'
es.related_image = 'events/media/ei_photos/musket.jpg'
es.high_price = 50.00
es.low_price = 40.00
es.area = ar

es.save()

es = mod.ExpectedSaleItem()
es.name = 'Gun Powder'
es.related_image = 'events/media/ei_photos/gun_powder.jpg'
es.high_price = 10.00
es.low_price = 5.00
es.area = ar

es.save()

################AREA2#############################33

ar = mod.Area()
ar.name = 'Sack Race'
ar.description = 'For some reason we are going to have a sack race'
ar.event = ev

ar.save()

es = mod.ExpectedSaleItem()
es.name = 'Potato Sacks'
es.related_image = 'events/media/ei_photos/potato_sacks.jpg'
es.high_price = 3.00
es.low_price = 2.99
es.area = ar

es.save()

es = mod.ExpectedSaleItem()
es.name = 'Special Shoes'
es.related_image = 'events/media/ei_photos/special_shoes.jpg'
es.high_price = 20.00
es.low_price = 15.00
es.area = ar

es.save()





ev = mod.Event()
ev.name = 'Native American Festival'
ev.related_image = 'events/media/event_photos/native_american_festival.jpg'
ev.start_date = '2016-3-1'
ev.end_date = '2016-4-1'

ev.save()


#############area1#############################

ar = mod.Area()
ar.name = 'Musket Station'
ar.description = 'Here you can shoot some awesome, black-powder muskets'
ar.event = ev

ar.save()

es = mod.ExpectedSaleItem()
es.name = 'Muskets'
es.related_image = 'events/media/ei_photos/musket.jpg'
es.high_price = 50.00
es.low_price = 40.00
es.area = ar

es.save()

es = mod.ExpectedSaleItem()
es.name = 'Gun Powder'
es.related_image = 'events/media/ei_photos/gun_powder.jpg'
es.high_price = 10.00
es.low_price = 5.00
es.area = ar

es.save()

################AREA2#############################33

ar = mod.Area()
ar.name = 'Sack Race'
ar.description = 'For some reason we are going to have a sack race'
ar.event = ev

ar.save()

es = mod.ExpectedSaleItem()
es.name = 'Potato Sacks'
es.related_image = 'events/media/ei_photos/potato_sacks.jpg'
es.high_price = 3.00
es.low_price = 2.99
es.area = ar

es.save()

es = mod.ExpectedSaleItem()
es.name = 'Special Shoes'
es.related_image = 'events/media/ei_photos/special_shoes.jpg'
es.high_price = 20.00
es.low_price = 15.00
es.area = ar

es.save()

#############################################################################
############################## TRANSACTIONS #################################
#############################################################################

for data in [

	{'customer': user}

]:

	transaction = mod.Transaction()

	for key in data:

		setattr(transaction, key, data[key])

	transaction.save()

################################# RENTAL #####################################

for data in [

	{'date_out':'2000-01-01 00:00:00', 'due_date': '2001-01-01', 'item':item, 'transaction':transaction, 'amount':40.87},
	{'date_out':'2014-01-01 00:00:00', 'due_date': '2015-02-19', 'item':wardrobe_item, 'transaction':transaction, 'amount':27.29},
	{'date_out':'2014-01-01 00:00:00', 'due_date': '2015-01-20', 'item':wardrobe_item, 'transaction':transaction, 'amount':280.14},

]:

    rental = mod.RentalItem()

    for key in data:

        setattr(rental, key, data[key])

    rental.save()