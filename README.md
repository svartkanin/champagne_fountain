# Champagne fountain simulation

This is a simple illustration of how liquid is distributed when poured over a fountain consisting of champagne glasses.


## Quick start

Install `Python 3.7` and run the code from the command line:

```python main.py --num-bottom-glasses 4 --pour 1000 --glass-capacity 250```

This will create a fountain with 4 glasses on the bottom, a capacity of 250 milliliters for each glass and a total amount of 1000 milliliters is poured on them.


## Run the tests
To run the tests, please install `pytest` first with

```pip install -r requirements```

then execute

```python -m pytest -s -x```

## Example output

```
$ python main.py --num-bottom-glasses 4 --pour 1000 --glass-capacity 250

Order was: 1000
Fountain total glasses: 10

             |  250  |
              ------- 
         |  250  ||  250  |
          -------  ------- 
    |  62.5 || 125.0 ||  62.5 |
     -------  -------  ------- 
|   0   ||   0   ||   0   ||   0   |
 -------  -------  -------  ------- 

0 milliliter were poured on the table
```

```
$ python main.py --num-bottom-glasses 6 --pour 10000 --glass-capacity 500

Order was: 10000
Fountain total glasses: 21

                         |   500  |
                          -------- 
                    |   500  ||   500  |
                     --------  -------- 
               |   500  ||   500  ||   500  |
                --------  --------  -------- 
          |   500  ||   500  ||   500  ||   500  |
           --------  --------  --------  -------- 
     | 156.25 ||   500  ||   500  ||   500  || 156.25 |
      --------  --------  --------  --------  -------- 
|    0   ||  375.0 ||   500  ||   500  ||  375.0 ||    0   |
 --------  --------  --------  --------  --------  -------- 

1437.5 milliliter were poured on the table
```
