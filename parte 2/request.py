class Request:
    def __init__(self, id, cpu_req, mem_req, priority):
        self.id = id
        self.cpu_req = cpu_req
        self.mem_req = mem_req
        self.priority = priority