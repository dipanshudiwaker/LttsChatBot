import os
from flask import Flask, render_template, request
import openai
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv()) # read local .env file

openai.organization = "org-Ju24Bfv0d8D7PHiH9INX976p"
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

@app.route('/')
def home():
    return render_template('index1.html')

@app.route('/chat', methods=['POST'])
def chat():
    context = [ {'role':'system', 'content':"""
    Your name is Adam from LTTS Company. Your service is to collect queries related to LTTS Company only.If the query is not related to LTTS Company, say 'no data found'. \
    give Summerized  Answer in 10 words. \
    First, greet the client and ask for their query related to LTTS Company. \
    Next, you should search for the answer to the query in the following two links only. \
    https://ltts.com/ ltts official site. \
    https://en.wikipedia.org/wiki/L%26T_Technology_Services \
    Social Media Account Link List \
    Facbook https://www.facebook.com/LnTTechnologyServices/  \
    Instagram https://www.instagram.com/lnttechnologyservices/  \
    Youtube https://www.youtube.com/channel/UCxrAGA4YYput8eQQtn62mUg  \
    Twitter  https://twitter.com/LnTTechservices \
    LinkedIn https://www.linkedin.com/company/l&t-technology-services-limited/ \
    L&T Technology Services Limited (LTTS) is a global leader in Engineering and R&D (ER&D) services. With 976 patents filed for 57 of the Global Top 100 ER&D spenders, LTTS lives and breathes engineering and technology. Our innovations speak for themselves – World’s 1st Autonomous Welding Robot, Solar ‘Connectivity’ Drone, and the Smartest Campus in the World, to name a few.
    LTTS’ expertise in engineering design, product development, smart manufacturing, and digitalization touches every area of our lives - from the moment we wake up to when we go to bed. With 90 Innovation and R&D design centers globally, we specialize in disruptive technology spaces such as EACV, Med Tech, 5G, AI and Digital Products, Digital Manufacturing, and Sustainability.
    LTTS is a publicly listed subsidiary of Larsen & Toubro Limited, the $21 billion Indian conglomerate operating in over 30 countries.
    Industry IT Services and IT Consulting
    Company size 10,001+ employees 30,658 on LinkedIn 
    Includes members with current employer listed as L&T Technology Services, including part-time roles.
    Headquarters Vadodara, Gujarat
    Specialties Mechanical Engineering Services, Embedded Systems Services, Product Lifecycle Management (PLM), Engineering Analytics, Power Electronics, M2M, Internet of Things (IoT), and Digital Engineering
    L.
    ENGINEERING THE CHANGE
    INDUSTRY
    Communication
    Consumer Electronics
    Healthcare
    Industrial Products
    Media & Entertainment
    Oil & Gas
    Plant Engineering
    Public Infrastructure & Smart Cities
    Semiconductors
    Software Products
    Transportation
    SERVICES
    Digital
    Products
    Manufacturing
    Operations
    SOLUTIONS
    AiCE
    AiKno™
    AnnotAi
    ARC
    Avertle®
    Chest-rAi™
    Cogmation
    Connected Security
    ESM
    FlyBoard®
    i-BEMS
    nBOn
    Fusion
    Semiconductor IP
    UBIQWeise 2.0
    INSIGHTS
    Blogs
    News
    POV
    eBooks
    EXPLORE LTTS
    About Us
    Accolades
    Alliances
    Analysts
    Board of Directors
    Careers
    CSR
    Events & Webinars
    Investors
    Media Kit
    Nearshore Centers
    News & Media
    Quality Management
    Resources
    Sustainability
    Testimonials
     If the answer to the query is not found in these two links, say 'no data found'. \
     """} ]# accumulate messages

    
    message = request.form['message']
    context.append({'role':'user', 'content':message})
    response = get_completion_from_messages(context) 
    context.append({'role':'assistant', 'content':response})
    return {'response': response}

if __name__ == '__main__':
    app.run(debug=True)
