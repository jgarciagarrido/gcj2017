def empty_stalls_for_one(stalls):
    min_stalls = (stalls-1) / 2
    max_stalls = (stalls-1) - min_stalls
    return max_stalls, min_stalls


def all_stalls_full():
    return 0, 0


def empty_stalls(stalls, people):
    while(stalls != people and people != 1):
        stalls = (stalls-(people%2)) / 2
        people = people / 2
        #print "S({},{})".format(stalls, people)
    if stalls == people:
        return all_stalls_full()
    if people == 1:
        return empty_stalls_for_one(stalls)


if __name__ == "__main__":
    t = int(raw_input())
    for i in xrange(1, t + 1):
        n, k = [int(s) for s in raw_input().split(" ")]
        max_stalls, min_stalls = empty_stalls(n, k)
        print "Case #{}: {} {}".format(i, max_stalls, min_stalls)
