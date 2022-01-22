
class options:
    def choice():
        print("1.Check available tickets    2.Booking tickets     3.Exit")
        option = int(input("enter the option:"))
        if option == 1:
            print(
                "Now", Bus.total_no_bus_tickets1[0]['total_ticket'], "are available")
            print(
                "Now", Train.total_no_train_tickets1[0]['total_ticket'], "are available")
            print(
                "Now", Flight.total_no_flight_tickets1[0]['total_ticket'], "are available")
            option_.choice()
        elif option == 2:
            option_.booking()
        elif option == 3:
            exit()
        else:
            print("You were selected wrong option please selerct currect one:")
            option_.choice()

    def booking():
        print("1.bus  2.train  3.flight  4.back")
        option = int(input("enter the option:"))
        if option == 1:
            bus_.bus()
        elif option == 2:
            train_.train()
        elif option == 3:
            flight_.flight()
        elif option == 4:
            option_.choice()
        else:
            print("You were selected wrong option please selerct currect one:")
            option_.booking()


option_ = options


class Bus:
    customer = []
    total_no_bus_tickets1 = [{"total_ticket": 10}]

    def bus():
        print("1.book  2.cancel  3.show availablity    4.show booking    5.back   6.exit  7.main menu")
        option = int(input("enter the option:"))
        if option == 1:
            bus_.book()
        elif option == 2:
            bus_.cancel()
        elif option == 3:
            bus_.show_avail()
        elif option == 4:
            bus_.show_booking()
        elif option == 5:
            option_.booking()
        elif option == 6:
            exit()
        elif option == 7:
            option_.booking()
        else:
            print("You were selected wrong option please selerct currect one:")
            option_.booking()

    def book():
        name = input("enter the name:")
        age = int(input("enter the age:"))
        from_ = input("your location:")
        to_ = input("your destination location:")
        ticket = int(input("enter the ticket:"))
        user = {"name": name, "age": age,
                "from": from_, "to": to_, "tickets": ticket}
        if ticket >= Bus.total_no_bus_tickets1[0]['total_ticket']+1:
            print("Only", Bus.total_no_bus_tickets1,
                  "tickets available now, please book again?")
        else:
            booked_tickets = Bus.total_no_bus_tickets1[0]['total_ticket']-ticket
            Bus.total_no_bus_tickets1[0]['total_ticket'] = booked_tickets
            Bus.customer.append(user)
            print(ticket, "tickets was booked")
            print(Bus.customer)
            print(Bus.total_no_bus_tickets1[0])
            pass
        bus_.bus()

    def cancel():
        print("you have total",
              Bus.total_no_bus_tickets1[0]['total_ticket'], "tickets")
        print("if you want to cancel your tickets please select the option: 1.yes   2.no :")
        option = int(input("enter your choice:"))
        if option == 1:
            options = input("enter your name for confirmation:")
            for i in range(len(Bus.customer)):
                if options == Bus.customer[i]['name']:
                    p = int(
                        input("how many tickets do you want cancel in your tickets:"))
                    if Bus.customer[i]['tickets'] >= p:

                        new = Bus.customer[i]["tickets"]-p
                        cvo = p + \
                            Bus.total_no_bus_tickets1[0]['total_ticket']
                        Bus.total_no_bus_tickets1[0]['total_ticket'] = cvo
                        Bus.customer[i]['tickets'] = new
                        print(p, "tickets was successfully canceled")
                    else:
                        print(
                            "you have", Bus.customer[i]['tickets'], "but you are tring to cancel", p)
                        bus_.cancel()
                else:
                    print("You were selected wrong option please selerct currect one:")
                    train_.train()
        elif option == 2:
            bus_.bus()
        else:
            print("You were selected wrong option please selerct currect one:")
        bus_.bus()

    def show_avail():
        print(
            "Now", Bus.total_no_bus_tickets1[0]['total_ticket'], "are available")
        bus_.bus()

    def show_booking():
        if len(Bus.customer) == 0:
            print("there is no booking here!!")
        else:
            for i in range(len(Bus.customer)):
                print("hi", Bus.customer[i]['name'], "you booked ",
                      Bus.customer[i]['tickets'], "tickets")

        bus_.bus()


bus_ = Bus


