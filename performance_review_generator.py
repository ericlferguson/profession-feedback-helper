DESCRIPTION = """
    Produces a performance assessment for an machine learning engineer employee using the Dropbox career framework as a scaffold.
    
    Framework is based on this:
    https://dropbox.github.io/dbx-career-framework/ic2_machine_learning_engineer.html
    
    """

from typing import List
import logging


class FeedbackPillars:
    def __init__(
        self,
        name: str,
        pronouns: List[str],
        role: str,
        level: str,
        get_chatgpt_feedback: bool = False,
    ) -> None:
        """
        Args:
            name (str): Name of the employee
            pronouns (List[str]): List of pronouns for the employee. E.g. ["he", "his"]
            role (str): Role of the employee. Currently only supports "Machine Learning Engineer"
            level (str): Level of the employee. Can be "junior", "intermediate", "senior", or "tech lead"
        """
        self.level = level
        self.role = role
        self.name = name
        self.pronouns = pronouns
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
            "0 means under-performing. "
            "1 means meets expectactions. "
            "2 means over-performing."
        )

        for key_responsibility in self.responsibilities:
            print(f"\n{key_responsibility}")
            for key_behaviors in self.responsibilities[key_responsibility]:
                print(f"\t{key_behaviors}")
                for key_behavior in self.responsibilities[key_responsibility][
                    key_behaviors
                ]:
                    rating = int(input(f"\t\t{key_behavior}\n"))
                    if rating == 0:
                        try:
                            self.feedback_list[key_responsibility].append(key_behavior)
                        except KeyError:
                            self.feedback_list[key_responsibility] = [key_behavior]
                    elif rating == 1:
                        try:
                            self.okay_list[key_responsibility].append(key_behavior)
                        except KeyError:
                            self.okay_list[key_responsibility] = [key_behavior]
                    elif rating == 2:
                        try:
                            self.going_well_list[key_responsibility].append(
                                key_behavior
                            )
                        except KeyError:
                            self.going_well_list[key_responsibility] = [key_behavior]

                    else:
                        pass  # todo: try again for input

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
            else:
                raise NotImplementedError(f"{self.level} level is not implemented!")
        else:
            raise NotImplementedError(f"{self.role} role is not implemented!")

    def make_results(self):
        if self.role == "Machine Learning Engineer":

            if self.level == "junior":
                return {
                    "impact": [
                        f"{self.name} works with {self.pronouns[1]} manager to prioritize tasks that add the most value and deliver high-quality results for my customer.",
                        f"{self.name} effectively participates in the core processes of my team (planning, on-call rotations, bug triage, metrics review, etc.)",
                    ],
                    "ownership": [
                        f"{self.name} follows through on {self.pronouns[1]} commitments, takes responsibility for {self.pronouns[1]} work, and delivers on time.",
                        f"{self.name} owns {self.pronouns[1]} failures and learns from them.",
                        f"{self.name} asks questions to clarify expectations.",
                    ],
                    "decision making": [
                        f"{self.name} escalates to {self.pronouns[1]} manager when they get stuck and reflect on ways that they can improve from their mistakes."
                    ],
                }
            elif self.level == "intermediate":
                return {
                    "impact": [
                        f"{self.name} acts with urgency and delivers high-quality work that will add the most value.",
                        f"{self.name} works with {self.pronouns[1]} manager to direct {self.pronouns[1]} focus so {self.pronouns[1]} work advances {self.pronouns[1]} team's goals.",
                        f"{self.name} prioritises the right things and doesn't over-complicate {self.pronouns[1]} work. When necessary, {self.pronouns[0]} proposes appropriate scope adjustments.",
                        f"{self.name} effectively participates in the core processes of {self.pronouns[1]} team, including recommending and implementing process improvements.",
                    ],
                    "ownership": [
                        f"{self.name} follows through on {self.pronouns[1]} commitments, takes responsibility for {self.pronouns[1]} work, and delivers on time.",
                        f"{self.name} proactively identifies and advocate for opportunities to improve the current state of projects.",
                        f"{self.name} owns {self.pronouns[1]} failures and learns from them.",
                        f"{self.name} thinks a step or two ahead in {self.pronouns[1]} work, solve the right problems before they become bigger problems, and problem-solve with {self.pronouns[1]} manager when {self.pronouns[0]} is stuck.",
                    ],
                    "decision making": [
                        f"{self.name} identifies and gathers input from others and considers customer needs to make informed and timely decisions."
                    ],
                }
            elif self.level == "senior":
                return {
                    "impact": [
                        f"{self.name} delivers some of {self.pronouns[1]} team's goals on time and with a high standard of quality.",
                        f"{self.name} understands {self.pronouns[1]} customers, the business's goals, and {self.pronouns[1]} team's goals. {self.pronouns[0]} ensures {self.pronouns[1]} work will have the greatest customer impact.",
                        f"{self.name} can identify when {self.pronouns[1]} results aren't moving the needle for our business/team goals or serving the needs of customers in a meaningful way and works with {self.pronouns[1]} manager to redirect {self.pronouns[1]} focus.",
                        f"{self.name} gets work to a simple place by focusing on the heart of the problem and prioritizing the right things.",
                    ],
                    "ownership": [
                        f"{self.name} proactively identifies new opportunities and advocates for and implements improvements to the current state of projects.",
                        f"{self.name} takes responsibility for {self.pronouns[1]} decisions and any mistakes on {self.pronouns[1]} project and takes action to prevent them in the future. {self.pronouns[0]} embraces and shares the learnings with others.",
                        f"When {self.name} encounters barriers, {self.pronouns[0]} unblocks {self.pronouns[1]}self and {self.pronouns[1]} team by proactively assessing and eliminating the root cause.",
                        f"{self.name} responds with urgency to operational issues (e.g., SEVs), owning resolution within {self.pronouns[1]} sphere of responsibility.",
                        f"{self.name} actively seeks out and eliminates sources of toil on the team and helps reduce the impact of KTLO and SEVs.",
                        f"{self.name} is unafraid of declaring a SEV when needed.",
                        f"{self.name} proactively creates and/or updates playbooks for components {self.pronouns[0]} owns.",
                    ],
                    "decision making": [
                        f"{self.name} makes informed decisions by consulting the right stakeholders and balancing details with the big picture. {self.pronouns[0]} executes against the spirit, and not just the letter, of the requirements.",
                        f"{self.name} understands the implications of {self.pronouns[1]} decisions and adjusts {self.pronouns[1]} approach based on the impact and risk in the short and long-term.",
                        f"{self.name} makes timely decisions and doesn't cut corners that would compromise {self.pronouns[1]} customer's trust.",
                        f"When possible, {self.pronouns[0]} leverages customer insights/data to inform decisions, balancing value for the customer with other business goals.",
                        f"{self.name} escalates to {self.pronouns[1]} manager when {self.pronouns[0]} needs help with a decision about {self.pronouns[1]} deliverables or priorities.",
                    ],
                }
            elif self.level == "tech lead":
                return {
                    "impact": [
                        f"{self.name} deliver many of {self.pronouns[1]} team's goals on time and with a high standard of quality.",
                        f"{self.name}'s understanding of the business context and {self.pronouns[1]} team's goals enable the greatest customer impact and allows independent technical decisions in the face of open-ended requirements.",
                        f"{self.name} can identify when {self.pronouns[1]} results aren't moving the needle for our business/team goals or serving the needs of customers in a meaningful way and works with {self.pronouns[1]} manager to redirect {self.pronouns[1]} focus",
                        f"{self.name} get work to a simple place by focusing on the heart of the problem and prioritizing the right things",
                        f"{self.name} improves how {self.pronouns[1]} team measures and communicates customer impact",
                    ],
                    "ownership": [
                        f"{self.name} proactively identifies new opportunities and advocate for and implement improvements to the current state of projects — potentially having broader business impact across teams or products.",
                        f"{self.name} takes responsibility for {self.pronouns[1]} decisions and failures on {self.pronouns[1]} projects and take action to prevent them in the future. {self.name} embraces and share the learnings from those failures.",
                        f"When {self.name} encounter barriers, {self.pronouns[0]} unblocks {HIS}self and {self.pronouns[1]} team by proactively assessing and eliminating the root cause, and focusing on the solutions.",
                        f"{self.name} responds with urgency to operational issues, owning resolution within my sphere of responsibility.",
                        f"{self.name} actively seeks out and eliminate sources of toil on the team and help improve developer velocity.",
                        f"{self.name} proactively creates and update playbooks for processes {self.pronouns[0]} owns.",
                    ],
                    "decision making": [
                        f"{self.name} makes informed decisions by having productive debates with the right stakeholders, seeking diverse perspectives, balancing details with the big picture, and optimizing for the company.",
                        f"{self.name} understands the implications of {self.pronouns[1]} decisions and adjusts {self.pronouns[1]} approach based on the impact and risk (e.g., choosing a more iterative approach based on the degree of uncertainty with respect to product fit, while maintaining a view of the long-term arc needed to accomplish business goals).",
                        f"{self.name} leverages insights about customers to inform decisions, balancing value for the customer with other business goals.",
                        f"{self.name} makes timely decisions and doesn't cut corners that would compromise {self.pronouns[1]} customer's trust.",
                    ],
                }
            else:
                raise NotImplementedError(f"{self.level} level is not implemented!")
        else:
            raise NotImplementedError(f"{self.role} role is not implemented!")

    def make_direction(self):
        if self.role == "Machine Learning Engineer":

            if self.level == "junior":
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
                        f"{self.name} generates excitement for {HIS}/the team's strategy.",
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
                        f"{self.name} open to and act upon feedback from {self.pronouns[1]} manager and peers.",
                        f"{self.name} is self-aware about {self.pronouns[1]} strengths and areas for development.",
                        f"{self.name} drives discussions with {self.pronouns[1]} manager about aspirational goals and seeks out opportunities to learn and grow.",
                    ],
                    "team development": [
                        f"{self.name} models integrity and a high standard of excellence for {self.pronouns[1]} work.",
                        f"{self.name} is learning to interview and assess candidates to help us build a diverse and talented team. {self.pronouns[0]} consistently provides timely, details, and evidence-based inteview feedback.",
                        f"{self.name} offers honest feedback that is delivered with empathy to help others learn and grow.",
                    ],
                }

            elif self.level == "intermediate":
                return {
                    "personal growth": [
                        f"{self.name} proactively asks for feedback from those {self.pronouns[0]} works with and identifies ways to act upon it.",
                        f"{self.name} has self-awareness about {self.pronouns[1]} strengths and areas for development.",
                        f"{self.name} drives discussions with {self.pronouns[1]} manager about aspirational goals and seeks out opportunities to learn and grow.",
                    ],
                    "hiring": [
                        f"{self.name} contributes to interviewing and assessing candidates to help us build a diverse and talented team. {self.pronouns[0]} is calibrated and consistently performs high-signal interviews.",
                        f"{self.name} is able to represent {self.pronouns[1]} team's initiatives and goals to candidates in a compelling way.",
                    ],
                    "talent development": [
                        f"{self.name} models integrity and a high standard of excellence for {self.pronouns[1]} work.",
                        f"{self.name} helps the more junior members of {self.pronouns[1]} team, hosts interns, or is a residency mentor.",
                        f"{self.name} offers honest feedback that is delivered with empathy to help others learn and grow.",
                    ],
                }
            elif self.level == "senior":
                return {
                    "personal growth": [
                        f"{self.name} proactively asks for feedback from {self.pronouns[1]} manager, team, and cross-functional stakeholders and identifies ways to act upon it.",
                        f"{self.name} has self-awareness about {self.pronouns[1]} strengths and works on {self.pronouns[1]} development areas.",
                        f"{self.name} connects with others with empathy and understanding.",
                        f"{self.name} drives discussions with {self.pronouns[1]} manager about aspirational goals and seeks out opportunities to learn and grow (e.g., PGP, Dropbox-offered training, leveraging perks allowance etc.).",
                    ],
                    "team development": [
                        f"{self.name} models integrity and a high standard of excellence for {self.pronouns[1]} work, leveraging this to influence and establish best practices.",
                        f"{self.name} supports the growth of {self.pronouns[1]} teammates by taking into account their unique skills, strengths, backgrounds, and working styles.",
                        f"{self.name} actively looks for opportunities to mentor new hires, interns, and apprentices.",
                        f"{self.name} solicits and offers honest and constructive feedback that is delivered with empathy to help others learn and grow.",
                        f"{self.name} actively contributes to interviewing and assessing candidates to help us build a diverse and talented team by conducting more advanced domain-specific and leveling interviews.",
                        f"{self.name} is able to represent {self.pronouns[1]} team's initiatives and goals to candidates in a compelling way.",
                    ],
                }
            elif self.level == "tech lead":
                return {
                    "personal growth": [
                        f"{self.name} proactively asks for feedback from {self.pronouns[1]} manager, team, and cross-functional stakeholders. {self.pronouns[0]} knows {self.pronouns[1]} strengths and identifies ways to take actions on {self.pronouns[1]} development areas.",
                        f"{self.name} has self-awareness and connects with others with empathy.",
                        f"{self.name} drives discussions with {self.pronouns[1]} manager about aspirational goals and seeks out opportunities to learn and grow.",
                    ],
                    "team development": [
                        f"{self.name} models integrity and a high standard of excellence for {self.pronouns[1]} work. {self.pronouns[0]} leverages this to set and hold the bar for quality and best practices for {self.pronouns[1]} team (e.g., via code and design reviews).",
                        f"{self.name} identifies and supports areas of growth for {self.pronouns[1]} teammates that take into account their unique skills, strengths, backgrounds, and working styles.",
                        f"{self.name} solicits and offers honest, constructive, direct, and actionable feedback that is delivered with empathy to help others learn and grow into the next level.",
                        f"{self.name} actively contributes to interviewing and gains the trust of candidates, representing Abyss's mission, strategy, and culture throughout the interview process.",
                        f"{self.name} is able to represent {self.pronouns[1]} team's technical challenges to potential candidates in a compelling way (e.g., 1:1 sell chats, blog posts, public speaking).",
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
                        f"{self.name} can effectively collaborate and adopt necesary tools and software packages used by {self.pronouns[1]} team.",
                        f"{self.name} work with {self.pronouns[1]} manager to engage with productive conflict and help resolve it with empathy and cooperation in mind.",
                        f"{self.name} promotes and role models organisation's core values.",
                    ],
                    "organisational health": [
                        f"{self.name} contributes to a positive sense of community on the team (e.g., engages in team lunches, team offsites, and other group activities, helps with new-hire on-boarding).",
                        f"{self.name} listens to different perspectives and {self.pronouns[0]} cuts biases from {self.pronouns[1]} words and actions.",
                    ],
                    "communication": [
                        f"{self.name} writes and speaks clearly.",
                        f"{self.name} listens to understand others and asks clarifying questions.",
                        f"{self.name} shares relevant information on {self.pronouns[1]} projects to {self.pronouns[1]} manager, team, and customers.",
                    ],
                }
            elif self.level == "intermediate":
                return {
                    "collaboration": [
                        f"{self.name} can effectively collaborate to get work done.",
                        f"{self.name} work with {self.pronouns[1]} manager to manage conflict with empathy and cooperation in mind.",
                    ],
                    "organisational health": [
                        f"{self.name} contributes to a positive sense of community on the team (e.g., engages in team lunches, team offsites, and other group activities, helps with new-hire on-boarding).",
                        f"{self.name} listens to different perspectives and {self.pronouns[0]} cuts biases from {self.pronouns[1]} words and actions.",
                    ],
                    "communication": [
                        f"{self.name} writes and speaks clearly.",
                        f"{self.name} listens to understand others and asks clarifying questions.",
                        f"{self.name} shares relevant information on {self.pronouns[1]} projects to {self.pronouns[1]} manager, team, and customers.",
                    ],
                }
            elif self.level == "senior":
                return {
                    "collaboration": [
                        f"{self.name} builds relationships across teams and helps get to positive outcomes.",
                        f"{self.name} engages in productive conflict with thoughtful questioning and has the courage to state {self.pronouns[1]} point of view.",
                        f"{self.name} proactively communicates and coordinates {self.pronouns[1]} team's requirements with other groups and teams in engineering.",
                        f"{self.name} is capable of working with cross-functional stakeholders to identify technical blind spots and clarify ambiguity in their ideas.",
                        f"{self.name} avoids blame and focuses on solving the right problems, disagreeing and committing when necessary to move decisions forward.",
                        f"{self.name} promotes and role models Abyss core values.",
                    ],
                    "organizational health": [
                        f"{self.name} contributes to a positive sense of community on the team (e.g., engage in team lunches, team offsites, and other group activities, help with new-hire onboarding).",
                        f"{self.name} listens to different perspectives and cuts biases from {self.pronouns[1]} words and actions.",
                        f"{self.name} helps foster effective communication across the team and promotes an inclusive meeting culture.",
                        f"{self.name} practices the Abyss Diversity Commitments on a regular basis.",
                        f"{self.name} champions good virtual first practices that help {self.pronouns[1]} team collaborate effectively.",
                        f"{self.name} helps shape the Abyss engineering culture through {self.pronouns[1]} involvement with activities outside of {self.pronouns[1]} team (e.g., presenting tech talks, participating in Eng RFCs, creating interview questions, planning hackweek).",
                    ],
                    "communication": [
                        f"{self.name} tailors {self.pronouns[1]} message to {self.pronouns[1]} audience, presenting it clearly and concisely at the right altitude.",
                        f"{self.name} proactively shares information so the right people are informed and aligned.",
                        f"{self.name} sets the right expectation with {self.pronouns[1]} manager to balance {self.pronouns[1]} work and mentorship requirements.",
                        f"If there is a significant issue not being addressed, {self.name} initiates a crucial conversation even when uncomfortable.",
                    ],
                }

            if self.level == "tech lead":
                return {
                    "collaboration": [
                        f"{self.name} promotes and role models Abyss core values, leading by example.",
                        f"{self.name} builds relationships and drives coordination across teams and disciplines, helping to achieve positive outcomes.",
                        f"{self.name} proactively communicates and coordinates {self.pronouns[1]} team's requirements with other groups and teams in engineering.",
                        f"{self.name} is effective at working with cross-functional stakeholders to identify technical blind spots and clarify ambiguity in their ideas.",
                        f"{self.name} engages in productive conflict with thoughtful questioning and has the courage to state {self.pronouns[1]} point of view.",
                        f"{self.name} avoids blame and focuses on solving the right problems, and is willing to disagree and commit when necessary to move decisions forward.",
                    ],
                    "organizational health": [
                        f"Working with {self.pronouns[1]} manager, {self.name} leverages the unique strengths and skills of the members of {self.pronouns[1]} team and helps identify talent gaps required for team success.",
                        f"{self.name} enables others to bring their authentic selves to work and contributes to building community at Abyss.",
                        f"{self.name} ensures diverse perspectives are included, leveraging inclusive meeting practices.",
                        f"{self.name} practices the Abyss Diversity Commitments on a regular basis.",
                        f"{self.name} champions good virtual-first practices that help {self.pronouns[1]} team collaborate effectively.",
                        f"{self.name} helps shape the Abyss engineering culture through {self.pronouns[1]} involvement with activities outside of {self.pronouns[1]} team (e.g., presenting tech talks, participating in Eng RFCs, creating interview questions, planning hackweek).",
                    ],
                    "communication": [
                        f"{self.name} communicates with clarity, brevity, focus, and tailors {self.pronouns[1]} message to {self.pronouns[1]} audience, presenting it at the right altitude.",
                        f"{self.name} proactively shares information so that relevant stakeholders are informed and aligned.",
                        f"{self.name} is effective in holding crucial conversations even when uncomfortable.",
                        f"{self.name} influences stakeholders across a variety of audiences.",
                        f"{self.name} seeks to listen and understand others.",
                    ],
                    "culture leader": [
                        f"{self.name} acts as a partner to {self.pronouns[1]} manager in setting the cultural tone for the team. {self.pronouns[0]} supports an environment of psychological safety where all Abyssians are included and heard to support connection, empathy, and productive conflict where dissenting opinions are valued and addressed.",
                        f"{self.name} helps {self.pronouns[1]} team network and build relationships across Abyss, creating connection and inclusion across {self.pronouns[1]} team and with other teams.",
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
                    "ML fluency": [
                        f"{self.name} works on ML models by adapting existing tutorials and examples for new purposes.",
                        f"{self.name} can analyze and present datasets or results of experiments with simple methods.",
                    ],
                    "ML design": [
                        f"{self.name} applies existing tools and libraries from my team to advance {self.pronouns[1]} projects.",
                        f"{self.name} understands the reasoning behind {self.pronouns[1]} team's design decisions to verify and debug implementations of the designs.",
                    ],
                    "code fluency": [
                        f"{self.name} translates ideas into clear code, written to be read as well as executed.",
                        f"{self.name} participates in code reviews and raises questions to help {self.pronouns[1]} learn the codebase and technologies relevant to {self.pronouns[1]} projects.",
                        f"{self.name}'s code is free of glaring errors - bugs are in edge cases or design, not mainline paths - and is well documented and well tested with appropriate use of manual vs automated tests.",
                        f"{self.name} is capable of reading and navigating through functions and modules that {self.pronouns[0]} did write.",
                        f"{self.name} is learning to tackle code tasks with high throughput while maintaining and appropriately high quality; {self.pronouns[0]} optmizes for either speed or quality, depending on the exlicitly stated needs of the project {self.pronouns[0]} is working on.",
                    ],
                }
            if self.level == "intermediate":
                return {
                    "ML fluency": [
                        f"{self.name} works effectively with the ML tools and software packages used by {self.pronouns[1]} team.",
                        f"{self.name} understands the ML algorithms and techniques used in {self.pronouns[1]} area, and can adapt them projects as needed.",
                        f"{self.name} can analyze and present datasets or results of experiments with statistical methods and/or visualization techniques {self.pronouns[1]} team may specify.",
                    ],
                    "ML design": [
                        f"{self.name} is able to build a model from standard components in order to solve a given computational task.",
                        f"{self.name} understands the stages of ML development lifecycle and their interactions within {self.pronouns[1]} projects, and make adjustments to existing designs for any stage when necessary.",
                        f"{self.name} understand the reasoning behind {self.pronouns[1]} team's design decisions in order to implement the designs.",
                    ],
                    "code fluency": [
                        f"{self.name} translates ideas into clear code, written to be read as well as executed.",
                        f"{self.name}'s code is free of glaring errors - bugs are in edge cases or design, not mainline paths - and is well documented and well tested with appropriate use of manual vs automated tests.",
                        f"{self.name} is able to read and navigate through a large code base and effectively debug others' code.",
                        f"{self.name} addresses code tasks with both high throughput and appropriately high quality for the stage of project {self.pronouns[0]} is working on.",
                    ],
                }
            elif self.level == "senior":
                return {
                    "ML fluency": [
                        f"{self.name} is familiar with a range of ML techniques (e.g., deep learning, optimization, regression, ensembles, tree-based methods, dimensionality reduction, Bayesian modeling, etc.), areas (CV, NLP, RL, etc.), and tools (sklearn, pytorch, tensorflow, etc.) and selects the right solution for {self.pronouns[1]} project.",
                        f"{self.name} maintains awareness of the state of the art and can select an appropriate algorithm, tool, or technique for a given problem.",
                        f"{self.name} can analyze and present datasets or results of experiments while choosing the appropriate statistical methods and visualization techniques.",
                    ],
                    "ML design": [
                        f"{self.name} can translate a business problem into a spec for a computational task such as classification, ranking, or generation.",
                        f"{self.name} is proficient in the ML development lifecycle and can design each stage according to the needs of the project.",
                        f"{self.name} defines and tracks offline and online metrics in service of business objectives.",
                        f"{self.name} prepares and conducts experiments, analyzes the results, and adapts {self.pronouns[1]} strategy to reflect significant findings.",
                    ],
                    "Code fluency": [
                        f"{self.name} writes code that captures the essential nature of the solution and is appropriately flexible, reusable, efficient, and adaptable to changing requirements.",
                        f"{self.name} ensures high code quality in code reviews and adopts approaches (e.g., set up best practices and coding standards, help resolve differences of opinions) to foster an effective/collaborative code review culture.",
                        f"{self.name} has a strong awareness of the ecosystem of tools and libraries supporting {self.pronouns[1]} primary programming language, development environment, and ML frameworks (like TensorFlow, Keras, PyTorch, etc.) and a strong grasp of the idioms and patterns of {self.pronouns[1]} language.",
                        f"{self.name} builds tools and produces technical documentation to improve developer efficiency and drive alignment within {self.pronouns[1]} team.",
                    ],
                    "Software design": [
                        f"{self.name} is able to independently design software components in well-scoped scenarios, with simplicity and maintenance as key considerations. {self.pronouns[1]} components are testable, debuggable, and have logical APIs that are not easily misused.",
                        f"{self.name} knows when to make significant refactors and when it's better to leave things as-is.",
                        f"{self.name} has a strong grasp of the libraries, platforms, and systems that {self.pronouns[0]} relies on, allowing them to apply them expertly.",
                    ],
                    "Business acumen": [
                        f"{self.name} engages in listening sessions (All Hands, Quarterly Business Updates, etc.) to increase {self.pronouns[1]} learning and guide {self.pronouns[1]} work/priorities.",
                        f"{self.name} has a working knowledge of Abyss's org/team structure and how teams work together across Abyss and is able to independently work with partner engineering teams to unblock code reviews and engineering designs.",
                    ],
                }
            if self.level == "tech lead":
                return {
                    "ML design": [
                        f"{self.name} formulates business objectives as computational tasks using the right approach for each objective.",
                        f"{self.name} provides critical feedback to other members of {self.pronouns[1]} team throughout the lifecycle* of an ML project.",
                        f"{self.name} critiques existing metrics and defines new offline and online metrics that stay valid throughout the model's lifetime.",
                        f"{self.name} defines an experimentation strategy and adapts {self.pronouns[1]} team's roadmap to reflect significant findings.",
                    ],
                    "code fluency": [
                        f"The expectations for L3 code fluency are still applicable here.",
                        f"{self.name} can find ways to improve developer efficiency as measured by cycle time, ramp-up time, or other similar measurements.",
                        f"{self.name} preemptively identifies and resolves technical risks before they jeopardize the project. {self.pronouns[0]} resolves cross-team dependencies earlier to ensure the successful execution of the project.",
                        f"{self.name} avoids re-inventing the wheel by leveraging other Abyss solutions or off-the-shelf solutions with the possible trade-off in mind. {self.pronouns[0]} writes libraries and modules that can be extended and adopted by other teams at Abyss to increase their efficiency.",
                    ],
                    "software design": [
                        f"{self.name} is able to give quality feedback on designs written by other members of {self.pronouns[1]} team, asking probing, insightful questions that solidify choices and surface erroneous assumptions.",
                        f"{self.name} effectively and quickly debugs cross-module issues and may intuit where bugs might lie due to {self.pronouns[1]} deep knowledge of the libraries, platforms, and systems that {self.pronouns[1]} software relies on.",
                    ],
                    "architecture design": [
                        f"{self.name} is able to create coherent designs with multiple components interacting across API or system boundaries, ensuring that bugs do not creep in at the boundaries due to mismatches in expectations of what is technically feasible.",
                        f"{self.name} is capable of rolling out a component or major feature reliably, including appropriate monitoring, paging, etc. {self.pronouns[0]} ensures that failure domains are understood and characterized appropriately before a large-scale rollout. For early-stage products, {self.pronouns[0]} is able to roll out with an eye toward achieving learning goals untainted by poor quality.",
                        f"{self.name} designs clear success metrics and consistently achieves those metrics post-launch throughout the lifetime of the system or feature. For early-stage products, the success metrics may be oriented around learning goals rather than usage goals, given the inherent unpredictability of achieving product/market fit.",
                    ],
                    "technical strategy": [
                        f"{self.name} is responsible for aligning the software and data models in {self.pronouns[1]} team to the overall technical and data strategy, making tradeoffs where appropriate in consultation with staff engineers.",
                    ],
                    "business acumen": [
                        f"{self.name} engages in listening sessions (All Hands, Quarterly Business Updates, etc.) to increase {self.pronouns[1]} learning and guide {self.pronouns[1]} work/priorities.",
                        f"{self.name} has a working knowledge of Abyss's org/team structure and how teams work together across Abyss, and is able to help {self.pronouns[1]} team effectively collaborate with other teams across the organization.",
                    ],
                }
            else:
                raise NotImplementedError(f"{self.level} level is not implemented!")
        else:
            raise NotImplementedError(f"{self.role} role is not implemented!")

    def give_feedback(self):
        feedback = ""

        feedback += "\n\nOVER PERFORMING:"
        for key_responsibility in self.going_well_list:
            feedback += f"\n{key_responsibility}"
            for comment in self.going_well_list[key_responsibility]:
                feedback += f"- {comment}"

        feedback += "\n\nMEETS EXPECTATIONS:"
        for key_responsibility in self.okay_list:
            feedback += f"\n{key_responsibility}"
            for comment in self.okay_list[key_responsibility]:
                feedback += f"- {comment}"

        feedback += "\n\nGIVE FEEDBACK:"
        for key_responsibility in self.feedback_list:
            feedback += f"\n{key_responsibility}"
            for comment in self.feedback_list[key_responsibility]:
                feedback += f"- {comment}"

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

        primer_prompt = f"""I want you to be an engineering manager coach. Someone like Claire Hughes Johnson, author of \"Scaling People: Tactics for Management and Company Building\", or  Patrick Lencioni author of \"five dysfunctions of a team\".
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
    name = "Amy"
    pronouns = ["she", "her"]
    level = "intermediate"

    feedback = FeedbackPillars(
        name=name,
        pronouns=pronouns,
        role="Machine Learning Engineer",
        level=level,
        get_chatgpt_feedback=True,
    )


if __name__ == "__main__":
    make_feedback()
