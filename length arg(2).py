def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")
display_info(name="Nikki",age=23,city="Rajkot")