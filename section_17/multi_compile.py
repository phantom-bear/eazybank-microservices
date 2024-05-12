import os
import sys

def build_images(parent_directory, excluded_subdirectories):
    # Iterate over the directories within the parent directory
    for dirpath, dirnames, filenames in os.walk(parent_directory):
        # Check if the directory should be excluded
        if any(excluded_subdir in dirpath for excluded_subdir in excluded_subdirectories):
            print(f"Excluding directory: {dirpath}")
            continue

        # Check if the directory contains a Spring Boot application
        if "pom.xml" in filenames:
            print(f"Building Docker image for Spring Boot application in directory: {dirpath}")
            os.chdir(dirpath)
            os.system("mvn compile jib:dockerBuild")
        else:
            print(f"Skipping directory {dirpath} as it does not contain a Spring Boot application.")

if __name__ == "__main__":
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python script.py <parent_directory> <excluded_subdirectories>")
        sys.exit(1)

    parent_directory = sys.argv[1]
    excluded_subdirectories = sys.argv[2].split(',')

    # Check if parent directory exists
    if not os.path.isdir(parent_directory):
        print(f"Parent directory '{parent_directory}' does not exist.")
        sys.exit(1)

    build_images(parent_directory, excluded_subdirectories)
