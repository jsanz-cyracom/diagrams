# Diagrams
Generate diagrams using Python. Helps with diagrams automation using AI. Supports SVGs which can be used in Lucid Charts

## Generate
1. Open in Devcontainer or Codespace using VSCode.
2. Access and run tasks configured in .vscode/tasks.json from the VSCode Command Palette.
3. Run the `Generate` task.

The output directory is called `diagrams`. This directory is included in .gitignore as to not publish the files to the repository.

## Creating Diagrams
The Python scripts to generate the diagrams are under the `src` directory. To create a new diagram add the script in this directory and make sure you have the correct interpreter selected in VSCode by selecting `Python: Select Interpreter` from the Command Palette and selecting the interpreter `('venv':venv)`. Now you are ready to write your Python script to generate a diagram, simply run the `Generate` task.