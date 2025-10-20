######### - Created by Adam Clark, final version 15-10-2025.
######### - No form of AI has been used, Category AITS descriptor is 1(No AI)
######### - All sources for reference accounted for. Previous and known knowledge used for vast majority of logic.
######### - Where further reading has been needed, i have included the reference link to the guide at the start of the appropriate area of code.
######### - planet images and planet information taken from google (https://i.ytimg.com/vi/lVdYYpoozZU/maxresdefault.jpg ) and wikipedia respectively.

import unittest
import csv
import tkinter
from tkinter import *
import tkinter as tk
import math
import sys

########## - Holding lists for Planet data from CSV

planet_name = []
planet_mass = []
planet_aphelion = []
planet_perihelion = []
planet_semi_major_axis = []
planet_moons = []
planet_dwarf = []


########## - Dictionary for earth weight and distance constants
constants_dict = {"earth_weight":float(5972168000000000000000000),"earth_distance":float(149600000)}

########## - Planets Class, used with populated data from the CSV, and Lists. Returns specific values of specific planets when called.
class Planets:
    def __init__(self, planet_name, planet_mass, planet_aphelion, planet_perihelion, planet_semi_major_axis, planet_moons):
        self.planet_name = planet_name
        self.planet_mass = planet_mass
        self.planet_aphelion = planet_aphelion
        self.planet_perihelion = planet_perihelion
        self.planet_semi_major_axis = planet_semi_major_axis
        self.planet_moons = planet_moons

    def print_mass(self):
        return (planet_mass[planet_name.index(self)])
    
    def print_aphelion(self):
        return (planet_aphelion[planet_name.index(self)])
    
    def print_perihelion(self):
        return (planet_perihelion[planet_name.index(self)])

    def print_semi_major_axis(self):
        return (planet_semi_major_axis[planet_name.index(self)])
    
    def print_moons(self):
        return (planet_moons[planet_name.index(self)])
    
    
########## - Open_CSVs_Planets Class, reads a pre-determined and populated file for the planet data. Checks if it exists in the file directory and prompts user if not.
########## - Reference link for study - https://docs.python.org/3/library/csv.html
########## - Reference for checking of missing file - https://stackoverflow.com/questions/71837032/python3-file-open-write-exception-handling
class Open_CSVs_Planets():
       
    while True:

        try:
            with open('planet_information.csv', mode='r' ) as file:
                try:                    
                        planet_information = csv.DictReader(file)
                        for row in planet_information:
            
                            try:
                                planet_name.append(row['Planet'])
                                planet_mass.append(row['Mass'])
                                planet_aphelion.append(row['Aphelion'])
                                planet_perihelion.append(row['Perihelion'])
                                planet_semi_major_axis.append(row['Semi-major axis'])
                                planet_moons.append(row['Moons'])

                                valid_number_input = float((row['Mass']))
                                valid_number_input = float((row['Aphelion']))
                                valid_number_input = float((row['Perihelion']))
                                valid_number_input = float((row['Semi-major axis']))

                            except ValueError as error_found_number:
                                print(f"Error with planet_information.csv, none numerical data samples in data,", error_found_number.args[0])
                                sys.exit("Check data and re-run program")

    ##### - Reference - https://stackoverflow.com/questions/13745514/get-key-name-from-python-keyerror-exception
    ##### - Whilst a file might be corrupt and my program intentionally stops to allow the user to fix it, it would be helpful to tell the end user
    ##### - which particular field there is a problem with.
                            except KeyError as error_found_key:
                                print(f"Error with planet_information.csv, missing data samples in", error_found_key.args[0])
                                sys.exit("Check data and re-run program")

                        break
                except (IOError, OSError):
                    print("Error opening planet_information.csv, please ensure the file is located in the same directory as the main Python file")
                    input("Press Enter to try again...")
        except (FileNotFoundError, PermissionError, OSError):
            print("Error opening planet_information.csv, please ensure the file is located in the same directory as the main Python file")
            input("Press Enter to try again...")

