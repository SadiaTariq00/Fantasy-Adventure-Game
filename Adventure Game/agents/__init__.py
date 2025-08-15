class Runner:
    def __init__(self, agents):
        self.agents = agents

    async def run(self, func, *args, **kwargs):
        result = func(*args, **kwargs)
        if hasattr(result, "__await__"):  
            return await result
        return result
