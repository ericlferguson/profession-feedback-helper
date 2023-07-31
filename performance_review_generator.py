DESCRIPTION = """
    Produces a performance assessment for an machine learning engineer employee using the Dropbox career framework as a scaffold.
    
    Framework is based on this:
    https://dropbox.github.io/dbx-career-framework/ic2_machine_learning_engineer.html
    
    """

NAME = "XXX"
HE = "she"
HIS = "her"
LEVEL = "senior"  # junior, intermediate, senior, tech lead


class FeedbackPillars:
    def __init__(self, level) -> None:
        self.level = level
        self.responsibilities = {
            "overview": self.make_overview(),
            "results": self.make_results(),
            "direction": self.make_direction(),
            "talent": self.make_talent(),
            "culture": self.make_culture(),
            "craft": self.make_craft(),
        }

    def make_overview(self):
        if self.level == "junior":
            return {
                "scope": [
                    f"{NAME} on defined tasks and contribute to solving problems with defined solutions.",
                ],
                "collaborative reach": [
                    f"{NAME} works primarily within the scope of {HIS} team with high level guidance from {HIS} manager/TL."
                ],
                "impact levers": [
                    f"Craft - {NAME} primarily focuses on improving {HIS} craft as an engineer",
                ],
            }
        elif self.level == "intermediate":
            return {
                "scope": [
                    f"{NAME} executes on defined projects to achieve team-level goals.",
                    f"{NAME} independently defines the right solutions or uses existing approaches to solve defined problems.",
                ],
                "collaborative reach": [
                    f"{NAME} works primarily within the scope of {HIS} team with high level guidance from {HIS} manager/TL."
                ],
                "impact levers": [
                    f"Craft - {NAME} is increasingly mastering {HIS} craft and leverage it for higher impact (e.g. software design)",
                    f"Mentorship - {NAME} may mentor new hires, interns, or more junior engineers.",
                ],
            }
        elif self.level == "senior":
            return {
                "scope": [
                    f"{NAME} owns and delivers projects in service of quarterly goals on the team.",
                    f"{NAME} independently identifies the right solutions to solve ambiguous, open-ended problems.",
                ],
                "collaborative reach": [
                    f"{NAME} works primarily with {HIS} direct team and cross-functional partners while driving cross-team collaboration for {HIS} project."
                ],
                "impact levers": [
                    "Project Leadership - {NAME} defines and delivers well-scoped milestones for a project. {HE} may be a technical lead for projects on {HIS} team.",
                    "Product Expertise - {NAME} actively keeps customer needs in mind and leverages input from product stakeholders as available to determine the right technical solutions to deliver customer value quickly.",
                    "Mentorship - {NAME} actively levels up less-experienced members of {HIS} team by helping them with their craft, providing guidance, and setting a good example.",
                ],
            }
        elif self.level == "tech lead":
            return {
                "scope": [
                    f"{NAME} owns and delivers semi-annual/annual goals for {HIS} team.",
                    f"{NAME} is an expert at identifying the right solutions to solve ambiguous, open-ended problems that require tough prioritization.",
                    f"{NAME} defines technical solutions or efficient operational processes that level up {HIS} team.",
                ],
                "collaborative reach": [
                    f"{NAME} is a strong leader for my team with {HIS} impact beginning to extend outside {HIS} team.",
                    f"{NAME} increasingly optimizes beyond just {HIS} team by driving cross-team or cross-discipline initiatives.",
                ],
                "impact levers": [
                    f"Technical Strategy - {NAME} plays a key role in setting medium-to-long term strategy for business-impacting projects.",
                    f"Project Leadership - {NAME} autonomously defines and deliver technical roadmaps of larger projects, often involving cross-team dependencies.",
                    f"Product Expertise - {NAME} actively keeps customer needs in mind and leverage input from product stakeholders as available to determine the right technical solutions to deliver customer value quickly.",
                    f"Mentorship - {NAME} actively levels-up less-experienced members of {HIS} team by helping them with their craft, providing guidance, and setting a good example.",
                ],
            }
        else:
            raise NotImplementedError(f"{self.level} level is not implemented!")

    def make_results(self):
        if self.level == "junior":
            return {
                "impact": [
                    f"{NAME} works with {HIS} manager to prioritize tasks that add the most value and deliver high-quality results for my customer.",
                    f"{NAME} effectively participates in the core processes of my team (planning, on-call rotations, bug triage, metrics review, etc.)",
                ],
                "ownership": [
                    f"{NAME} follows through on {HIS} commitments, takes responsibility for {HIS} work, and delivers on time.",
                    f"{NAME} owns {HIS} failures and learns from them.",
                    f"{NAME} asks questions to clarify expectations.",
                ],
                "decision making": [
                    f"{NAME} escalates to {HIS} manager when they get stuck and reflect on ways that they can improve from their mistakes."
                ],
            }
        elif self.level == "intermediate":
            return {
                "impact": [
                    f"{NAME} acts with urgency and delivers high-quality work that will add the most value.",
                    f"{NAME} works with {HIS} manager to direct {HIS} focus so {HIS} work advances {HIS} team's goals.",
                    f"{NAME} prioritises the right things and doesn't over-complicate {HIS} work. When necessary, {HE} proposes appropriate scope adjustments.",
                    f"{NAME} effectively participates in the core processes of {HIS} team, including recommending and implementing process improvements.",
                ],
                "ownership": [
                    f"{NAME} follows through on {HIS} commitments, takes responsibility for {HIS} work, and delivers on time.",
                    f"{NAME} proactively identifies and advocate for opportunities to improve the current state of projects.",
                    f"{NAME} owns {HIS} failures and learns from them.",
                    f"{NAME} thinks a step or two ahead in {HIS} work, solve the right problems before they become bigger problems, and problem-solve with {HIS} manager when {HE} is stuck.",
                ],
                "decision making": [
                    f"{NAME} identifies and gathers input from others and considers customer needs to make informed and timely decisions."
                ],
            }
        elif self.level == "senior":
            return {
                "impact": [
                    f"{NAME} delivers some of {HIS} team's goals on time and with a high standard of quality.",
                    f"{NAME} understands {HIS} customers, the business's goals, and {HIS} team's goals. {HE} ensures {HIS} work will have the greatest customer impact.",
                    f"{NAME} can identify when {HIS} results aren't moving the needle for our business/team goals or serving the needs of customers in a meaningful way and works with {HIS} manager to redirect {HIS} focus.",
                    f"{NAME} gets work to a simple place by focusing on the heart of the problem and prioritizing the right things.",
                ],
                "ownership": [
                    f"{NAME} proactively identifies new opportunities and advocates for and implements improvements to the current state of projects.",
                    f"{NAME} takes responsibility for {HIS} decisions and any mistakes on {HIS} project and takes action to prevent them in the future. {HE} embraces and shares the learnings with others.",
                    f"When {NAME} encounters barriers, {HE} unblocks {HIS}self and {HIS} team by proactively assessing and eliminating the root cause.",
                    f"{NAME} responds with urgency to operational issues (e.g., SEVs), owning resolution within {HIS} sphere of responsibility.",
                    f"{NAME} actively seeks out and eliminates sources of toil on the team and helps reduce the impact of KTLO and SEVs.",
                    f"{NAME} is unafraid of declaring a SEV when needed.",
                    f"{NAME} proactively creates and/or updates playbooks for components {HE} owns.",
                ],
                "decision making": [
                    f"{NAME} makes informed decisions by consulting the right stakeholders and balancing details with the big picture. {HE} executes against the spirit, and not just the letter, of the requirements.",
                    f"{NAME} understands the implications of {HIS} decisions and adjusts {HIS} approach based on the impact and risk in the short and long-term.",
                    f"{NAME} makes timely decisions and doesn't cut corners that would compromise {HIS} customer's trust.",
                    f"When possible, {HE} leverages customer insights/data to inform decisions, balancing value for the customer with other business goals.",
                    f"{NAME} escalates to {HIS} manager when {HE} needs help with a decision about {HIS} deliverables or priorities.",
                ],
            }
        elif self.level == "tech lead":
            return {
                "impact": [
                    f"{NAME} deliver many of {HIS} team's goals on time and with a high standard of quality.",
                    f"{NAME}'s understanding of the business context and {HIS} team's goals enable the greatest customer impact and allows independent technical decisions in the face of open-ended requirements.",
                    f"{NAME} can identify when {HIS} results aren't moving the needle for our business/team goals or serving the needs of customers in a meaningful way and works with {HIS} manager to redirect {HIS} focus",
                    f"{NAME} get work to a simple place by focusing on the heart of the problem and prioritizing the right things",
                    f"{NAME} improves how {HIS} team measures and communicates customer impact",
                ],
                "ownership": [
                    f"{NAME} proactively identifies new opportunities and advocate for and implement improvements to the current state of projects — potentially having broader business impact across teams or products.",
                    f"{NAME} takes responsibility for {HIS} decisions and failures on {HIS} projects and take action to prevent them in the future. {NAME} embraces and share the learnings from those failures.",
                    f"When {NAME} encounter barriers, {HE} unblocks {HIS}self and {HIS} team by proactively assessing and eliminating the root cause, and focusing on the solutions.",
                    f"{NAME} responds with urgency to operational issues, owning resolution within my sphere of responsibility.",
                    f"{NAME} actively seeks out and eliminate sources of toil on the team and help improve developer velocity.",
                    f"{NAME} proactively creates and update playbooks for processes {HE} owns.",
                ],
                "decision making": [
                    f"{NAME} makes informed decisions by having productive debates with the right stakeholders, seeking diverse perspectives, balancing details with the big picture, and optimizing for the company.",
                    f"{NAME} understands the implications of {HIS} decisions and adjusts {HIS} approach based on the impact and risk (e.g., choosing a more iterative approach based on the degree of uncertainty with respect to product fit, while maintaining a view of the long-term arc needed to accomplish business goals).",
                    f"{NAME} leverages insights about customers to inform decisions, balancing value for the customer with other business goals.",
                    f"{NAME} makes timely decisions and doesn't cut corners that would compromise {HIS} customer's trust.",
                ],
            }
        else:
            raise NotImplementedError(f"{self.level} level is not implemented!")

    def make_direction(self):
        if self.level == "junior":
            return {
                "agility / innovation": [
                    f"{NAME} shares new ideas and can adapt {HIS} work when circumstances change.",
                ],
            }
        elif self.level == "intermediate":
            return {
                "agility": [
                    f"{NAME} is open to change and enthusiastic about new initiatives.",
                    f"{NAME} works with {HIS} manager to navigate complex and ambiguous situations",
                ],
                "innovation": [
                    f"{NAME} asks questions and contributes to new ideas/approaches.",
                    f"{NAME} experiments with new approaches and share what {HE} has learned.",
                ],
            }
        elif self.level == "senior":
            return {
                "agility": [
                    f"{NAME} embraces change and adapts quickly to it.",
                    f"{NAME} remains resilient through change by staying calm under pressure and taking care of {HIS} well-being.",
                    f"{NAME} navigates ambiguity by focusing on the greater purpose, goals, and desired impact to move forward one step at a time.",
                ],
                "innovation": [
                    f"{NAME} asks questions and contributes to new ideas/approaches.",
                    f"{NAME} has a growth mindset and is comfortable experimenting with new approaches, learning, owning the outcomes, and sharing what {HE} learned.",
                    f"{NAME} works with {HIS} manager to find new ways of utilizing customer feedback to influence our teams' plans.",
                ],
                "strategy": [
                    f"{NAME} works collaboratively with {HIS} manager to set realistic and ambitious short-term goals to deliver customer value quickly, and break them down to smaller projects for my team or myself.",
                    f"{NAME} executes the development roadmap for multi-phase projects, possibly as a project lead.",
                ],
            }

        elif self.level == "tech lead":
            return {
                "agility": [
                    f"{NAME} embraces change and adapts quickly to it.",
                    f"{NAME} remains resilient through change by staying calm under pressure and taking care of {HIS} well-being.",
                    f"{NAME} navigates ambiguity by focusing on the greater purpose, goals, and desired impact to move forward one step at a time.",
                ],
                "innovation": [
                    f"{NAME} has a growth mindset and is comfortable experimenting with new approaches, learning, owning the outcomes, and sharing what {HE} learned.",
                    f"{NAME} sets audacious goals, takes risks, and shares lessons learned.",
                    f"{NAME} is beginning to push boundaries using industry best practices and customer feedback to implement strategies that drive our products, tools, or services forward.",
                ],
                "strategy": [
                    f"{NAME} defines the technical roadmap for impactful multi-phase projects, refining it as the projects progress to deliver customer value quickly, and provides leadership for the people executing on the project.",
                    f"In partnership with {HIS} manager, {NAME} defines {HIS} team's priorities and secures buy-in by engaging stakeholders and aligning with company priorities and customer needs.",
                    f"{NAME} generates excitement for {HIS}/the team's strategy.",
                ],
            }
        else:
            raise NotImplementedError(f"{self.level} level is not implemented!")

    def make_talent(self):
        if self.level == "intermediate":
            return {
                "personal growth": [
                    f"{NAME} proactively asks for feedback from those {HE} works with and identifies ways to act upon it.",
                    f"{NAME} has self-awareness about {HIS} strengths and areas for development.",
                    f"{NAME} drives discussions with {HIS} manager about aspirational goals and seeks out opportunities to learn and grow.",
                ],
                "hiring": [
                    f"{NAME} contributes to interviewing and assessing candidates to help us build a diverse and talented team. {HE} is calibrated and consistently performs high-signal interviews.",
                    f"{NAME} is able to represent {HIS} team's initiatives and goals to candidates in a compelling way.",
                ],
                "talent development": [
                    f"{NAME} models integrity and a high standard of excellence for {HIS} work.",
                    f"{NAME} helps the more junior members of {HIS} team, hosts interns, or is a residency mentor.",
                    f"{NAME} offers honest feedback that is delivered with empathy to help others learn and grow.",
                ],
            }
        elif self.level == "senior":
            return {
                "personal growth": [
                    f"{NAME} proactively asks for feedback from {HIS} manager, team, and cross-functional stakeholders and identifies ways to act upon it.",
                    f"{NAME} has self-awareness about {HIS} strengths and works on {HIS} development areas.",
                    f"{NAME} connects with others with empathy and understanding.",
                    f"{NAME} drives discussions with {HIS} manager about aspirational goals and seeks out opportunities to learn and grow (e.g., PGP, Dropbox-offered training, leveraging perks allowance etc.).",
                ],
                "team development": [
                    f"{NAME} models integrity and a high standard of excellence for {HIS} work, leveraging this to influence and establish best practices.",
                    f"{NAME} supports the growth of {HIS} teammates by taking into account their unique skills, strengths, backgrounds, and working styles.",
                    f"{NAME} actively looks for opportunities to mentor new hires, interns, and apprentices.",
                    f"{NAME} solicits and offers honest and constructive feedback that is delivered with empathy to help others learn and grow.",
                    f"{NAME} actively contributes to interviewing and assessing candidates to help us build a diverse and talented team by conducting more advanced domain-specific and leveling interviews.",
                    f"{NAME} is able to represent {HIS} team’s initiatives and goals to candidates in a compelling way.",
                ],
            }
        if self.level == "tech lead":
            return {
                "personal growth": [
                    f"{NAME} proactively asks for feedback from {HIS} manager, team, and cross-functional stakeholders. {HE} knows {HIS} strengths and identifies ways to take actions on {HIS} development areas.",
                    f"{NAME} has self-awareness and connects with others with empathy.",
                    f"{NAME} drives discussions with {HIS} manager about aspirational goals and seeks out opportunities to learn and grow.",
                ],
                "team development": [
                    f"{NAME} models integrity and a high standard of excellence for {HIS} work. {HE} leverages this to set and hold the bar for quality and best practices for {HIS} team (e.g., via code and design reviews).",
                    f"{NAME} identifies and supports areas of growth for {HIS} teammates that take into account their unique skills, strengths, backgrounds, and working styles.",
                    f"{NAME} solicits and offers honest, constructive, direct, and actionable feedback that is delivered with empathy to help others learn and grow into the next level.",
                    f"{NAME} actively contributes to interviewing and gains the trust of candidates, representing Abyss's mission, strategy, and culture throughout the interview process.",
                    f"{NAME} is able to represent {HIS} team's technical challenges to potential candidates in a compelling way (e.g., 1:1 sell chats, blog posts, public speaking).",
                ],
            }
        else:
            raise NotImplementedError(f"{self.level} level is not implemented!")

    def make_culture(self):
        if self.level == "intermediate":
            return {
                "collaboration": [
                    f"{NAME} can effectively collaborate to get work done.",
                    f"{NAME} work with {HIS} manager to manage conflict with empathy and cooperation in mind.",
                ],
                "organisational health": [
                    f"{NAME} contributes to a positive sense of community on the team (e.g., engages in team lunches, team offsites, and other group activities, helps with new-hire on-boarding).",
                    f"{NAME} listens to different perspectives and {HE} cuts biases from {HIS} words and actions.",
                ],
                "communication": [
                    f"{NAME} writes and speaks clearly.",
                    f"{NAME} listens to understand others and asks clarifying questions.",
                    f"{NAME} shares relevant information on {HIS} projects to {HIS} manager, team, and customers.",
                ],
            }
        elif self.level == "senior":
            return {
                "collaboration": [
                    f"{NAME} builds relationships across teams and helps get to positive outcomes.",
                    f"{NAME} engages in productive conflict with thoughtful questioning and has the courage to state {HIS} point of view.",
                    f"{NAME} proactively communicates and coordinates {HIS} team’s requirements with other groups and teams in engineering.",
                    f"{NAME} is capable of working with cross-functional stakeholders to identify technical blind spots and clarify ambiguity in their ideas.",
                    f"{NAME} avoids blame and focuses on solving the right problems, disagreeing and committing when necessary to move decisions forward.",
                    f"{NAME} promotes and role models Abyss core values.",
                ],
                "organizational health": [
                    f"{NAME} contributes to a positive sense of community on the team (e.g., engage in team lunches, team offsites, and other group activities, help with new-hire onboarding).",
                    f"{NAME} listens to different perspectives and cuts biases from {HIS} words and actions.",
                    f"{NAME} helps foster effective communication across the team and promotes an inclusive meeting culture.",
                    f"{NAME} practices the Abyss Diversity Commitments on a regular basis.",
                    f"{NAME} champions good virtual first practices that help {HIS} team collaborate effectively.",
                    f"{NAME} helps shape the Abyss engineering culture through {HIS} involvement with activities outside of {HIS} team (e.g., presenting tech talks, participating in Eng RFCs, creating interview questions, planning hackweek).",
                ],
                "communication": [
                    f"{NAME} tailors {HIS} message to {HIS} audience, presenting it clearly and concisely at the right altitude.",
                    f"{NAME} proactively shares information so the right people are informed and aligned.",
                    f"{NAME} sets the right expectation with {HIS} manager to balance {HIS} work and mentorship requirements.",
                    f"If there is a significant issue not being addressed, {NAME} initiates a crucial conversation even when uncomfortable.",
                ],
            }

        if self.level == "tech lead":
            return {
                "collaboration": [
                    f"{NAME} promotes and role models Abyss core values, leading by example.",
                    f"{NAME} builds relationships and drives coordination across teams and disciplines, helping to achieve positive outcomes.",
                    f"{NAME} proactively communicates and coordinates {HIS} team's requirements with other groups and teams in engineering.",
                    f"{NAME} is effective at working with cross-functional stakeholders to identify technical blind spots and clarify ambiguity in their ideas.",
                    f"{NAME} engages in productive conflict with thoughtful questioning and has the courage to state {HIS} point of view.",
                    f"{NAME} avoids blame and focuses on solving the right problems, and is willing to disagree and commit when necessary to move decisions forward.",
                ],
                "organizational health": [
                    f"Working with {HIS} manager, {NAME} leverages the unique strengths and skills of the members of {HIS} team and helps identify talent gaps required for team success.",
                    f"{NAME} enables others to bring their authentic selves to work and contributes to building community at Abyss.",
                    f"{NAME} ensures diverse perspectives are included, leveraging inclusive meeting practices.",
                    f"{NAME} practices the Abyss Diversity Commitments on a regular basis.",
                    f"{NAME} champions good virtual-first practices that help {HIS} team collaborate effectively.",
                    f"{NAME} helps shape the Abyss engineering culture through {HIS} involvement with activities outside of {HIS} team (e.g., presenting tech talks, participating in Eng RFCs, creating interview questions, planning hackweek).",
                ],
                "communication": [
                    f"{NAME} communicates with clarity, brevity, focus, and tailors {HIS} message to {HIS} audience, presenting it at the right altitude.",
                    f"{NAME} proactively shares information so that relevant stakeholders are informed and aligned.",
                    f"{NAME} is effective in holding crucial conversations even when uncomfortable.",
                    f"{NAME} influences stakeholders across a variety of audiences.",
                    f"{NAME} seeks to listen and understand others.",
                ],
                "culture leader": [
                    f"{NAME} acts as a partner to {HIS} manager in setting the cultural tone for the team. {HE} supports an environment of psychological safety where all Abyssians are included and heard to support connection, empathy, and productive conflict where dissenting opinions are valued and addressed.",
                    f"{NAME} helps {HIS} team network and build relationships across Abyss, creating connection and inclusion across {HIS} team and with other teams.",
                ],
            }
        else:
            raise NotImplementedError(f"{self.level} level is not implemented!")

    def make_craft(self):
        if self.level == "intermediate":
            return {
                "ML fluency": [
                    f"{NAME} works effectively with the ML tools and software packages used by {HIS} team.",
                    f"{NAME} understands the ML algorithms and techniques used in {HIS} area, and can adapt them projects as needed.",
                    f"{NAME} can analyze and present datasets or results of experiments with statistical methods and/or visualization techniques {HIS} team may specify.",
                ],
                "ML design": [
                    f"{NAME} is able to build a model from standard components in order to solve a given computational task.",
                    f"{NAME} understands the stages of ML development lifecycle and their interactions within {HIS} projects, and make adjustments to existing designs for any stage when necessary.",
                    f"{NAME} understand the reasoning behind {HIS} team's design decisions in order to implement the designs.",
                ],
                "code fluency": [
                    f"{NAME} translates ideas into clear code, written to be read as well as executed.",
                    f"{NAME}'s code is free of glaring errors - bugs are in edge cases or design, not mainline paths - and is well documented and well tested with appropriate use of manual vs automated tests.",
                    f"{NAME} is able to read and navigate through a large code base and effectively debug others' code.",
                    f"{NAME} addresses code tasks with both high throughput and appropriately high quality for the stage of project {HE} is working on.",
                ],
            }
        elif self.level == "senior":
            return {
                "ML fluency": [
                    f"{NAME} is familiar with a range of ML techniques (e.g., deep learning, optimization, regression, ensembles, tree-based methods, dimensionality reduction, Bayesian modeling, etc.), areas (CV, NLP, RL, etc.), and tools (sklearn, pytorch, tensorflow, etc.) and selects the right solution for {HIS} project.",
                    f"{NAME} maintains awareness of the state of the art and can select an appropriate algorithm, tool, or technique for a given problem.",
                    f"{NAME} can analyze and present datasets or results of experiments while choosing the appropriate statistical methods and visualization techniques.",
                ],
                "ML design": [
                    f"{NAME} can translate a business problem into a spec for a computational task such as classification, ranking, or generation.",
                    f"{NAME} is proficient in the ML development lifecycle and can design each stage according to the needs of the project.",
                    f"{NAME} defines and tracks offline and online metrics in service of business objectives.",
                    f"{NAME} prepares and conducts experiments, analyzes the results, and adapts {HIS} strategy to reflect significant findings.",
                ],
                "Code fluency": [
                    f"{NAME} writes code that captures the essential nature of the solution and is appropriately flexible, reusable, efficient, and adaptable to changing requirements.",
                    f"{NAME} ensures high code quality in code reviews and adopts approaches (e.g., set up best practices and coding standards, help resolve differences of opinions) to foster an effective/collaborative code review culture.",
                    f"{NAME} has a strong awareness of the ecosystem of tools and libraries supporting {HIS} primary programming language, development environment, and ML frameworks (like TensorFlow, Keras, PyTorch, etc.) and a strong grasp of the idioms and patterns of {HIS} language.",
                    f"{NAME} builds tools and produces technical documentation to improve developer efficiency and drive alignment within {HIS} team.",
                ],
                "Software design": [
                    f"{NAME} is able to independently design software components in well-scoped scenarios, with simplicity and maintenance as key considerations. {HIS} components are testable, debuggable, and have logical APIs that are not easily misused.",
                    f"{NAME} knows when to make significant refactors and when it’s better to leave things as-is.",
                    f"{NAME} has a strong grasp of the libraries, platforms, and systems that {HE} relies on, allowing them to apply them expertly.",
                ],
                "Business acumen": [
                    f"{NAME} engages in listening sessions (All Hands, Quarterly Business Updates, etc.) to increase {HIS} learning and guide {HIS} work/priorities.",
                    f"{NAME} has a working knowledge of Abyss’s org/team structure and how teams work together across Abyss and is able to independently work with partner engineering teams to unblock code reviews and engineering designs.",
                ],
            }
        if self.level == "tech lead":
            return {
                "ML design": [
                    f"{NAME} formulates business objectives as computational tasks using the right approach for each objective.",
                    f"{NAME} provides critical feedback to other members of {HIS} team throughout the lifecycle* of an ML project.",
                    f"{NAME} critiques existing metrics and defines new offline and online metrics that stay valid throughout the model's lifetime.",
                    f"{NAME} defines an experimentation strategy and adapts {HIS} team's roadmap to reflect significant findings.",
                ],
                "code fluency": [
                    f"The expectations for L3 code fluency are still applicable here.",
                    f"{NAME} can find ways to improve developer efficiency as measured by cycle time, ramp-up time, or other similar measurements.",
                    f"{NAME} preemptively identifies and resolves technical risks before they jeopardize the project. {HE} resolves cross-team dependencies earlier to ensure the successful execution of the project.",
                    f"{NAME} avoids re-inventing the wheel by leveraging other Abyss solutions or off-the-shelf solutions with the possible trade-off in mind. {HE} writes libraries and modules that can be extended and adopted by other teams at Abyss to increase their efficiency.",
                ],
                "software design": [
                    f"{NAME} is able to give quality feedback on designs written by other members of {HIS} team, asking probing, insightful questions that solidify choices and surface erroneous assumptions.",
                    f"{NAME} effectively and quickly debugs cross-module issues and may intuit where bugs might lie due to {HIS} deep knowledge of the libraries, platforms, and systems that {HIS} software relies on.",
                ],
                "architecture design": [
                    f"{NAME} is able to create coherent designs with multiple components interacting across API or system boundaries, ensuring that bugs do not creep in at the boundaries due to mismatches in expectations of what is technically feasible.",
                    f"{NAME} is capable of rolling out a component or major feature reliably, including appropriate monitoring, paging, etc. {HE} ensures that failure domains are understood and characterized appropriately before a large-scale rollout. For early-stage products, {HE} is able to roll out with an eye toward achieving learning goals untainted by poor quality.",
                    f"{NAME} designs clear success metrics and consistently achieves those metrics post-launch throughout the lifetime of the system or feature. For early-stage products, the success metrics may be oriented around learning goals rather than usage goals, given the inherent unpredictability of achieving product/market fit.",
                ],
                "technical strategy": [
                    f"{NAME} is responsible for aligning the software and data models in {HIS} team to the overall technical and data strategy, making tradeoffs where appropriate in consultation with staff engineers.",
                ],
                "business acumen": [
                    f"{NAME} engages in listening sessions (All Hands, Quarterly Business Updates, etc.) to increase {HIS} learning and guide {HIS} work/priorities.",
                    f"{NAME} has a working knowledge of Abyss's org/team structure and how teams work together across Abyss, and is able to help {HIS} team effectively collaborate with other teams across the organization.",
                ],
            }


