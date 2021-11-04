# use appropriate data structures to store the item code, description and price information 
#for themobile devices, SIM cards and accessories

phone_item_code = ["BPCM", "BPSH", "RPSH", "RPLL", "YPLS", "YPLL"]   
tablet_item_code = ["RTMS", "RTLM", "TYLM", "YTLL"]            
sim_item_code = ["SMNO", "SMPG"]  
case_item_code = [ "CSST", "CSLX"]
charger_item_code = ["CGCR", "CHHM"]
phone_description = ["Compact", "Clam Shell", "RoboPhone – 5-inch screen and 64GB memory",
                "RoboPhone – 6-inch screen and 256GB memory", "Y-Phone Standard – 6-inch screen and 64 GB memory", 
                "Y-Phone Deluxe – 6-inch screen and 256 GB memory"]
tablet_description = ["RoboTab – 8-inch screen and 64 GB memory", 
                "RoboTab – 10-inch screen and 128 GB memory", "Y-Tab Standard – 10-inch screen and 128 GB memory", 
                "Y-Tab Deluxe – 10-inch screen and 256 GB memory"]
sim_description = ["SIM Free (no SIM card purchased)", 
                "Pay As You Go (SIM card purchased)"]
case_description = ["Standard", "Luxury"]
charger_description = ["Car", "Home"]
                             
phone_price = [29.99, 49.99, 199.99, 499.99, 549.99, 649.99]
tablet_price = [149.99, 299.99, 499.99, 
        599.99]       
sim_price = [0.00, 9.99]
case_price = [0.00, 50.00]
charger_price = [19.99, 15.99]

#• allow the customer to choose a specific phone or tablet

def print_phone_menu():
    print ("Phones Menu")
    for i in range (len(phone_item_code)):
        print (i+1, end="\t")
        print (phone_description[i], end="\t$")
        print (phone_price[i])

def print_tablet_menu():
    print ("Tablet Menu")
    for i in range (len(tablet_item_code)):
        print (i+1, end="\t")
        print (tablet_description[i], end="\t$")
        print (tablet_price[i]) 
 
print ("Welcome to the store\n")
print_phone_menu()
print_tablet_menu()

tab_or_phone = input("\n Do you want a phone or tablet \n> ")

if tab_or_phone.lower() == "phone":
    print_phone_menu()
    choice_phone_model = int(input("Which model would you like, select the number from the menu above\n>"))
    sim_choice = int(input("do you want 1= SIM free, 2= Pay as you go\n>"))
   
elif tab_or_phone.lower() == "tablet":
    print_tablet_menu()
    choice_tablet_model = int(input("Which model would you like, select the number from the menu above\n>"))
else:
    print ("not a choice")

case_choice = int(input("do you want 1= standard case, 2= LUX case\n>"))
charger_choice = int(input("do you want 1= no charger, 2= car charger, 3= Home charger 4=both car & home charger\n>"))
if charger_choice == 1:
    customer_charger_price = 0
elif charger_choice == 2:
    customer_charger_price = charger_price[0]
elif charger_choice == 3:
    customer_charger_price = charger_price[1]
elif charger_choice == 4:
    customer_charger_price = charger_price[0] + charger_price[1]

print ("You have odered")

###############################################
print ("############# RECEIPT ###############")
# printing receipt of items
if tab_or_phone.lower() == "phone":
    price = phone_price[choice_phone_model-1] + sim_price[sim_choice-1] + case_price[case_choice-1] + customer_charger_price
    print (f"{phone_item_code[choice_phone_model-1]}\t{phone_description [choice_phone_model-1]}\t${phone_price[choice_phone_model-1]}")
    print (f"{sim_item_code[sim_choice-1]}\t {sim_description[sim_choice-1]}\t$ {sim_price[sim_choice-1]}")

if tab_or_phone.lower() == "tablet":
    price = tablet_price[choice_tablet_model-1] + case_price[case_choice-1] + customer_charger_price
    print (f"{tablet_item_code[choice_tablet_model-1]}\t{tablet_description [choice_tablet_model-1]}\t${tablet_price[choice_tablet_model-1]}")
    
print (f"{case_item_code[case_choice-1]}\t {case_description[case_choice-1]}\t ${case_price[case_choice-1]}\t")

# printing charger prices
if charger_choice == 1:
    print ("no charger\t $0")
elif charger_choice == 2 or charger_choice == 3:
    print (f"{charger_item_code[charger_choice-2]} \t{charger_description[charger_choice-2]} \t${charger_price[charger_choice-2]}")
elif charger_choice == 4:
    print (f"{charger_item_code[charger_choice-4]} \t{charger_description[charger_choice-4]} \t${charger_price[charger_choice-4]}")
    print (f"{charger_item_code[charger_choice-3]} \t{charger_description[charger_choice-3]} \t${charger_price[charger_choice-3]}")

price = round(price,2)
print (f"Your total price is $ {price}")
      



