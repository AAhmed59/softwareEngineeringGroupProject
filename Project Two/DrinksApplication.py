from tkinter import *
from PIL import ImageTk, Image 
import json
from datetime import *

#------------------------------set tKinter window-------------------------------
root = Tk()
root.geometry("1000x600")
root.title('BarMaster')
root['background'] = '#6495ED'


#-------------------text labels for sections on tKinter window------------------
welcomeTitle = Label(text = "Welcome to the Bar!\n\n", background='#6495ED', font = 'Helvetica 20 bold')
welcomeTitle.grid(row = 0, column = 6)

instructions = Label(text = "please choose the drink you are serving to update the inventory", background='#6495ED', font = 'Helvetica 18')
instructions.grid(row=1, column = 6)

alcoholicTitle = Label(text = "The Popular Alcoholic Drinks:", background='#6495ED', font = 'Helvetica 18 bold')
alcoholicTitle.grid(row = 5, column = 6)

nonAlcoholicTitle = Label(text = "The Popular Non-Alcoholic Drinks:", background='#6495ED', font = 'Helvetica 18 bold')
nonAlcoholicTitle.grid(row = 13, column = 6)


# we need 2 json files, one for inventory, and one for a log
# below functions will update these files
# need a function that will ask for employee number, and return the beginnning of a log statement, "Emp # orderd ______ at 0:00 PM"
#---------class to order drinks, update inventory, and add to order log---------
def transactionData():
    empID = int(input("Please enter employee ID # from 1 - 10: "))

    if empID == 1:
        employee = 'Employee 1'
    elif empID == 2:
        employee = 'Employee 2'
    elif empID == 3:
        employee = 'Employee 3'
    elif empID == 4: 
        employee = 'Employee 4'
    elif empID == 5: 
        employee = 'Employee 5'
    elif empID == 6: 
        employee = 'Employee 6'
    elif empID == 7: 
        employee = 'Employee 7'
    elif empID == 8:
        employee = 'Employee 8'
    elif empID == 9:
        employee = 'Employee 9'
    elif empID == 10:
        employee = 'Employee 10'
    else:
        print("Invalid Employee ID entered. Please quit and try again!")

    ct = datetime.now()

    log_message = f"At {ct}, {employee} served a "
    return str(log_message)
    


#class to hold drink functions
class Orders:
    def cosmo():
        transactionLog = []
        transaction_data = transactionData()
        transaction_data +="Cosmo"
        print(transaction_data)
        transactionLog.append(transaction_data)

        
        #transactionData()
        print("\nYou placed an order for a Cosmo!")
        

        with open('Inventory.json', 'r') as jsonFile:
            data = json.load(jsonFile)

        data['vodka'] -= 2
        data['triple_sec'] -= 2
        data['juice'] -= 1
        data['fruit'] -= 1
        
        with open('Inventory.json', 'w') as jsonFile:
            json.dump(data,jsonFile)

        currentTime = datetime.now()
        formattedTime = currentTime.strftime("%m/%d/%Y, %H:%M:%S")
        time_entry = {'time': formattedTime}
        drink_entry = {'drink': 'cosmo'}
        transaction_entry = {'transaction': transaction_data}

        with open('systemLog.json', 'r') as otherFile:
            log = json.loads(otherFile.read())


        log.append(time_entry)
        log.append(drink_entry)
        log.append(transaction_entry)

        with open('systemLog.json', "w") as file:
            json.dump(log, file)
        
        

    def marg():
       return
    def pina():
        return    
    def daq():
        return
    def white():
        return
    def mule():
        return
    def arnold():
        return
    def shirley():
        return
    def mocktail():
        return


    
#-----------open and size images -- fix paths to not be absolute----------------
cosmoImg = Image.open('Photos/cosmo.png')
cosmoResize = cosmoImg.resize((80, 80))
cosmo = ImageTk.PhotoImage(cosmoResize)

arnoldImg = Image.open('Photos/arnoldPalmer.png')
arnoldResize = arnoldImg.resize((80, 80))
arnold = ImageTk.PhotoImage(arnoldResize)

shirleyImg = Image.open('Photos/shirleyTemple.png')
shirleyResize = shirleyImg.resize((80, 80))
shirley= ImageTk.PhotoImage(shirleyResize)

margImg = Image.open('Photos/marg.png')
margResize = margImg.resize((80, 80))
marg= ImageTk.PhotoImage(margResize)

mocktailImg = Image.open('Photos/mocktail.png')
mocktailResize = mocktailImg.resize((80, 80))
mocktail = ImageTk.PhotoImage(mocktailResize)

muleImg = Image.open('Photos/mule.png')
muleResize = muleImg.resize((80, 80))
mule = ImageTk.PhotoImage(muleResize)

pinaColadaImg = Image.open('Photos/pinaColada.png')
pinaColadaResize = pinaColadaImg.resize((80, 80))
pina = ImageTk.PhotoImage(pinaColadaResize)

strawberryImg = Image.open('Photos/strawDaq.png')
strawberryResize = strawberryImg.resize((80, 80))
strawberry = ImageTk.PhotoImage(strawberryResize)

whiteImg = Image.open('Photos/whiteLady.png')
whiteResize = whiteImg.resize((80, 80))
white = ImageTk.PhotoImage(whiteResize)

#-------------------Drink Buttons with images and labels------------------------
arnoldButton = Button(root, text = 'Arnold Palmer', image=arnold, command= Orders.arnold(), compound = TOP)
cosmoButton = Button(root, text = 'Cosmopolitan', image=cosmo, command= Orders.cosmo, compound = TOP)
shirleyButton = Button(root, text = 'Shirley Temple', image=shirley, command= Orders.shirley, compound = TOP)
margButton = Button(root, text = 'Margarita', image=marg, command= Orders.marg, compound = TOP)
mocktailButton = Button(root, text = 'Island Mocktail', image=mocktail, command= Orders.mocktail, compound = TOP)
muleButton = Button(root, text = 'Mexican Mule', image=mule, command= Orders.mule, compound = TOP)
pinaButton = Button(root, text = 'Piña Colada', image=pina, command= Orders.pina, compound = TOP)
daqButton = Button(root, text = 'Strawberry Daquiri', image=strawberry, command= Orders.daq, compound = TOP)
whiteButton = Button(root, text = 'White Lady', image=white, command= Orders.white, compound = TOP)

#----------------Position and post buttons to tkinter window--------------------
muleButton.grid(row=6, column = 4)
margButton.grid(row=6, column = 6)
cosmoButton.grid(row=6, column = 8)

pinaButton.grid(row=10, column = 4)
daqButton.grid(row=10, column = 6)
whiteButton.grid(row=10, column = 8)

arnoldButton.grid(row=14, column = 4)
shirleyButton.grid(row=14, column = 6)
mocktailButton.grid(row=14, column = 8)



#run the page
root.mainloop()
