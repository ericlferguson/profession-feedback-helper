# Engineering Feedback Tool

This tool is designed to assist professional Engineering Managers in providing effective and structured feedback to their direct reports. The feedback framework is heavily based on the [Dropbox Engineering Career Framework](https://dropbox.github.io/dbx-career-framework/), ensuring that expectations and responsibilities are clear and consistent.

## Features

- **Structured Feedback**: Provides a systematic way to deliver feedback aligned with established career frameworks.
- **Role-Based Expectations**: Feedback is tailored based on specific roles within the engineering team.
- **ChatGPT driven summaries**: ChatGPT will summaries and turn specific feedback into a more approachable narrative. This optional feature requires an [OpenAI api key](https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key).

## Current Scope

Please note that the current implementation is limited to the **Machine Learning Engineer (MLE)** role. Support for additional roles will be added in future updates.

## Usage Instructions

### Prerequisites

- Python 3.7 or above installed.
- Install the necessary dependencies by running:
  ```bash
  pip install -r requirements.txt
  ```
- For the ChatGPT feedback feature, you will need an [OpenAI API key](https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key). Make sure to save your key in `~/.open-ai/open-ai-key`.

### Running the Feedback Tool

1. **Clone the repository** to your local machine:

   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. **Create feedback** for a Machine Learning Engineer by running:

   ```
   bash python feedback_tool.py
   ```

3. **Input the details**: You will be prompted to provide feedback for specific performance areas. Use the following inputs:

   - `0` for under-performing
   - `1` for meets expectations
   - `2` for over-performing

   Follow the prompts in your terminal to rate different aspects of the engineer's performance.

4. **Review the generated feedback**: Once you complete the input, the tool will produce a summary of the feedback, divided into sections indicating areas of strength, improvement opportunities, and challenges.

5. **Optional ChatGPT Feedback**: If you have an OpenAI API key and want to get ChatGPT to summarize the feedback into a more narrative format, set `get_chatgpt_feedback=True` when initializing the `FeedbackPillars` class. The narrative will be printed after the structured feedback.

### Example Usage

To generate feedback for an intermediate-level Machine Learning Engineer named "Amy", you can modify the `make_feedback()` function like this:

```python
feedback = FeedbackPillars(
    name="Amy",
    pronouns=["she", "her"],
    role="Machine Learning Engineer",
    level="intermediate",
    get_chatgpt_feedback=True,
)
```

Then run:
```bash
python feedback_tool.py
```
The generated feedback and optional ChatGPT narrative will be displayed in the console.

### Notes

- **Feedback Ratings**: The feedback ratings must be provided interactively in the terminal. Ensure that you provide a valid number (0, 1, or 2) for each question.
- **ChatGPT API Key**: For the ChatGPT-based narrative feedback, ensure that the API key file is in the correct location (`~/.open-ai/open-ai-key`). The tool will use this key to interact with OpenAI's API.
```

You can copy and paste this text directly into your README file. Let me know if you need any more edits!

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss potential changes.

## License

This project is licensed under the MIT License.
