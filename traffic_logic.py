def calculate_duration(cars, bigs):
    base_time = 10
    car_weight = 2
    big_weight = 4

    duration = base_time + (cars * car_weight) + (bigs * big_weight)

    return min(duration, 80)
