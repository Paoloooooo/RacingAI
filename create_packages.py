import os

"""
This code is used to create __init__.py files in all subdirectories of a given directory, 
making everything in that directory a package.
"""


def create_init_files(start_dir):
    for root, dirs, files in os.walk(start_dir):
        init_file = os.path.join(root, "__init__.py")
        if "__init__.py" not in files:
            with open(init_file, "w") as f:
                # Write the __all__ statement
                py_files = [
                    os.path.splitext(f)[0]
                    for f in files
                    if f.endswith(".py") and f != "__init__.py"
                ]
                all_statement = "__all__ = " + str(py_files) + "\n"
                f.write("# This file makes this directory a package\n")
                f.write(all_statement)
            print(f"Created: {init_file}")
        else:
            with open(init_file, "r") as f:
                content = f.read()
            py_files = [
                os.path.splitext(f)[0]
                for f in files
                if f.endswith(".py") and f != "__init__.py"
            ]
            all_statement = "__all__ = " + str(py_files) + "\n"
            if all_statement not in content:
                with open(init_file, "a") as f:
                    f.write(all_statement)
                print(f"Updated: {init_file}")


# Replace 'your_project_directory' with the root directory of your project
create_init_files(".")
