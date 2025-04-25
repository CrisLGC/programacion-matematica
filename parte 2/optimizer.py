import pulp

class AssignmentOptimizer:
    def __init__(self, servers, requests, cost_matrix):
        self.servers = servers
        self.requests = requests
        self.cost_matrix = cost_matrix
        self.model = pulp.LpProblem("AsignacionSolicitudes", pulp.LpMinimize)
        self.x = None

    def definir_variables(self):
        S = len(self.servers)
        R = len(self.requests)
        self.x = pulp.LpVariable.dicts("x", ((i, j) for i in range(S) for j in range(R)), cat='Binary')

    def funcion_objetivo(self):
        self.model += pulp.lpSum(
            self.cost_matrix[i][j] * (1 / self.requests[j].priority) * self.x[(i, j)]
            for i in range(len(self.servers))
            for j in range(len(self.requests))
        )

    def restricciones(self):
        S = len(self.servers)
        R = len(self.requests)

        for j in range(R):
            self.model += pulp.lpSum(self.x[(i, j)] for i in range(S)) == 1

        for i in range(S):
            self.model += pulp.lpSum(
                self.requests[j].cpu_req * self.x[(i, j)] for j in range(R)
            ) <= self.servers[i].cpu_capacity

            self.model += pulp.lpSum(
                self.requests[j].mem_req * self.x[(i, j)] for j in range(R)
            ) <= self.servers[i].mem_capacity

    def construir_modelo(self):
        self.definir_variables()
        self.funcion_objetivo()
        self.restricciones()

    def resolver(self):
        self.model.solve()
        resultado = []
        for (i, j), var in self.x.items():
            if var.varValue == 1:
                resultado.append((self.servers[i].id, self.requests[j].id))
        return resultado

    def obtener_costo_total(self):
        return pulp.value(self.model.objective)