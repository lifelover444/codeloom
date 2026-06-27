import subprocess
import sys
from pathlib import Path


def test_acceptance_script_has_help():
    script = Path("scripts/check_codeloom_acceptance.py")

    assert script.exists()

    result = subprocess.run(
        [sys.executable, str(script), "--help"],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )

    assert result.returncode == 0
    assert "Validate the Codeloom wrapper experience" in result.stdout
