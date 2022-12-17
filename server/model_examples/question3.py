from cohere.classify import Example
import cohere
co = cohere.Client('rQqHCRnyHOS8JLTNbvYPzdrSwqu6fb0qwxD4MXvu')

# 3. What is your greatest weakness
examples = [
    # bad
    Example("I am the perfect being and have no weaknesses. My biggest strength is my self-confidence.", "Bad"),  # 1
    Example(
        "My greatest weakness is an overabundance of my greatest strength", "Bad"),  # 2
    Example("I forget to put exclamation points on every other sentence in emails and therefore get accused of being rude", "Bad"),  # 3
    Example("My greatest weakness is that I’m a perfectionist. My strength is that I’m a perfectionist.", "Bad"),  # 4
    Example("My complete lack of social skills.", "Bad"),  # 5
    Example("Deep-seated fear of rejection. There's more, the cracks spread throughout after all, but that's the core of it.", "Bad"),  # 6
    Example("Heavy pessimism.....I cause my pain.", "Bad"),  # 7
    Example("The only one I can struggle with is myself. I let the person and things occupy space in my head.", "Bad"),  # 8
    Example("My refusal to try and sell myself short.", "Bad"),  # 9
    Example("Being scared of shit that is not going to happen.", "Bad"),  # 10
    # Example("lorem", "Bad"),  # 11
    # Example("lorem", "Bad"),  # 12
    # Example("lorem", "Bad"),  # 13
    # Example("lorem", "Bad"),  # 14
    # Example("lorem", "Bad"),  # 15
    # Example("lorem", "Bad"),  # 16
    # Example("lorem", "Bad"),  # 17
    # Example("lorem", "Bad"),  # 18
    # Example("lorem", "Bad"),  # 19
    # Example("lorem", "Bad"),  # 20

    # good
    Example("I tend to be overly critical of myself. Whenever I complete a project, I can’t help but feel that I could have done more even if my work received a positive response. This often leads me to overwork myself and leaves me feeling burned out. Over the past few years, I’ve tried to take time to look at my achievements objectively and celebrate those wins. This has not only improved my work and my confidence, but it has helped me to appreciate my team and other support systems that are always behind me in everything I do. ", "Good"),  # 1
    Example("I am incredibly introverted, which makes me wary of sharing my ideas in a group setting or speaking up during team meetings. I feel that I had good intentions, I just wasn't always comfortable speaking up. After my team didn’t meet expectations on two consecutive projects, I decided to start making changes to get more familiar with sharing my ideas for the benefit of my team. I took local improv classes and started trying to get comfortable discussing my thoughts. It's still a work in progress, but it's something that I've improved dramatically over the past year.", "Good"),  # 2
    Example("I tend to want to take on complete projects all on my own without any outside help. In the past, this caused me to experience unnecessary pressure and stress. One specific example was last year when I was responsible for planning our annual event. I tried to do everything on my own, from the most substantial decisions like the venue to the tiniest things like organizing the table settings. I was so stressed leading up to the event, and I narrowly pulled it off. This taught me to take a step back and analyze when I need help. After that experience, I am trying to teach myself how to ask for help so I can keep my sanity. I've also found a team of people can produce a better outcome than one harrowed person. ", "Good"),  # 3
    Example("I'm not familiar with the latest version of the software that you use. I’ve spent my time recently focused on generating a positive user experience and have always been willing to learn new things. Throughout my career software has always changed and I’ve always been willing to adapt to changing technology. I will put in the time it takes to learn this new software. ", "Good"),  # 4
    Example("I always try to avoid confrontation, in both my personal and professional life. This caused me to compromise sometimes on the quality of my work or what I needed to complete a project just to keep the peace. This became a real problem when I became a manager. One of the most critical aspects of managing people is telling them what they need to hear and not what they want to hear. I recognized this weakness and had been actively working to voice my opinions constructively and helpfully for the betterment of the team.", "Good"),  # 5
    Example("When I’m given a task, I am very goal-oriented and work hard to complete that task. However, when new projects come across my plate, I sometimes jump right into those projects and halt work on the projects I had in progress. Having to jump between tasks, so many times throughout the day hinders my productivity and prevents me from delivering my best work. I have been using a project management tool to help me manage my tasks and my time, which has helped me become more aware of prioritization. Since implementing this project management mentality, I have only improved my efficiency and productivity.", "Good"),  # 6
    Example("My biggest weakness has always been my communication skills. I’ve been pretty shy and anxious as a kid. Over the years, however, I’ve been really working on the issue. At this stage, I’m much better than I’ve ever been, but I’m still far from perfect. This, however, won’t have any impact on my job as a programmer. Despite lacking communication skills, I’m very good at working in a team.", "Good"),  # 7
    Example("Well, as a recent graduate, I’d say my biggest weakness is the lack of real-life work experience. While I’ve worked on a dozen software projects in the university, I don’t have the experience of working in a fully agile environment with an experienced team. I am, however, willing to do my best and catch up as fast as I can.", "Good"),  # 8
    Example("I don't have much patience when working with a team — I am incredibly self-sufficient, so it's difficult when I need to rely on others to complete my work. That's why I've pursued roles that require someone to work independently. However, I've also worked to improve this weakness by enrolling in team-building workshops. While I typically work independently, it's important I learn how to trust my coworkers and ask for outside help when necessary", "Good"),  # 9
    Example("I struggle with organization. While it hasn't ever impacted my performance, I've noticed my messy desk and cluttered inbox nonetheless interfere with my efficiency. Over time, I've learned to set aside time to organize my physical and digital space, and I've seen it improve my efficiency levels throughout the week.", "Good"),  # 10
    Example("I sometimes find it difficult to delegate responsibility when I feel I can finish the task well myself. However, when I became manager in my last role, it became critical I learn to delegate tasks. To maintain a sense of control when delegating tasks, I implemented a project management system to oversee the progress of a project. This system enabled me to improve my ability to delegate efficiently.", "Good"),  # 11
    Example("Oftentimes, I can be timid when providing constructive feedback to coworkers or managers, out of fear of hurting someone's feelings. However, in my last role, my coworker asked me to edit some of his pieces and provide feedback for areas of improvement. Through my experience with him, I realized feedback can be both helpful and kind when delivered the right way. Since then, I've become better at offering feedback, and I've realized that I can use empathy to provide thoughtful, productive feedback.", "Good"),  # 12
    Example("My blunt, straightforward nature has allowed me to succeed over the years as a team manager, because I'm able to get things done efficiently, and people often appreciate my honesty. However, I've recognized my bluntness doesn't always serve my employees well when I'm delivering feedback. To combat this, I've worked to develop empathy and deeper relationships with those I manage. Additionally, I took an online leadership management course, and worked with the professor to develop my ability to deliver feedback.", "Good"),  # 13
    Example("Public speaking makes me nervous. While I don't need to do much public speaking in my role as a web designer, I still feel that it's an important skill — especially when I want to offer my opinion during a meeting. To combat this, I spoke with my manager and she recommended I speak at each team meeting for a few minutes about our project timeline, deadlines, and goals when developing a website for a client. This practice has enabled me to relax and see public speaking as an opportunity to help my team members do their jobs effectively.", "Good"),  # 14
    Example("I'm not great at analyzing data or numbers. However, I recognize this flaw can prevent me from understanding how my content is performing online. In my last role, I set up monthly meetings with the SEO manager to discuss analytics and how our posts were performing. Additionally, I received my Google Analytics certificate, and I make it a point to analyze data related to our blog regularly. I've become much more comfortable analyzing data through these efforts.", "Good"),  # 15
    Example("Sometimes I struggle with ambiguity and making decisions when directions aren't clear. I come from a work environment that always gave clear and direct instructions. I had such a strong team and leadership that I haven't had much practice making decisions in the heat of the moment. I'm working on this by leaning more into my experience and practicing listening to my gut", "Good"),  # 16
    Example("My inner critic can be debilitating at times. I take pride in producing good work, but I feel like I struggle feeling satisfied with it, which has led to burnout in the past. However, I've started to push back against this inner voice by taking care of myself before and after work. I'm also learning to recognize when my inner critic is right and when I need to dismiss it.", "Good"),  # 17
    Example("I used to work in industries where I had to cultivate a solid work ethic in my employees. This style of training has been so ingrained in me that I've forgotten to discern who may need that coaching and who does not. I've been reading books on effective delegation and team building to work on this shortcoming. One technique that works for me is assuring myself that if I establish clear expectations, then my team will follow. I've also learned to trust my team members.", "Good"),  # 18
    Example("I enjoy developing a relationship with my coworkers by engaging in conversation, and that's a great team-building skill. However, I have a habit of carrying on a conversation to a point where it may distract other coworkers. I have learned since then that there are other ways to connect with my coworkers, and that if I'm asking about their day, I need to keep it brief and redirect myself back to my work.", "Good"),  # 19
    Example("I've struggled with work-life balance, especially after I started working remotely during the pandemic. This increased my stress levels to the point where my productivity was at an all-time low and I didn't bring my best self to work. Because I want to continue working remotely, I've started adding more structure to my day and instituted a sharp start and end time. I've already seen improvements in my levels of focus during work hours.", "Good"),  # 20

]

# manual entry for testing
inputs = [
    "lorem sucks",  # bad
    "lorem dumbass",  # bad
    "lorem love",  # good
    "lorem good"  # good
]

response = co.classify(
    model='medium',  # Consider changing to large?
    inputs=inputs,
    examples=examples)

print(response.classifications)
