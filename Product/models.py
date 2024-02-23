from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.db import models
from django.conf import settings
from django_extensions.db import fields as extension_fields
from django.utils import timezone
from datetime import timedelta, datetime
from django_currentuser.db.models import CurrentUserField
from datetime import timedelta
from django.db import models

from geopy.distance import geodesic





class Product(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    image = models.ImageField(upload_to="media/Product-images/", null=True, blank=True)
    
    

    


    class Meta:
        ordering = ('category', '-created',)



    def average_rating(self):
        reviews = self.reviews.all()
        if reviews:
            total = sum([int(review.rating) for review in reviews])
            return total / len(reviews)
        return 0
    
    def __str__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('Product_product_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('Product_product_update', args=(self.slug,))
    
    def average_rating(self):
        reviews = self.reviews.all()
        if reviews:
            total = sum([int(review.rating) for review in reviews])
            return total / len(reviews)
        return 0

    def __str__(self):
        return self.name
    
class ReviewRating(models.Model):
    STAR_CHOICES = [
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    ]

    # Fields
    product = models.ForeignKey(
        blank=True,
        null=True,
        on_delete=models.CASCADE,  # Corrected import here
        related_name='reviews',
        to='Product.Product',
    )

    
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,default=None
    )
    comment = models.TextField(blank=True, null=True)
    rating = models.IntegerField(choices=STAR_CHOICES)
    subject= models.CharField(max_length=255, blank=True)
    review=models.TextField(max_length=255, blank=True)
    rating=models.FloatField(max_length=255, blank=True)
    ip= models.CharField(max_length=20, blank=True)
    status=models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        
        return self.subject
    
    
    

    def get_absolute_url(self):
        return reverse('review_detail', args=[str(self.id)])    


class Order(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=10, null=True)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    address = models.TextField(max_length=100, null=True)
    count = models.IntegerField(default=1)
    cost = models.IntegerField(default=0)
    delivered = models.BooleanField(default=False)
    result = timezone.now() + timedelta(minutes=30)
    delivered_on = models.DateTimeField(default=result)
    
    


    # Relationship Fields
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE, related_name="orders", null=True, blank=True
    )
    order_by = CurrentUserField(blank=True, null=True, related_name="orders_user", on_delete=models.CASCADE)

    
   

        
      

        
       
    

    def save(self, commit=True):
        # Calculate the adjusted time before saving the form
        adjusted_time = self.calculate_adjusted_time()
        self.instance.adjusted_time = adjusted_time

        return super().save(commit)

    class Meta:
        ordering = ('delivered','-created',)

    
    def __str__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('Product_order_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('Product_order_update', args=(self.slug,))


    def save(self, *args, **kwargs):
        if self.delivered:
            if not self.delivered_on:
                self.delivered_on = timezone.now()
        super(Order, self).save(*args, **kwargs)


    
