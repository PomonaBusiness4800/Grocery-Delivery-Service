# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Address(models.Model):
    useraddressid = models.AutoField(db_column='userAddressID', primary_key=True)  # Field name made lowercase.
    user_userid = models.ForeignKey('User', models.DO_NOTHING, db_column='user_userID')  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=45)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=45)  # Field name made lowercase.
    streetaddress = models.CharField(db_column='streetAddress', max_length=45)  # Field name made lowercase.
    city = models.CharField(max_length=45)
    zipcode = models.IntegerField(db_column='zipCode')  # Field name made lowercase.
    state = models.CharField(max_length=45)
    def getUserAddressID(self): return self.useraddressid
    def getUserID(self): return self.user_userid.getUserID()
    def getUserInfo(self): return self.user_userid
    def getFirstName(self): return self.firstname
    def getLastName(self): return self.lastname
    def getStreetAddress(self): return self.streetaddress
    def getCity(self): return self.city
    def getZipCode(self): return self.zipcode
    def getState(self): return self.state
    

    class Meta:
        managed = False
        db_table = 'address'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Deliverydriver(models.Model):
    driverid = models.AutoField(db_column='driverID', primary_key=True)  # Field name made lowercase.
    driverfirstname = models.CharField(db_column='driverFirstName', max_length=45)  # Field name made lowercase.
    driverlastname = models.CharField(db_column='driverLastName', max_length=45)  # Field name made lowercase.
    carmodel = models.CharField(db_column='carModel', max_length=45)  # Field name made lowercase.
    licenseplate = models.CharField(db_column='licensePlate', max_length=45)  # Field name made lowercase.
    def getDriverID(self): return self.driverid
    def getDriverFirstName(self): return self.driverfirstname
    def getDriverLastName(self): return self.driverlastname
    def getCarModel(self): return self.carmodel
    def getLicensePlate(self): return self.licenseplate

    def __str__(self):
        return self.driverfirstname + ' ' + self.driverlastname + ' id: ' + str(self.driverid)
    class Meta:
        managed = False
        db_table = 'deliveryDriver'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Groceryitem(models.Model):
    groceryid = models.AutoField(db_column='groceryID', primary_key=True)  # Field name made lowercase.
    grocerystore_storeid = models.ForeignKey('Grocerystore', models.DO_NOTHING, db_column='groceryStore_storeID')  # Field name made lowercase.
    groceryname = models.CharField(db_column='groceryName', max_length=45)  # Field name made lowercase.
    category = models.CharField(max_length=45)
    price = models.FloatField()
    brand = models.CharField(max_length=45)
    description = models.CharField(max_length=100)
    stock = models.IntegerField()
    def getGroceryID(self): return self.groceryid
    def getStrGroceryID(self): return str(self.groceryid)
    def getStoreID(self): return self.grocerystore_storeid.getStoreID()
    def getStoreInfo(self): return self.grocerystore_storeid
    def getGroceryName(self): return self.groceryname
    def getCategory(self): return self.category
    def getPrice(self): return self.price 
    def getBrand(self): return self.brand
    def getDescription(self): return self.description
    def getStock(self): return self.stock

    def __str__(self):
        return str(self.groceryid)

    class Meta:
        managed = False
        db_table = 'groceryItem'


class Grocerystore(models.Model):
    storeid = models.AutoField(db_column='storeID', primary_key=True)  # Field name made lowercase.
    grocerystoreadd_storeaddressid = models.ForeignKey('Grocerystoreadd', models.DO_NOTHING, db_column='groceryStoreAdd_storeAddressID')  # Field name made lowercase.
    storename = models.CharField(db_column='storeName', max_length=45)  # Field name made lowercase.
    description = models.CharField(max_length=45)
    def getStoreID(self): return self.storeid
    def getAddressID(self): return self.grocerystoreadd_storeaddressid.getStoreAddressID()
    def getAddressInfo(self): return self.grocerystoreadd_storeaddressid
    def getStoreName(self): return self.storename
    def getDescription(self): return self.description

    def __str__(self):
        return 'Store ID: ' + str(self.storeid) + ' Store name: ' + self.storename
    

    class Meta:
        managed = False
        db_table = 'groceryStore'


class Grocerystoreadd(models.Model):
    storeaddressid = models.AutoField(db_column='storeAddressID', primary_key=True)  # Field name made lowercase.
    streetaddress = models.CharField(db_column='streetAddress', max_length=45)  # Field name made lowercase.
    city = models.CharField(max_length=45)
    zipcode = models.IntegerField(db_column='zipCode')  # Field name made lowercase.
    state = models.CharField(max_length=45)
    def getStoreAddressID(self): return self.storeaddressid
    def getStreet(self): return self.streetaddress
    def getCity(self): return self.city
    def getZipCode(self): return self.zipcode
    def getState(self): return self.state

    def __str__(self):
        return self.streetaddress + ' ' + self.city + ' ' + self.zipcode + ' ' + self.state

    class Meta:
        managed = False
        db_table = 'groceryStoreAdd'


