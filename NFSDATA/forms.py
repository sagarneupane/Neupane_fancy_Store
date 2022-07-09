from django import forms
from .models import *


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        
        widgets = {
            "category_name":forms.TextInput(attrs={"class":"form-control p-2"}),
            "cateogry_details":forms.Textarea(attrs={"class":"form-control p-2"})
        }
        
class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = "__all__"
        widgets = {
            "sub_cat_name":forms.TextInput(attrs={"class":"form-control p-2"}),
            "sub_cat_details":forms.Textarea(attrs={"class":"form-control p-2"})
        }
        labels = {
            "sub_cat_name":"Sub Category Name",
            "sub_cat_details":"Sub Category Details"
        }

class DateInput(forms.DateInput):
    input_type = 'date'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = "__all__"
        widgets = {
            
                    "product_name" : forms.TextInput(attrs={"class":"form-control p-2"}),
                    "product_amount" : forms.NumberInput(attrs={"class":"form-control p-2"}),
                    "product_cost_price" : forms.NumberInput(attrs={"class":"form-control p-2"}),
                    "product_category" : forms.Select(attrs={"class":"form-control p-2"}),
                    "product_subcategory" : forms.Select(attrs={"class":"form-control p-2"}),
                    "product_gender" : forms.Select(attrs={"class":"form-control p-2"}),
                    "product_age_groups" : forms.Select(attrs={"class":"form-control p-2"}),
                    "product_brand" : forms.Select(attrs={"class":"form-control p-2"}),
                    "product_minicategory" : forms.TextInput(attrs={"class":"form-control p-2"}),
                    "product_size" : forms.SelectMultiple(attrs={"class":"form-control p-2"}),
                    "product_image":forms.FileInput(attrs={"class":"form-control"}),
                    "date_added":DateInput(attrs={"class":"form-control p-2"}),
            
        }
    
class SoldProductsFrom(forms.ModelForm):
    class Meta:
        model = SoldProducts
        fields = ["product_selling_price","product_amount_sold","added_date"]
        
        labels = {
            "product_selling_price":"Enter Selling Price of Product",
            "product_amount_sold":"Enter Amount of Product You Have Sold",
            "added_date":"Select The Day When You Have Sold The Item"
        }
        
        widgets = {
            "product_selling_price":forms.NumberInput(attrs={"class":"form-control p-2"}),
            "product_amount_sold":forms.NumberInput(attrs={"class":"form-control p-2"}),
            "added_date":DateInput(attrs={"class":"form-control p-2"}),
        } 
        
        
class SearchForm(forms.Form):
    search_data = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mr-sm-2 border border-primary p-2 m-2",
                                                                "arial-label":"Search",
                                                                "type":"number",
                                                       }))



class GenerateBillForm(forms.Form):
    bill_no = forms.CharField(widget=forms.NumberInput(attrs={
        "class":"form-control border border-info p-1",
        
    }))
    customer_detail = forms.CharField(
        widget=forms.TextInput(attrs={
        "class":"form-control border border-info p-1",
        
    })
    )
    customer_phonenumber = forms.CharField(
        widget=forms.TextInput(attrs={
        "class":"form-control border border-info p-1",
        
    })
    )
    # items_amount = forms.IntegerField(
    #     widget=forms.NumberInput(attrs={
    #     "class":"form-control border border-info p-1",
        
    # })
    # )
    # items_selling_price = forms.FloatField(
    #     widget=forms.NumberInput(attrs={
    #     "class":"form-control border border-info p-1",
        
    # })
    # )
    date_billed = forms.DateField(
        widget=DateInput(attrs={
        "class":"form-control border border-info p-1",
        
    })
    )
    
        
    
    