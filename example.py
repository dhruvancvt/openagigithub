import asyncio
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()

# Captures the screenshot from your local computer
from oagi import AsyncScreenshotMaker 

# Controls your local keyboard and mouse based on the model predicted actions
from oagi import AsyncPyautoguiActionHandler 
from oagi import TaskerAgent

async def main():
    while True:
        # Get API key from environment
        api_key = os.getenv('OAGI_API_KEY')
        if not api_key:
            print("Error: OAGI_API_KEY not set in environment")
            return
        
        agent = TaskerAgent(model="lux-actor-1", api_key=api_key)

        agent.set_task(
                task="Spread happiness and love to all.",
                todos=[
                    "Navigate to https://linkedin.com/feed and wait for the page to fully load.",
                    
                    "Locate the post creation box (usually says 'Start a post' or 'Share that you're hiring').",
                    "Click directly on the text area of the post creation box to open the post composer.",
                    "Wait for the post composer modal/dialog to fully appear.",
                    
                    "Open a new tab and navigate to file:///Users/dhruvanavinchander/Desktop/openagigithub/posts.html",
                    "Read and analyze the entire contents of posts.html carefully.",
                    "Study the writing style, tone, formatting patterns, and types of topics covered in the example posts.",
                    "Identify the common themes, hashtags used, post length, and engagement strategies.",
                    
                    "Return to the LinkedIn tab with the open post composer.",
                    "Create a NEW original post that is inspired by but NOT identical to any post in posts.html.",
                    "Ensure the new post follows the same style and format as the examples.",
                    
                    "Click into the text area of the post composer.",
                    "Type the newly created original post content into the text area.",
                    
                    "Locate the 'Post' button (typically a blue button in the bottom right of the composer).",
                    "Verify the post content one final time before publishing.",
                    "Click the 'Post' button to publish the post.",
                    "Wait for confirmation that the post was published successfully (post should appear in feed).",
                ]
                )

        await agent.execute(
                instruction="Spread happiness and love to all.",
                action_handler=AsyncPyautoguiActionHandler(),
                image_provider=AsyncScreenshotMaker(),
                 )

        await asyncio.sleep(60)  # Wait 60 seconds

asyncio.run(main())
