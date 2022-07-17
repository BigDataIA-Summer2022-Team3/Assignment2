import sys
import os
sys.path.append(os.path.abspath('../service'))

from count_airplanes_in_given_image import count_airplanes_in_given_image as counter
from return_images_with_given_number_of_aircraft import return_images_with_given_number_of_aircraft as numOfAircraft
from return_images_with_maximum_airplanes import return_images_with_maximum_airplanes as maxNumAirplanes
from return_images_with_truncated_aircraft import return_images_with_truncated_aircraft as numTruncatedAircraft
from display_top_aircraft import display_top_aircraft as display_top
from has_aircraft_in_given_x_y_coordinate import has_aircraft_in_given_x_y_coordinate as has_aircraft
from get_coordinates_of_all_airplanes import get_coordinates_of_all_airplanes as get_coordinates

def test_count_airplane():
    res = counter("1e7e0450-6eb3-479e-88c2-990abc8207fa.jpg") 
    assert res == {'number_of_airplanes': 52};

def test_count_airplane_not_found_data():
    res = counter("wrong_info")
    assert res == "No image found related to the image_id. Try effective image_id"

    res1 = counter("错误信息")
    assert res1 == "No image found related to the image_id. Try effective image_id"

    res2 = counter("")
    assert res2 == "No image found related to the image_id. Try effective image_id"


def test_return_images_with_given_number_of_aircraft():
    res = numOfAircraft(30, 3)
    assert res == { 0: {'img_id': '074737f4-7f59-4729-be5d-67f6f1d34668.jpg'}, 
                    1: {'img_id': '3da0b873-fdde-4faf-9a85-021248c7dacf.jpg'}, 
                    2: {'img_id': '5c9e817a-dc4b-42ab-952c-3128e2de12e8.jpg'}};

    res0 = numOfAircraft(-2,1000000)
    assert res0 == "Both Input numbers should be positive"

    res1 = numOfAircraft(2,1000000)
    assert res1 == "limit_of_image should between [1,10]"

    res3 = numOfAircraft(3)
    assert res3 == "No image in database has 3 airplanes. Please try another possible number"

    res4 = numOfAircraft("wrong_info")
    assert res4 == "Please enter two integer number."

    res5 = numOfAircraft("")
    assert res5 == "Please enter two integer number."
                

def test_return_images_with_given_number_of_aircraft_wrong_numbers():
    res = numOfAircraft(-2,1000000)
    assert res == "Both Input numbers should be positive"

    res1 = numOfAircraft(2,1000000)
    assert res1 == "limit_of_image should between [1,10]"

    res3 = numOfAircraft(3)
    assert res3 == "No image in database has 3 airplanes. Please try another possible number"

    res4 = numOfAircraft("wrong_info")
    assert res4 == "Please enter two integer number."

    res5 = numOfAircraft("")
    assert res5 == "Please enter two integer number."



def test_return_images_with_maximum_airplanes():
    res = maxNumAirplanes(3)
    assert res == { 0: {'img_id': 'd9399a45-6745-4e59-8903-90640b2ddf9f.jpg', 'num_of_airplanes': 92}, 
                    1: {'img_id': 'cbd51501-ed0f-411c-b472-df4357cca40c.jpg', 'num_of_airplanes': 88}, 
                    2: {'img_id': '56e2d3d3-6b16-401f-a300-847272373df5.jpg', 'num_of_airplanes': 71}
                };

def test_return_images_with_maximum_airplanes_wrong_numbers():
    res = maxNumAirplanes(-2)
    assert res == "limit_of_image should between [1,10]"

    res1 = maxNumAirplanes("wrong_info")
    assert res1 == "Please enter integer number."

    res2 = maxNumAirplanes("")
    assert res2 == "Please enter integer number."



def test_return_images_with_truncated_aircraft():
    res = numTruncatedAircraft(-2)
    assert res == "limit_of_image should between [1,10]"

    res1 = numTruncatedAircraft("wrong_info")
    assert res1 == "Please enter integer number."

    res2 = numTruncatedAircraft("")
    assert res2 == "Please enter integer number."

    res3 = numTruncatedAircraft(2)
    assert res3 == {0: {'img_id': 'af67041b-f363-47ae-8ddd-f652db3a6bab.jpg', 'number_of_truncated_airplanes': 12}, 
                    1: {'img_id': '6627e7c7-2fdd-4f3c-965e-b4d73d0a4cc2.jpg', 'number_of_truncated_airplanes': 8}
                    }



def test_display_big():
    big = display_top("5c9e817a-dc4b-42ab-952c-3128e2de12e8.jpg",5, True)
    assert big == { 0: {'Xmin': 2067, 'Ymin': 1344, 'Xmax': 2269, 'Ymax': 1568}, 
                    1: {'Xmin': 979, 'Ymin': 1641, 'Xmax': 1192, 'Ymax': 1853}, 
                    2: {'Xmin': 2079, 'Ymin': 1574, 'Xmax': 2287, 'Ymax': 1789}, 
                    3: {'Xmin': 1990, 'Ymin': 472, 'Xmax': 2182, 'Ymax': 685}, 
                    4: {'Xmin': 1555, 'Ymin': 479, 'Xmax': 1758, 'Ymax': 651}
                    }

    small = display_top("5c9e817a-dc4b-42ab-952c-3128e2de12e8.jpg",3, False)
    assert small == { 0: {'Xmin': 634, 'Ymin': 2062, 'Xmax': 724, 'Ymax': 2137}, 
                    1: {'Xmin': 272, 'Ymin': 1590, 'Xmax': 377, 'Ymax': 1676}, 
                    2: {'Xmin': 36, 'Ymin': 1730, 'Xmax': 122, 'Ymax': 1836}
                    }

    invalid_id = display_top("123",5, True)
    assert invalid_id == "No image found related to the image_id. Try effective image_id"

    ask_too_many = display_top("5c9e817a-dc4b-42ab-952c-3128e2de12e8.jpg", 20, True)
    assert ask_too_many == "limit_of_image should between [1,10]"



