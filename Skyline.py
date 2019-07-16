import heapq
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        
        height = {}
        elevation = []
        skyline = []
        points = []
        for bno,item in enumerate(buildings):
            l,r,h = item
            points.append((l,'l', bno))
            points.append((r,'r', bno))
            height[bno] = h
        
        points.sort()
        
        for p in points:
            x, side, bno = p
            
            if not elevation:
                b_ht = height[bno]
                heapq.heappush(elevation, (-b_ht, bno))
                skyline.append([x, b_ht])
                continue
            
            if side == 'l':
                b_ht = height[bno]
                curr_elevation = -elevation[0][0]
                if b_ht > curr_elevation:
                    if skyline[-1][0] == x:
                        skyline.pop()
                    skyline.append([x, b_ht])
                heapq.heappush(elevation, (-b_ht, bno))
                continue
            
            if side == 'r':
                if bno == elevation[0][1]:
                    _top = heapq.heappop(elevation)
                    b_ht = -_top[0]
                    curr_elevation = 0
                    if elevation:
                        curr_elevation = -elevation[0][0]
                    if b_ht > curr_elevation:
                        if skyline[-1][0] == x:
                            curr_elevation = min(curr_elevation, skyline[-1][1])
                            skyline.pop()
                        skyline.append([x, curr_elevation])
                else:
                    _tmp = []
                    while elevation:
                        _top = heapq.heappop(elevation)
                        if _top[1] == bno:
                            break
                        _tmp.append(_top)
                    
                    for t in _tmp:
                        heapq.heappush(elevation, t)
            
        
        return skyline