########## - Open_CSVs_Dwarfs Class, reads a pre-determined and populated file for the dwarf planet data. Checks if it exists in the file directory and prompts user if not.
########## - Reference link for study - https://docs.python.org/3/library/csv.html
########## - Reference for checking of missing file - https://stackoverflow.com/questions/71837032/python3-file-open-write-exception-handling
class Open_CSVs_Dwarfs():
       
    while True:

        try:
            with open('dwarf_planet_information.csv', mode='r' ) as file:
                try:                    
                        dwarf_planet_information = csv.DictReader(file)
                        for row in dwarf_planet_information:
            
                            try:
                                planet_dwarf.append(row['Dwarf'])
                               

    ##### - Reference - https://stackoverflow.com/questions/13745514/get-key-name-from-python-keyerror-exception
    ##### - Whilst a file might be corrupt and my program intentionally stops to allow the user to fix it, it would be helpful to tell the end user
    ##### - which particular field there is a problem with.
                            except KeyError as error_found_key:
                                print(f"Error with dwarf_planet_information.csv, missing data samples in", error_found_key.args[0])
                                sys.exit("Check data and re-run program")

                        break
                except (IOError, OSError):
                    print("Error opening dwarf_planet_information.csv, please ensure the file is located in the same directory as the main Python file")
                    input("Press Enter to try again...")
        except (FileNotFoundError, PermissionError, OSError):
            print("Error opening dwarf_planet_information.csv, please ensure the file is located in the same directory as the main Python file")
            input("Press Enter to try again...")


########## - Reference for TKinter creation - https://www.geeksforgeeks.org/python/python-tkinter-tutorial/
########## - Whole guide was used in creation of the TKinter features in this program, very useful document.
########## - TKinter page construction for when a planet is clicked. Obtains all information and displays in the GUI.

def click_image(planet_name_passed_in):
 
    planet_details_gui = tk.Tk()
    planet_details_gui.attributes("-toolwindow",1,"-topmost", True)
    
    planet_details_gui.title("Information on the planet "+planet_name_passed_in)
    planet_details_gui.configure(background="grey")
    planet_details_gui.minsize(300, 100)
    planet_details_gui.geometry("600x300+400+300")
    planet_details_gui = Listbox(planet_details_gui, width=75)
    
########## - Pulls data out of the Planet class for the corresponding button that gets clicked on the main GUI.   
    
    planet_details_gui.insert(2, 'Mass is given as ' 
                              + str('{:.2e}'.format(float(Planets.print_mass(planet_name_passed_in)) * constants_dict["earth_weight"])) + ' kgs')
    planet_details_gui.insert(3, 'Aphelion distance (maximum distance from the sun) is given as '
                               + str('{:.2e}'.format(float(Planets.print_aphelion(planet_name_passed_in)) * constants_dict["earth_distance"])) + ' kms')
    planet_details_gui.insert(4, 'Perihelion distance (minimum distance from the sun) is given as ' 
                              + str('{:.2e}'.format(float(Planets.print_perihelion(planet_name_passed_in))* constants_dict["earth_distance"]))+ ' kms')
    planet_details_gui.insert(5, 'Semi-major axis distance (average distance from the sun) is given as ' 
                              + str('{:.2e}'.format(float(Planets.print_semi_major_axis(planet_name_passed_in))* constants_dict["earth_distance"]))+ ' kms')
    
    if Planets.print_moons(planet_name_passed_in) == "none" or Planets.print_moons(planet_name_passed_in) == "":
        planet_details_gui.insert(6, 'The planet ' +planet_name_passed_in+ ' has no moons')
    elif len((Planets.print_moons(planet_name_passed_in)).split()) == 1:
        planet_details_gui.insert(6, 'The planet ' +planet_name_passed_in+ ' has a single moon called ' + Planets.print_moons(planet_name_passed_in))
    else:
        planet_details_gui.insert(6, 'The moons of the planet ' +planet_name_passed_in+ ' are ' + Planets.print_moons(planet_name_passed_in))
        
########## - Launches the planet details GUI.
   
    planet_details_gui.pack()
    
   
########## - Menu interface selection.    
def print_interface_menu_selection():
    print("\nPlease choose a menu interface: \n"
    "(Option 1) Classic Command Line Interface\n"
    "(Option 2) Fancy GUI with TKinter \n"
    "(Option 3) Exit the program \n")
  
    while True:
        try:
            interface_menu_selection = int(input("Option - "))
            if interface_menu_selection <= 3:
                return (interface_menu_selection)
                break
            else:
                print("Input not a valid option")
            
        except ValueError:
            print("Input not a valid option")

########## - Menu information selection
def print_option_main_menu():
    print("\nPlease choose information to lookup : \n"
    "(Option 1) Mass of a planet\n"
    "(Option 2) Distance from the sun of a planet \n"
    "(Option 3) Moons of a planet \n"
    "(Option 4) All information of a planet \n"
    "(Option 5) Return to previous menu")
    while True:
        try:
            option_main_menu_selection = int(input("Option - "))
            if option_main_menu_selection <= 5:
                return (option_main_menu_selection)
                break
            else:
                print("Input not a valid option")
            
        except ValueError:
            print("Input not a valid option")