def test_has_aircraft():
    wrong_image = has_aircraft("123",1600, 500)
    assert wrong_image == "No image found related to the image_id. Try effective image_id"
    
    overbound = has_aircraft("123", 10, 3000)
    assert overbound == "Input X and Y should within (0,2560)"
    
    invalid_id = has_aircraft("123",1950,280)
    assert invalid_id == "No image found related to the image_id. Try effective image_id"

    found = has_aircraft("5c9e817a-dc4b-42ab-952c-3128e2de12e8.jpg",1600,500)
    assert found == {'image_id': '5c9e817a-dc4b-42ab-952c-3128e2de12e8.jpg', 
                    'has_airplane': True, 
                    'coordinate': {'Xmin': 1555, 'Ymin': 479, 'Xmax': 1758, 'Ymax': 651}
                    }

    not_found = has_aircraft("5c9e817a-dc4b-42ab-952c-3128e2de12e8.jpg", 2000, 1600)
    assert not_found ==  {'image_id': '5c9e817a-dc4b-42ab-952c-3128e2de12e8.jpg', 
                        'has_airplane': False}


def test_get_all_coordinates(): 
    all_coordinates = get_coordinates("5c9e817a-dc4b-42ab-952c-3128e2de12e8.jpg")
    assert all_coordinates == {'image_id': '5c9e817a-dc4b-42ab-952c-3128e2de12e8.jpg', 'coordinates': {0: {'Xmin': 1950, 'Ymin': 280, 'Xmax': 2139, 'Ymax': 436}, 1: {'Xmin': 1990, 'Ymin': 472, 'Xmax': 2182, 'Ymax': 685}, 2: {'Xmin': 1989, 'Ymin': 722, 'Xmax': 2187, 'Ymax': 894}, 3: {'Xmin': 1539, 'Ymin': 304, 'Xmax': 1729, 'Ymax': 453}, 4: {'Xmin': 1555, 'Ymin': 479, 'Xmax': 1758, 'Ymax': 651}, 5: {'Xmin': 1572, 'Ymin': 671, 'Xmax': 1768, 'Ymax': 840}, 6: {'Xmin': 1604, 'Ymin': 868, 'Xmax': 1789, 'Ymax': 1018}, 7: {'Xmin': 876, 'Ymin': 350, 'Xmax': 1048, 'Ymax': 482}, 8: {'Xmin': 898, 'Ymin': 529, 'Xmax': 1061, 'Ymax': 668}, 9: {'Xmin': 467, 'Ymin': 590, 'Xmax': 643, 'Ymax': 743}, 10: {'Xmin': 2067, 'Ymin': 1344, 'Xmax': 2269, 'Ymax': 1568}, 11: {'Xmin': 2079, 'Ymin': 1574, 'Xmax': 2287, 'Ymax': 1789}, 12: {'Xmin': 2090, 'Ymin': 1806, 'Xmax': 2293, 'Ymax': 1978}, 13: {'Xmin': 2108, 'Ymin': 2042, 'Xmax': 2288, 'Ymax': 2212}, 14: {'Xmin': 1632, 'Ymin': 1370, 'Xmax': 1820, 'Ymax': 1531}, 15: {'Xmin': 1643, 'Ymin': 1568, 'Xmax': 1841, 'Ymax': 1718}, 16: {'Xmin': 1664, 'Ymin': 1739, 'Xmax': 1841, 'Ymax': 1889}, 17: {'Xmin': 1686, 'Ymin': 1926, 'Xmax': 1860, 'Ymax': 2081}, 18: {'Xmin': 1701, 'Ymin': 2112, 'Xmax': 1887, 'Ymax': 2257}, 19: {'Xmin': 958, 'Ymin': 1445, 'Xmax': 1137, 'Ymax': 1601}, 20: {'Xmin': 979, 'Ymin': 1641, 'Xmax': 1192, 'Ymax': 1853}, 21: {'Xmin': 993, 'Ymin': 1901, 'Xmax': 1207, 'Ymax': 2057}, 22: {'Xmin': 1004, 'Ymin': 2110, 'Xmax': 1212, 'Ymax': 2276}, 23: {'Xmin': 634, 'Ymin': 2062, 'Xmax': 724, 'Ymax': 2137}, 24: {'Xmin': 597, 'Ymin': 1701, 'Xmax': 715, 'Ymax': 1794}, 25: {'Xmin': 231, 'Ymin': 2086, 'Xmax': 344, 'Ymax': 2210}, 26: {'Xmin': 48, 'Ymin': 2072, 'Xmax': 197, 'Ymax': 2226}, 27: {'Xmin': 36, 'Ymin': 1730, 'Xmax': 122, 'Ymax': 1836}, 28: {'Xmin': 272, 'Ymin': 1590, 'Xmax': 377, 'Ymax': 1676}, 29: {'Xmin': 164, 'Ymin': 1718, 'Xmax': 317, 'Ymax': 1866}}}

    invalid_id = get_coordinates(123)
    assert invalid_id == "No image found related to the image_id. Try effective image_id"


# if __name__=='main':
    