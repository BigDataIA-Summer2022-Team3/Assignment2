from count_airplanes_in_given_image import count_airplanes_in_given_image as counter

def test_count_airplane():
    res = counter("1e7e0450-6eb3-479e-88c2-990abc8207fa.jpg") 
    assert res == 52;

def test_count_airplane_not_found_data():
    res = counter("wrong_info")
    assert res == "Sorry, we don't find the picture. Please check you enter info."

    res1 = counter("错误信息")
    assert res1 == "Sorry, we don't find the picture. Please check you enter info."

    res2 = counter("")
    assert res2 == "Sorry, we don't find the picture. Please check you enter info."


from return_images_with_given_number_of_aircraft import return_images_with_given_number_of_aircraft as numOfAircraft

def test_return_images_with_given_number_of_aircraft():
    res = numOfAircraft(30, 3)
    assert res == "Finish";

def test_return_images_with_given_number_of_aircraft_wrong_numbers():
    res = numOfAircraft(-2,1000000)
    assert res == "The number should be positive"

    res1 = numOfAircraft(2,1000000)
    assert res1 == "limit_of_image should between [1,10]"

    res3 = numOfAircraft(3)
    assert res3 == "Sorry, we don't find your needed"

    res4 = numOfAircraft("wrong_info")
    assert res4 == "Please enter two integer number."

    res5 = numOfAircraft("")
    assert res5 == "Please enter two integer number."


from return_images_with_maximum_airplanes import return_images_with_maximum_airplanes as maxNumAirplanes

def test_return_images_with_maximum_airplanes():
    res = maxNumAirplanes(6)
    assert res == "Finish";

def test_return_images_with_maximum_airplanes_wrong_numbers():
    res = maxNumAirplanes(-2)
    assert res == "limit_of_image should between [1,10]"

    res1 = maxNumAirplanes("wrong_info")
    assert res1 == "Please enter integer number."

    res2 = maxNumAirplanes("")
    assert res2 == "Please enter integer number."


from return_images_with_truncated_aircraft import return_all_images_with_truncated_aircraft as numTruncatedAircraft

def test_return_images_with_truncated_aircraft():
    res = numTruncatedAircraft(-2)
    assert res == "limit_of_image should between [1,10]"

    res1 = numTruncatedAircraft("wrong_info")
    assert res1 == "Please enter integer number."

    res2 = numTruncatedAircraft("")
    assert res2 == "Please enter integer number."

    res3 = numTruncatedAircraft(2)
    assert res3 == "Finish"


from display_top_aircraft import display_biggest_aircraft as display_big

def test_display_big():
    big = display_big("5c9e817a-dc4b-42ab-952c-3128e2de12e8.jpg",5)
    assert big == [(2067, 1344, 2269, 1568), (979, 1641, 1192, 1853), (2079, 1574, 2287, 1789), (1990, 472, 2182, 685), (1555, 479, 1758, 651)]
    
    wro = display_big("123",5)
    assert wro == "No image found related to the image_id. Try effective image_id"

from display_smallest_aircraft import display_smallest_aircraft as display_small

def test_display_small():
    sma = display_small("5c9e817a-dc4b-42ab-952c-3128e2de12e8.jpg", 5)
    assert sma == [(634, 2062, 724, 2137), (272, 1590, 377, 1676), (36, 1730, 122, 1836), (597, 1701, 715, 1794), (231, 2086, 344, 2210)]

    wro = display_small("123",5)
    assert wro == "No image found related to the image_id. Try effective image_id"

from has_aircraft_in_given_x_y_coordinate import has_aircraft_in_given_x_y_coordinate as has_aircraft

def test_has_aircraft_in_given_coor():
    wrong_image = has_aircraft("123",1600, 500)
    assert wrong_image == "No image found related to the image_id. Try effective image_id"
    
    overbound = has_aircraft("123", 10, 3000)
    assert overbound == "Input X and Y should within (0,2560)"
    
    found = has_aircraft("5c9e817a-dc4b-42ab-952c-3128e2de12e8.jpg",1600,500)
    assert found == "Found"
    not_found = has_aircraft("5c9e817a-dc4b-42ab-952c-3128e2de12e8.jpg", 2000, 1600)
    assert not_found ==   [(1950, 280, 2139, 436),
                            (1990, 472, 2182, 685),
                            (1989, 722, 2187, 894),
                            (1539, 304, 1729, 453),
                            (1555, 479, 1758, 651),
                            (1572, 671, 1768, 840),
                            (1604, 868, 1789, 1018),
                            (876, 350, 1048, 482),
                            (898, 529, 1061, 668),
                            (467, 590, 643, 743),
                            (2067, 1344, 2269, 1568),
                            (2079, 1574, 2287, 1789),
                            (2090, 1806, 2293, 1978),
                            (2108, 2042, 2288, 2212),
                            (1632, 1370, 1820, 1531),
                            (1643, 1568, 1841, 1718),
                            (1664, 1739, 1841, 1889),
                            (1686, 1926, 1860, 2081),
                            (1701, 2112, 1887, 2257),
                            (958, 1445, 1137, 1601),
                            (979, 1641, 1192, 1853),
                            (993, 1901, 1207, 2057),
                            (1004, 2110, 1212, 2276),
                            (634, 2062, 724, 2137),
                            (597, 1701, 715, 1794),
                            (231, 2086, 344, 2210),
                            (48, 2072, 197, 2226),
                            (36, 1730, 122, 1836),
                            (272, 1590, 377, 1676),
                            (164, 1718, 317, 1866)]
    found_2 = has_aircraft("5c9e817a-dc4b-42ab-952c-3128e2de12e8.jpg",1950,280)
    assert found_2 == "Found"

# if __name__=='main':
    