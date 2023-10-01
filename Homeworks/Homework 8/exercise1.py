"""
PROGRAMMING ASSIGNMENT 07
Filename: 'exercise1.py'
"""
# Place your imports here if any

def build_attraction_dict(filename):
    """
    Read from the file for which the filename was given and returns a dictionary

    The key / value pairs in the dictionary will be:
        • key → attraction name (str type)
        • value → Province (str type)
    """
    # TODO


def add_attraction(dic):
    """
    This function takes a dictionary as a parameter and does not return anything.

    The function:
        • asks the user to input an attraction name
        • asks the user to input a province
        • updates the dictionary with a new key / value pair (with a similar format for
        task 1)
    """
    # TODO


def build_province_attraction_dict(dic):
    """
    This function takes a dictionary as a parameter and returns another dictionary.

    The input dictionary is constituted of key / value pairs similar to the ones built in task 1.

    The returned dictionary should have key / value pair with:
        • key → Province (str type)
        • value → list of attraction names (list of str type) associated to the Province
    """
    # TODO


def most_attractions(dic):
    """
    This function takes a dictionary as a parameter and returns a set.

    The input dictionary is constituted of key / value pairs similar to the ones built in task 3.

    The returned set should contain the Provinces which have at least 3 tourist attractions
    (in the input dictionary).
    """
    # TODO


def main():
    """
    The main() function will
        1. calls `build_province_attraction_dict` with filename top_tourist_attractions.txt as 
            parameter to generate the first dictionary.
        2. calls `add_attraction` one time in order to update the dictionary. The user will input
            a new (non-existing) attraction name/Province pair.
        3. calls `build_province_attraction_dict` in order to generate a second dictionary.
        4. calls `most_attractions` in order to generate the set of Provinces with at least 3 attractions.
        5. prints the Provinces with at least 3 attractions. Display one Province per line.
            See sample examples for the proper format (empty line + Header line).
            
    """
    # TODO


if __name__ == '__main__':
    main()
