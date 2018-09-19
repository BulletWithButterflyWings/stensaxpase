print ("Hello")
print ("andra kommandot")

#Mitt bankprogram
print("*** Välkommen till Alfons Bankprogram***")
print("!.Skriv in det önskade antalet")
+ "2. Skriv in hur mycket pengar du vill överföra"
+ "3. Avsluta och uppdatera sidan")
Bankbalans = ""
withdraw = 0
while withdraw != 3:
    try:
        withdraw = int (input ("Ange hur mycket du vill överföra"))
        except :
            print("Du måste ange hur mycket du vill överföra!")

            if withdraw ==1: 
                Balans += input("Skriv in den balans di önskar: ") + ","
                elif withdraw == 2:
                    print ("Din angivna överföring är: ", överföring)
                    elif withdraw == 3:
                        print ("Tack för idag!")
                        else:
                            print("Du angav inget tal, försök gärna igen")