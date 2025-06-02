DESCRIPTION = """
    Produces a performance assessment for an machine learning engineer employee using the Dropbox career framework as a scaffold.
    
    Framework is based on this:
    https://dropbox.github.io/dbx-career-framework/ic2_machine_learning_engineer.html
    
    """

from typing import List
import logging

# Maps user-friendly levels to Dropbox IC levels
LEVEL_MAP = {
    "junior": "IC1",
    "intermediate": "IC2",
    "senior": "IC3",
    "tech lead": "IC4",
    "principal": "IC5",
}


class PerformanceReviewGenerator:
    def __init__(
        self,
        name: str,
        pronouns: List[str],
        role: str,
        level: str,
        get_chatgpt_feedback: bool = False,
    ) -> None:
        self.name = name
        self.pronouns = pronouns
        self.role = role
        self.level = level.lower()
        self.valid_levels = list(LEVEL_MAP.keys())
        if self.level not in self.valid_levels:
            raise ValueError(f"Invalid level '{self.level}'. Must be one of {', '.join(self.valid_levels)}.")
        self.ic_level = LEVEL_MAP[self.level]
        # Optionally, display both for debugging
        print(f"Level selected: {self.level} (Dropbox {self.ic_level})")
        
        self.responsibilities = {
            "overview": self.make_overview(),
            "results": self.make_results(),
            "direction": self.make_direction(),
            "talent": self.make_talent(),
            "culture": self.make_culture(),
            "craft": self.make_craft(),
        }

        self.okay_list = dict()
        self.going_well_list = dict()
        self.feedback_list = dict()

        self.collect_feedback_from_user()
        self.give_feedback()

        print(self.feedback)

        if get_chatgpt_feedback:
            self.get_chatgpt_feedback()
            print(self.chatgpt_feedback)

    def collect_feedback_from_user(self):
        print(
            "Input [0,1,2] for feedback on an item. "
            "0 means does not meet expectations. "
            "1 means meets expectactions. "
            "2 means exceeds expectactions."
        )

        for key_responsibility in self.responsibilities:
            print(f"\n{key_responsibility}")
            for key_behaviors in self.responsibilities[key_responsibility]:
                print(f"\t{key_behaviors}")
                for key_behavior in self.responsibilities[key_responsibility][
                    key_behaviors
                ]:
                    rating = -1
                    valid_ratings = [0, 1, 2]
                    while rating not in valid_ratings:
                        try:
                            rating = int(input(f"\t\t{key_behavior}\n"))
                        except ValueError:
                            pass  # deal with invalid input
                        if rating == 0:
                            if self.feedback_list.get(key_responsibility) is None:
                                self.feedback_list[key_responsibility] = [key_behavior]
                            else:
                                self.feedback_list[key_responsibility].append(
                                    key_behavior
                                )
                        elif rating == 1:
                            if self.okay_list.get(key_responsibility) is None:
                                self.okay_list[key_responsibility] = [key_behavior]
                            else:
                                self.okay_list[key_responsibility].append(key_behavior)
                        elif rating == 2:
                            if self.going_well_list.get(key_responsibility) is None:
                                self.going_well_list[key_responsibility] = [
                                    key_behavior
                                ]
                            else:
                                self.going_well_list[key_responsibility].append(
                                    key_behavior
                                )

                        else:
                            print(
                                f"Invalid input. Valid choices are {valid_ratings}. Try again."
                            )

    def make_overview(self):
        if self.role == "Machine Learning Engineer":
            if self.level == "junior":
                return {
                    "scope": [
                        f"{self.name} executes on defined tasks and contributes to solving problems with defined solutions.",
                    ],
                    "collaborative reach": [
                        f"{self.name} works primarily within the scope of {self.pronouns[1]} team with high level guidance from {self.pronouns[1]} manager/TL."
                    ],
                    "impact levers": [
                        f"Craft - {self.name} primarily focuses on improving {self.pronouns[1]} craft as an engineer",
                    ],
                }
            elif self.level == "intermediate":
                return {
                    "scope": [
                        f"{self.name} executes on defined projects to achieve team-level goals.",
                        f"{self.name} independently defines the right solutions or uses existing approaches to solve defined problems.",
                    ],
                    "collaborative reach": [
                        f"{self.name} works primarily within the scope of {self.pronouns[1]} team with high level guidance from {self.pronouns[1]} manager/TL."
                    ],
                    "impact levers": [
                        f"Craft - {self.name} is increasingly mastering {self.pronouns[1]} craft and leverage it for higher impact (e.g. software design)",
                        f"Mentorship - {self.name} may mentor new hires, interns, or more junior engineers.",
                    ],
                }
            elif self.level == "senior":
                return {
                    "scope": [
                        f"{self.name} owns and delivers projects in service of quarterly goals on the team.",
                        f"{self.name} independently identifies the right solutions to solve ambiguous, open-ended problems.",
                    ],
                    "collaborative reach": [
                        f"{self.name} works primarily with {self.pronouns[1]} direct team and cross-functional partners while driving cross-team collaboration for {self.pronouns[1]} project."
                    ],
                    "impact levers": [
                        f"Project Leadership - {self.name} defines and delivers well-scoped milestones for a project. {self.pronouns[0]} may be a technical lead for projects on {self.pronouns[1]} team.",
                        f"Product Expertise - {self.name} actively keeps customer needs in mind and leverages input from product stakeholders as available to determine the right technical solutions to deliver customer value quickly.",
                        f"Mentorship - {self.name} actively levels up less-experienced members of {self.pronouns[1]} team by helping them with their craft, providing guidance, and setting a good example.",
                    ],
                }
            elif self.level == "tech lead":
                return {
                    "scope": [
                        f"{self.name} owns and delivers semi-annual/annual goals for {self.pronouns[1]} team.",
                        f"{self.name} is an expert at identifying the right solutions to solve ambiguous, open-ended problems that require tough prioritization.",
                        f"{self.name} defines technical solutions or efficient operational processes that level up {self.pronouns[1]} team.",
                    ],
                    "collaborative reach": [
                        f"{self.name} is a strong leader for my team with {self.pronouns[1]} impact beginning to extend outside {self.pronouns[1]} team.",
                        f"{self.name} increasingly optimizes beyond just {self.pronouns[1]} team by driving cross-team or cross-discipline initiatives.",
                    ],
                    "impact levers": [
                        f"Technical Strategy - {self.name} plays a key role in setting medium-to-long term strategy for business-impacting projects.",
                        f"Project Leadership - {self.name} autonomously defines and deliver technical roadmaps of larger projects, often involving cross-team dependencies.",
                        f"Product Expertise - {self.name} actively keeps customer needs in mind and leverage input from product stakeholders as available to determine the right technical solutions to deliver customer value quickly.",
                        f"Mentorship - {self.name} actively levels-up less-experienced members of {self.pronouns[1]} team by helping them with their craft, providing guidance, and setting a good example.",
                    ],
                }
            elif self.level == "principal":
                return {
                    "scope": [
                        f"{self.name} owns and delivers multi-year, org-level goals that push forward the boundaries of our business and technology.",
                        f"{self.name} is an organization-wide technical leader who sets the direction for the company's Machine Learning strategy.",
                    ],
                    "collaborative reach": [
                        f"{self.name} works across the entire engineering organization and partners closely with senior leadership.",
                        f"{self.name} represents the company's technical capabilities to external stakeholders and the broader tech community.",
                    ],
                    "impact levers": [
                        f"Organizational Strategy - {self.name} plays a key role in shaping the long-term technical strategy of the entire organization.",
                        f"Technical Innovation - {self.name} drives major technical innovations that create new capabilities for the company.",
                        f"Industry Influence - {self.name} is recognized as a thought leader in the Machine Learning field, influencing industry trends.",
                        f"Organizational Growth - {self.name} significantly contributes to the growth and development of the engineering organization as a whole.",
                    ],
                }
            else:
                raise NotImplementedError(f"{self.level} level is not implemented!")
        else:
            raise NotImplementedError(f"{self.role} role is not implemented!")

    def make_results(self):
        if self.role == "Machine Learning Engineer":
            if self.level == "junior":
                return {
                    "impact": [
                        f"{self.name} delivers on assigned tasks and contributes to team projects.",
                        f"{self.name} implements and tests machine learning models under guidance.",
                    ],
                    "execution": [
                        f"{self.name} follows established best practices and coding standards.",
                        f"{self.name} writes clear and maintainable code for defined tasks.",
                    ],
                    "initiative": [
                        f"{self.name} asks questions to clarify requirements and seeks help when stuck.",
                        f"{self.name} shows eagerness to learn and apply new ML techniques.",
                    ],
                }
            elif self.level == "intermediate":
                return {
                    "impact": [
                        f"{self.name} independently delivers on medium-sized projects.",
                        f"{self.name} implements and optimizes machine learning models with minimal guidance.",
                    ],
                    "execution": [
                        f"{self.name} designs and implements efficient ML pipelines.",
                        f"{self.name} identifies and resolves common issues in ML workflows.",
                    ],
                    "initiative": [
                        f"{self.name} proactively suggests improvements to existing ML systems.",
                        f"{self.name} takes ownership of their work and sees it through to completion.",
                    ],
                }
            elif self.level == "senior":
                return {
                    "impact": [
                        f"{self.name} leads the delivery of large, complex ML projects.",
                        f"{self.name} develops novel ML solutions that significantly improve product performance.",
                    ],
                    "execution": [
                        f"{self.name} architects scalable and maintainable ML systems.",
                        f"{self.name} optimizes ML pipelines for performance and resource efficiency.",
                    ],
                    "initiative": [
                        f"{self.name} identifies new opportunities for applying ML to solve business problems.",
                        f"{self.name} mentors junior team members and elevates the team's ML capabilities.",
                    ],
                }
            elif self.level == "tech lead":
                return {
                    "impact": [
                        f"{self.name} drives the success of multiple high-impact ML initiatives across teams.",
                        f"{self.name} defines and implements ML strategies that create significant business value.",
                    ],
                    "execution": [
                        f"{self.name} designs and oversees the implementation of complex, distributed ML systems.",
                        f"{self.name} establishes best practices and architectural patterns for ML at scale.",
                    ],
                    "initiative": [
                        f"{self.name} anticipates future ML needs and proactively develops solutions.",
                        f"{self.name} fosters a culture of innovation and continuous improvement in ML practices.",
                    ],
                }
            elif self.level == "principal":
                return {
                    "impact": [
                        f"{self.name} drives org-wide ML initiatives that fundamentally enhance the company's capabilities.",
                        f"{self.name} pioneers cutting-edge ML technologies that position the company as an industry leader.",
                    ],
                    "execution": [
                        f"{self.name} architects transformative ML systems that operate at massive scale.",
                        f"{self.name} defines the technical vision for ML across the organization.",
                    ],
                    "initiative": [
                        f"{self.name} identifies and pursues breakthrough ML research opportunities.",
                        f"{self.name} influences the broader ML community through publications, talks, and open-source contributions.",
                    ],
                }
            else:
                raise NotImplementedError(f"{self.level} level is not implemented!")
        else:
            raise NotImplementedError(f"{self.role} role is not implemented!")
    def make_direction(self):
        if self.role == "Machine Learning Engineer":
            if self.level == "junior":
{{ ... }}
                return {
                    "agility / innovation": [
                        f"{self.name} shares new ideas and can adapt {self.pronouns[1]} work when circumstances change.",
                    ],
                }
            elif self.level == "intermediate":
                return {
                    "agility": [
                        f"{self.name} is open to change and enthusiastic about new initiatives.",
                        f"{self.name} works with {self.pronouns[1]} manager to navigate complex and ambiguous situations",
                    ],
                    "innovation": [
                        f"{self.name} asks questions and contributes to new ideas/approaches.",
                        f"{self.name} experiments with new approaches and share what {self.pronouns[0]} has learned.",
                    ],
                }
            elif self.level == "senior":
                return {
                    "agility": [
                        f"{self.name} embraces change and adapts quickly to it.",
                        f"{self.name} remains resilient through change by staying calm under pressure and taking care of {self.pronouns[1]} well-being.",
                        f"{self.name} navigates ambiguity by focusing on the greater purpose, goals, and desired impact to move forward one step at a time.",
                    ],
                    "innovation": [
                        f"{self.name} asks questions and contributes to new ideas/approaches.",
                        f"{self.name} has a growth mindset and is comfortable experimenting with new approaches, learning, owning the outcomes, and sharing what {self.pronouns[0]} learned.",
                        f"{self.name} works with {self.pronouns[1]} manager to find new ways of utilizing customer feedback to influence our teams' plans.",
                    ],
                    "strategy": [
                        f"{self.name} works collaboratively with {self.pronouns[1]} manager to set realistic and ambitious short-term goals to deliver customer value quickly, and break them down to smaller projects for my team or myself.",
                        f"{self.name} executes the development roadmap for multi-phase projects, possibly as a project lead.",
                    ],
                }

            elif self.level == "tech lead":
                return {
                    "agility": [
                        f"{self.name} embraces change and adapts quickly to it.",
                        f"{self.name} remains resilient through change by staying calm under pressure and taking care of {self.pronouns[1]} well-being.",
                        f"{self.name} navigates ambiguity by focusing on the greater purpose, goals, and desired impact to move forward one step at a time.",
                    ],
                    "innovation": [
                        f"{self.name} has a growth mindset and is comfortable experimenting with new approaches, learning, owning the outcomes, and sharing what {self.pronouns[0]} learned.",
                        f"{self.name} sets audacious goals, takes risks, and shares lessons learned.",
                        f"{self.name} is beginning to push boundaries using industry best practices and customer feedback to implement strategies that drive our products, tools, or services forward.",
                    ],
                    "strategy": [
                        f"{self.name} defines the technical roadmap for impactful multi-phase projects, refining it as the projects progress to deliver customer value quickly, and provides leadership for the people executing on the project.",
                        f"In partnership with {self.pronouns[1]} manager, {self.name} defines {self.pronouns[1]} team's priorities and secures buy-in by engaging stakeholders and aligning with company priorities and customer needs.",
                        f"{self.name} generates excitement for {self.pronouns[1]}/the team's strategy.",
                    ],
                }
            elif self.level == "principal":
                return {
                    "agility": [
                        f"{self.name} leads through change and helps the organization adapt quickly.",
                        f"{self.name} models resilience and helps others navigate ambiguity and uncertainty.",
                        f"{self.name} creates clarity and confidence in times of ambiguity by focusing on the bigger picture and communicating a clear path forward.",
                    ],
                    "innovation": [
                        f"{self.name} fosters a culture of innovation within the organization.",
                        f"{self.name} identifies and champions transformative opportunities that can significantly impact the company's ML capabilities.",
                        f"{self.name} pushes the boundaries of what's possible in ML, driving the adoption of cutting-edge techniques and technologies.",
                    ],
                    "strategy": [
                        f"{self.name} develops and drives the long-term ML strategy for the organization, aligning it with overall business objectives.",
                        f"{self.name} influences company-wide technical decisions and priorities.",
                        f"{self.name} anticipates industry trends and positions the organization to capitalize on emerging opportunities in the ML space.",
                    ],
                }
            else:
                raise NotImplementedError(f"{self.level} level is not implemented!")
        else:
            raise NotImplementedError(f"{self.role} role is not implemented!")

    def make_talent(self):
        if self.role == "Machine Learning Engineer":
            if self.level == "junior":
                return {
                    "personal growth": [
                        f"{self.name} is open to and acts upon feedback from {self.pronouns[1]} manager and peers.",
                        f"{self.name} is self-aware about {self.pronouns[1]} strengths and areas for development.",
                        f"{self.name} drives discussions with {self.pronouns[1]} manager about {self.pronouns[1]} career goals.",
                    ],
                }
            elif self.level == "intermediate":
                return {
                    "personal growth": [
                        f"{self.name} proactively asks for feedback from those {self.pronouns[0]} works with and identifies ways to act upon it.",
                        f"{self.name} has self-awareness about {self.pronouns[1]} strengths and development areas.",
                        f"{self.name} reflects on {self.pronouns[1]} experiences to identify areas of growth.",
                    ],
                    "mentorship": [
                        f"{self.name} supports new hires on {self.pronouns[1]} team through onboarding.",
                        f"{self.name} may mentor interns or apprentices.",
                    ],
                }
            elif self.level == "senior":
                return {
                    "personal growth": [
                        f"{self.name} seeks out challenging or stretch opportunities to advance {self.pronouns[1]} learning and development.",
                        f"{self.name} actively works on {self.pronouns[1]} development areas and seeks feedback to confirm progress.",
                    ],
                    "mentorship": [
                        f"{self.name} mentors other engineers on the team.",
                        f"{self.name} supports personal and professional development of team members.",
                        f"{self.name} is a role model for good engineering practices and strong team behaviors.",
                    ],
                    "talent development": [
                        f"{self.name} participates in interviewing and helps improve our hiring processes.",
                        f"{self.name} contributes to developing and delivering engineering onboarding and training materials.",
                    ],
                }
            elif self.level == "tech lead":
                return {
                    "personal growth": [
                        f"{self.name} has a strong sense of self-awareness and actively works on {self.pronouns[1]} development areas.",
                        f"{self.name} seeks out challenging, high-impact opportunities to advance {self.pronouns[1]} learning and development.",
                    ],
                    "mentorship": [
                        f"{self.name} actively mentors multiple team members, including senior engineers.",
                        f"{self.name} helps other engineers to set goals and develop their careers.",
                        f"{self.name} is a role model for engineering excellence and professional growth.",
                    ],
                    "talent development": [
                        f"{self.name} plays a key role in recruiting and hiring decisions for the team.",
                        f"{self.name} identifies and creates opportunities for team members to grow and take on new challenges.",
                        f"{self.name} contributes significantly to the team's strategy for developing and retaining talent.",
                    ],
                }
            elif self.level == "principal":
                return {
                    "personal growth": [
                        f"{self.name} continues to grow and develop as a leader in the field of machine learning.",
                        f"{self.name} seeks out opportunities to learn from other industry leaders and bring that knowledge back to the organization.",
                    ],
                    "mentorship": [
                        f"{self.name} serves as a mentor and advisor to senior engineers and tech leads across the organization.",
                        f"{self.name} actively develops the next generation of technical leaders within the company.",
                    ],
                    "talent development": [
                        f"{self.name} plays a crucial role in shaping the organization's overall talent strategy for machine learning engineers.",
                        f"{self.name} creates and champions programs for developing ML talent across the company.",
                        f"{self.name} is instrumental in attracting top ML talent to the organization.",
                        f"{self.name} influences the industry's perception of the company as a great place for ML engineers to work and grow.",
                    ],
                }
            else:
                raise NotImplementedError(f"{self.level} level is not implemented!")
        else:
            raise NotImplementedError(f"{self.role} role is not implemented!")

    def make_culture(self):
        if self.role == "Machine Learning Engineer":
            if self.level == "junior":
                return {
                    "collaboration": [
                        f"{self.name} works effectively with {self.pronouns[1]} immediate team members.",
                        f"{self.name} actively participates in team meetings and discussions.",
                    ],
                    "communication": [
                        f"{self.name} clearly communicates status updates and blockers to {self.pronouns[1]} manager and team.",
                        f"{self.name} asks questions to clarify requirements and expectations.",
                    ],
                    "company values": [
                        f"{self.name} demonstrates understanding of Dropbox values in day-to-day work.",
                        f"{self.name} shows enthusiasm for the company mission and product.",
                    ],
                }
            elif self.level == "intermediate":
                return {
                    "collaboration": [
                        f"{self.name} works well across teams and disciplines on {self.pronouns[1]} projects.",
                        f"{self.name} proactively shares knowledge with team members.",
                    ],
                    "communication": [
                        f"{self.name} effectively communicates technical concepts to both technical and non-technical audiences.",
                        f"{self.name} provides constructive feedback in code reviews and design discussions.",
                    ],
                    "company values": [
                        f"{self.name} consistently demonstrates and promotes Dropbox values.",
                        f"{self.name} contributes to a positive team environment.",
                    ],
                }
            elif self.level == "senior":
                return {
                    "collaboration": [
                        f"{self.name} fosters a collaborative environment within and across teams.",
                        f"{self.name} proactively identifies and addresses team dynamics issues.",
                    ],
                    "communication": [
                        f"{self.name} communicates complex technical ideas clearly and persuasively.",
                        f"{self.name} tailors communication style to diverse audiences effectively.",
                        f"{self.name} represents the team well in cross-functional settings.",
                    ],
                    "company values": [
                        f"{self.name} is a strong advocate for Dropbox values and positively influences team culture.",
                        f"{self.name} promotes inclusive practices and supports diversity initiatives.",
                    ],
                }
            elif self.level == "tech lead":
                return {
                    "collaboration": [
                        f"{self.name} builds strong relationships across the organization to drive alignment and collaboration.",
                        f"{self.name} creates an environment of psychological safety where team members feel comfortable taking risks and sharing ideas.",
                    ],
                    "communication": [
                        f"{self.name} articulates technical vision and strategy clearly to various stakeholders.",
                        f"{self.name} facilitates effective communication within the team and across teams.",
                        f"{self.name} provides impactful presentations at the organizational level.",
                    ],
                    "company values": [
                        f"{self.name} is a role model for Dropbox values and actively shapes team and org culture.",
                        f"{self.name} champions diversity, equity, and inclusion in all aspects of work.",
                    ],
                }
            elif self.level == "principal":
                return {
                    "collaboration": [
                        f"{self.name} drives collaboration at the highest levels of the organization.",
                        f"{self.name} breaks down silos and aligns diverse groups towards common goals.",
                        f"{self.name} creates systems and processes that foster collaboration across the entire engineering organization.",
                    ],
                    "communication": [
                        f"{self.name} communicates complex technical strategies to senior leadership and external stakeholders.",
                        f"{self.name} influences company-wide communication practices and standards.",
                        f"{self.name} represents Dropbox's technical vision and culture externally (e.g., conferences, industry events).",
                    ],
                    "company values": [
                        f"{self.name} embodies and evangelizes Dropbox values, significantly influencing company culture.",
                        f"{self.name} drives organizational initiatives that reinforce and evolve company values.",
                        f"{self.name} is a thought leader in creating an inclusive and innovative engineering culture.",
                    ],
                }
            else:
                raise NotImplementedError(f"{self.level} level is not implemented!")
        else:
            raise NotImplementedError(f"{self.role} role is not implemented!")

    def make_craft(self):
        if self.role == "Machine Learning Engineer":
            if self.level == "junior":
                return {
                    "technical skills": [
                        f"{self.name} demonstrates basic proficiency in Python and ML libraries like TensorFlow or PyTorch.",
                        f"{self.name} understands fundamental ML concepts and can implement simple models.",
                    ],
                    "best practices": [
                        f"{self.name} writes clean, readable code following team coding standards.",
                        f"{self.name} participates in code reviews and incorporates feedback.",
                    ],
                    "domain knowledge": [
                        f"{self.name} is developing understanding of the problem domain and Dropbox's ML use cases.",
                    ],
                }
            elif self.level == "intermediate":
                return {
                    "technical skills": [
                        f"{self.name} has strong proficiency in ML frameworks and can implement and tune various types of models.",
                        f"{self.name} understands and can apply advanced ML concepts like regularization, feature engineering, and hyperparameter tuning.",
                    ],
                    "best practices": [
                        f"{self.name} writes efficient, scalable code and understands ML system design principles.",
                        f"{self.name} implements proper error handling and logging in ML pipelines.",
                    ],
                    "domain knowledge": [
                        f"{self.name} has solid understanding of Dropbox's ML infrastructure and can independently work on existing ML systems.",
                    ],
                }
            elif self.level == "senior":
                return {
                    "technical skills": [
                        f"{self.name} has deep expertise in multiple areas of ML and can architect complex ML systems.",
                        f"{self.name} stays current with state-of-the-art ML techniques and can evaluate their applicability to Dropbox's problems.",
                    ],
                    "best practices": [
                        f"{self.name} designs and implements robust, scalable ML pipelines.",
                        f"{self.name} establishes best practices for model development, testing, and deployment.",
                    ],
                    "domain knowledge": [
                        f"{self.name} has comprehensive understanding of Dropbox's ML ecosystem and can make significant improvements to it.",
                        f"{self.name} translates business problems into ML solutions effectively.",
                    ],
                }
            elif self.level == "tech lead":
                return {
                    "technical skills": [
                        f"{self.name} has exceptional breadth and depth of ML knowledge and can tackle the most complex ML challenges.",
                        f"{self.name} architects large-scale, distributed ML systems that push the boundaries of what's possible at Dropbox.",
                    ],
                    "best practices": [
                        f"{self.name} defines and drives adoption of ML best practices across multiple teams.",
                        f"{self.name} implements strategies for monitoring and improving ML system performance at scale.",
                    ],
                    "domain knowledge": [
                        f"{self.name} is a subject matter expert in Dropbox's ML systems and can guide strategic technical decisions.",
                        f"{self.name} has deep understanding of how ML fits into Dropbox's broader technical and business strategy.",
                    ],
                }
            elif self.level == "principal":
                return {
                    "technical skills": [
                        f"{self.name} is recognized as a thought leader in ML, both within Dropbox and in the broader tech community.",
                        f"{self.name} drives innovation in ML techniques and technologies that have company-wide or industry-wide impact.",
                    ],
                    "best practices": [
                        f"{self.name} defines ML engineering standards and practices that are adopted across the organization and potentially the industry.",
                        f"{self.name} creates frameworks and tools that significantly enhance ML development and deployment capabilities.",
                    ],
                    "domain knowledge": [
                        f"{self.name} has unparalleled understanding of Dropbox's technical landscape and how ML can drive business value.",
                        f"{self.name} shapes the long-term vision for ML at Dropbox and influences industry trends.",
                    ],
                }
            else:
                raise NotImplementedError(f"{self.level} level is not implemented!")
        else:
            raise NotImplementedError(f"{self.role} role is not implemented!")
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

    def get_chatgpt_feedback(self, model="chatgpt-4o-latest"):
        from openai import OpenAI
        from tenacity import (
            retry,
            stop_after_attempt,
            wait_random_exponential,
        )  # for exponential backoff
        from os.path import expanduser

        @retry(wait=wait_random_exponential(min=1, max=10), stop=stop_after_attempt(3))
        def submit_prompt(client, model, prompt: str, transaction: str):
            logging.info(f"Submitting prompt...")

            prompt = prompt + transaction
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": prompt},
                    {"role": "user", "content": transaction},
                ],
            )

            return response

        # open ai api key from file
        try:
            with open(expanduser("~/.open-ai/open-ai-key"), "r") as f:
                api_key = f.read().strip()
        except FileNotFoundError:
            print(
                "Please create a file at ~/.open-ai/open-ai-key with your OpenAI API key."
            )
            return
        except Exception as e:
            print(f"An error occurred while reading the API key file: {e}")
            return

        client = OpenAI(api_key=api_key)

        primer_prompt = f"""I want you to be an engineering manager coach. Someone like Claire Hughes Johnson, author of \"Scaling People: Tactics for Management and Company Building\", or  Patrick Lencioni author of \"five dysfunctions of a team\". Reply is australian english.
        I am giving writing a performance review for a {self.level} {self.role}. I have rated {self.pronouns[1]} skills on the basis of: over performing; meeting expectations; and under performing. Build me a narrative basis for {self.pronouns[1]} performance review.
        break it into these sections:
        - What are some things they do well?
        - How could they improve?
        - What are their biggest challenges? 

        now, here is the specific rated skills:\n"""

        self.chatgpt_response = submit_prompt(
            client, model, primer_prompt, self.feedback
        )

        self.chatgpt_feedback = self.chatgpt_response.choices[0].message.content


def make_feedback():
    name = "Bob"
    pronouns = ["he", "his"]
    level = "tech lead"

    feedback = PerformanceReviewGenerator(
        name=name,
        pronouns=pronouns,
        role="Machine Learning Engineer",
        level=level,
        get_chatgpt_feedback=True,
    )


if __name__ == "__main__":
    make_feedback()
