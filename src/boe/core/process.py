from subprocess import run, PIPE
import os


class ProcessError(Exception):
    pass


class Process:

    @staticmethod
    def run(cmd):

        env = os.environ.copy()

        tool_dir = os.path.dirname(str(cmd[0]))

        if tool_dir:
            env["PATH"] = (
                tool_dir
                + os.pathsep
                + env.get("PATH", "")
            )

        result = run(
            [str(x) for x in cmd],
            stdout=PIPE,
            stderr=PIPE,
            text=True,
            env=env
        )

        if result.returncode != 0:
            print("\n========== PROCESS ERROR ==========")
            print("CMD:")
            print(" ".join(str(x) for x in cmd))
            print()
            print("RETURN CODE:")
            print(result.returncode)
            print()
            print("STDOUT:")
            print(result.stdout)
            print()
            print("STDERR:")
            print(result.stderr)
            print("==================================")

            raise ProcessError(
                result.stderr.strip()
                or "Process failed"
            )

        return result