okay_list = dict()
going_well_list = dict()
feedback_list = dict()
feedback = FeedbackPillars(level=LEVEL)

## use the class. To do: make this a proper CLI tool

print(
    "Input [0,1,2] for feedback on an item."
    "0 means under-performing."
    "1 means meets expectactions."
    "2 means over-performing."
)
for key_responsibility in feedback.responsibilities:
    print(f"\n{key_responsibility}")
    for key_behaviors in feedback.responsibilities[key_responsibility]:
        print(f"\t{key_behaviors}")
        for key_behavior in feedback.responsibilities[key_responsibility][
            key_behaviors
        ]:
            rating = int(input(f"\t\t{key_behavior}\n"))
            if rating == 0:
                try:
                    feedback_list[key_responsibility].append(key_behavior)
                except KeyError:
                    feedback_list[key_responsibility] = [key_behavior]
            elif rating == 1:
                try:
                    okay_list[key_responsibility].append(key_behavior)
                except KeyError:
                    okay_list[key_responsibility] = [key_behavior]
            elif rating == 2:
                try:
                    going_well_list[key_responsibility].append(key_behavior)
                except KeyError:
                    going_well_list[key_responsibility] = [key_behavior]

            else:
                pass  # todo: try again for input

print("\n\nOVER PERFORMING:")
for key_responsibility in going_well_list:
    print(f"\n{key_responsibility}")
    for comment in going_well_list[key_responsibility]:
        print(f"- {comment}")

print("\n\nMEETS EXPECTATIONS:")
for key_responsibility in okay_list:
    print(f"\n{key_responsibility}")
    for comment in okay_list[key_responsibility]:
        print(f"- {comment}")

print("\n\nGIVE FEEDBACK:")
for key_responsibility in feedback_list:
    print(f"\n{key_responsibility}")
    for comment in feedback_list[key_responsibility]:
        print(f"- {comment}")
