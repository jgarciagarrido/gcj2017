import math


def max_surface_exposed(k, pancakes):
    pancakes_by_radius = sorted(pancakes, key= lambda pancake: pancake['radius'])
    radius_min = pancakes_by_radius[k-1]['radius']
    pancakes_for_base = [pancake for pancake in pancakes_by_radius if pancake['radius'] >= radius_min]
    base_pancake = max(pancakes_for_base, key= lambda pancake: pancake['area_total'])
    next_pancakes = [pancake for pancake in pancakes_by_radius if pancake['radius']<=base_pancake['radius']]
    next_pancakes = sorted(next_pancakes , key= lambda pancake: pancake['height'], reverse=True)
    selected_pancakes = next_pancakes[0:k-1]
    area_sides = reduce(lambda area, pancake: area + pancake['area_side'], selected_pancakes, 0)
    return (base_pancake['area_total'] + area_sides) * math.pi


if __name__ == '__main__':
    t = int(raw_input())
    for i in xrange(1, t + 1):
        n, k = [int(s) for s in raw_input().split(" ")]
        pancakes = []
        for j in xrange(0, n):
            r, h = [int(s) for s in raw_input().split(" ")]
            area_top = r * r
            area_side = 2*r*h
            pancake = {
                'radius': r,
                'height': h,
                'area_top': area_top,
                'area_side': area_side,
                'area_total': area_top + area_side}
            pancakes.append(pancake)
        print "Case #{}: {:0.9f}".format(i, max_surface_exposed(k, pancakes))
