class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        speed_hmap = {}
        time_hmap = {}
        for i in range(0, len(position)):
            speed_hmap[position[i]] = speed[i]        
        speed_hmap = dict(sorted(speed_hmap.items(), reverse=True))
        print(speed_hmap)        
        for i in speed_hmap:
            time_hmap[i] = (target - i )/ speed_hmap[i]        
        time_taken = list(time_hmap.values())
        print(time_hmap)
        fleet = len(time_taken)
        r = 1

        position.sort(reverse=True)

        while r < len(position):

            if time_hmap[position[r]] <= time_hmap[position[r-1]]:
                fleet = fleet - 1
                time_hmap[position[r]] = time_hmap[position[r-1]]
            r = r + 1


        

        return fleet
        

        