class Orderstatus(models.Model):
    orderstatusid = models.AutoField(db_column='orderStatusID', primary_key=True)  # Field name made lowercase.
    purchaseinfo_purchaseid = models.ForeignKey('Purchaseinfo', models.DO_NOTHING, db_column='purchaseInfo_purchaseID')  # Field name made lowercase.
    deliverydriver_driverid = models.ForeignKey(Deliverydriver, models.DO_NOTHING, db_column='deliveryDriver_driverID')  # Field name made lowercase.
    status = models.CharField(max_length=45)
    def getOrderStatusID(self): return self.orderstatusid
    def getPurchaseInfoID(self): return self.purchaseinfo_purchaseid.getPurchaseInfoID()
    def getPurchaseInfo(self): return self.purchaseinfo_purchaseid
    def getDeliveryDriverID(self): return self.deliverydriver_driverid.getDriverID()
    def getDeliverDriverInfo(self): return self.deliverydriver_driverid
    def getStatus(self): return self.status

    def __str__(self):
        return 'Order ID: ' + self.orderstatusid + '\nDelivery Driver: ' + self.getDeliverDriverInfo() + '\nStatus: ' + self.status

    class Meta:
        managed = False
        db_table = 'orderStatus'


class Purchaseinfo(models.Model):
    purchaseid = models.AutoField(db_column='purchaseID', primary_key=True)  # Field name made lowercase.
    userpaymentinfo_paymentid = models.ForeignKey('Userpaymentinfo', models.DO_NOTHING, db_column='userPaymentInfo_paymentID')  # Field name made lowercase.
    grocerystore_storeid = models.ForeignKey(Grocerystore, models.DO_NOTHING, db_column='groceryStore_storeID')  # Field name made lowercase.
    totalprice = models.FloatField(db_column='totalPrice')  # Field name made lowercase.
    totalitems = models.IntegerField(db_column='totalItems')  # Field name made lowercase.
    date = models.CharField(max_length=45)
    time = models.CharField(max_length=45)
    def getPurchaseID(self): return self.purchaseid
    def getUserPaymentInfoID(self): return self.userpaymentinfo_paymentid.getUserPaymentInfoID()
    def getUserPaymentInfo(self): return self.userpaymentinfo_paymentid
    def getStoreID(self): return self.grocerystore_storeid.getStoreID()
    def getStoreInfo(self): return self.grocerystore_storeid
    def getTotalPrice(self): return self.totalprice
    def getTotalItems(self): return self.totalitems
    def getDate(self): return self.date
    def getTime(self): return self.time
    
    def __str__(self):
        return 'Total Items Bought: ' + self.totalitems + '\nTotal Price: ' + self.totalprice + '\nTime of Purchase: ' + self.date + ' ' + self.time

    class Meta:
        managed = False
        db_table = 'purchaseInfo'


class User(models.Model):
    userid = models.AutoField(db_column='userID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=32)
    firstname = models.CharField(max_length=45)
    lastname = models.CharField(max_length=45)
    emailaddress = models.CharField(max_length=45)
    def getUserID(self): return self.userid
    def getUserName(self): return self.username
    def getPassword(self): return self.password
    def getFirstName(self): return self.firstname
    def getLastName(self): return self.lastname
    def getEmailAddress(self): return self.emailaddress
    
    def __str__(self):
        return self.firstname + ' ' + self.lastname + ' id: ' + str(self.userid)

    class Meta:
        db_table = 'user'


class Userpaymentinfo(models.Model):
    paymentid = models.AutoField(db_column='paymentID', primary_key=True)  # Field name made lowercase.
    user_userid = models.ForeignKey(User, models.DO_NOTHING, db_column='user_userID')  # Field name made lowercase.
    cardnumber = models.CharField(max_length=16)
    securitynumber = models.IntegerField()
    expirationdate = models.CharField(db_column='expirationDate', max_length=10)  # Field name made lowercase.
    zipcode = models.IntegerField()
    def getPaymentID(self): return self.paymentid
    def getUserID(self): return self.user_userid.getUserID()
    def getUserInfo(self): return self.user_userid
    def getCardNumber(self): return self.cardnumber
    def getSecurityNumber(self): return self.securitynumber
    def getExpirationDate(self): return self.expirationdate
    def getZipCode(self): return self.zipcode
    
    def __str__(self):
        return self.user_userid + '\nCard Number: ' + self.cardnumber + ' Security Number: ' + self.securitynumber + '\nExpiration Date: ' + self.expirationdate + ' Zipcode: ' + self.zipcode

    class Meta:
        managed = False
        db_table = 'userPaymentInfo'
