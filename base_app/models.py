#############################################################
# Author: John Turner
# Version 2.0
#
# Last Updated: Feb 20, 2015
# 
# This file contains all of the models for the chef site.
# Eventually, these models will be split among the other apps.
#############################################################
#
#############################################################
# Changes since Sprint 1:
#
# - Implemented the User class through extending AbstractUser
# - Added Address Class to store all addresses, rather than having the fields in other classes
# - Got rid of Legal Entity
# - Got rid of Person 
# - Got rid of Agent, and added attribute to User class to distinguish agents
# - Added Phone number to the User class and got rid of the Phone Class
# - Reworked the Shopping Cart model/associated classes:
#   - Added Cart Line Item as the items that make up the shopping cart
#   - Shopping Cart is no longer associated with a Transaction
# - Reworked the Products/Items classes:
#   - All products/items inherit from superclass called Inventory
#   - Inventory is associated with Product Specification, which describes the Inventory
#   - Product Specification is associated with Category for type of items
#   - Item, by default contains non-wardrobe items. Wardrobe Item inherits from Item.
#   - Items are distinguished as rentable by not having null in several attributes
# - Reworked the Transaction/Order/Rental classes:
#   - Changed the name of "order" to "transaction"
#   - Added Line Items, which can either be a fee, rental, or sale (see classes that inherit from LineItem)
#   - Added a fee class which is the superclass for damage fees and late fees
#   - Added a FK in the RentalItem class to User which indicates the Agent that processes the return of a rental
# - Reworked the Events area:
#   - Events are tied to Public Events to allow for templating of events that are needed multiple times
# - Added more detailed comments for each class overall
# - Minor attribute changes including types of fields and naming of the attributes
# - Added several new methods to several classes to match new SD's. 
#############################################################
#
#############################################################
# John's Changes since Sprint 3
# 
# - Made Shopping Cart (and all related models) transient through tying it to the session
# - 
#
#############################################################

from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator
from django.contrib.auth.models import AbstractUser, Group, Permission

#########################################################################################
################################### ADDRESS CLASS #######################################
#########################################################################################

# Stores all addresses used in relation to Venues and Users

class Address(models.Model):
    address1 = models.TextField(max_length=100)
    address2 = models.TextField(null=True)
    city     = models.TextField(max_length=100)
    state    = models.TextField(max_length=2)
    ZIP      = models.TextField(max_length=10)

    def __str__(self):
        return '{0} {1}, {2}'.format(self.address1, self.city, self.state)

#########################################################################################
################################# CUSTOM USER CLASS #####################################
#########################################################################################

# This custom class will be the overall user for the system

class User(AbstractUser):

    # The following is imported from AbstractUser
    # username 
    # first_name
    # last_name
    # email
    # is_staff
    # is_active
    # date_joined
    # objects = UserManager()

    # USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['email']

    # def get_full_name(self):

    # def get_short_name(self):

    # def email_user(self, subject, message, from_email=None, **kwargs):
        
    phone                  = models.TextField()
    date_appointed_agent   = models.DateField(null=True)
    security_question      = models.TextField(max_length=255)
    security_answer        = models.TextField(max_length=255)
    organization_name      = models.TextField(null=True)
    bio_sketch             = models.TextField(null=True, max_length=1000)
    emergency_contact_name = models.TextField(null=True, max_length=100)
    emergency_phone        = models.TextField(null=True, max_length=14)
    emergency_relationship = models.TextField(null=True, max_length=100)

    # The address column is not null by default, though the business logic will prevent people from being 
    # created without an address (except the original superuser created by the initialize script)
    address = models.ForeignKey(Address, null=True)

    def send_password_recovery_email(self):
        "Returns confirmation that password recovery email was sent and sends confirmation email"
        # Currently, we don't understand how to exactly create these methods
        # but we wanted to be able to model them for future reference
        
    recovery_email = property(send_password_recovery_email)

#########################################################################################
##################################### PHOTOGRAPH ########################################
#########################################################################################

# Photograph will store all of the photos for the people and things in the 
# system.

class Photograph(models.Model):
    date_taken   = models.DateField(default=timezone.now())
    place_taken  = models.TextField()
    image        = models.ImageField()
    description  = models.TextField(max_length=1000)
    photographer = models.ForeignKey(User)

    def __str__(self):
        return self.image

#########################################################################################
######################################## VENUE ##########################################
#########################################################################################

# Venues are where Events take place. Instances of Events will have a foreign key from Venue, 
# so that each venue can be stored for use later.

class Venue(models.Model):
    name    = models.TextField(max_length=100)
    address = models.ForeignKey(Address)

    def __str__(self):
        return self.name

#########################################################################################
#################################### PUBLIC EVENT #######################################
#########################################################################################

# PublicEvent is the "template" for frequently used Events. You can create an event Template
# and then have the Event pull from the template and fill in the instance info.

class PublicEvent(models.Model):
    name        = models.TextField(max_length=100)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name

    def create_event_sumary(self):
        '''Returns summary information about an event after it is completed'''
        # Currently, we don't understand how to exactly create these methods
        # but we wanted to be able to model them for future reference
    
    event_summary = property(create_event_sumary)

