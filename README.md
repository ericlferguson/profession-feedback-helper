# Profession Feedback Helper

A modern, extensible tool for generating structured, role-specific performance feedback for engineers, based on the [Dropbox Engineering Career Framework](https://dropbox.github.io/dbx-career-framework/).

## Features

- **Web-based GUI**: Collect and review feedback fully in your browser—no CLI required.
- **YAML-driven role definitions**: Easily add or update behaviors, expectations, and levels for any role by editing YAML files.
- **Supports Multiple Roles**: Out-of-the-box support for both Machine Learning Engineer and Software Engineer roles. Add more roles by dropping in a new YAML.
- **Personalized Feedback**: Dynamic substitution of names and pronouns for tailored reviews.
- **Section-based Ratings**: Behaviors grouped by pillar (Overview, Results, Culture, etc.) with radio-button ratings and per-section comments.
- **Summary & Export**: See a clear summary of strengths, meets, and improvement areas, plus the full Dropbox-style feedback text.
- **Optional ChatGPT Narrative**: Summarize structured feedback into a narrative with OpenAI (requires API key).

## Quick Start

### Prerequisites
- Python 3.8+
- [pip](https://pip.pypa.io/en/stable/installation/)
- (Optional) [OpenAI API key](https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key) for ChatGPT summaries

### Installation
```bash
pip install -r requirements.txt
```

### Running the Web App
1. Start the Flask app:
   ```bash
   python3 webapp.py
   ```
2. Open your browser to [http://127.0.0.1:5000](http://127.0.0.1:5000)
3. Fill out the form (name, pronouns, role, level) and click **Start Review**
4. For each behavior, select a rating (Does not meet / Meets / Exceeds) and add optional section comments
5. Submit to see a summary and the generated Dropbox-style feedback

### Example Workflow
- Select role (e.g., "Software Engineer") and level (e.g., "senior")
- Rate each behavior in the interactive form
- Add comments for any section as needed
- View/download the results and use for 1:1s or official reviews

### YAML Role Definitions
- Role definitions live in `role_definitions/` as YAML files
- Each YAML covers all levels and all Dropbox pillars for that role
- To add a new role: copy an existing YAML, edit as needed, and restart the app

### Enabling ChatGPT Summaries
- Save your OpenAI API key to `~/.open-ai/open-ai-key`
- The CLI and backend support generating a narrative summary using ChatGPT
- (Web UI integration for ChatGPT is planned—PRs welcome!)

## Extending & Customizing
- **Add new roles**: Drop a new YAML file into `role_definitions/`
- **Edit behaviors**: Update YAML for your org's values, levels, or feedback style
- **UI Tweaks**: Edit `templates/` for branding or UX changes

## CLI Usage (Legacy/Optional)
- The original CLI workflow is still available for power users and testing
- See `performance_review_generator.py` for CLI entrypoint and test harness

## Contributing
Contributions are welcome! Please open issues or PRs for new roles, UX improvements, or integrations.

## License
MIT License
