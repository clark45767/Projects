# Python Recursion Q&A Program

questions = {
    "What is recursion?":
        "Recursion is when a function calls itself to solve a smaller version of a problem.",

    "What is a base case?":
        "A base case is the stopping condition that prevents infinite recursion.",

    "What does countdown() do?":
        "countdown() repeatedly decreases a number until it reaches 0.",

    "What does count_up() do?":
        "count_up() recursively counts from 1 to 10.",

    "What does build_and_unwind() demonstrate?":
        "It shows what happens before and after a recursive call.",

    "What is factorial?":
        "Factorial is the product of a number and all positive integers below it.",

    "What is stack overflow?":
        "Stack overflow happens when recursion has no base case and never stops."
}

print("=== Python Recursion Q&A ===")

for question, answer in questions.items():
    print("\nQ:", question)
    input("Press Enter to see the answer...")
    print("A:", answer)

print("\nEnd of Q&A.")