import asyncio

from app.agent.manus import Manus
from app.logger import logger

PROMPT_TEMPLATE = """
Given the mathematical topic: {topic}, organize the relevant conceptual knowledge, design a detailed animation storyboard and generate manim code based on the storyboard.

# Steps

1. **Understand the Topic**:
   - Identify the main mathematical or physical concepts involved in the topic.
   - List the key principles, equations, and any other relevant information.
   - 

2. **Design the Storyboard**:
   - Break down the topic into a sequence of scenes. For each scene, describe the visual elements, transitions, and any text or equations to be displayed.
   - Ensure the storyboard is coherent and follows a logical flow.

3. **Generate Manim Code**:
   - Translate the storyboard into manim code.
   - Include necessary imports, class definitions, and methods to create the animation.
   - Ensure the code is well-structured and follows best practices for manim.
   
# Output Format

- **Storyboard**: A JSON object with the following structure:
  ```json
  {
    "scenes": [
      {
        "scene_number": 1,
        "description": "Description of the scene",
        "visual_elements": ["List of visual elements"],
        "transitions": ["List of transitions"],
        "text_and_equations": ["List of text and equations"]
      },
      // Additional scenes
    ]
  }
  ```

# Notes

- Ensure the storyboard and manim code are aligned and consistent.
- Use clear and concise language in the conceptual knowledge section.
- The manim code should be well-structured and follow best practices for readability and maintainability.

""".strip()

async def main():
    agent = Manus()
    try:
        prompt = PROMPT_TEMPLATE.format(topic="二次函数")
        await agent.run(prompt)
        logger.info("Request processing completed.")
    except KeyboardInterrupt:
        logger.warning("Operation interrupted.")
    finally:
        # Ensure agent resources are cleaned up before exiting
        await agent.cleanup()


if __name__ == "__main__":
    # asyncio.run(main())
    prompt = PROMPT_TEMPLATE.format(topic="二次函数")
    print(prompt)