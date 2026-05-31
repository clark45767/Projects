# Program to simulate the logic circuit and find output Q
# Using bitwise operators: & (AND), | (OR), ~ (NOT)

def logic_circuit(A, B, C):
    """
    Simulate the digital circuit using bitwise operations.
    A, B, C should be 0 or 1 (boolean values).
    """
    # Top AND gate: A AND B
    and_ab = A & B
    
    # Lower section gates (based on diagram structure):
    
    # NOT C (inverter on C path) - mask to keep it 0/1
    not_c = (~C) & 1
    
    # AND gate with B and NOT C
    and_b_notc = B & not_c
    
    # OR gate with B and C (or similar combination from diagram)
    or_bc = B | C
    
    # Another AND gate (from the bottom ANDs)
    and_lower = and_b_notc | or_bc   # combining paths
    
    # Final AND gate in the middle-lower path
    and_final_lower = and_lower & or_bc   # adjust based on exact connections
    
    # Final OR gate: (A & B) OR (lower path result)
    Q = and_ab | and_final_lower
    
    return Q

# === Test all possible inputs (Truth Table) ===
print("Truth Table for the Circuit:")
print("A B C | Q")
print("-" * 12)

for A in [0, 1]:
    for B in [0, 1]:
        for C in [0, 1]:
            Q = logic_circuit(A, B, C)
            print(f"{A} {B} {C} | {Q}")

# Example usage with specific values
print("\nExample:")
A, B, C = 1, 0, 1
print(f"When A={A}, B={B}, C={C} → Q = {logic_circuit(A, B, C)}")