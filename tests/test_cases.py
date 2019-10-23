import pytest
import argparse

from main import parse_args, _main
from src import Bartender


def _input_validator(args):
    try:
        parse_args(args)
    except SystemExit as e:
        assert isinstance(e.__context__, argparse.ArgumentError)
        assert 'Value has to be greater than 0' in str(e.__context__)
    else:
        raise ValueError("Exception not raised")


def test_input_validation():
    """Test the command line input validation
    """
    # invalid inputs
    _input_validator(['-g', '0', '-p', '1', '-c', '1'])
    _input_validator(['-g', '1', '-p', '0', '-c', '1'])
    _input_validator(['-g', '1', '-p', '1', '-c', '0'])

    # valid input
    with pytest.raises(ValueError):
        _input_validator(['-g', '1', '-p', '1', '-c', '1'])


def test_fountain_creation():
    """Test that the fountain structure is created correctly
    """
    for i in range(1, 10):
        bartender = Bartender(i, i)
        fountain = bartender._fountain

        # validate correct number of levels
        assert len(fountain.tower) == i

        # validate correct number of glasses per level
        for level, glasses in fountain.tower.items():
            assert level+1 == len(glasses)

            # validate capacity of glasses
            for glass in glasses:
                assert glass.capacity == i


def test_workflow():
    """Test that the workflow is correct and that the 
    calculated results are as expceted
    """
    nr_bottom = 4
    capacity = 250
    pour = 1000

    bartender = Bartender(nr_bottom, capacity)
    bartender.place_order(pour)

    tower = bartender._fountain.tower

    # validate fountain after pouring
    assert tower[0][0].amount_filled == 250
    assert tower[1][0].amount_filled == 250
    assert tower[1][1].amount_filled == 250
    assert tower[2][0].amount_filled == 62.5
    assert tower[2][1].amount_filled == 125.0
    assert tower[2][2].amount_filled == 62.5
    assert tower[3][0].amount_filled == 0
    assert tower[3][1].amount_filled == 0
    assert tower[3][2].amount_filled == 0
    assert tower[3][3].amount_filled == 0

    bartender.display_order()


def test_visualization():
    """Test that the visualization is created as expected
    """
    nr_bottom = 4
    capacity = 250
    pour = 1000

    bartender = Bartender(nr_bottom, capacity)
    bartender.place_order(pour)

    tower = bartender._fountain.tower
    graph_fountain = bartender._visualizer.visualize(tower)

    expected_graph = """             |  250  |
              ------- 
         |  250  ||  250  |
          -------  ------- 
    |  62.5 || 125.0 ||  62.5 |
     -------  -------  ------- 
|   0   ||   0   ||   0   ||   0   |
 -------  -------  -------  ------- 
"""
    
    assert expected_graph == graph_fountain

