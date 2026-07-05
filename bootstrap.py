from boe.core.doctor import run_doctor
from boe.core.tool_manager import setup_tools
from boe.runtime.workspace import Workspace


def main():
    print("\n[BOE] Bootstrap starting...\n")

    Workspace().create()

    setup_tools()

    run_doctor()

    print("\n[BOE] Ready for firmware processing.\n")


if __name__ == "__main__":
    main()
