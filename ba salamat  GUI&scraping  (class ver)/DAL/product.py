#img,tile,score,city,pricebefore,discount,pricenow
class product:
    def __init__(self,img,title=str,score=int,city=str,pricebefor=str,discount=str,priceafter=str) -> None:
        self.img=img
        self.title=title
        self.score=score
        self.city=city
        self.pricebefor=pricebefor
        self.discount=discount
        self.priceafter=priceafter
    def __str__(self) -> str:
        return "{0}{1}{2}{3}{4}{5}{6}".format(self.img,self.title,self.score,self.city,self.pricebefor,self.discount,self.priceafter)