## Inspiration
We all wish to be seen for our best qualities, but most assessments are focused not on qualifications or technical proficiency but the how well you can sell yourself. It isn’t enough to be technically brilliant; one must also appear socially well-rounded. This part of the interview is behavioral-based and more abstract, leaving most people ill-prepared to articulate themselves elegantly while remaining truthful. Being ill-prepared or not meeting the minute of specifications, hastily attempting to compensate for one's lack of ability within a closing time window, make the job search process a test of endurance. Typically, it takes a highly self-aware person and a lot of time to create a brilliant answer considering multiple perspectives on their own. Our team believes this is another skill that can be taught and simplified with coaching and practice in the privacy of your own home.
## What it does
We created a web app that prompts the user with an interview question and then allows the user to answer the questions in the form of voice or text. After the questions, our AI grades your submission and offers advice for your current skill level and overall score. 
## How we built it
We started with researching the nuances behind answering some of the most general interview questions. After collecting over 140+ responses and weighting their viability, we trained a model using python and the Cohere API. We then arbitrarily devised a formula for grading based on classification and confidence in scoring. Typically Cohere can only analyze text, but we decided to leverage Google Cloud speech-to-text together to create a more natural feeling interview environment using the spoken word. For accessibility reasons, we enabled a text submissions option to accommodate individuals unable to complete voice submissions for medical or technological limitations.
## Challenges we ran into
Tackling a project with a high technical rigger was difficult and intermediating, but we are proud of the results of our hard work. 
## Accomplishments that we're proud of
We are proud of our efforts to improve our current skill level and dig deep, pulling from as many resources as possible. 
## What we learned
When considering accessibility, we originally wanted to integrate sign language interpretation using machine learning and a python SDK. After reviewing documentation on how the mute compatibility typically traverses the internet, we learned the same hand dexterity needed for sign language usually requires better dexterity proficiency than typing. Thus typing is primarily preferred in the mute community for fasting web interfacing. We ultimately decided to add a text editor option. 
## What's next for Interviewer-Reviewer
In the future, we would like to subtly create nuances to enhance lessons like learning emotional context, among the most critical skills for your upcoming interview. As such, the interviewer is a friendly emoji that expresses emotions based on the results of your last question; we hope this implementation can mimic the primary unidirectional conversational flow of an actual interview where the interviewee must interpret the interviewer's expression in real-time and adjust accordingly as this is your only feedback in an organic interview.
### Contributors
Alejandro
Caleb
Josh
Mike
