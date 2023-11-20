class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        single_travel =  sum(travel)
        total_travel = single_travel * 3
        total_collect = 0
        last_m = -1 # last position of m
        last_p = -1 # last position of p
        last_g = -1 # last position of g

        for i, house in enumerate(garbage):
            total_collect += len(house)
            # we keep updating the last position of p, m and g
            if "P" in house:
                last_p = i
            if "M" in house:
                last_m = i
            if "G" in house:
                last_g = i

        if last_m != -1:  # we subtract the rest of the traveling distance from the last house that has garbage M, as requested by the question
            total_travel -= sum(travel[last_m:])
        else:   # if there is no M in any house, we don't even need to send the truck, hence subtract the entire travel distance 
            total_travel -= single_travel 

        if last_p != -1:
            total_travel -= sum(travel[last_p:])
        else:   
            total_travel -= single_travel 

        if last_g != -1:
            total_travel -= sum(travel[last_g:])
        else:   
            total_travel -= single_travel   


        return total_travel + total_collect    