from rest_framework import serializers
from . models import Customer,Products,Category

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields= '__all__'

    def validate_email(self,data):
        existing_customer = Customer.objects.filter(email=data).exclude(id=self.instance.id if self.instance else None).first()
        if existing_customer:
            raise serializers.ValidationError('Email already exists.')

        return data
    

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name','id']    
    
class ProductsSerializer(serializers.ModelSerializer):
    
    category_info = serializers.SerializerMethodField()

    class Meta:
        model = Products
        fields = '__all__'  
        # depth=1      

    def get_categoryinfo(self, obj):
        category = Category.objects.get(id=obj.category.id)
        return {
            'category_name': category.category_name,
            'category_description': category.category_description
        }
