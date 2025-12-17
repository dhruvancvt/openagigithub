# OpenAGI LinkedIn Automation

An automated LinkedIn posting system powered by OpenAGI that uses AI agents to create and publish original posts inspired by example content.

## Description

This project automates LinkedIn post creation and publishing using OpenAGI's TaskerAgent. The system reads example posts from an HTML file, analyzes their style and format, generates original content inspired by the examples, and automatically posts to LinkedIn using screen capture and keyboard/mouse automation.

## Features

- 🤖 **AI-Powered Content Generation**: Creates original LinkedIn posts inspired by example content
- 📸 **Screen Capture**: Automatically captures screenshots for visual understanding
- 🖱️ **Automated Actions**: Controls keyboard and mouse to interact with LinkedIn
- 🔄 **Continuous Operation**: Runs in a loop, posting at regular intervals
- 📝 **Style Analysis**: Analyzes example posts to maintain consistent tone and format

## Requirements

- Python 3.7+
- OpenAGI library (`oagi`)
- python-dotenv
- OAGI API key

## Setup

1. **Install dependencies:**
   ```bash
   pip install oagi python-dotenv
   ```

2. **Set up environment variables:**
   Create a `.env` file in the project root:
   ```
   OAGI_API_KEY=your_api_key_here
   ```

3. **Prepare your posts template:**
   Ensure `posts.html` contains example posts in the format shown in the file.

## Usage

Run the automation script:
```bash
python example.py
```

The script will:
1. Navigate to LinkedIn feed
2. Open the post creation interface
3. Read and analyze example posts from `posts.html`
4. Generate an original post inspired by the examples
5. Type and publish the post to LinkedIn
6. Wait 60 seconds before repeating

## Configuration

You can customize the behavior by modifying:
- **Task description**: Change the `task` parameter in `agent.set_task()`
- **Todo list**: Modify the `todos` array to change the automation steps
- **Wait time**: Adjust `asyncio.sleep(60)` to change the interval between posts
- **Model**: Change the `model` parameter (default: "lux-actor-1")

## Files

- `example.py` - Main automation script
- `posts.html` - Example posts used as inspiration for content generation
- `.env` - Environment variables (create this file with your API key)

## Notes

- Ensure LinkedIn is accessible in your default browser
- The script requires the posts.html file path to be correctly set
- Make sure your OAGI API key has sufficient credits/quota
- The automation runs continuously until stopped (Ctrl+C)

## License

This project is provided as-is for educational and automation purposes.

