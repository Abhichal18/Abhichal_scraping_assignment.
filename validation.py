import string
import re

class ProductValidator:
    punctuations=string.punctuation
    chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789’ ”“é"
    all_chars=chars+punctuations
    valid_chars = set(all_chars)
    url_pattern = re.compile(r'^https?://(?:www\.)?\w+\.\w{2,4}/?.*$')    
    def validate_product_id(product_id):
        return isinstance(product_id,str) and len(product_id)>0 and all(char in ProductValidator.valid_chars for char in product_id)

    def validate_title(title):
        return isinstance(title,str) and len(title)>0 and all(char in ProductValidator.valid_chars for char in title)

    def validate_subtitle(subtitle):
        # doing this here beacause scraping the data will consume a lot of time again. We can do this while scraping only
        subtitle=re.sub(r'[^\x00-\x7F]+',' ', subtitle)
        subtitle=subtitle.replace('\n',' ')
        return isinstance(subtitle,str) and all(char in ProductValidator.valid_chars for char in subtitle)

    def validate_description(description):
        # doing this here beacause scraping the data will consume a lot of time again. We can do this while scraping only
        description=re.sub(r'[^\x00-\x7F]+',' ', description)
        description=description.replace('\n',' ')
        return isinstance(description,str) and len(description)>10 and all(char in ProductValidator.valid_chars for char in description)

    def validate_url(url):
        if not ProductValidator.url_pattern.match(url):
            return False
        return True

    def validate_price(price):
        price=price[1:]
        price=price.replace(',','')
        try:
            price=float(price)
            return isinstance(price, (int, float)) and price>0
        except:
            return False

    def validate_quantity(quantity):
        qunatity=quantity.split(' ')[0]
        s=''
        for i in quantity:
            if i.isnumeric():
                s+=i
        return len(quantity)>0 and float(s)>0

    def validate_image_url(image):
        if not ProductValidator.url_pattern.match(image):
            return False
        return True

    def validate_variants_images(colors,variants_images):
        if len(colors)>0:
            if len(variants_images)>0:
                return True
        elif len(colors)==0:
            if len(variants_images)>=0:
                return True
        return False

    def validate_variants_images_urls(variants_images):
        for url in variants_images:
            if not ProductValidator.url_pattern.match(url):
                return False
        return True
        
    def validate_ingredients(ingredients):
        return len(ingredients)>0

    def validate_servings(servings):
        return len(servings)>0

    def validate_calories(calories):
        return len(calories)>0

    def validate_weight(weight):
        s=''
        for i in weight:
            if i.isnumeric():
                s+=i
        return len(weight)>0 and float(s)>0

    def validate_consume_advice(consume_advice):
        return len(consume_advice)>0

    def validate_nutritional_values(nutritional_values):
        return len(nutritional_values)>0

    def validate_vegan(vegan):
        return len(vegan)>0