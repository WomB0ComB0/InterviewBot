from cohere.classify import Example
import cohere
import dotenv
import os

dotenv.load_dotenv()

co = cohere.Client(os.getenv("COHERE_API_KEY"))

# 2. What are your strengths?
examples = [
    # bad
    Example("What are my strengths? Where do I begin? I’m Superman. I mean look. I take off my glasses - Superman. I put them back on - Clark Kent. You can see it. Yeah, you can! Plus, I’m so good at stuff that you’ll think I’m a psychic. I’ll get work done before there is work to do.  I can already guarantee you that I’m better than all your other employees combined", "Bad"),  # 1
    Example("What are my strengths? Well, I guess I’m pretty good at breathing? I don’t know. That’s what my mom said. She’s usually right about stuff. So, I guess yeah. I guess I could say I’m a good breather.", "Bad"),  # 2
    Example("I guess that I’m a strong people person as long as I don’t have to write emails and can talk to that person face-to-face.", "Bad"),  # 3
    Example("My strengths? Where do I start? I’m great at customer service, organizing stuff, writing, sales, and marketing. Oh! I almost forgot. I can also administer medication to large domestic animals.", "Bad"),  # 4
    Example("My greatest strength is administering assistance.", "Bad"),  # 5
    Example("Well, I’m not all that bad at throwing together an Excel spreadsheet. I can do a Powerpoint presentation now and then. I guess my other strengths are making coffee, stapling things, and typing. Oh yeah, and I can open emails, talk on the telephone, send emails, and use scissors.", "Bad"),  # 6
    Example("Without wanting to appear self-indulging, I do tend to have a good sense of humour and am lighthearted so most people enjoy my company. I also genuinely care about people and therefore most people feel comfortable around me. Just don't make me angry because you'll be in for a surprise.", "Bad"),  # 7
    Example("Strengths: I'm really good at spacing off, spinning in my office chair, typing really fast (questionable accuracy), making tea, using pens as drumsticks, using pens as projectiles, using pens as pens, turning staple removers into dragons and other mythical creatures, and taking breaks.", "Bad"),  # 8
    # Example("lorem", "Bad"),  # 9
    # Example("lorem", "Bad"),  # 10
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
    Example("Whenever new software is released, I’m always the first one to test and get familiar with it. I love pushing the edge and learning every aspect of the new software. In fact, just last week I found a software issue with one of my video games. I called the developer, and they fixed it right away. This position will give me the opportunity to apply my passion and help make programs better for your company. ", "Good"),  # 1
    Example(" I’ve always preferred to work in groups and find that my collaborative nature is one of my strongest attributes. On projects that I directed, I work well to inspire diverse team members and work side by side with them to achieve the project goals. In fact, I’ve increased productivity by ten percent over the course of two years. ", "Good"),  # 2
    Example("My greatest strength is my writing skills. I work well under pressure, and I've never missed a deadline. One specific example that comes to mind is when I was asked to complete a project that a fellow colleague forgot about. My editor didn’t realize this until two hours before the deadline. It was an important piece, so I got to work, and with feverish precision, I was able to complete the article. Not only was it finished on time, but it was received very well by readers of the publication.", "Good"),  # 3
    Example("I’m relatively new to the finance industry, but I find that I’m good at working with numbers and I truly love it. I love helping people save money and finding new investment opportunities for my clients. Learning about their needs and finding ways to help them achieve the lifestyle they want is so gratifying to me, and I’ve helped my clients increase their net worth by 10% collectively. ", "Good"),  # 4
    Example("I’m an empathetic person who is skilled at relating to people and understanding their needs. At my internship over the summer, I was working the support line and received a call from a disgruntled customer who had been dropped from our service. While the company couldn’t find a solution for her, I walked her through other options she might have so she walked away with a positive interaction with the company. I know the importance of a happy customer, and I'm willing to remain upbeat and solutions-oriented.", "Good"),  # 5
    Example("I believe that my greatest strength is the ability to solve problems quickly and efficiently. I can see any given situation from multiple perspectives, which makes me uniquely qualified to complete my work even under challenging conditions. That problem solving allows me to be a better communicator. I am just as comfortable speaking to senior executives as I am junior team members. I think my ability to see all sides of an issue will make me a great asset to the team.", "Good"),  # 6
    Example("I know the industry inside and out. After working in sales and marketing for over 15 years I know I have the skills to maximize your marketing dollars and improve your bottom line. In fact, when I started at my last company, their sales were declining, and under my leadership, I was able to increase revenue in consecutive years, by 7% and 5%, respectively.", "Good"),  # 7
    Example("My strongest asset is my work ethic and my willingness to step in when needed. I’m not afraid to take on a difficult client or do a project that nobody else wants because those are the clients and projects that teach me the most. I typically love to work outside of my job description and do whatever is asked of me. I'm not above any single task, and I take great pride in my ability to step in and adapt to any situation to get the best results for the company.", "Good"),  # 8
    Example("My biggest strength is that I’m good at picking up new skills. I’ve worked a variety of different odd jobs - things like working as a waiter, house-keeper, cook, and a lot more (as you’ve probably seen on my resume). For most of those jobs, I ended up picking up all the needed skills within 1 or 2 weeks (with basically no previous experience). So, I’m pretty sure while I don’t have any experience as a bartender, I have the right certification, and I believe I can get good at it within a week or two.", "Good"),  # 9
    Example("My biggest strength is that I’m very efficient at working under pressure. No matter the crisis or stress, I can make the right decisions on-the-spot. As an event manager at Company X, we were organizing an IT conference for a client. There were a ton of last-minute hiccups - some speakers canceled and the catering company said they’d be late for the lunch break. On top of that, we were understaffed because 2 of our volunteer organizers got sick and couldn’t show up. At that point, things looked so bleak that we were considering canceling the event or postponing it. Instead, I took the initiative in my hands and sorted through the problems one by one.", "Good"),  # 10
    Example("""My greatest strength is my writing skills. I can also work to tight deadlines under pressure. For example, I was once asked to complete a project that fell through the cracks. My editor discovered the mistake two hours before the deadline. It was an important piece that gave our publication a scoop on the topic in question. Not only did the piece have to go out on time, but it had to be perfect. I hunkered down and wrote. The result? The article was on time and acclaimed.""", "Good"),  # 11
    # Example("lorem", "Good"),  # 12
    # Example("lorem", "Good"),  # 13
    # Example("lorem", "Good"),  # 14
    # Example("lorem", "Good"),  # 15
    # Example("lorem", "Good"),  # 16
    # Example("lorem", "Good"),  # 17
    # Example("lorem", "Good"),  # 18
    # Example("lorem", "Good"),  # 19
    # Example("lorem", "Good"),  # 20

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
