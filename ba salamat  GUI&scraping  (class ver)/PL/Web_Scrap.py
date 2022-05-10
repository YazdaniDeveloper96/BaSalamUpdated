##################################### import requirment ##################################
import sys
sys.path.insert(0,'C:/Users/MohammadReza/Desktop/webscraping/BaSalamUpdated')
#######################
import requests
from bs4 import BeautifulSoup
import re
#######################
from DAL.product import product


##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################
##################################### main code ##########################################

#img,tile,score,city,pricebefore,discount,pricenow
class scraping:
    def __init__(self,url=str) -> None:
        self.link=requests.get(url)
        self.soup=BeautifulSoup(self.link.content,'html.parser')

    @staticmethod
    def __get_details(item):
        #----get img--------------------------------------------------------------------
        img=item.find('div',attrs={'class':'product-card__image'})
        final_image=img.a.img['src']
        #----get title------------------------------------------------------------------
        title=item.find('div',attrs={'class':'product-card__content'})
        final_title=title.a.text.strip()
        #----get score------------------------------------------------------------------
        final_score="none"
        score=item.find('span',attrs={'class':'reviews__star-count'})
        if score:
            final_score=score.text.strip()
        #----get city ------------------------------------------------------------------
        final_city='none'
        city=item.find('span',attrs={'class':'vendor-details__city-name'})
        if city.text:
            final_city=re.findall(r'(.+)\|',city.text.strip())[0]
        #----get price -----------------------------------------------------------------
        final_price_after=0
        price_after=item.find('span',attrs={'class':'product-card__price-original mt-1'})
        if price_after:
            final_price_after=int("".join(price_after.text.strip().split(',')))
        #---- get discount -------------------------------------------------------------
        final_discount=0
        discount=item.find('span',attrs={'class':'product-card__price-discount-badge'})
        if discount:
            final_discount=int(re.findall(r'(\d+)٪',discount.text.strip())[0])
        #----get before price-----------------------------------------------------------
        final_price_before=0
        price_before=item.find('span',attrs={'class':'product-card__price-discounted ml-1'})
        if price_before:
            final_price_before=int("".join(price_before.text.strip().split(',')))

        return product(final_image,final_title,final_score,final_city,final_price_before,final_discount,final_price_after)

    def get_data(self):
        list_of_products=[]
        list_of_data=self.soup.find_all('div',attrs={'class':'product-card product-card--vertical'})
        for item in list_of_data:
            product=scraping.__get_details(item)
            list_of_products.append(product)
        return list_of_products
    

        






















# s1=scraping('https://basalam.com/search?sort=6&minP=10000000&maxP=105560000&ready=true&namedTags=73270&rating=1&hasDelivery=true&type=products&literal=true')
# with open('f.json','w',encoding='utf_8') as file1:
#         json.dump(s1.get_data(),file1,indent=8,ensure_ascii=False)