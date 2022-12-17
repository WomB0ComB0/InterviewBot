from cohere.classify import Example
import cohere
co = cohere.Client('rQqHCRnyHOS8JLTNbvYPzdrSwqu6fb0qwxD4MXvu')

# 5. Why did you leave your previous job?
examples = [
    # bad
    Example("My manager was so unprofessional!", "Bad"),  # 1
    Example("Oh, well, the company started bleeding cash and was on its way to bankruptcy.", "Bad"),  # 2
    Example("Things started to get really boring, and the boss man was kind of mean. I totally deserve better, so I just ghosted them and now I’m looking for a new company. Hi!", "Bad"),  # 3
    Example("I got fired for missing work for a week without an excuse.", "Bad"),  # 4
    Example("I quit my job because I didn’t like it. That’s all. It didn’t suit me.", "Bad"),  # 5
    Example("I got fired because I did not get along with my supervisor. We went together like peanut butter and asparagus. She was the asparagus. Obviously.", "Bad"),  # 6
    Example("I haven’t quite figured out what I want to do yet. That’s why I’ve been moving around trying things on for size.", "Bad"),  # 7
    Example("It was too stressful and unrewarding. There was no support from senior management at all. I took a less stressful role elsewhere but for the same wage.", "Bad"),  # 8
    Example("We were sabotaged by upper management and the work conditions were unbearable.  They fired 75% of our team, resulting in 70+ hour weeks and 24/7 on-call shifts.  I got my review that year and no raise...they gave me a year end bonus of $36.  That is less than one hour of pay for me.  I felt insulted and had a new job literally the next day.", "Bad"),  # 9
    Example("We had a security situation and the manager fucked up and tried to pin it on me, even though I did exactly what I was trained to do according to policy, so I left.", "Bad"),  # 10
    Example("I was fired because my depression was affecting my output.", "Bad"),  # 11
    Example("I'm going to quit my job this week (only been there 3 months) but the environment and my coworkers are toxic in every possible way; my mental health has taken a nosedive as a result.", "Bad"),  # 12
    Example("Just say that the atmosphere was uncomfortable and that it caused you too much stress.", "Bad"),  # 13
    Example("It was a scheduling issue. An unstable schedule prevented me from having a proper-work life balance, and even prevented me from accomplishing basic tasks of my job. Thing is, other places I apply to expect me to be flexible with scheduling, and I am, but this one job I left was way too extreme.", "Bad"),  # 14
    # Example("lorem", "Bad"),  # 15
    # Example("lorem", "Bad"),  # 16
    # Example("lorem", "Bad"),  # 17
    # Example("lorem", "Bad"),  # 18
    # Example("lorem", "Bad"),  # 19
    # Example("lorem", "Bad"),  # 20

    # good
    Example("I felt like the job didn’t align with my career aspirations. I decided that I wanted to work as a C++ developer, but the job I worked was that of a web developer.", "Good"),  # 1
    Example("I excelled at my last job, achieved all the KPIs, and managed to complete Project X successfully and on time, all this over the 5 years I was working there. Despite it all, I didn’t get promoted to the management position, which I found very demotivating.", "Good"),  # 2
    Example("I realized that Company X wasn’t giving me the growth opportunities I need at this stage of my career.", "Good"),  # 3
    Example(
        "I left Company X because Company Y offered me a better position.", "Good"),  # 4
    Example("I recently had a child and wanted to free up my time by switching to a freelancing arrangement.", "Good"),  # 5
    Example("I wanted to move to Jackson, Wyoming, and so I looked for a company that offered the option to work remotely.", "Good"),  # 6
    Example("When my supervisor left the company, the work environment was just not the same. Their replacement was a bit too micromanaging, which is not something I like in a job.", "Good"),  # 7
    Example("I had a family emergency and had to take care of my mother full-time for a few months.", "Good"),  # 8
    Example("The job didn’t actually match the job description. I was expecting to work as a React developer (which is the skill I wanted to develop), but it instead involved working with a very obscure framework that is not related to my desired career path.", "Good"),  # 9
    Example("The project I was working on got canceled, and as the company didn’t have any openings in other projects they had to let me go. That said, I’m still very close with the management team at Company X, and if you’d like, I can provide a reference.", "Good"),  # 10
    Example("I was fired because of a mismatch between the job and my understanding of it. I expected for the role to be more focused on illustrations (which is what I excel at), but I ended up doing a lot of UX/UI work instead, which isn’t necessarily my strong suit, nor what I want to do with my career. As such, I underperformed at the role, and the management just didn’t like my output.", "Good"),  # 11
    Example("My manager was micromanaging the team’s work too much, which led to decreased productivity.", "Good"),  # 12
    Example("The last company I got hired in just wasn’t what I expected. The hiring manager didn’t communicate the role well enough. As you already know, I’m a copywriter - I write sales copy. I work with: -Landing pages -Email marketing -And sales pages Around a week after I started work at the company, I realized that they were actually looking for something completely different. They asked me to write generic blog and social media posts, which is pretty far off from what I do.", "Good"),  # 13
    Example(
        "Well, as a start, my first job was in a big corporation straight out of university. While I did learn a lot there about Software Engineering practices, I also learned that a huge company with lots of regulations, rules, and the like isn’t for me. So, at the end of my internship there, I decided to try working at a startup. I enjoyed that job a LOT more, as it gave me a lot of freedom when it comes to problem-solving. I wasn't told HOW to do it. Rather, I was given the option of coming up with my own solution. Unfortunately, the company went belly-up after failing to raise money, putting me back on the job market. And here we are - [Company X] is pretty much THE place I’ve always wanted to work in. I’ve heard a lot about your company culture, and thought I’d really belong there.", "Good"),  # 14
    Example("I felt like it was time - I got to a point where everything I was doing felt monotonous. I learned as much as I could at this position while delivering amazing results. It was, however, time to switch to something new.", "Good"),  # 15
    Example("I didn’t feel like the company’s values coincide with mine. The management was too controlling and micromanaging. I prefer to have some control over my work, and being able to contribute by going above and beyond my requirements.", "Good"),  # 16
    Example("I was fired, actually. The fault was in my communication skills at the time. I misunderstood my supervisor’s instructions and ended ended up setting a higher monthly spend on ad account for the client. The losses were not more than 3-figures, but apparently, the relationship with the client was already strained, so they ended up leaving.", "Good"),  # 17
    Example("Of course, I really took this to heart and worked very hard on improving my communication skills, to ensure that I don’t make any mistakes of this nature ever again.", "Good"),  # 18
    Example("I quit my job to pursue new opportunities and take a new step in my career.", "Good"),  # 19
    Example("I’m leaving my current job to pivot into a different industry. As you can see, I left on good terms with my former employer as he is one of my references.", "Good"),  # 20
    Example("I spent less than a year in my last position because of corporate layoffs. Now, I know that I want to work for a smaller company that is more involved in my local community.", "Good"),  # 21

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
