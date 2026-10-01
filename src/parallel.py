from concurrent.futures import ThreadPoolExecutor


def process_node(node):
    return f"Processed node: {node}"


def parallel_processing(nodes):

    with ThreadPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(process_node, nodes))

    return results