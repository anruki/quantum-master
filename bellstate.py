from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.visualization import circuit_drawer

# Create a quantum register with 2 qubits
q = QuantumRegister(2)
# Create a classical register with 2 bits
c = ClassicalRegister(2)
# Create a quantum circuit
bell_circuit = QuantumCircuit(q, c)
# Create a Bell state
bell_circuit.h(q[0])
bell_circuit.cx(q[0], q[1])
# Measure the qubits
bell_circuit.measure(q, c)
# Draw the circuit
print(circuit_drawer(bell_circuit, output='text'))