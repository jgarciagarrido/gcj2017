def arrive_horse(horse, goal_km):
    time_to_find = (goal_km-horse['km'])/float(horse['speed'])
    return time_to_find, goal_km, horse['speed']


def catch_horse(horse_back, horse_front, goal_km):
    if (horse_back['speed'] > horse_front['speed']):
        distance_between_horses = horse_front['km']-horse_back['km']
        time_to_find = distance_between_horses / float(horse_back['speed'] - horse_front['speed'])

        distance_find = time_to_find * horse_back['speed']
        km_find = horse_back['km'] + distance_find
        current_speed = horse_front['speed']
        if(km_find > goal_km):
            return arrive_horse(horse_back, goal_km)
        return time_to_find, km_find, current_speed
    else:
        return arrive_horse(horse_back, goal_km)


def arrive_annie(goal_km, n_horses, horses):
    if(n_horses == 1):
        time_elapsed, km_find, current_speed= arrive_horse(horses[0], goal_km)
        return goal_km/float(time_elapsed)
    horses = sorted(horses, key=lambda horse: horse['km'])
    time_elapsed = 0
    horse_front = horses.pop()
    km_find = horse_front['km']
    current_speed = horse_front['speed']
    while(len(horses)>0 and km_find < goal_km):
        horse_back = horses.pop()
        time_to_find, km_find, current_speed = catch_horse(horse_back, horse_front, goal_km)
        time_elapsed += time_to_find
        horse_front = {"km": km_find, "speed": current_speed}
    if(km_find < goal_km):
        time_to_find, km_find, current_speed= arrive_horse(horse_front, goal_km)
        time_elapsed += time_to_find
    return goal_km/float(time_elapsed)


if __name__ == "__main__":
    t = int(raw_input())
    for i in xrange(1, t + 1):
        kilometers, number_of_horses = [int(s) for s in raw_input().split(" ")]
        horses = []
        for horse in xrange(1, number_of_horses+1):
            kilometer, speed = [int(s) for s in raw_input().split(" ")]
            horses.append({"km": kilometer, "speed": speed})
        print "Case #{}: {:0.6f}".format(i, arrive_annie(kilometers, number_of_horses, horses))