#########################################################################################
######################################## EVENT ##########################################
#########################################################################################

# An event is an instance of Public Event (if the Public Event is used). It is made up of 
# areas, and takes place at a venue. 

class Event(models.Model):
    name           = models.TextField(max_length=100)
    start_date     = models.DateTimeField()
    end_date       = models.DateTimeField()
    event_map      = models.FileField()
    venue          = models.ForeignKey(Venue)
    event_template = models.ForeignKey(PublicEvent, null=True)

    def __str__(self):
        return self.name

#########################################################################################
######################################### AREA ##########################################
#########################################################################################

# Events are made up of areas, which are different physical locations in an event, where
# different activities are going on. 
# 
# Note that there are 2 foreign keys to the User class which are for the coordinator/supervisor
# roles. 

class Area(models.Model):
    name         = models.TextField(max_length=100)
    description  = models.TextField(max_length=1000)
    place_number = models.IntegerField(validators=[MinValueValidator(1)])
    coordinator  = models.ForeignKey('User', related_name='coordinator')
    supervisor   = models.ForeignKey('User', related_name='supervisor')
    event        = models.ForeignKey(Event)

    def __str__(self):
        return self.name

#########################################################################################
################################## EXPECTED SALE ITEM ###################################
#########################################################################################

# Expected Sale Items are items that are possibly going to be sold in a given area for a 
# given event. They are purely informational, therefore they do not need to be tied to 
# the inventory.

class ExpectedSaleItem(models.Model):
    name        = models.TextField(max_length=100)
    description = models.TextField(max_length=1000)
    low_price   = models.DecimalField(max_digits=10, decimal_places=2)
    high_price  = models.DecimalField(max_digits=10, decimal_places=2)
    area        = models.ForeignKey(Area) 

    def __str__(self):
        return self.name

#########################################################################################
####################################### CATEGORY ########################################
#########################################################################################

# Category is tied to Product Specification, which describes the category of the item

class Category(models.Model):
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.description

#########################################################################################
################################# PRODUCT SPECIFICATION #################################
#########################################################################################

# Product Specification holds/is related to the classes that hold all of the information
# needed to define and understand an inventory item. 

class ProductSpecification(models.Model):
    name            = models.TextField(max_length=100)
    price           = models.DecimalField(max_digits=10, decimal_places=2)
    description     = models.TextField(max_length=1000)
    manufacturer    = models.TextField(max_length=100)
    average_cost    = models.DecimalField(max_digits=10, decimal_places=2)
    sku             = models.TextField(null=True)
    order_form_name = models.TextField(null=True, max_length=255)
    production_time = models.TextField(null=True, max_length=15)
    photograph      = models.ForeignKey(Photograph, null=True)
    
    # Produced by is for any user that also makes this product
    produced_by = models.ForeignKey(User, null=True)
    category    = models.ForeignKey(Category, null=True)

    def __str__(self):
        return self.name

#########################################################################################
###################################### INVENTORY ########################################
#########################################################################################

# Inventory is the top-level item/product that all items and products inherit from.
# 
# It is associated with Product Specification, wherein the description, name, categorizing... 
# are located. 

class Inventory(models.Model):
    quantity_on_hand = models.IntegerField(validators=[MinValueValidator(0)])
    shelf_location   = models.TextField(max_length=100)
    order_file       = models.TextField(max_length=1000)
    condition        = models.TextField(max_length=100)
    note             = models.TextField(null=True)
    specs            = models.ForeignKey(ProductSpecification)

    def __str__(self):
        return '{0}: {1} on hand'.format(self.specs.name, self.quantity_on_hand)

#########################################################################################
######################################## ITEM ###########################################
#########################################################################################

# Item inherits from Inventory, and it is the parent class of the "rentals" side of the 
# inventory. By default, if an item exists here and NOT as a wardrobe item (which inherits
# from Item), then it is a non-wardrobe item

