def weight_on_planets():
    w = float(input("What do you weigh on earth? "))
    m = w * 0.38
    j = w * 2.34
   
    print("\nOn Mars you would weigh " + str(m) + " pounds.\nOn Jupiter you would weigh " + str(j) + " pounds.")
   
if __name__ == '__main__':
    weight_on_planets()
