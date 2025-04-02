import subprocess
import os

from app.config import config
from app.tool import BaseTool

# TODO add description
_MANIM_TOOL_DESCRIPTION = "A tool that executes manim animation code and returns the generated video"

TEMP_DIRS = {}
# Get Manim executable path from environment variables or assume it's in the system PATH
MANIM_EXECUTABLE = os.getenv("MANIM_EXECUTABLE", "manim")   #MANIM_PATH "/Users/[Your_username]/anaconda3/envs/manim2/Scripts/manim.exe"
BASE_DIR = os.path.join(config.workspace_root, "media")

class ManimTool(BaseTool):
    """A tool that executes manim animation code and returns the generated video"""

    name: str = "manim"
    description: str = _MANIM_TOOL_DESCRIPTION
    parameters: dict = {
        "type": "object",
        "properties": {
            "code": {
                "type": "string",
                "description": "manim code"
            },
            "quality": {
                "type": "string",
                "description": "quality"
            }
        },
        "required": ["code"],
    }

    async def execute(self, code: str) -> str:
        return self.execute_manim_code(code)

    def execute_manim_code(self, manim_code: str) -> str:
        """Execute manim code"""
        tmpdir = os.path.join(BASE_DIR, "manim_tmp")
        os.makedirs(tmpdir, exist_ok=True)  # Ensure the temp folder exists
        script_path = os.path.join(tmpdir, "scene.py")

        try:
            # Write the Manim script to the temp directory
            with open(script_path, "w") as script_file:
                script_file.write(manim_code)

            # Execute Manim with the correct path
            result = subprocess.run(
                [config.manim, "-p", script_path],
                # MANIM_PATH "/Users/[Your_username]/anaconda3/envs/manim2/Scripts/manim.exe"
                capture_output=True,
                text=True,
                cwd=tmpdir
            )

            if result.returncode == 0:
                TEMP_DIRS[tmpdir] = True
                print(f"Check the generated video at: {tmpdir}")

                return "Execution successful. Video generated."
            else:
                return f"Execution failed: {result.stderr}"

        except Exception as e:
            return f"Error during execution: {str(e)}"
        return ""