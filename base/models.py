from django.db import models


class User(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    avatar=models.ImageField()


class Matatu(models.Model):
    image=models.ImageField()
    registration=models.CharField(max_length=20)
    driver=models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name="driver")
    conductor=models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name="conductor")
    routes=models.CharField(max_length=100)
    

class Trips(models.Model):
    time=models.DateTimeField(auto_now_add=True)
    matatu=models.ForeignKey(Matatu,on_delete=models.DO_NOTHING)


class Route(models.Model):
    route_name=models.CharField(max_length=50)

class Sacco(models.Model):
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=20)
    route=models.ForeignKey(Route,on_delete=models.DO_NOTHING)
    trips=models.ForeignKey(Trips,on_delete=models.DO_NOTHING)

class Seat(models.Model):
    seat_number=models.CharField(max_length=5)
    customer=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    matatu=models.ForeignKey(Matatu,on_delete=models.DO_NOTHING)




