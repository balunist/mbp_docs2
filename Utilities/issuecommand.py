import shlex
import subprocess


def issue_command(
    cmd: str,
    *,
    verbose=False,
    ignore=False,
) -> tuple[int, list[str]]:
    try:
        proc = subprocess.Popen(  # noqa: S603
            shlex.split(cmd),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        (output_str, stderr_str) = proc.communicate()
        return_code = proc.wait()
        success = output_str != b"Failed\n" and return_code == 0

        # if not success:
        #     output_str = stderr_str

        lines = output_str.decode().splitlines() if output_str is not None else []
        if len(lines) > 1 and "Your branch is up to date" in lines[1]:
            return 0, []
        if verbose or (not success and not ignore):
            for line in lines:
                print(line)

    except (OSError, subprocess.SubprocessError) as err:
        print(err)
        return 99, []
    else:
        return return_code, lines
