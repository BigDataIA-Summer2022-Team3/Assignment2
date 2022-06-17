import count_airplanes_in_given_image as counter

def test_count_airplane():
    res = counter("1e7e0450-6eb3-479e-88c2-990abc8207fa.jpg") 
    assert res == 52;