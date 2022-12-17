from cohere.classify import Example
import cohere
import dotenv
import os

dotenv.load_dotenv()

co = cohere.Client(os.getenv("COHERE_API_KEY"))

# 4. Where do you see yourself in 5 years?
examples = [
    # Bad
    Example("Finally done with college, wrapping up a masters, working full time, and one year ETS'd out of the Army. I cannot fucking wait.", "Bad"),
    Example("Inshallah starting a doctorate in Anthropology. That or I could be dead you never know.", "Bad"),
    Example("Watching Mr Chickadee on YT makes me want to sell my house and move my family into a forest to build a timber house and live a minimalist life.", "Bad"),
    Example("Either dead, or happier that I worked towards my desires/goals.", "Bad"),
    Example("Dead. I have to have several surgeries to correct 3 old surgeries. I don’t have it in me, it all hurts so much.", "Bad"),
    Example("Hopefully out of America, and in a country that actually gives a shit about the health and well-being of its people.", "Bad"),
    Example("3 kids. Better job. 1 million personal net worth.", "Bad"),
    Example("Hopefully still in my current job with a pay-raise, but living in a different apartment. I like the place, but some neighbors are... difficult.", "Bad"),
    Example(
        "Hopefully in a different city, in a different house. Maybe with a dog.", "Bad"),
    Example("On the cusp of finishing college, hopefully having a boyfriend and planning to move to a rather small but well connected town to start teaching", "Bad"),
    Example("Farm somewhere in the south that I can grow peppers and citrus trees year round if not a much better growing season than where I am now.", "Bad"),
    Example("I'll be sitting where you are, asking some new kid that same question. And you'll be in your cold cold grave.", "Bad"),
    Example("Happier , Healthier. In school, certified in some fields, part time job, savings, decent relationship with friends and fam ; and ready to travel.", "Bad"),
    Example("Hopefully healthier, has a house, has the courage to drive, and either have kid(s) or (still) in the military.", "Bad"),
    Example("Bruh idk where I’ll be tomorrow let alone 5 years", "Bad"),
    Example(
        "Probably jail for public intoxication or I'll still be at my shitty job", "Bad"),
    Example("If we don’t stop rampant capitalism, then in 5-10 years climate change could cause economic collapse (see prof. Rupert Read and Roger Hallam). By the end of the century, if we reach a 4c temperature increase, then according to Dr. Ira Leifer, a leading climate scientist, the answer to “where do you see yourself” is in either Antarctica or the Arctic. Our economy is a Ponzi scheme.", "Bad"),
    Example("5 years older, none the wiser, a lot poorer", "Bad"),
    Example("I'd like to talk to people who answered that question 5 years ago. Betcha nobody thought up the pandemic.", "Bad"),
    Example("In 5 years - owning a home again, published author, and if all goes well finally with someone who loves me the way I can love.", "Bad"),

    # Good
    Example("I’m exceptionally delighted about being a part of Solution Logics Incorporated because in the next five years, I’d love to be perceived as an expert petrochemical engineer and I believe Solution Logics Incorporated as a leader in the petroleum industry is the best training ground for someone like me who’s willing to contribute to the society. I’m equally excited about the prospects of working with some of the most brilliant minds in Europe.", "Good"),
    Example("Within the next 5 years, I’d like to reach the position of a Senior Business Consultant. During the time period, I would like to accomplish the following: Help 20+ organizations improve their business Create a personal network of highly specialized professionals Learn as much as I can about optimizing and improving clients’ businesses, as well as the essentials of operating a company", "Good"),
    Example("""As a start, I want to learn if accounting is the right field for me. While I loved what I studied at the university, I want to see if working in the field feels the same. If I do end up enjoying it, I’d like to specialize in either internal auditing or forensic accounting, as I really like to discover and solve problems. From what I’ve seen from your job ads, you guys are hiring for both, so I hope it’s going to be possible to move up from the position of an "intern" within the next few months!
            """, "Good"),
    Example("""I’m someone who loves solving problems, so in five years, I’d love to be seen as the go-to financial analyst when departments or projects need to save money and achieve their business goals. I will have worked with senior financial analysts to learn from their approaches before taking on a few smaller budgets myself and slowly building up from there. But I will have also completed a few courses on business operations using XYZ Co’s professional development allowance since I want to make sure that any suggestions I make go toward not just saving money, but increasing efficiency and achieving company goals.
            """, "Good"),
    Example("""In five years, I’d like to be in a position where I know more about my longer-term career aspirations as a designer. I will have gotten experience working for a design agency and know more about the industry overall. I’ll have grown my technical skills and learned how to take feedback from clients and incorporate it. And the way your agency is set up, I’ll also have gotten the opportunity to design different kinds of deliverables—including websites, branding, and ad campaigns—for different kinds of clients to see where I really feel at home before settling on a focus.
            """, "Good"),
    Example("I’ve found that the most rewarding part of working in HR has been when I get to be part of putting together a training or development session—it’s so satisfying to help my coworkers learn something new and useful. So in five years I’d like to be more of an expert in learning and development. I’ll have learned more about what goes into putting together development opportunities for employees and have hopefully coordinated or run some training sessions myself. In a training and development coordinator role like this, I’ll also learn more about how to work with individual employees or teams to identify prime opportunities to upskill and find the best form of training available so I’m delivering programs that are useful to individuals and the org overall. Hopefully, in five years I’ll be helping make decisions about what kinds of programs a business will offer and how to make sure employees are benefitting and growing.", "Good"),
    Example("In five years I would like to expand my horizons by jumping in feet first and learning as much as I can, as quickly as I can, with the organization. From there, I'd seek out opportunities — at least one to two a year — to expand my knowledge through training and educational opportunities to support my job. I'd love to participate in at least one project geared toward leadership training, if the opportunity arises. I also understand that the organization has a strong volunteer team, and I'd like to be an active participant of that team, as well. At some point, I'd also like to be considered for a supervisory or management-level role.", "Good"),
    Example("It’s only been two years since I graduated and began working, but I’d say that my goal in five years is to see significant growth in my sales skills. One of my longer-term career goals is to be involved in sales training and mentoring, maybe as a Manager or corporate trainer, but I know the first step is to master the day-to-day work. So in the next five years, I look forward to continuing to build my sales skills, both in-person and over the phone, and continuing on my current career path as a salesperson. I reviewed your job posting and it seems like this position would offer some great challenges and learning opportunities for someone relatively new in their sales career like myself.", "Good"),
    Example("In the next 5-10 years, I hope to be leading a team or department. I’ve always enjoyed leadership in my career, so growing as a leader is one of my core career goals right now. Your job posting looked exciting and mentions some great leadership opportunities, so I was eager to have a job interview and learn more about this opportunity.", "Good"),
    Example("""Since becoming a Project Lead in my last job, I’ve found I really like project management. In five years, I hope to be leading larger projects, or maybe managing multiple project teams. I thought your Senior Project Manager position was a great step in that direction and would provide a nice challenge, while also making use of my 2 + years of prior project leadership experience in this same industry.
            """, "Good"),
    Example("I’ve actually been developing my five year plan recently. Since I’m looking for an entry level position in social media and content marketing right now, in five years I would like to be a manager or supervisor in this area, or possibly a project manager. So that means that in the next few years, I need to master the fundamentals and hands-on aspects of the role to advance in the future. And then in the very long term outlook for my career, I’d love to branch out into other areas of digital marketing and lead an entire marketing department for my company. This position seems like a great fit for my five-year goal, based on what I saw on the job description, so I was eager to come have an interview to learn more.", "Good"),
    Example("In five years, I see myself continuing to grow in my career and taking on more responsibility within the company by leveraging the expertise I’ve gained working in this industry for the past 5 years. I’m also looking to start a family in the next few years, so I’ll be balancing work and home life. I think that my career goals and personal goals will complement each other nicely and help me to achieve a healthy work-life balance.", "Good"),
    Example("I see myself in a leadership position, helping to lead and develop a productive and successful team. I believe I’m uniquely positioned for this career path I’ve consistently met or exceeded sales goals in every position I’ve held. I would also like to continue developing soft skills and technical skills by taking on additional training opportunities. I think that being in a management position will give me the opportunity to do both of these things.", "Good"),
    Example("In five years, I see myself as an integral part of the company who has helped contribute to the growth and success of the organization. I would like to continue developing my skills and knowledge in order to be able to take on more responsibility within the company. I’m also looking forward to taking on more leadership roles and mentoring other members of the team by utilizing the leadership and mentorship certifications I’ve completed.", "Good"),
    Example("In five years, my goal is to successfully obtain two certificates that are related to my position. I took some time to review your website before this interview, and I noticed that you offer your employees education advancement opportunities that include pursuing certifications to further their careers. Using the resources your company provides its employees, I truly believe that I can pursue my career goals and eventually move into a management position within your organization over the next few years.", "Good"),
    Example("My ultimate goal for the next five years is to master my position and advance into a managerial role within my department. I was drawn to the personalized training approach your company outlines on its website, and I truly believe this approach to training will allow me to learn new skills and grow within this position. Over the next five years, I see myself taking on new and exciting projects within your company that will prepare me for a management role with the organization.", "Good"),
    Example("A few of the goals I’ve set for myself over the next few years include leading a writing team and gaining new project management skills within my position. I’m excited about the opportunities this job would provide me, as I believe they will support my long-term career goals and allow me to grow within your company and give back by utilizing the skills I’ll gain.", "Good"),
    Example("As a freelance writer working with several major tech companies on blog and website content, I feel like my knowledge of SEO is still limited as I often require assistance. That’s why one of my short-term goals is to complete an SEO course and become fully independent in SEO tools like Moz, Semrush or Ahrefs. That will also allow me to enhance my service portfolio.", "Good"),
    Example(
        "After changing jobs for the last three years, my biggest career goal right now is to gain some career stability. I really enjoy my work in [Company] – I think it’s challenging, exciting, and fun. I also have the perfect work-life balance, which I greatly appreciate now that I’m in my forties and have a growing family.", "Good"),
    Example("One of my biggest career goals is to improve my presentation skills and master public speaking. I think there’s an imbalance between my technical knowledge and the way I organize and verbalize my thoughts. Getting good at speaking in front of a group would help me with some of my long-term career goals, such as getting a leadership position.", "Good")
]

# manual entry for testing
inputs = [
    "I see myself nowhere in 5 years",  # bad
    "Can we skip to the next question?",  # bad
    "In 5 years, I'd like to own a house. I'd also like join a growing team so that I can have more critical impacts on my projects. Hopefully this can be at your company in X department.",  # good
    "I've been honing in on my craft - manging larger and larger teams in order to get more experience as a project manager. Five years from now, I am confident I will be in a director role overseeing operations."  # good
]


response = co.classify(
    model='medium',  # Consider changing to large?
    inputs=inputs,
    examples=examples)

print(response.classifications)
