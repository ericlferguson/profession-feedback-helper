DESCRIPTION = """
    Produces a performance assessment for an machine learning engineer employee using the Dropbox career framework as a scaffold.
    
    Framework is based on this:
    https://dropbox.github.io/dbx-career-framework/
    
    """

"""
Performance review generator for Dropbox career framework roles.
"""

import os
import logging
from typing import List
import yaml

# Default LEVEL_MAP for backward compatibility
DEFAULT_LEVEL_MAP = {
    "junior": "IC1",
    "intermediate": "IC2",
    "senior": "IC3",
    "tech lead": "IC4",
    "principal": "IC5",
    "distinguished": "IC6",
}


class PerformanceReviewGenerator:
    """
    Generates performance reviews for a given role and level using Dropbox career framework YAML definitions.
    """
    def __init__(
        self,
        name: str,
        pronouns: List[str],
        role: str,
        level: str,
        get_chatgpt_feedback: bool = False,
    ) -> None:
        """
        Initialize the performance review generator.
        """
        self.name = name
        self.pronouns = pronouns
        self.role = role
        self.level = level.lower()
        # Load role YAML to check for a level_map
        self.role_data = self.load_role_definition(role)
        self.level_map = self.role_data.get('level_map', DEFAULT_LEVEL_MAP)
        self.valid_levels = list(self.level_map.keys())
        if self.level not in self.valid_levels:
            raise ValueError(f"Invalid level '{self.level}'. Must be one of {', '.join(self.valid_levels)}.")
        self.ic_level = self.level_map[self.level]
        print(f"Level selected: {self.level} (Dropbox {self.ic_level})")

        # Load YAML for the role
        self.role_data = self.load_role_definition(self.role)
        if self.level not in self.role_data['levels']:
            raise ValueError(f"Level '{self.level}' not found in YAML for role '{self.role}'")
        self.level_data = self.role_data['levels'][self.level]

        # Dynamically populate responsibilities from YAML
        self.responsibilities = {}
        for section, section_dict in self.level_data.items():
            self.responsibilities[section] = {}
            for subsection, behaviors in section_dict.items():
                self.responsibilities[section][subsection] = [
                    s.format(name=self.name, pronouns=self.pronouns)
                    for s in behaviors
                ]
        
        self.okay_list = dict()
        self.going_well_list = dict()
        self.feedback_list = dict()

        # Only collect feedback interactively if running as main
        import sys
        if hasattr(sys, 'ps1') or getattr(sys, 'argv', [None])[0] == '' or __name__ == '__main__':
            self.collect_feedback_from_user()
            self.give_feedback()
            print(self.feedback)
            if get_chatgpt_feedback:
                self.get_chatgpt_feedback()
                print(self.chatgpt_feedback)

    def collect_feedback_from_user(self):
        """Collects user feedback for each behavior, with reduced nesting for clarity."""
        print(
            "Input [0,1,2] for feedback on an item. "
            "0 means does not meet expectations. "
            "1 means meets expectations. "
            "2 means exceeds expectations."
        )

        def add_to_list(list_dict, key, value):
            if list_dict.get(key) is None:
                list_dict[key] = [value]
            else:
                list_dict[key].append(value)

        valid_ratings = [0, 1, 2]

        for responsibility, behaviors_dict in self.responsibilities.items():
            print(f"\n{responsibility}")
            for behavior_category, behaviors in behaviors_dict.items():
                print(f"\t{behavior_category}")
                for behavior in behaviors:
                    rating = None
                    while rating not in valid_ratings:
                        try:
                            user_input = input(f"\t\t{behavior}\n")
                            rating = int(user_input)
                        except ValueError:
                            continue
                    if rating == 0:
                        add_to_list(self.feedback_list, responsibility, behavior)
                    elif rating == 1:
                        add_to_list(self.okay_list, responsibility, behavior)
                    elif rating == 2:
                        add_to_list(self.going_well_list, responsibility, behavior)

    def give_feedback(self):
        feedback = ""

        feedback += "\nOVER PERFORMING:"
        for key_responsibility in self.going_well_list:
            feedback += f"\n{key_responsibility}\n"
            for comment in self.going_well_list[key_responsibility]:
                feedback += f"- {comment}\n"

        feedback += "\nMEETS EXPECTATIONS:"
        for key_responsibility in self.okay_list:
            feedback += f"\n{key_responsibility}\n"
            for comment in self.okay_list[key_responsibility]:
                feedback += f"- {comment}\n"

        feedback += "\nGIVE FEEDBACK:"
        for key_responsibility in self.feedback_list:
            feedback += f"\n{key_responsibility}\n"
            for comment in self.feedback_list[key_responsibility]:
                feedback += f"- {comment}\n"

        self.feedback = feedback

    def load_role_definition(self, role):
        """
        Loads the YAML definition for the given role from the role_definitions directory.
        """
        yaml_path = os.path.join(os.path.dirname(__file__), "role_definitions", f"{role.lower().replace(' ', '_')}.yaml")
        if not os.path.exists(yaml_path):
            raise FileNotFoundError(f"Role definition YAML not found: {yaml_path}")
        with open(yaml_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        return data

    def make_overview(self):
        """Legacy: Returns overview section for the current role/level. Now handled by YAML."""
        overview_data = self.role_data['overview']
        overview = {}
        for section, section_dict in overview_data.items():
            overview[section] = []
            for item in section_dict:
                overview[section].append(item.format(name=self.name, pronouns=self.pronouns))
        return overview

    def make_results(self):
        """Legacy: Returns results section for the current role/level. Now handled by YAML."""
        results_data = self.role_data['results']
        results = {}
        for section, section_dict in results_data.items():
            results[section] = []
            for item in section_dict:
                results[section].append(item.format(name=self.name, pronouns=self.pronouns))
        return results

    def make_direction(self):
        """Returns direction section for the current role/level, loaded from YAML."""
        direction_data = self.level_data.get('direction', {})
        direction = {}
        for section, behaviors in direction_data.items():
            direction[section] = [
                s.format(name=self.name, pronouns=self.pronouns)
                for s in behaviors
            ]
        return direction

    def make_talent(self):
        """Returns talent section for the current role/level, loaded from YAML."""
        talent_data = self.level_data.get('talent', {})
        talent = {}
        for section, behaviors in talent_data.items():
            talent[section] = [
                s.format(name=self.name, pronouns=self.pronouns)
                for s in behaviors
            ]
        return talent

    def make_culture(self):
        """Returns culture section for the current role/level, loaded from YAML."""
        culture_data = self.level_data.get('culture', {})
        culture = {}
        for section, behaviors in culture_data.items():
            culture[section] = [
                s.format(name=self.name, pronouns=self.pronouns)
                for s in behaviors
            ]
        return culture

    def make_craft(self):
        """Returns craft section for the current role/level, loaded from YAML."""
        craft_data = self.level_data.get('craft', {})
        craft = {}
        for section, behaviors in craft_data.items():
            craft[section] = [
                s.format(name=self.name, pronouns=self.pronouns)
                for s in behaviors
            ]
        return craft

    def give_feedback(self):
        """Formats feedback into sections for output, using helpers for clarity."""
        def format_section(title, section_dict):
            if not section_dict:
                return f"\n{title}:\n(No feedback)\n"
            lines = [f"\n{title}:"]
            for responsibility, comments in section_dict.items():
                lines.append(f"{responsibility}")
                for comment in comments:
                    lines.append(f"- {comment}")
            return "\n".join(lines)

        feedback = ""
        feedback += format_section("OVER PERFORMING", self.going_well_list)
        feedback += format_section("MEETS EXPECTATIONS", self.okay_list)
        feedback += format_section("GIVE FEEDBACK", self.feedback_list)
        self.feedback = feedback

    def get_chatgpt_feedback(self, model="chatgpt-4o-latest"):
        from openai import OpenAI
        from tenacity import retry, stop_after_attempt, wait_random_exponential
        from os.path import expanduser

        def create_error_message(error_type, error_detail=""):
            """Create a standardized error message with the prompt included."""
            return f"""ChatGPT feedback is not available - {error_type}{error_detail}.

In the meantime, you can paste this prompt into your favourite LLM in order to get your feedback:

{primer_prompt}"""

        @retry(wait=wait_random_exponential(min=1, max=10), stop=stop_after_attempt(3))
        def submit_prompt(client, model, prompt: str, transaction: str):
            logging.info("Submitting prompt...")
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": prompt + transaction},
                    {"role": "user", "content": transaction},
                ]
            )
            return response

        # Define the prompt template
        primer_prompt = f"""I want you to be an engineering manager coach. Someone like Claire Hughes Johnson, author of "Scaling People: Tactics for Management and Company Building", or  Patrick Lencioni author of "five dysfunctions of a team". Reply with UK english spelling. Avoid hyperbole.
        I am giving writing a performance review for a {self.level} {self.role}. Build me a narrative for {self.name}'s performance review, based on my ratings of {self.pronouns[1]} skills.
        break it into these sections:
        - What are some things they do well?
        - How could they improve?
        - What are their biggest challenges? 

        I have rated their skills on the basis of: going well; meets; and needs improvement.
        Here is the specific rated skills. Pay note to any additional comments made also. The tone should not be too casual.

{self.feedback}"""

        # Try to read the API key
        try:
            with open(expanduser("~/.open-ai/open-ai-key"), "r") as f:
                api_key = f.read().strip()
        except FileNotFoundError:
            print("Please create a file at ~/.open-ai/open-ai-key with your OpenAI API key.")
            self.chatgpt_feedback = create_error_message("missing API key", " Please add your OpenAI API key to ~/.open-ai/open-ai-key to enable this feature")
            return
        except Exception as e:
            print(f"An error occurred while reading the API key file: {e}")
            self.chatgpt_feedback = create_error_message("error reading key file", f": {e}")
            return

        # Create client and submit prompt
        client = OpenAI(api_key=api_key)
        self.chatgpt_response = submit_prompt(client, model, primer_prompt, self.feedback)
        self.chatgpt_feedback = self.chatgpt_response.choices[0].message.content