########## - Menu planet selection
def print_option_sub_menu():
    print("\nPlease select a planet : \n"
    "(Option 1) Mercury\n"
    "(Option 2) Venus \n"
    "(Option 3) Earth \n"
    "(Option 4) Mars \n"
    "(Option 5) Jupiter \n"
    "(Option 6) Saturn \n"
    "(Option 7) Uranus \n"
    "(Option 8) Neptune \n"
    "(Option 9) Pluto \n"
    "(Option 10) Return to previous menu")

    while True:
        try:
            option_sub_menu_selection = int(input("Option - "))
            if option_sub_menu_selection <= 10 and option_sub_menu_selection != 9 :
                return (option_sub_menu_selection)
            elif option_sub_menu_selection == 9:
                print("\nPluto, technically is no longer a planet, it has been re-classified as a dwarf planet")
                while True:
                    try:
            
                        more_planets = input("Would you like to see a list of similar dwarf planets? Yes/No \n")
                
                        if more_planets.lower() == 'yes':
                            print(f"Examples of dwarf planets are:\n", *planet_dwarf,sep=" ", end="\n")
                            input("Press Enter to continue...")
                        
                            return 10
                            break
                    
                        elif more_planets.lower() == 'no':
                            #option_main_menu = 5
                            
                            return 10
                            break

                        print("Input not a valid option")

                    except ValueError:
                        print("Input not a valid option")
            else:
                print("Input not a valid option")
            
        except ValueError:
            print("Input not a valid option")

########## - Main program procedure
def main():

    

##### - Sets up the planet information from the CSV file and Planet Class.
    mercury = Planets(planet_name[planet_name.index("Mercury")],
                      planet_mass[planet_name.index("Mercury")], 
                      planet_aphelion[planet_name.index("Mercury")], 
                      planet_perihelion[planet_name.index("Mercury")], 
                      planet_semi_major_axis[planet_name.index("Mercury")], 
                      planet_moons[planet_name.index("Mercury")])
    
    venus = Planets(planet_name[planet_name.index("Venus")],
                    planet_mass[planet_name.index("Venus")], 
                    planet_aphelion[planet_name.index("Venus")], 
                    planet_perihelion[planet_name.index("Venus")], 
                    planet_semi_major_axis[planet_name.index("Venus")], 
                    planet_moons[planet_name.index("Venus")])
    
    earth = Planets(planet_name[planet_name.index("Earth")],
                    planet_mass[planet_name.index("Earth")], 
                    planet_aphelion[planet_name.index("Earth")], 
                    planet_perihelion[planet_name.index("Earth")], 
                    planet_semi_major_axis[planet_name.index("Earth")], 
                    planet_moons[planet_name.index("Earth")])
    
    mars = Planets(planet_name[planet_name.index("Mars")],
                   planet_mass[planet_name.index("Mars")], 
                   planet_aphelion[planet_name.index("Mars")], 
                   planet_perihelion[planet_name.index("Mars")], 
                   planet_semi_major_axis[planet_name.index("Mars")], 
                   planet_moons[planet_name.index("Mars")])
    
    jupiter = Planets(planet_name[planet_name.index("Jupiter")],
                      planet_mass[planet_name.index("Jupiter")], 
                      planet_aphelion[planet_name.index("Jupiter")], 
                      planet_perihelion[planet_name.index("Jupiter")], 
                      planet_semi_major_axis[planet_name.index("Jupiter")], 
                      planet_moons[planet_name.index("Jupiter")])
    
    saturn = Planets(planet_name[planet_name.index("Saturn")],
                     planet_mass[planet_name.index("Saturn")], 
                     planet_aphelion[planet_name.index("Saturn")], 
                     planet_perihelion[planet_name.index("Saturn")], 
                     planet_semi_major_axis[planet_name.index("Saturn")], 
                     planet_moons[planet_name.index("Saturn")])
    
    uranus = Planets(planet_name[planet_name.index("Uranus")],
                     planet_mass[planet_name.index("Uranus")], 
                     planet_aphelion[planet_name.index("Uranus")], 
                     planet_perihelion[planet_name.index("Uranus")], 
                     planet_semi_major_axis[planet_name.index("Uranus")], 
                     planet_moons[planet_name.index("Uranus")])
    
    neptune = Planets(planet_name[planet_name.index("Neptune")],
                      planet_mass[planet_name.index("Neptune")], 
                      planet_aphelion[planet_name.index("Neptune")], 
                      planet_perihelion[planet_name.index("Neptune")], 
                      planet_semi_major_axis[planet_name.index("Neptune")], 
                      planet_moons[planet_name.index("Neptune")])
    


