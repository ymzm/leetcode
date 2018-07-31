class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        time_list = []
        fleet_time = 0 
        fleet_cnt = 0
        dic = {}
        length = len(position)
        
        for i in range(length):
            dic[position[i]] = speed[i]
            
        position.sort();
        position = position[::-1]
        
        for i in range(length):
            time_list.append(float(target - position[i])/dic[position[i]])
            if time_list[i] > fleet_time:
                fleet_cnt += 1
                fleet_time = time_list[i]
                
        return fleet_cnt