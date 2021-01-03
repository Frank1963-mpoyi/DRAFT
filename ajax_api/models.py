from    django.db                   import   models
from    django.core.files.storage   import   FileSystemStorage


class Shirt(models.Model):
    brand       = models.CharField('BRAND',           max_length=100)
    price       = models.DecimalField('PRICE',         max_digits=5,   decimal_places=2)
    visited     = models.IntegerField('VISITED')
    picture     = models.ImageField('PICTURE',      upload_to='shirts')
    
    def serialize(self):
        shirt = {
            "id":       self.id,
            "brand":    self.brand,
            "price":    self.price,
            "picture":  self.picture.url
            
        }
        return shirt
