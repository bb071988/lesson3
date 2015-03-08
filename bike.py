# bicycle objects lesson

class Wheel(object):
  def __init__(self, weight, cost):
    self.weight = weight
    self.cost = cost
 
  def __repr__(self):
    return "A wheel that weighs {} and costs {}.".format(self.weight, self.cost)

  
class Frame(object):
  def __init__(self, weight, cost):
    self.weight = weight
    self.cost = cost
    
  def __repr__(self):
    return "A frame that weighs {} and costs {}.".format(self.weight, self.cost)

class Bike(object):
    def __init__(self, bike_name, wheel, frame):
        self.bike_name = bike_name
        self.wheel = wheel
        self.frame = frame
    
    def weight(self):
      return (self.wheel.weight * 2) + self.frame.weight
    
    def prod_cost(self):
      return (self.wheel.cost * 2) + self.frame.cost
      

class BikeShop(object):  # StudlyCaps for classes per pep8
    def __init__(self, inventory, markup, shop_name):
        self.inventory = inventory
        self.markup = markup
        self.shop_name = shop_name
        self.__total_profit = 0
        self.__trans_profit = 0

    
    def get_sales_price(self):
        for value in self.inventory.itervalues():
            print 'We charge {} for {} bikes'.format(
              value['bike_obj'].prod_cost() * (1 + self.markup), 
              value['bike_obj'].bike_name
            )
            
    def sell_bike(self, bike_name):
                
        # decrease inventory 
        self.inventory[bike_name]['quant'] = self.inventory[bike_name]['quant'] -1
        
        self.__trans_profit = (self.inventory[bike_name]['bike_obj'].prod_cost() * 
                             (1+self.markup)) - self.inventory[bike_name]['bike_obj'].prod_cost()  

        self.__total_profit = self.__total_profit + self.__trans_profit
        
        # return the markup for customer funds calculation
        return self.inventory[bike_name]['bike_obj'].prod_cost() * (1+self.markup)
    
    def get_profit(self):
        return self.__total_profit
        
      
        
        #get_sales_price(self, inventory, markup)
        
    ## Note: self.inventory
    def print_inventory(self):
         # print out all the bikes in inventory
        for value in self.inventory.itervalues():
            print 'Starting out we have {} {} bikes in stock'.format(value['quant'], value['bike_obj'].bike_name)

        
    def offer_bikes(self, cust_name, funds):  

        for key in inventory:
            if funds >= inventory[key]['bike_obj'].prod_cost() * (1 + self.markup):
                print '{} Since you have ${} you could buy a {} bike for ${}'.format(cust_name,funds, inventory[key]['bike_obj'].bike_name,
                                                                                     inventory[key]['bike_obj'].prod_cost() * (1 + self. markup))

    
class Customer(object):
    def __init__(self, cust_name, funds):
        self.cust_name = cust_name
        self.funds = funds
        
    def buy_bike(self, Bike, BikeShop):
        print 'Customer Name is: {}'.format(self.cust_name)
        print '{} wants to buy a {} bike'.format(self.cust_name, Bike.bike_name)
        print 'shopping at {}'.format(BikeShop.shop_name)
        print '{} has ${} to spend'.format(self.cust_name, self.funds)
        print 'funds before purchase *** ' + str(self.funds)
        bike_cost = BikeShop.sell_bike(Bike.bike_name)
        print 'The bike cost {}'.format(bike_cost)
        self.funds = self.funds - bike_cost
        print 'funds after purchase  *** ' + str(self.funds)
        

if __name__ == '__main__':
    
####################  setup the bikes, bike shop and customers 

    w1 = Wheel(1, 100)
    w2 = Wheel(.75, 200)
    w3 = Wheel(.70, 300)
  
    f1 = Frame(5, 500)
    f2 = Frame(4, 700)
    f3 = Frame(3, 900)
  
  
# Create 6 Bike objects    
    silver = Bike('silver',w1, f1)
    black = Bike('black', w1, f2)
    green = Bike('green',w1, f3)
    blue = Bike('blue',w2, f1)
    red = Bike('red', w2, f2)
    white = Bike('white',w2, f3)
    
    
    # Load the bike shop inventory database
    inventory = {}
    inventory['silver'] = {'bike_obj':silver,'quant':3}
    inventory['black'] = {'bike_obj':black, 'quant':4}
    inventory['green'] = {'bike_obj':green, 'quant':6}
    inventory['blue'] = {'bike_obj':blue, 'quant':8}
    inventory['red'] = {'bike_obj':red, 'quant': 5}
    inventory['white'] = {'bike_obj': white, 'quant':3}
    
   
    # create the customers
    abe = Customer('Abe',5000)
    bob = Customer('Bob',500)
    cheryl = Customer('Cheryl',2000)
    
    cust_list = [abe,bob,cheryl] # add the customers to a list.
    
############### create the bike shop, offer the bikes  
    
    
     # Load the inventory into new BikeShop object
    
    BobsBikes = BikeShop(inventory, .2,"Bob's Bikes")  
    
    BobsBikes.get_sales_price()
    
    BobsBikes.print_inventory() # print a list of beginning inventory
    
    # print offer the bikes to the customers
    
    for cust in cust_list:
        BobsBikes.offer_bikes(cust.cust_name, cust.funds)
                              
    # have each customer buy a bike.
    
    print 'Abe buys a bike'
    abe.buy_bike(silver, BobsBikes) # Abe buys a silver bike from Bobs Bikes
    
    print ' Bob Buys a bike'
    bob.buy_bike(green, BobsBikes)
    
    print ' Cheryl buys a bike'
    cheryl.buy_bike(red, BobsBikes)
    
    # print remaining inventory and profit for Bob's Bikes.
    BobsBikes.print_inventory()
    
    print 'total profit is:'
    print BobsBikes.get_profit()
    

    
    
    
    
    
    
    
 