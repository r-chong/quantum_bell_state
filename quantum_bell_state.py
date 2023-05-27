from qiskit import QuantumCircuit, transpile
from qiskit.providers.aer import AerSimulator
from qiskit.visualization import plot_state_city

# create a quantum circuit with 2 qubits, classical bits
qc = QuantumCircuit(2, 2)

# hadamard gate @index 0 aka superposition
qc.h(0)

# CNOT logic gate aka entanglement
qc.cx(0, 1)

# store into classical bits
qc.measure([0,1], [0,1])

# start transpile!
backend_sim = AerSimulator(method='statevector')
transpiled_qc = transpile(qc, backend_sim)

result = backend_sim.run(transpiled_qc).result()
print(result.get_counts(qc))

plot_state_city(result.get_statevector(qc))