##### - While loop which drives the menu options, allowing the user to navigate between different menu levels.    
    option_interface_menu_selection = 0
    option_main_menu = 0
    option_sub_menu = 0
    
    while option_interface_menu_selection != 3:
        option_interface_menu_selection = print_interface_menu_selection()

        
        while (option_interface_menu_selection) == 1:
            
            option_main_menu = print_option_main_menu()
            if  (option_main_menu) == 5:
                break
                


            while option_main_menu != 5:
                if  (option_main_menu) == 1:
                    option_sub_menu = print_option_sub_menu()
                    if option_sub_menu != 10:
                    
                        print(f"\nThe mass of the planet", planet_name[option_sub_menu-1], "is", ('{:.2e}'.format(float(planet_mass[option_sub_menu-1]) * constants_dict["earth_weight"])),"kgs\n"
                              "The equivalant of",(planet_mass[option_sub_menu-1]),"earths\n" )
                        input("Press Enter to continue...")
                        break
                    break

                if  (option_main_menu) == 2:
                    option_sub_menu = print_option_sub_menu()
                    if option_sub_menu != 10:
                        print(f"\nThe distance of the planet",planet_name[option_sub_menu-1],"from the sun is given as:\n",
                              ('{:.2e}'.format((float(planet_aphelion[option_sub_menu-1]) * constants_dict["earth_distance"]))),"km's as its Aphelion (maxmium distance)\n",
                              ('{:.2e}'.format((float(planet_perihelion[option_sub_menu-1]) * constants_dict["earth_distance"]))),"km's as its Perhihelion (minumum distance)\n",
                              ('{:.2e}'.format((float(planet_semi_major_axis[option_sub_menu-1]) * constants_dict["earth_distance"]))),"km's as its average distance")
                        input("Press Enter to continue...")
                        break
                    break

                if  (option_main_menu) == 3:
                    option_sub_menu = print_option_sub_menu()
                    if option_sub_menu != 10:
                        if planet_moons[option_sub_menu-1] == "none" or planet_moons[option_sub_menu-1] == "":
                            print(f"\n",planet_name[option_sub_menu-1],"has no moons \n")
                            input("Press Enter to continue...")
                        elif len((planet_moons[option_sub_menu-1]).split()) == 1:
                            print(f"\nThe planet",planet_name[option_sub_menu-1],"has a single moon called",planet_moons[option_sub_menu-1],"\n")
                            input("Press Enter to continue...")
                        else:                        
                            print(f"\nThe moons of the planet", planet_name[option_sub_menu-1],"are",planet_moons[option_sub_menu-1]," \n" )
                            input("Press Enter to continue...")
                        break
                    break

                
                if  (option_main_menu) == 4:
                    option_sub_menu = print_option_sub_menu()
                    if option_sub_menu != 10:

                        
                        print(f"\nThe mass of the planet", planet_name[option_sub_menu-1], "is", ('{:.2e}'.format(float(planet_mass[option_sub_menu-1]) * constants_dict["earth_weight"])),"kgs\n"
                              "The equivalant of",(planet_mass[option_sub_menu-1]),"earths.\n" )
                        print(f"The distance of the planet",planet_name[option_sub_menu-1],"from the sun is given as:\n",
                              ('{:.2e}'.format(float(planet_aphelion[option_sub_menu-1]) * constants_dict["earth_distance"])),"km's as its Aphelion (maxmium distance)\n",
                              ('{:.2e}'.format(float(planet_perihelion[option_sub_menu-1]) * constants_dict["earth_distance"])),"km's as its Perhihelion (minumum distance)\n",
                              ('{:.2e}'.format(float(planet_semi_major_axis[option_sub_menu-1]) * constants_dict["earth_distance"])),"km's as its average distance")
                        
                        if planet_moons[option_sub_menu-1] == "none" or planet_moons[option_sub_menu-1] == "":
                            print(f"",planet_name[option_sub_menu-1],"has no moons \n")
                            input("Press Enter to continue...")
                        elif len((planet_moons[option_sub_menu-1]).split()) == 1:
                            print(f"The planet",planet_name[option_sub_menu-1],"has a single moon called",planet_moons[option_sub_menu-1],"\n")
                            input("Press Enter to continue...")
                        else:                        
                            print(f"The moons of the planet", planet_name[option_sub_menu-1],"are",planet_moons[option_sub_menu-1]," \n" )
                            input("Press Enter to continue...")
                        break
                    break
                    
           