def make_feedback():
    name = "Bob"
    pronouns = ["he", "his"]
    level = "senior"

    feedback = PerformanceReviewGenerator(
        name=name,
        pronouns=pronouns,
        role="Machine Learning Engineer",
        level=level,
        get_chatgpt_feedback=True,
    )


if __name__ == "__main__":
    # === YAML-driven PerformanceReviewGenerator Test Harness ===
    # This harness simulates feedback for multiple roles/levels without user input.

    class TestablePerformanceReviewGenerator(PerformanceReviewGenerator):
        def collect_feedback_from_user(self):
            # Simulate all ratings as '1' (meets expectations)
            for responsibility, behaviors_dict in self.responsibilities.items():
                for behavior_category, behaviors in behaviors_dict.items():
                    for behavior in behaviors:
                        self.okay_list.setdefault(responsibility, []).append(behavior)

    def run_test(role, level, name="Test User", pronouns=["they", "their"]):
        print(f"\n=== TEST: {role} ({level}) ===")
        gen = TestablePerformanceReviewGenerator(
            name=name,
            pronouns=pronouns,
            role=role,
            level=level,
            get_chatgpt_feedback=False,
        )
        print(gen.feedback)

    print("\n===== YAML-Driven Performance Review Generator Smoke Tests =====")
    tests = [
        ("Machine Learning Engineer", "junior", "Alice", ["she", "her"]),
        ("Machine Learning Engineer", "senior", "Bob", ["he", "his"]),
        ("Software Engineer", "junior", "Charlie", ["they", "their"]),
        ("Software Engineer", "principal", "Dana", ["she", "her"]),
    ]
    for role, level, name, pronouns in tests:
        run_test(role, level, name=name, pronouns=pronouns)
