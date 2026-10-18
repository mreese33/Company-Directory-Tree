class EmployeeNode:
    '''
    A class to represent a node in the binary tree.
    Attributes:
        name (str): The name of the employee.
        left (EmployeeNode): The left child node, representing the left subordinate.
        right (EmployeeNode): The right child node, representing the right subordinate.
    '''

    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class TeamTree:
    '''
    A class to represent a binary tree for managing a team structure.
    Attributes:
        root (EmployeeNode): The root node of the tree, representing the team lead.
    Methods:
        insert(manager_name, employee_name, side, current_node=None): Inserts a new employee under the specified manager.
        print_tree(node=None, level=0): Prints the tree structure starting from the given node.
    '''

    def __init__(self):
        self.root = None

    def insert(self, manager_name, employee_name, side, current_node=None):
        if self.root is None:
            print("Please add a team lead first.")
            return False

        if side not in ("left", "right"):
            print("Invalid side. Choose left or right.")
            return False

        if current_node is None:
            current_node = self.root

        if current_node.name == manager_name:
            if getattr(current_node, side) is None:
                new_employee = EmployeeNode(employee_name)
                setattr(current_node, side, new_employee)
                print(f"{employee_name} added to the {side.upper()} of {manager_name}")
                return True
            else:
                print(f"The {side} side of {manager_name} is already taken.")
                return False

        if current_node.left is not None:
            if self.insert(manager_name, employee_name, side, current_node.left):
                return True

        if current_node.right is not None:
            if self.insert(manager_name, employee_name, side, current_node.right):
                return True
 
        if current_node == self.root:
            print(f"Manager {manager_name} was not found.")
            
        return False

    def print_tree(self, node=None, level=0):
        if node is None:
            if level == 0:
                node = self.root
            else:
                return

        if node is None:
            print("No employees in the directory.")
            return

        print("  " * level + "- " + node.name)

        self.print_tree(node.left, level + 1)
        self.print_tree(node.right, level + 1)


# Test your code here









# CLI functionality
def company_directory():
    tree = TeamTree()

    while True:
        print("\n📋 Team Management Menu")
        print("1. Add Team Lead (root)")
        print("2. Add Employee")
        print("3. Print Team Structure")
        print("4. Exit")
        choice = input("Choose an option (1–4): ")

        if choice == "1":
            if tree.root:
                print("⚠️ Team lead already exists.")
            else:
                name = input("Enter team lead's name: ")
                tree.root = EmployeeNode(name)
                print(f"✅ {name} added as the team lead.")

        elif choice == "2":
            manager = input("Enter the manager's name: ")
            employee = input("Enter the new employee's name: ")
            side = input("Should this employee be on the LEFT or RIGHT of the manager? ")
            side = side.lower()
            tree.insert(manager, employee, side)

        elif choice == "3":
            print("\n🌳  Current Team Structure:")
            tree.print_tree()

        elif choice == "4":
            print("Good Bye!")
            break
        else:
            print("❌ Invalid option. Try again.")

if __name__ == "__main__":
    company_directory()