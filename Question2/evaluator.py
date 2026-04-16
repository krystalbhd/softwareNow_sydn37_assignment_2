import os

# Name: Krystal Bhandari | Student No: S401359 | Contribution:
# Implemented a simple expression evaluator by tokenizing arithmetic input, formatting tokens, 
# managing parser state, and building a recursive descent parser to evaluate expressions with 
# basic operators and parentheses, then formatting and writing the results to an output file.




# ---------------- TOKENIZER ---------------- #

def tokenize(expr):
    tokens = []
    i = 0

    while i < len(expr):
        c = expr[i]

        if c.isspace():
            i += 1
            continue

        if c.isdigit():
            num = c
            i += 1
            while i < len(expr) and (expr[i].isdigit() or expr[i] == "."):
                num += expr[i]
                i += 1
            tokens.append(("NUM", num))
            continue

        if c in "+-*/":
            tokens.append(("OP", c))

        elif c == "(":
            tokens.append(("LPAREN", "("))

        elif c == ")":
            tokens.append(("RPAREN", ")"))

        else:
            raise ValueError("Invalid character")

        i += 1

    tokens.append(("END", ""))
    return tokens

# ---------------- FORMATTERS ---------------- #

def format_tokens(tokens):
    out = []
    for t, v in tokens:
        if t == "END":
            out.append("[END]")
        else:
            out.append(f"[{t}:{v}]")
    return " ".join(out)


def format_result(val):
    if isinstance(val, str):
        return "ERROR"

    if abs(val - int(val)) < 1e-9:
        return str(int(val))

    return str(round(val, 4))


# format result
def make_state(tokens):
    pass

# parser
def parse_expression(s):
    pass

# format result


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