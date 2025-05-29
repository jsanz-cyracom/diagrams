# Guidelines for AI Contributors

This repository hosts Python utilities that produce architecture diagrams. Two main diagram types are created:

* **Component diagrams** generated with the [diagrams](https://diagrams.mingrammer.com/) package. See `src/generate_calls_service_component.py` for an example.
* **Sequence diagrams** produced via Mermaid CLI as in `src/generate_svc_ccs_agents_provisioning_sequence_diagram.py`.

Generated images are stored in the `diagrams/` directory which is listed in `.gitignore`. The script `src/generate_directory_structure.py` writes `diagrams/directory_structure.txt` to illustrate the repo layout.

## Development workflow
1. Run the **Prepare** task from `.vscode/tasks.json` to install dependencies and set up the `venv` environment.
2. Run **Generate** to execute every script in `src/` and produce PNG and SVG outputs.

## Icons
Custom icons reside in `assets/icons/`. Use these paths when creating nodes in component diagrams. If no appropriate graphic exists, reference `assets/icons/placeholder.png` and mention that a real icon should be supplied later.

## Coding style
* Python files use four-space indentation and a maximum line length of 250 characters (see `.pylintrc`).
* Replace any comment beginning with `AII:` once its instruction is completed.