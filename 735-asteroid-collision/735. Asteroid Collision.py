class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for astr in asteroids:
            # we found a collision
            while stack and astr < 0 and stack[-1] > 0:
                if -astr == stack[-1]:
                    stack.pop()
                    break
                elif -astr > stack[-1]:
                    stack.pop()
                    continue
                elif -astr < stack[-1]:
                    break
            else:
                stack.append(astr)
        return stack           