##### - TKinter which creates the main GUI, showing pictures of the planets allowing for a user friendly interface.
##### - Reference for works - https://www.geeksforgeeks.org/python/python-tkinter-tutorial/
##### - Images taken from https://i.ytimg.com/vi/lVdYYpoozZU/maxresdefault.jpg               
  
       
        while (option_interface_menu_selection) == 2:
            planet_gui = tk.Tk()
            planet_gui.attributes("-toolwindow",1, "-topmost", True)
            planet_gui.title("Solar System Explorer - Created by A.Clark")
            planet_gui.configure(background="black")
            planet_gui.minsize(1150, 650)
            planet_gui.geometry("900x300+150+150")


            tk.Label(planet_gui, text="Welcome to the Solar System Planet Explorer V1.0", font=("Arial", 25)).place(x=200, y=20)
            tk.Label(planet_gui, text="Click on a planet to learn more..", font=("Arial", 15)).place(x=425, y=80)
            
##### - Performs data check that picture files are located in the same directory as program.
            try:
                planet_gui_mercury_image = tk.PhotoImage(file="mercury.gif")
                planet_gui_venus_image = tk.PhotoImage(file="venus.gif")
                planet_gui_earth_image = tk.PhotoImage(file="earth.gif")
                planet_gui_mars_image = tk.PhotoImage(file="mars.gif")
                planet_gui_jupiter_image = tk.PhotoImage(file="jupiter.gif")
                planet_gui_saturn_image = tk.PhotoImage(file="saturn.gif")
                planet_gui_uranus_image = tk.PhotoImage(file="uranus.gif")
                planet_gui_neptune_image = tk.PhotoImage(file="neptune.gif")
                              
            except (TclError):
                print("Error with the planet gifs, please ensure all the planet gifs are located in the same directory as the Main Python file")
                sys.exit("Check data and re-run program")

                
                              
            img_label= Label(image=planet_gui_mercury_image)

            tk.Label(planet_gui, image=planet_gui_mercury_image, borderwidth=0, highlightthickness=0).place(x=50, y=200)
            tk.Label(planet_gui, image=planet_gui_venus_image, borderwidth=0, highlightthickness=0).place(x=350, y=200)
            tk.Label(planet_gui, image=planet_gui_earth_image, borderwidth=0, highlightthickness=0).place(x=650, y=200)
            tk.Label(planet_gui, image=planet_gui_mars_image, borderwidth=0, highlightthickness=0).place(x=950, y=200)
            tk.Label(planet_gui, image=planet_gui_jupiter_image, borderwidth=0, highlightthickness=0).place(x=50, y=400)
            tk.Label(planet_gui, image=planet_gui_saturn_image, borderwidth=0, highlightthickness=0).place(x=320, y=390)
            tk.Label(planet_gui, image=planet_gui_uranus_image, borderwidth=0, highlightthickness=0).place(x=650, y=400)
            tk.Label(planet_gui, image=planet_gui_neptune_image, borderwidth=0, highlightthickness=0).place(x=950, y=400)


            planet_gui_mercury_image_click= Button(planet_gui, image=planet_gui_mercury_image,borderwidth=0, highlightthickness=0, command=lambda: click_image("Mercury")).place(x=50, y=200)
            planet_gui_venus_image_click= Button(planet_gui, image=planet_gui_venus_image,borderwidth=0, highlightthickness=0, command=lambda: click_image("Venus")).place(x=350, y=200)
            planet_gui_earth_image_click= Button(planet_gui, image=planet_gui_earth_image,borderwidth=0, highlightthickness=0, command=lambda: click_image("Earth")).place(x=650, y=200)
            planet_gui_mars_image_click= Button(planet_gui, image=planet_gui_mars_image,borderwidth=0, highlightthickness=0, command=lambda: click_image("Mars")).place(x=950, y=200)
            planet_gui_jupiter_image_click= Button(planet_gui, image=planet_gui_jupiter_image,borderwidth=0, highlightthickness=0, command=lambda: click_image("Jupiter")).place(x=50, y=400)
            planet_gui_saturn_image_click= Button(planet_gui, image=planet_gui_saturn_image,borderwidth=0, highlightthickness=0, command=lambda: click_image("Saturn")).place(x=320, y=390)
            planet_gui_uranus_image_click= Button(planet_gui, image=planet_gui_uranus_image,borderwidth=0, highlightthickness=0, command=lambda: click_image("Uranus")).place(x=650, y=400)
            planet_gui_neptune_image_click= Button(planet_gui, image=planet_gui_neptune_image,borderwidth=0, highlightthickness=0, command=lambda: click_image("Neptune")).place(x=950, y=400)

########## - Launches the main planet GUI.
            planet_gui.mainloop()
            break
    print(f"Goodbye")
if __name__ == '__main__':
    main()


