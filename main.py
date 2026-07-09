# ==========================================================
# MATRIX OPERATIONS TOOL
# ==========================================================

# Import NumPy library for matrix operations
import numpy as np


# Function to accept matrix input from the user
def input_matrix(rows, cols):
    matrix = []

    # Read each row of the matrix
    print("Enter matrix elements:")
    for i in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)

    # Convert list into NumPy array
    return np.array(matrix)


# Run the program until the user chooses Exit
while True:

    # Display the menu
    print("\n==========================================")
    print("         MATRIX OPERATIONS TOOL")
    print("==========================================")
    print("1. Matrix Addition")
    print("2. Matrix Subtraction")
    print("3. Matrix Multiplication")
    print("4. Matrix Transpose")
    print("5. Matrix Determinant")
    print("6. Exit")
    print("==========================================")

    # Get user's choice
    choice = int(input("Enter your choice : "))

    # =====================================================
    # Matrix Addition
    # =====================================================
    if choice == 1:

        # Get matrix dimensions
        rows = int(input("Enter rows : "))
        cols = int(input("Enter columns : "))

        # Read Matrix A
        print("\nEnter Matrix A")
        A = input_matrix(rows, cols)

        # Read Matrix B
        print("\nEnter Matrix B")
        B = input_matrix(rows, cols)

        # Display addition result
        print("\nAddition Result")
        print(A + B)

    # =====================================================
    # Matrix Subtraction
    # =====================================================
    elif choice == 2:

        # Get matrix dimensions
        rows = int(input("Enter rows : "))
        cols = int(input("Enter columns : "))

        # Read Matrix A
        print("\nEnter Matrix A")
        A = input_matrix(rows, cols)

        # Read Matrix B
        print("\nEnter Matrix B")
        B = input_matrix(rows, cols)

        # Display subtraction result
        print("\nSubtraction Result")
        print(A - B)

    # =====================================================
    # Matrix Multiplication
    # =====================================================
    elif choice == 3:

        # Get dimensions of Matrix A
        r1 = int(input("Enter rows of Matrix A : "))
        c1 = int(input("Enter columns of Matrix A : "))

        # Read Matrix A
        print("\nEnter Matrix A")
        A = input_matrix(r1, c1)

        # Get dimensions of Matrix B
        r2 = int(input("Enter rows of Matrix B : "))
        c2 = int(input("Enter columns of Matrix B : "))

        # Check whether multiplication is possible
        if c1 != r2:
            print("\nMatrix multiplication is not possible.")

        else:

            # Read Matrix B
            print("\nEnter Matrix B")
            B = input_matrix(r2, c2)

            # Display multiplication result
            print("\nMultiplication Result")
            print(np.dot(A, B))

    # =====================================================
    # Matrix Transpose
    # =====================================================
    elif choice == 4:

        # Get matrix dimensions
        rows = int(input("Enter rows : "))
        cols = int(input("Enter columns : "))

        # Read Matrix
        print("\nEnter Matrix")
        A = input_matrix(rows, cols)

        # Display transpose
        print("\nTranspose of Matrix")
        print(np.transpose(A))

    # =====================================================
    # Matrix Determinant
    # =====================================================
    elif choice == 5:

        # Get order of square matrix
        n = int(input("Enter order of square matrix : "))

        # Read square matrix
        print("\nEnter Matrix")
        A = input_matrix(n, n)

        # Display determinant
        print("\nDeterminant")
        print(round(np.linalg.det(A), 2))

    # =====================================================
    # Exit Program
    # =====================================================
    elif choice == 6:

        # Exit the program
        print("\nThank You!")
        break

    # =====================================================
    # Invalid Choice
    # =====================================================
    else:

        # Handle invalid menu option
        print("\nInvalid Choice! Please try again.")