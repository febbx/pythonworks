class Shipping:

    def calc_shipping_cost(self,weight):

        print(weight*5)


class ExpressShipping:
    def calc_shipping_cost(self,weight):
        print(weight*20)


class StandardShipping:
    def calc_shipping_cost(self,weight):
        print(weight*10)

exp_instance =ExpressShipping()
exp_instance.calc_shipping_cost(10)
std_instance = StandardShipping()
std_instance.calc_shipping_cost(10)