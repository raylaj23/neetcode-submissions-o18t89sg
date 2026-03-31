class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i], i) for i in range(len(position))]
        cars.sort(reverse = True)
        stack = []
        for pos, idx in cars:
            time = (target - pos) / speed[idx]
            if len(stack) > 0:
                last = stack.pop()
                stack.append(last)
                if last < time:
                    stack.append(time)
            else:
                stack.append(time)
        
        return len(stack)