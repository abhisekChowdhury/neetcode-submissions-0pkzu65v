class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []

        for asteroid in asteroids:
            alive = True
            while res and alive and asteroid < 0 and res[-1] > 0:
                if res[-1] < abs(asteroid):
                    res.pop()
                elif res[-1] == abs(asteroid):
                    res.pop()
                    alive = False
                else:
                    alive = False
            
            if alive:
                res.append(asteroid)
        return res