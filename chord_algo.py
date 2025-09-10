class Node:
    def __init__(self, node_id, M):
        self.id = node_id
        self.M = M
        self.finger = [None] * M
        self.successor = None

def find_successor(key, nodes, RING_SIZE):
    ids = sorted(n.id for n in nodes)
    for nid in ids:
        if nid >= key:
            return next(n for n in nodes if n.id == nid)
    return next(n for n in nodes if n.id == ids[0])

def build_finger_tables(nodes, M, RING_SIZE):
    for n in nodes:
        for i in range(M):
            start = (n.id + (1 << i)) % RING_SIZE
            n.finger[i] = find_successor(start, nodes, RING_SIZE)
        n.successor = n.finger[0]

def print_fingers(nodes, M, RING_SIZE, title):
    print(title)
    for n in sorted(nodes, key=lambda x: x.id):
        print(f"Node {n.id} finger table:")
        print(" Index | Successor")
        print("-------+----------")
        for i in range(M):
            print(f"   {i+1:<3} | {n.finger[i].id}")
        print("Successor:", n.successor.id)
        print("-" * 30)


def lookup(key, start_node, nodes, M, RING_SIZE):
    current = start_node
    while not (current.id < key <= current.successor.id or
               (current.id > current.successor.id and (key > current.id or key <= current.successor.id))):
        for i in reversed(range(M)):
            if current.finger[i].id != current.id and (
                (current.id < key and current.finger[i].id < key and current.finger[i].id > current.id) or
                (current.id > key and (current.finger[i].id > current.id or current.finger[i].id < key))
            ):
                current = current.finger[i]
                break
        else:
            current = current.successor
    return current.successor

def run_test_case(M, node_ids, test_keys):
    RING_SIZE = 2 ** M
    nodes = [Node(i, M) for i in node_ids]

    build_finger_tables(nodes, M, RING_SIZE)
    print_fingers(nodes, M, RING_SIZE,
                  f"=== Finger table (m={M}; nodes: {', '.join(str(n.id) for n in nodes)}) ===")

    print("=== Result Test Cases ===")
    start_node = nodes[0]
    for key in test_keys:
        responsible = lookup(key, start_node, nodes, M, RING_SIZE)
        print(f"Key {key:2} → Node {responsible.id}")
    print("\n")

if __name__ == "__main__":
    # Test case 1
    run_test_case(
        M=4,
        node_ids=[1, 5, 7, 9, 12],
        test_keys=[0,3,5,8,10,11]
    )
    # Test case 2
    run_test_case(
        M=3,
        node_ids=[0, 3, 6],
        test_keys=list(range(0, 8))
    )
    # Test case 3
    run_test_case(
        M=5,
        node_ids=[2, 8, 15, 20, 25],
        test_keys=[0, 5, 10, 18, 24, 31]
    )
