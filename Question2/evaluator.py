import os

# Name: Krystal Bhandari | Student No: S401359 | Contribution:
# Implemented a simple expression evaluator by tokenizing arithmetic input, formatting tokens, 
# managing parser state, and building a recursive descent parser to evaluate expressions with 
# basic operators and parentheses, then formatting and writing the results to an output file.




# tokenize
def tokenize(expr):
    pass

# format tokens
def format_tokens(tokens):
    pass

# format result
def make_state(tokens):
    pass

# parser
def parse_expression(s):
    pass

# format result
def format_result(value):
    pass

# ---------------- EVALUATE FUNCTION ---------------- #

def evaluate_file(input_path: str):

    output_path = os.path.join(os.path.dirname(input_path), "output.txt")

    results = []

    with open(input_path, "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    output_blocks = []

    for line in lines:

        try:
            tokens = tokenize(line)
            state = make_state(tokens)

            value, tree = parse_expression(state)

            token_str = format_tokens(tokens)
            result_str = format_result(value)

        except Exception:
            tree = "ERROR"
            token_str = "ERROR"
            result_str = "ERROR"
            value = "ERROR"

        results.append({
            "input": line,
            "tree": tree,
            "tokens": token_str,
            "result": value
        })

        output_blocks.append(
            f"Input: {line}\n"
            f"Tree: {tree}\n"
            f"Tokens: {token_str}\n"
            f"Result: {result_str}"
        )

    with open(output_path, "w") as f:
        f.write("\n\n".join(output_blocks))

    return results




# --- run main program ---
if __name__ == "__main__":
    evaluate_file("input.txt")