class Train:
    customer1 = []
    total_no_train_tickets1 = [{"total_ticket": 30}]

    def train():
        print("1.book  2.cancel  3.show availablity    4.show booking    5.back   6.exit  7.main menu")
        option = int(input("enter the option:"))
        if option == 1:
            train_.book()
        elif option == 2:
            train_.cancel()
        elif option == 3:
            train_.show_avail()
        elif option == 4:
            train_.show_booking()
        elif option == 5:
            option_.booking()
        elif option == 6:
            exit()
        elif option == 7:
            option_.choice()
        else:
            print("You were selected wrong option please selerct currect one:")
            train_.train()

    def book():
        name = input("enter the name:")
        age = int(input("enter the age:"))
        from_ = input("your location:")
        to_ = input("your destination location:")
        ticket = int(input("enter the ticket:"))
        user = {"name": name, "age": age,
                "from": from_, "to": to_, "tickets": ticket}

        if ticket >= Train.total_no_train_tickets1[0]['total_ticket']+1:
            print("Only", Train.total_no_train_tickets1,
                  "tickets available now, please book again?")
        else:
            booked_tickets = Train.total_no_train_tickets1[0]['total_ticket']-ticket
            Train.total_no_train_tickets1[0]['total_ticket'] = booked_tickets
            Train.customer1.append(user)
            print(ticket, "tickets was booked")
        train_.train()

    def cancel():
        print("if you want to cancel your tickets please select the option: 1.yes   2.no :")
        option = int(input("enter your choice:"))
        if option == 1:
            options = input("enter your name for confirmation:")
            for i in range(len(Train.customer1)):
                if options == Train.customer1[i]['name']:
                    p = int(
                        input("how many tickets do you want cancel in your tickets:"))
                    if Train.customer1[i]['tickets'] >= p:
                        new = Train.customer1[i]["tickets"]-p
                        cvo = p + \
                            Train.total_no_train_tickets1[0]['total_ticket']
                        Train.total_no_train_tickets1[0]['total_ticket'] = cvo
                        Train.customer1[i]['tickets'] = new
                        print(p, "tickets was successfully canceled")
                    else:
                        print(
                            "you have", Train.customer1[i]['tickets'], "but you are tring to cancel", p)
                        train_.cancel()
                else:
                    print("You were selected wrong option please selerct currect one:")
                    train_.train()

        elif option == 2:
            train_.train()

        else:
            print("You were selected wrong option please selerct currect one:")
        train_.train()

    def show_avail():
        print(
            "Now", Train.total_no_train_tickets1[0]['total_ticket'], "are available")
        train_.train()

    def show_booking():
        if len(Train.customer1) == 0:
            print("there is no booking here!!")
        else:
            for i in range(len(Train.customer1)):
                print("hi", Train.customer1[i]['name'], "you booked ",
                      Train.customer1[i]['tickets'], "tickets")

        train_.train()


train_ = Train


class Flight(options):
    customer2 = []
    total_no_flight_tickets1 = [{"total_ticket": 30}]

    def flight():
        print("1.book  2.cancel  3.show availablity    4.show booking    5.back   6.exit  7.main menu")
        option = int(input("enter the option:"))
        if option == 1:
            flight_.book()
        elif option == 2:
            flight_.cancel()
        elif option == 3:
            flight_.show_avail()
        elif option == 4:
            flight_.show_booking()
        elif option == 5:
            option_.booking()
        elif option == 6:
            exit()
        elif option == 7:
            option_.booking()
        else:
            print("You were selected wrong option please selerct currect one:")
            option_.choice()

    def book():
        name = input("enter the name:")
        age = int(input("enter the age:"))
        from_ = input("your location:")
        to_ = input("your destination location:")
        ticket = int(input("enter the ticket:"))
        user = {"name": name, "age": age,
                "from": from_, "to": to_, "tickets": ticket}
        if ticket >= Flight.total_no_flight_tickets1[0]['total_ticket']+1:
            print("Only", Flight.total_no_flight_tickets1,
                  "tickets available now, please book again?")
        else:
            booked_tickets = Flight.total_no_flight_tickets1[0]['total_ticket']-ticket
            Flight.total_no_flight_tickets1[0]['total_ticket'] = booked_tickets
            Flight.customer2.append(user)
            print(ticket, "tickets was booked")

        flight_.flight()

    def cancel():
        print("if you want to cancel your tickets please select the option: 1.yes   2.no :")
        option = int(input("enter your choice:"))
        if option == 1:
            options = input("enter your name for confirmation:")
            for i in range(len(Flight.customer2)):
                if options == Flight.customer2[i]['name']:
                    p = int(
                        input("how many tickets do you want cancel in your tickets:"))
                    if Flight.customer2[i]['tickets'] >= p:
                        new = Flight.customer2[i]["tickets"]-p
                        print(new)
                        cvo = p + \
                            Flight.total_no_flight_tickets1[0]['total_ticket']
                        Flight.total_no_flight_tickets1[0]['total_ticket'] = cvo
                        Flight.customer2[i]['tickets'] = new
                        print(p, "tickets was successfully canceled")
                    else:
                        print(
                            "you have", Flight.customer2[i]['tickets'], "but you are tring to cancel", p)
                        flight_.cancel()
                else:
                    print("You were selected wrong option please selerct currect one:")
                    flight_.cancel()
        elif option == 2:
            train_.train()
        else:
            print("You were selected wrong option please selerct currect one:")
            flight_.cancel()

        flight_.flight()

    def show_avail():
        print(
            "Now", Flight.total_no_flight_tickets1[0]['total_ticket'], "are available")
        flight_.flight()

    def show_booking():
        if len(Flight.customer2) == 0:
            print("there is no booking here!!")
        else:
            for i in range(len(Flight.customer2)):
                print("hi", Flight.customer2[i]['name'], "you have booked ",
                      Flight.customer2[i]['tickets'], "flight tickets")
        flight_.flight()


flight_ = Flight


option_.choice()
