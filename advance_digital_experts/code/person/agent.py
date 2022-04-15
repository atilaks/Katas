class Agent:

    def __init__(self):
        self._agent = {"name": "", "police_id": "", "department": ""}
        self._availability = True

    def set_agent(self, data):
        counter = 0
        for i in self._agent.keys():
            self._agent[i] = data[counter]
            counter += 1

    def get_agent(self):
        return self._agent
