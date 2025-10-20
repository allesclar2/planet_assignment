######### - Created by Adam Clark, final version 15-10-2025.
######### - No form of AI has been used, Category AITS descriptor is 1(No AI)
######### - All sources for reference accounted for. Previous and known knowledge used for vast majority of logic.
######### - Where further reading has been needed, i have included the reference link to the guide at the start of the appropriate area of code.
######### - This test file has been created to be used in condjustion with the debugging method included (provided with screenshots)

import pytest
from planet_assignment_with_cli_gui import print_interface_menu_selection
from planet_assignment_with_cli_gui import click_image
from planet_assignment_with_cli_gui import Planets

def test_1():
    assert click_image("Mercury") != ValueError
    #value check inputed into click_image
    
def test_2():
    try:
        click_image("Mercury")
    except MyError:
        pytest.fail("Unexpected MyError")
    #passed data into GUI build and returns with no errors, GUI successfully built

def test_3():
    assert Planets.print_aphelion("Mercury") != ""
   

def test_4():
    assert Planets.print_perihelion("Mercury") != ""

def test_5():
    assert Planets.print_mass("Mercury") != ""
 

def test_6():
    assert Planets.print_semi_major_axis("Mercury") != ""

def test_7():
    assert Planets.print_moons("Mercury") != ""
   
def test_9():
    object_1 = Planets("Mercury",50,100,40,20,"Big Cheese")
    assert object_1.planet_aphelion != ""
    assert object_1.planet_mass != ""
    assert object_1.planet_moons != ""
    assert object_1.planet_name != ""
    assert object_1.planet_perihelion != ""
    assert object_1.planet_semi_major_axis != ""

    #raised exception if no data input test
    ##### - Reference - https://python-forum.io/thread-5727.html
def test_10():
    with pytest.raises(Exception) as e_info:
        object_2 = Planets()

def test_11():
    with pytest.raises(Exception) as e_info:
        object_3 = click_image()