class Item(Inventory):
    # If the item has a standard rental price, times rented is filled, price per day is listed
    # and it has a replacement price, then it is rentable
    standard_rental_price = models.DecimalField(null=True, max_digits=10, decimal_places=2)
    owner                 = models.ForeignKey(User, null=True)
    times_rented          = models.IntegerField(null=True, validators=[MinValueValidator(0)])
    price_per_day         = models.DecimalField(null=True, max_digits=10, decimal_places=2)
    replacement_price     = models.DecimalField(null=True, max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    def generate_inventory_report(self):
        "Returns the information about the products held in inventory"
        # Currently, we don't understand how to exactly create these methods
        # but we wanted to be able to model them for future reference
        
    inventory_report = property(generate_inventory_report)

#########################################################################################
#################################### WARDROBE ITEM ######################################
#########################################################################################

# Inherits from Item. 

class WardrobeItem(Item):
    size          = models.IntegerField(validators=[MinValueValidator(0)])
    size_modifier = models.TextField(max_length=10)
    gender        = models.TextField(max_length=1)
    color         = models.TextField(max_length=10)
    pattern       = models.TextField(max_length=100)
    start_year    = models.DateField()
    end_year      = models.DateField()

    def __str__(self):
        return self.note

#########################################################################################
################################### SERIALIZED PRODUCT ##################################
#########################################################################################

# Branches down a different side, the "products" for sale side from Inventory. 

class SerializedProduct(Inventory):
    serial_number = models.TextField(max_length=100)
    date_acquired = models.DateTimeField(default=timezone.now())
    cost          = models.DecimalField(max_digits=10, decimal_places=2)
    status        = models.TextField(max_length=100)


    def __str__(self):
        return self.inventory.description

    def generate_product_list(self):
        "Generates a product list and returns the names of the products"
        # Currently, we don't understand how to exactly create these methods
        # but we wanted to be able to model them for future reference
        
    product_list = property(generate_product_list)

#########################################################################################
###################################### TRANSACTION ######################################
#########################################################################################

# Transactions are any rentals or sales that a customer completes through the system. 
# It is made up of Line Items (seen below) and what kind of line item will determine 
# whether or not it is a rental or a sale.

class Transaction(models.Model):
    transaction_date = models.DateTimeField(default=timezone.now())
    date_packed      = models.DateTimeField(null=True)
    packed_by        = models.ForeignKey(User, related_name='packer', null=True)
    date_paid        = models.DateTimeField(null=True)
    payment_handler  = models.ForeignKey(User, related_name='handler', null=True)
    date_shipped     = models.DateTimeField(null=True)
    shipped_by       = models.ForeignKey(User, related_name='shipper', null=True)
    tracking_number  = models.TextField(max_length=100, null=True)
    customer         = models.ForeignKey(User)

    # An agent is a user that has been appointed as an agent, and the one that handles the transaction
    # if it is in the store
    agent = models.ForeignKey('User',related_name='agent', null=True)

    def __str__(self):
        return self.tracking_number

    def email_receipt(self):
        '''
            Emails receipt to user and returns confirmation that it was sent
        '''
        # Currently, we don't understand how to exactly create these methods
        # but we wanted to be able to model them for future reference
        
    receipt = property(email_receipt)

    def add_shipping_info(self):
        '''
            Gets the customer's shipping info

            We'll add the logic here later
        '''

    def add_payment_info(self):
        '''
            Gets the payment info from the customer

            We'll add the logic later.
        '''

#########################################################################################
####################################### LINE ITEM #######################################
#########################################################################################

# Line items make up the transaction. This class is abstract, and the different type of 
# line items inherit from it. 

class LineItem(models.Model):
    amount      = models.DecimalField(max_digits=10, decimal_places=2)
    transaction = models.ForeignKey(Transaction)

    class Meta:
        abstract = True

    def __str__(self):
        return self.amount

#########################################################################################
########################################## FEE ##########################################
#########################################################################################

# This class is the abstract super class to the two different fee types. Rentals are 
# associated with fees. 
# 
# NOTE! This class should be treated as abstract, though, because a FK references it, it 
# cannot be abstract. 

class Fee(LineItem):
    waived = models.BooleanField(default=False)

    def __str__(self):
        return self.waived

#########################################################################################
######################################## LATE FEE #######################################
#########################################################################################

# Late fees are applied when the rental is returned after the due date.

class LateFee(Fee):
    days_late = models.IntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return self.days_late

#########################################################################################
####################################### DAMAGE FEE ######################################
#########################################################################################

# Damage fees are applied when the rental is returned in a worse state than when it was
# rented. 

class DamageFee(Fee):
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.description

#########################################################################################
###################################### RENTAL ITEM ######################################
#########################################################################################

# Rental item inherits from Line Item, it is associated with an Item and a fee, if there
# are any

class RentalItem(LineItem):
    date_out         = models.DateTimeField(default=timezone.now())
    due_date         = models.DateField()
    date_in          = models.DateTimeField(null=True)
    discount_percent = models.DecimalField(max_digits=3, decimal_places=2, null=True, default=None)
    item             = models.ForeignKey(Item)
    
    # the agent is the user that processes the return for the rental
    agent = models.ForeignKey(User, null=True)
    fee = models.ForeignKey(Fee, null=True)

    def __str__(self):
        return self.item.specs.name 

    def get_overdue_items(self):
        '''
            Returns the list of all items that are overdue

            We'll put the logic here later.
        '''

    def notify_items_due(self):
        '''
            Notifies the managers that the rental item is due/overdue

            We will put the logic here a bit later. 
        '''

    def print_rental_contract(self):
        '''
            Prints a rental contract for the given rental item. 

            We will put the logic here a bit later. 
        '''

    rental_contract = property(print_rental_contract)

#########################################################################################
####################################### SALE ITEM #######################################
#########################################################################################

# Sale items are the items that are SOLD, and inherit from LineItem. 

class SaleItem(LineItem):
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    
    # The product is the inventory item that is being sold
    product = models.ForeignKey(Inventory)

    def __str__(self):
        return self.product.name