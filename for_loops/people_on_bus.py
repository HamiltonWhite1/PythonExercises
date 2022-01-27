bus_list = [[5,0], [3,8], [6,8]]
def num_bus(bus_stops):
    on_bus = 0
    remainder = 0
    for stops in bus_stops[0:-1]:
        for i in stops:
            on_bus += i
    for remaining in bus_stops[-1]:
        remainder += remaining
    return on_bus - remainder

num_bus(bus_list)