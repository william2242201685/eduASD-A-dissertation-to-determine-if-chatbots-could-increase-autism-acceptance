#!/usr/bin/env python
# coding: utf-8

# In[1]:


import warnings
warnings.simplefilter('ignore')


# In[2]:


from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import json
import sys
import requests
import re
import os


# In[3]:


import nltk


# In[4]:


from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()


# In[5]:


from nltk.corpus import stopwords
nltk.download('stopwords', quiet=True)


# In[6]:


print("Hello and welcome to the EDUasd web scraper! This is designed to scrape over 50 medical and proffesional websites about autism! This should only take 1-2 minutes to complete")


# In[7]:


def get_data():
    nhs_sites = ["https://www.nhs.uk/conditions/autism/signs/adults/", "https://www.nhs.uk/conditions/autism/getting-diagnosed/how-to-get-diagnosed/", "https://www.nhs.uk/conditions/autism/what-is-autism/", "https://www.what0-18.nhs.uk/health-for-young-people/mental-health-and-wellbeing/autistic-spectrum-condition-asc"]
    nhs_support = ["https://www.nhs.uk/conditions/autism/support/"]
    nhs_treat = ["https://www.nhs.uk/conditions/autism/autism-and-everyday-life/treatments-that-are-not-recommended-for-autism/"]
    nhs_highlow = ["https://www.england.nhs.uk/learning-disabilities/about/get-involved/involving-people/making-information-and-the-words-we-use-accessible/"]
    nhs_born = ["https://www.nhsinform.scot/illnesses-and-conditions/brain-nerves-and-spinal-cord/autism-spectrum-disorder-asd"]
    nhs_cbt = ["https://www.nhs.uk/mental-health/talking-therapies-medicine-treatments/talking-therapies-and-counselling/cognitive-behavioural-therapy-cbt/overview/"]
    nhs_dbt = ["https://www.nhs.uk/mental-health/conditions/borderline-personality-disorder/treatment/"]
    autism_society_sites = ["https://www.autism.org.uk/advice-and-guidance/topics/behaviour/meltdowns/all-audiences"]
    autism_society_ang = ["https://www.autism.org.uk/advice-and-guidance/topics/behaviour/anger-management/parents"]
    autism_society_stimming = ["https://www.autism.org.uk/advice-and-guidance/topics/behaviour/stimming/all-audiences"]
    autism_societyeat = ["https://www.autism.org.uk/advice-and-guidance/topics/behaviour/eating/all-audiences"]
    autism_societyharm = ["https://www.autism.org.uk/advice-and-guidance/topics/behaviour/self-injurious-behaviour/all-audiences"]
    autism_societysmear = ["https://www.autism.org.uk/advice-and-guidance/topics/behaviour/smearing/all-audiences"]
    autism_societyobsessions = ["https://www.autism.org.uk/advice-and-guidance/topics/behaviour/obsessions/all-audiences"]
    autism_societydistressed = ["https://www.autism.org.uk/advice-and-guidance/topics/behaviour/distressed-behaviour/all-audiences"]
    autism_societychange = ["https://www.autism.org.uk/advice-and-guidance/topics/behaviour/dealing-with-change/all-audiences"]
    autism_societyfindjob = ["https://www.autism.org.uk/advice-and-guidance/topics/employment/seeking-work/autistic-adults"]
    autism_societygirl = ["https://www.autism.org.uk/advice-and-guidance/what-is-autism/autistic-women-and-girls"]
    autism_societycatatonia = ["https://www.autism.org.uk/advice-and-guidance/topics/mental-health/catatonia/parents"]
    autism_societyburnout = ["https://www.autism.org.uk/advice-and-guidance/topics/mental-health/autistic-fatigue/parents"]
    autism_societyanxiety = ["https://www.autism.org.uk/advice-and-guidance/topics/mental-health/anxiety"]
    autism_societysuicide = ["https://www.autism.org.uk/advice-and-guidance/topics/mental-health/suicide"]
    autism_societyaddiction = ["https://www.autism.org.uk/advice-and-guidance/topics/mental-health/addiction"]
    autism_societysensory = ["https://www.autism.org.uk/advice-and-guidance/what-is-autism"]
    autism_societyscreening = ["https://www.autism.org.uk/advice-and-guidance/topics/diagnosis/diagnostic-tools"]
    autism_societyscreeningtool = ["https://www.autism.org.uk/advice-and-guidance/topics/diagnosis/diagnostic-tools/all-audiences"]
    autism_societylonely = ["https://www.autism.org.uk/advice-and-guidance/topics/loneliness"]
    autism_societydepression = ["https://www.autism.org.uk/advice-and-guidance/topics/mental-health/depression"]
    autism_societyothercon = ["https://www.autism.org.uk/advice-and-guidance/topics/related-conditions/related-conditions/all-audiences"]
    autism_societybullying = ["https://www.autism.org.uk/advice-and-guidance/topics/bullying/bullying/parents"]
    autism_societyinsom = ["https://www.autism.org.uk/advice-and-guidance/topics/physical-health/sleep/autistic-adults"]
    beyondAutism = ["https://www.beyondautism.org.uk/about-autism/understanding-autism/autism-faq/", "https://www.beyondautism.org.uk/about-autism/understanding-autism/causes-of-autism/", "https://www.beyondautism.org.uk/about-autism/understanding-autism/diagnosis/"]
    changeyourreaction = ["https://changeyourreactions.com/faqs/#:~:text=Is%20autism%20a%20visible%20disability,autistic%20individual%20is%20behaving%20differently"]
    autismService = ["https://www.theautismservice.co.uk/news/what-are-the-symptoms-of-autism/"]
    theSpectrum = ["https://thespectrum.org.au/faq/"]
    autismAcceptweek = ["https://www.awarenessdays.com/awareness-days-calendar/world-autism-acceptance-week-2023/"]
    autismMilton = ["https://www.milton-keynes.gov.uk/autism"]
    autismSurrey = ["https://nassurreybranch.org/about-autism/"]
   
    scraped_sites = []
    header = []
    response = []
    
    
    for i in nhs_sites:
        decom = ["nhsuk-card nhsuk-card--care nhsuk-card--care--non-urgent", "nhsuk-inset-text", "nhsuk-u-visually-hidden"]
        link = requests.get(i)
        link.encoding = None
        soup = BeautifulSoup(link.text, "html.parser")
        for i in decom:
            try:
                soup.find('div',class_=i).decompose()
            except:
                expect = "met"
        try:
            rm = soup.select_one('p[data-block-key="d77ct"]')
            rm.decompose()
        except:
            expect = "met"
        try:
            div = soup.find_all(class_='nhsuk-inset-text')
            for i in div:
                i.decompose()
        except:
            expect = "met"
        data_scrape, header_scrape, response_scrape = nhs(soup)
        header.append(header_scrape)
        scraped_sites.append(data_scrape)
        response.append(response_scrape)
        
    for i in nhs_support:
        link = Request(i , headers={'User-Agent': 'Mozilla/5.0'})
        site = urlopen(link).read()
        soup = BeautifulSoup(site, "html.parser")
        data_scrape, header_scrape, response_scrape = data_scrape_nhs_support(soup)
        header.append(header_scrape)
        scraped_sites.append(data_scrape)
        response.append(response_scrape)
        
    for i in nhs_treat:
        link = Request(i , headers={'User-Agent': 'Mozilla/5.0'})
        site = urlopen(link).read()
        soup = BeautifulSoup(site, "html.parser")
        data_scrape, header_scrape, response_scrape = nhs_treatment(soup)
        header.append(header_scrape)
        scraped_sites.append(data_scrape)
        response.append(response_scrape)
        
    for i in autism_society_sites:
        link = Request(i , headers={'User-Agent': 'Mozilla/5.0'})
        site = urlopen(link).read()
        soup = BeautifulSoup(site, "html.parser")
        data_scrape, header_scrape, response_scrape = autism_society(soup)
        header.append(header_scrape)
        scraped_sites.append(data_scrape)
        response.append(response_scrape)
        
    for i in autism_society_ang:
        link = Request(i , headers={'User-Agent': 'Mozilla/5.0'})
        site = urlopen(link).read()
        soup = BeautifulSoup(site, "html.parser")
        soup.find("ul", class_="navigation__list").decompose()
        data_scrape, header_scrape, response_scrape = autism_society_anger(soup)
        header.append(header_scrape)
        scraped_sites.append(data_scrape)
        response.append(response_scrape)
        
    for i in autism_society_stimming:
        link = Request(i , headers={'User-Agent': 'Mozilla/5.0'})
        site = urlopen(link).read()
        soup = BeautifulSoup(site, "html.parser")
        soup.find("ul", class_="navigation__list").decompose()
        data_scrape, header_scrape, response_scrape = autism_society_stim(soup)
        header.append(header_scrape)
        scraped_sites.append(data_scrape)
        response.append(response_scrape)
    
    for i in autism_societyeat:
        link = Request(i , headers={'User-Agent': 'Mozilla/5.0'})
        site = urlopen(link).read()
        soup = BeautifulSoup(site, "html.parser")
        soup.find("ul", class_="navigation__list").decompose()
        data_scrape, header_scrape, response_scrape = autism_society_eat(soup)
        header.append(header_scrape)
        scraped_sites.append(data_scrape)
        response.append(response_scrape)
    
    for i in autism_societyharm:
        link = Request(i , headers={'User-Agent': 'Mozilla/5.0'})
        site = urlopen(link).read()
        soup = BeautifulSoup(site, "html.parser")
        soup.find("ul", class_="navigation__list").decompose()
        data_scrape, header_scrape, response_scrape = autism_society_harm(soup)
        header.append(header_scrape)
        scraped_sites.append(data_scrape)
        response.append(response_scrape)

    for i in autism_societysmear:
        link = Request(i , headers={'User-Agent': 'Mozilla/5.0'})
        site = urlopen(link).read()
        soup = BeautifulSoup(site, "html.parser")
        soup.find("ul", class_="navigation__list").decompose()
        data_scrape, header_scrape, response_scrape = autism_society_smear(soup)
        header.append(header_scrape)
        scraped_sites.append(data_scrape)
        response.append(response_scrape)
    
    for i in autism_societyobsessions:
        link = Request(i , headers={'User-Agent': 'Mozilla/5.0'})
        site = urlopen(link).read()
        soup = BeautifulSoup(site, "html.parser")
        soup.find("ul", class_="navigation__list").decompose()
        data_scrape, header_scrape, response_scrape = autism_society_obsessions(soup)
        header.append(header_scrape)
        scraped_sites.append(data_scrape)
        response.append(response_scrape)
    
    for i in autism_societydistressed:
        link = Request(i , headers={'User-Agent': 'Mozilla/5.0'})
        site = urlopen(link).read()
        soup = BeautifulSoup(site, "html.parser")
        soup.find("ul", class_="navigation__list").decompose()
        data_scrape, header_scrape, response_scrape = autism_society_distressed(soup)
        header.append(header_scrape)
        scraped_sites.append(data_scrape)
        response.append(response_scrape)
    
    for i in autism_societychange:
        link = Request(i , headers={'User-Agent': 'Mozilla/5.0'})
        site = urlopen(link).read()
        soup = BeautifulSoup(site, "html.parser")
        soup.find("ul", class_="navigation__list").decompose()
        data_scrape, header_scrape, response_scrape = autism_society_change(soup)
        header.append(header_scrape)
        scraped_sites.append(data_scrape)
        response.append(response_scrape)
    
    for i in autism_societyfindjob:
        link = Request(i , headers={'User-Agent': 'Mozilla/5.0'})
        site = urlopen(link).read()
        soup = BeautifulSoup(site, "html.parser")
        soup.find("ul", class_="navigation__list").decompose()
        data_scrape, header_scrape, response_scrape = autism_society_find_job(soup)
        header.append(header_scrape)
        scraped_sites.append(data_scrape)
        response.append(response_scrape)
        
    for i in autism_societycatatonia:
        link = Request(i , headers={'User-Agent': 'Mozilla/5.0'})
        site = urlopen(link).read()
        soup = BeautifulSoup(site, "html.parser")
        soup.find("ul", class_="navigation__list").decompose()
        data_scrape, header_scrape, response_scrape = autism_society_catatonia(soup)
        header.append(header_scrape)
        scraped_sites.append(data_scrape)
        response.append(response_scrape)
    
    for i in nhs_highlow:
        link = Request(i , headers={'User-Agent': 'Mozilla/5.0'})
        site = urlopen(link).read()
        soup = BeautifulSoup(site, "html.parser")
        data_scrape, header_scrape, response_scrape = nhs_high_low(soup)
        header.append(header_scrape)
        scraped_sites.append(data_scrape)
        response.append(response_scrape)
    
    for i in nhs_born:
        link = Request(i , headers={'User-Agent': 'Mozilla/5.0'})
        site = urlopen(link).read()
        soup = BeautifulSoup(site, "html.parser")
        data_scrape, header_scrape, response_scrape = nhs_bornwithautism(soup)
        header.append(header_scrape)
        scraped_sites.append(data_scrape)
        response.append(response_scrape)
        
    for i in autism_societyburnout:
        link = Request(i , headers={'User-Agent': 'Mozilla/5.0'})
        site = urlopen(link).read()
        soup = BeautifulSoup(site, "html.parser")
        soup.find("ul", class_="navigation__list").decompose()
        data_scrape, header_scrape, response_scrape = autism_society_burnout(soup)
        header.append(header_scrape)
        scraped_sites.append(data_scrape)
        response.append(response_scrape)
        
    for i in autism_societyanxiety:
        link = Request(i , headers={'User-Agent': 'Mozilla/5.0'})
        site = urlopen(link).read()
        soup = BeautifulSoup(site, "html.parser")
        soup.find("ul", class_="navigation__list").decompose()
        data_scrape, header_scrape, response_scrape = autism_society_anxiety(soup)
        header.append(header_scrape)
        scraped_sites.append(data_scrape)
        response.append(response_scrape)
        
    for i in autism_societysuicide:
        link = Request(i , headers={'User-Agent': 'Mozilla/5.0'})
        site = urlopen(link).read()
        soup = BeautifulSoup(site, "html.parser")
        data_scrape, header_scrape, response_scrape = autism_society_suicide(soup)
        header.append(header_scrape)
        scraped_sites.append(data_scrape)
        response.append(response_scrape)
    
    for i in autism_societyaddiction:
        link = Request(i , headers={'User-Agent': 'Mozilla/5.0'})
        site = urlopen(link).read()
        soup = BeautifulSoup(site, "html.parser")
        data_scrape, header_scrape, response_scrape = autism_society_addiction(soup)
        header.append(header_scrape)
        scraped_sites.append(data_scrape)
        response.append(response_scrape)
        
    for i in autism_societysensory:
        link = Request(i , headers={'User-Agent': 'Mozilla/5.0'})
        site = urlopen(link).read()
        soup = BeautifulSoup(site, "html.parser")
        data_scrape, header_scrape, response_scrape = autism_society_sensory(soup)
        header.append(header_scrape)
        scraped_sites.append(data_scrape)
        response.append(response_scrape)
    
    for i in autism_societyscreening:
        link = Request(i , headers={'User-Agent': 'Mozilla/5.0'})
        site = urlopen(link).read()
        soup = BeautifulSoup(site, "html.parser")
        data_scrape, header_scrape, response_scrape = autism_society_screening(soup)
        header.append(header_scrape)
        scraped_sites.append(data_scrape)
        response.append(response_scrape)
    
    for i in autism_societyscreeningtool:
        link = Request(i , headers={'User-Agent': 'Mozilla/5.0'})
        site = urlopen(link).read()
        soup = BeautifulSoup(site, "html.parser")
        data_scrape, header_scrape, response_scrape = autism_society_screening_tool(soup)
        header.append(header_scrape)
        scraped_sites.append(data_scrape)
        response.append(response_scrape)
    
    for i in nhs_cbt:
        link = Request(i , headers={'User-Agent': 'Mozilla/5.0'})
        site = urlopen(link).read()
        soup = BeautifulSoup(site, "html.parser")
        data_scrape, header_scrape, response_scrape = nhs_cbt_thrp(soup)
        header.append(header_scrape)
        scraped_sites.append(data_scrape)
        response.append(response_scrape)
    
    for i in nhs_dbt:
        link = Request(i , headers={'User-Agent': 'Mozilla/5.0'})
        site = urlopen(link).read()
        soup = BeautifulSoup(site, "html.parser")
        data_scrape, header_scrape, response_scrape = nhs_dbt_thrp(soup)
        header.append(header_scrape)
        scraped_sites.append(data_scrape)
        response.append(response_scrape)
        
    for i in autism_societylonely:
        link = Request(i , headers={'User-Agent': 'Mozilla/5.0'})
        site = urlopen(link).read()
        soup = BeautifulSoup(site, "html.parser")
        data_scrape, header_scrape, response_scrape = autism_society_lonely(soup)
        header.append(header_scrape)
        scraped_sites.append(data_scrape)
        response.append(response_scrape)
        
    for i in autism_societydepression:
        link = Request(i , headers={'User-Agent': 'Mozilla/5.0'})
        site = urlopen(link).read()
        soup = BeautifulSoup(site, "html.parser")
        data_scrape, header_scrape, response_scrape = autism_society_depression(soup)
        header.append(header_scrape)
        scraped_sites.append(data_scrape)
        response.append(response_scrape)
    
    for i in autism_societyothercon:
        link = Request(i , headers={'User-Agent': 'Mozilla/5.0'})
        site = urlopen(link).read()
        soup = BeautifulSoup(site, "html.parser")
        data_scrape, header_scrape, response_scrape = autism_society_other_con(soup)
        header.append(header_scrape)
        scraped_sites.append(data_scrape)
        response.append(response_scrape)
    
    for i in autism_societybullying:
        link = Request(i , headers={'User-Agent': 'Mozilla/5.0'})
        site = urlopen(link).read()
        soup = BeautifulSoup(site, "html.parser")
        data_scrape, header_scrape, response_scrape = autism_society_bullying(soup)
        header.append(header_scrape)
        scraped_sites.append(data_scrape)
        response.append(response_scrape)
        
    for i in autism_societyinsom:
        link = Request(i , headers={'User-Agent': 'Mozilla/5.0'})
        site = urlopen(link).read()
        soup = BeautifulSoup(site, "html.parser")
        data_scrape, header_scrape, response_scrape = autism_society_insom(soup)
        header.append(header_scrape)
        scraped_sites.append(data_scrape)
        response.append(response_scrape)
        
    for i in beyondAutism:
        link = requests.get(i)
        link.encoding = None
        soup = BeautifulSoup(link.text, "html.parser")
        if i != "https://www.beyondautism.org.uk/about-autism/understanding-autism/diagnosis/":
            data_scrape, header_scrape, response_scrape = beyond_autism(soup)
        else:
            data_scrape, header_scrape, response_scrape = beyond_autism_diag(soup)
        header.append(header_scrape)
        scraped_sites.append(data_scrape)
        response.append(response_scrape)
        
    for i in autismService:
        link = Request(i , headers={'User-Agent': 'Mozilla/5.0'})
        site = urlopen(link).read()
        soup = BeautifulSoup(site, "html.parser")
        data_scrape, header_scrape, response_scrape = autism_service(soup)
        header.append(header_scrape)
        scraped_sites.append(data_scrape)
        response.append(response_scrape)
    
    for i in theSpectrum:
        link = Request(i , headers={'User-Agent': 'Mozilla/5.0'})
        site = urlopen(link).read()
        soup = BeautifulSoup(site, "html.parser")
        data_scrape, header_scrape, response_scrape = the_spectrum(soup)
        header.append(header_scrape)
        scraped_sites.append(data_scrape)
        response.append(response_scrape)
    
    for i in autismAcceptweek:
        link = Request(i , headers={'User-Agent': 'Mozilla/5.0'})
        site = urlopen(link).read()
        soup = BeautifulSoup(site, "html.parser")
        data_scrape, header_scrape, response_scrape = autism_acceptweek(soup)
        header.append(header_scrape)
        scraped_sites.append(data_scrape)
        response.append(response_scrape)
    
    for i in autismMilton:
        link = requests.get(i)
        link.encoding = None
        soup = BeautifulSoup(link.text, "html.parser")
        data_scrape, header_scrape, response_scrape = autism_milton(soup)
        header.append(header_scrape)
        scraped_sites.append(data_scrape)
        response.append(response_scrape)
    
    for i in autismSurrey:
        link = Request(i , headers={'User-Agent': 'Mozilla/5.0'})
        site = urlopen(link).read()
        soup = BeautifulSoup(site, "html.parser")
        data_scrape, header_scrape, response_scrape = autism_surrey(soup)
        header.append(header_scrape)
        scraped_sites.append(data_scrape)
        response.append(response_scrape)
        
    for i in changeyourreaction:
        link = Request(i , headers={'User-Agent': 'Mozilla/5.0'})
        site = urlopen(link).read()
        soup = BeautifulSoup(site, "html.parser")
        data_scrape, header_scrape, response_scrape = change_your_reaction(soup)
        header.append(header_scrape)
        scraped_sites.append(data_scrape)
        response.append(response_scrape)

    data = data_separator(scraped_sites)
    header = data_separator(header)
    response = data_separator(response)
    
    return data, header, response 


# In[8]:


def sentence_clean(h_txt):
    punc = "."
    h_txt = h_txt.replace("-", " ")
    h_txt = re.sub(r'\s+', ' ', h_txt)
    h_txt = h_txt.replace("?", "")
    h_txt = h_txt.replace("‘", "")
    h_txt = h_txt.replace("’", "")
    h_txt = h_txt.replace("!", "")
    h_txt = h_txt.replace("/", " ")
    h_txt = h_txt.lstrip()
    h_txt = h_txt.rstrip()
    
    for txt in h_txt:
        if txt in punc:
            h_txt = h_txt.replace(txt, "")
            h_txt = h_txt.rstrip()
    
    return h_txt


# In[9]:


def autism_society_insom(soup):
    lst = []
    header_vector = []
    response = []
    
    h_txt = ""
    
    main = soup.find("div", {'class':'col-xs-12 col-sm-12 col-md-8 col-lg-8 guidance__main-content col'})
    h1 = main.find_all("h2")
    p1 = main.find("p")
    p1 = p1.text.strip()
    
    header_vector.append(sentence_clean("What links insomnia and Autism") + ".")
    header_vector.append(sentence_clean("insomnia is related to autism") + ".")
    header_vector.append(sentence_clean("Do autistic people have insomnia") + ".")
    header_vector.append(sentence_clean("Do they have insomnia") + ".")
    header_vector.append(sentence_clean("What links sleep and Autism") + ".")
    header_vector.append(sentence_clean("sleep is related to autism") + ".")
    header_vector.append(sentence_clean("sleeping") + ".")
    header_vector.append(sentence_clean("bad sleep") + ".")
    header_vector.append(sentence_clean("sleep") + ".")
    
    for i in h1:
        if i.text.strip() == "Why might I struggle to sleep?":
            for sib in i.find_next_siblings():
                if sib.name == "h2":
                    break
                else:
                    if sib.name=="ul":
                        bp = sib.findAll("li")
                        for j in bp:
                            h_txt += " "
                            h_txt += j.text.strip() + " "
                    else:
                        h_txt += " "
                        h_txt += sib.text.strip()
    
    h_txt = h_txt.strip()
    h_txt = h_txt.replace("\xa0", " ")
    lst.append("placeholder.")
    response.append(sentence_clean(h_txt) + ".")
    
    return lst, header_vector, response


# In[10]:


def autism_society_bullying_adult_alt():
    url = "https://www.autism.org.uk/advice-and-guidance/topics/bullying/bullying/autistic-adults"
    link = Request(url , headers={'User-Agent': 'Mozilla/5.0'})
    site = urlopen(link).read()
    soup = BeautifulSoup(site, "html.parser")
    soup.find("ul", class_="navigation__list").decompose()
    
    h_txt = ""
    main = soup.find("div", {'class':'col-xs-12 col-sm-12 col-md-8 col-lg-8 guidance__main-content col'})
    h1 = main.find_all("h2")
    
    for i in h1:
        if str(i.text.strip()) != "Bullying at work" and str(i.text.strip()) != "Equality Act 2010 and Northern Ireland Disability Act":
            continue
        else:
            for sib in i.find_next_siblings():
                if sib.name == "h2":
                    break
                else:
                    if sib.name=="ul":
                        bp = sib.findAll("li")
                        for j in bp:
                            h_txt += " "
                            h_txt += j.text.strip() + " "
                    else:
                        h_txt += " "
                        h_txt += sib.text.strip()
            h_txt += " "
    
    return(h_txt)


# In[11]:


def autism_society_bullying(soup):
    lst = []
    header_vector = []
    response = []
    
    h_txt = ""
    main = soup.find("div", {'class':'col-xs-12 col-sm-12 col-md-8 col-lg-8 guidance__main-content col'})
    h1 = main.find_all("h2")
    
    
    header_vector.append(sentence_clean("What links bullying and Autism") + ".")
    header_vector.append(sentence_clean("bullying is related to autism") + ".")
    header_vector.append(sentence_clean("Do autistic people bullied") + ".")
    header_vector.append(sentence_clean("Bullying") + ".")
    header_vector.append(sentence_clean("Bullied") + ".")
    header_vector.append(sentence_clean("Bully") + ".")
    
    for i in h1:
        if str(i.text.strip()) != "Autistic children and bullying" and str(i.text.strip()) != "How to tell if your child is being bullied" and str(i.text.strip()) != "My child is bullying others":
            continue
        else:
            for sib in i.find_next_siblings():
                if sib.name == "h2":
                    break
                else:
                    if sib.name=="ul":
                        bp = sib.findAll("li")
                        for j in bp:
                            h_txt += " "
                            h_txt += j.text.strip() + " "
                    else:
                        h_txt += " "
                        h_txt += sib.text.strip()
            h_txt += " "
    
    h_txt = h_txt + " " + autism_society_bullying_adult_alt()
    h_txt = h_txt.strip()
    h_txt = h_txt.replace("\xa0", " ")
    h_txt = h_txt.replace("\u202f", " ")
    h_txt = h_txt.strip()
    
    lst.append("placeholder.")
    response.append(sentence_clean(h_txt) + ".")
    
    return lst, header_vector, response


# In[12]:


def autism_society_other_con(soup):
    lst = []
    header_vector = []
    response = []
    
    p = soup.find("strong")
    p = p.text.strip() + ": " + "This means that this and many other conditions are somewhat related to autism but also means that such conditions are not experienced by all autistic individuals: "

    h1 = soup.find("div", {'class':'col-xs-12 col-sm-12 col-md-8 col-lg-8 guidance__main-content col'})
    header = h1.find_all("h2")

    for i in header:
        h_txt = ""
        if str(i.get("paraid")) == "1489520295":
            header_vector.append(sentence_clean("What links ADHD and Autism") + ".")
            header_vector.append(sentence_clean("ADHD is related to autism") + ".")
            header_vector.append(sentence_clean("Do autistic people have ADHD") + ".")
            header_vector.append(sentence_clean("Do they have ADHD") + ".")
            header_vector.append(sentence_clean("ADHD") + ".")
            
            for sib in i.find_next_siblings():
                if sib.name == "h2":
                    break
                else:
                    if sib.name=="ul":
                        bp = sib.findAll("li")
                        for j in bp:
                            h_txt += " "
                            h_txt += j.text.strip() + " "
                    else:
                        h_txt += " "
                        h_txt += sib.text.strip()
            
            h_txt = p.strip() + h_txt.strip()
            lst.append("placeholder.")
            response.append(sentence_clean(h_txt) + ".")
            
            
        elif str(i.get("paraid")) == "1491392977":
            header_vector.append(sentence_clean("What links Dyslexia and Autism") + ".")
            header_vector.append(sentence_clean("Dyslexia is related to autism") + ".")
            header_vector.append(sentence_clean("Do autistic people have Dyslexia") + ".")
            header_vector.append(sentence_clean("Do they have Dyslexia") + ".")
            header_vector.append(sentence_clean("Are they dyslexic") + ".")
            header_vector.append(sentence_clean("Are autistic people dyslexic") + ".")
            header_vector.append(sentence_clean("Dyslexia") + ".")
            header_vector.append(sentence_clean("Dyslexic") + ".")
            
            for sib in i.find_next_siblings():
                if sib.name == "h2":
                    break
                else:
                    if sib.name=="ul":
                        bp = sib.findAll("li")
                        for j in bp:
                            h_txt += " "
                            h_txt += j.text.strip() + " "
                    else:
                        h_txt += " "
                        h_txt += sib.text.strip()
            
            h_txt = p.strip() + h_txt.strip()
            lst.append("placeholder.")
            response.append(sentence_clean(h_txt) + ".")
        
        elif str(i.get("paraid")) == "2046495":
            header_vector.append(sentence_clean("What links Dyspraxia and Autism") + ".")
            header_vector.append(sentence_clean("Dyspraxia is related to autism") + ".")
            header_vector.append(sentence_clean("Do autistic people have Dyspraxia") + ".")
            header_vector.append(sentence_clean("Do they have Dyspraxia") + ".")
            header_vector.append(sentence_clean("Are they dyspraxic") + ".")
            header_vector.append(sentence_clean("Are autistic people dyspraxic") + ".")
            header_vector.append(sentence_clean("Dyspraxia") + ".")
            header_vector.append(sentence_clean("Dyspraxic") + ".")
            
            for sib in i.find_next_siblings():
                if sib.name == "h2":
                    break
                else:
                    if sib.name=="ul":
                        bp = sib.findAll("li")
                        for j in bp:
                            h_txt += " "
                            h_txt += j.text.strip() + " "
                    else:
                        h_txt += " "
                        h_txt += sib.text.strip()
            
            h_txt = p.strip() + h_txt.strip()
            lst.append("placeholder.")
            response.append(sentence_clean(h_txt) + ".")
            
        elif str(i.get("paraid")) == "111667975":
            header_vector.append(sentence_clean("What links Epilepsy and Autism") + ".")
            header_vector.append(sentence_clean("Epilepsy is related to autism") + ".")
            header_vector.append(sentence_clean("Do autistic people have Epilepsy") + ".")
            header_vector.append(sentence_clean("Do they have Epilepsy") + ".")
            header_vector.append(sentence_clean("Are they Epileptic") + ".")
            header_vector.append(sentence_clean("Are autistic people Epileptic") + ".")
            header_vector.append(sentence_clean("Epilepsy") + ".")
            header_vector.append(sentence_clean("Epileptic") + ".")
            
            for sib in i.find_next_siblings():
                if sib.name == "h2":
                    break
                else:
                    if sib.name=="ul":
                        bp = sib.findAll("li")
                        for j in bp:
                            h_txt += " "
                            h_txt += j.text.strip() + " "
                    else:
                        h_txt += " "
                        h_txt += sib.text.strip()
            
            h_txt = p.strip() + h_txt.strip()
            lst.append("placeholder.")
            response.append(sentence_clean(h_txt) + ".")
            break
        else:
            continue
    
    return lst, header_vector, response


# In[13]:


def autism_society_depression(soup):
    lst = []
    header_vector = []
    response = []
    
    h_txt = ""
    h1 = soup.find_all("div", {'class':'rich-text-editor'})
    p1 = h1[0].text.strip()
    
    header = h1[3].find_all("h2")
    
    header_vector.append(sentence_clean("Depression is related to autism") + ".")
    header_vector.append(sentence_clean("What links depression and autism") + ".")
    header_vector.append(sentence_clean("Do autistic people have depression") + ".")
    header_vector.append(sentence_clean("Why are they depressed") + ".")
    header_vector.append(sentence_clean("low mood") + ".")
    header_vector.append(sentence_clean("Why are they sad") + ".")
    header_vector.append(sentence_clean("Do autistic people depressed") + ".")
    header_vector.append(sentence_clean("Depression") + ".")
    header_vector.append(sentence_clean("Depressed") + ".")
    header_vector.append(sentence_clean("sadness") + ".")
    header_vector.append(sentence_clean("sad") + ".")
    
    
    for i in header:
        if i.text.strip() == "What is depression?" or i.text.strip() == "Why might autistic people experience depression?":
            for sib in i.find_next_siblings():
                if sib.name == "h2":
                    break
                else:
                    if sib.name=="ul":
                        bp = sib.findAll("li")
                        for j in bp:
                            h_txt += " "
                            h_txt += j.text.strip() + " "
                    else:
                        h_txt += " "
                        h_txt += sib.text.strip()
    
    h_txt = p1.strip() + " " + h_txt.strip()
    h_txt = h_txt.replace("\n", " ")
    h_txt = h_txt.replace("\xa0", " ")
    
    lst.append("placeholder.")
    response.append(sentence_clean(h_txt) + ".")
    
    return lst, header_vector, response


# In[14]:


def autism_society_lonely(soup):
    lst = []
    header_vector = []
    response = []
    
    h_txt = ""
    h1 = soup.find_all("div", {'class':'rich-text-editor'})
    p1 = h1[0].text.strip()
    
    header = h1[3].find_all("h2")
    
    header_vector.append(sentence_clean("Are autistic people lonely") + ".")
    header_vector.append(sentence_clean("What links loneliness and autism") + ".")
    header_vector.append(sentence_clean("Loneliness is related to autism") + ".")
    header_vector.append(sentence_clean("Do autistic people feel lonely") + ".")
    header_vector.append(sentence_clean("Why are they lonely") + ".")
    header_vector.append(sentence_clean("Feel alone") + ".")
    header_vector.append(sentence_clean("Feel lonely") + ".")
    header_vector.append(sentence_clean("Loneliness") + ".")
    header_vector.append(sentence_clean("lonely") + ".")
    
    for i in header:
        if i.text.strip() == "What is loneliness?" or i.text.strip() == "Why might I feel lonely?":
            for sib in i.find_next_siblings():
                if sib.name == "h2":
                    break
                else:
                    if sib.name=="ul":
                        bp = sib.findAll("li")
                        for j in bp:
                            h_txt += " "
                            h_txt += j.text.strip() + " "
                    else:
                        h_txt += " "
                        h_txt += sib.text.strip()
    
    h_txt = p1.strip() + " " + h_txt.strip()
    h_txt = h_txt.replace("\n", " ")
    h_txt = h_txt.replace("\xa0", " ")
    
    lst.append("placeholder.")
    response.append(sentence_clean(h_txt) + ".")
    
    return lst, header_vector, response


# In[15]:


def nhs_dbt_thrp(soup):
    lst = []
    header_vector = []
    response = []
    
    h_txt = ""

    main = soup.find("main", {'class':'nhsuk-main-wrapper nhsuk-u-padding-top-0 nhsuk-u-padding-top-0'})
    hd = main.find_all("h3")
    
    header_vector.append(sentence_clean("What is Dialectical behaviour therapy") + ".")
    header_vector.append(sentence_clean("What does Dialectical behaviour therapy mean") + ".")
    header_vector.append(sentence_clean("What is DBT") + ".")
    header_vector.append(sentence_clean("What does DBT mean") + ".")
    header_vector.append(sentence_clean("Dialectical behaviour therapy") + ".")
    header_vector.append(sentence_clean("DBT") + ".")
    
    for i in hd:
        if str(i.get("data-block-key")) != "vv64m":
            continue
        else:
            for sib in i.find_next_siblings():
                if sib.name == "h3":
                    break
                else:
                    if sib.name=="ul":
                        bp = sib.findAll("li")
                        for j in bp:
                            h_txt += " "
                            h_txt += j.text.strip() + " "
                    else:
                        h_txt += " "
                        h_txt += sib.text.strip()
    
    lst.append("placeholder.")
    response.append(sentence_clean(h_txt) + ".")
    
    return lst, header_vector, response


# In[16]:


def nhs_cbt_thrp(soup):
    lst = []
    header_vector = []
    response = []
    
    h_txt = ""
    p1 = soup.find("p", {'data-block-key':'rsr61'})
    p2 = soup.find("p", {'data-block-key':'uutua'})
    
    main = soup.find("main", {'class':'nhsuk-main-wrapper nhsuk-u-padding-top-0 nhsuk-u-padding-top-0'})
    hd = main.find_all("h2")
    
    header_vector.append(sentence_clean("What is Cognitive behavioural therapy") + ".")
    header_vector.append(sentence_clean("What does Cognitive behavioural therapy mean") + ".")
    header_vector.append(sentence_clean("What is CBT") + ".")
    header_vector.append(sentence_clean("What does CBT mean") + ".")
    header_vector.append(sentence_clean("Cognitive behavioural therapy") + ".")
    header_vector.append(sentence_clean("CBT") + ".")
    
    for i in hd:
        if i.text.strip() != "How CBT works":
            continue
        else:
            for sib in i.find_next_siblings():
                if sib.name == "h2":
                    break
                else:
                    h_txt += " "
                    h_txt += sib.text.strip()
    
    h_txt = p1.text.strip() + " " + p2.text.strip() + h_txt.strip()
    
    lst.append("placeholder.")
    response.append(sentence_clean(h_txt) + ".")
    
    return lst, header_vector, response


# In[17]:


def autism_society_screening_tool(soup):
    lst = []
    header_vector = []
    response = []
    
    main = soup.find("div", {'class':'col-xs-12 col-sm-12 col-md-8 col-lg-8 guidance__main-content col'})
    h2 = main.find_all("h2")
    
    for header in h2:
        h_txt = ""
        if str(header.get("paraid")) == "1381090807":
            header_vector.append(sentence_clean("What is DISCO") + ".")
            header_vector.append(sentence_clean("What does DISCO mean") + ".")
            header_vector.append(sentence_clean("What is the DISCO") + ".")
            header_vector.append(sentence_clean("DISCO") + ".")
            
            for sib in header.find_next_siblings():
                if sib.name == "h2":
                    break
                else:
                    h_txt += " "
                    h_txt += sib.text.strip()
            
            lst.append("placeholder.")
            response.append(sentence_clean(h_txt) + ".")
                 
        elif str(header.get("paraid")) == "833611272":
            header_vector.append(sentence_clean("What is ADOS") + ".")
            header_vector.append(sentence_clean("What does ADOS mean") + ".")
            header_vector.append(sentence_clean("What is the ADOS") + ".")
            header_vector.append(sentence_clean("ADOS") + ".")
            
            for sib in header.find_next_siblings():
                if sib.name == "h2":
                    break
                else:
                    h_txt += " "
                    h_txt += sib.text.strip()
            
            lst.append("placeholder.")
            response.append(sentence_clean(h_txt) + ".")
             
        elif str(header.get("paraid")) == "978153277":
            header_vector.append(sentence_clean("What is ADIR") + ".")
            header_vector.append(sentence_clean("What does ADIR mean") + ".")
            header_vector.append(sentence_clean("What is the ADIR") + ".")
            header_vector.append(sentence_clean("ADIR") + ".")

            
      
            for sib in header.find_next_siblings():
                if sib.name == "h2":
                    break
                else:
                    h_txt += " "
                    h_txt += sib.text.strip()
                    
            lst.append("placeholder.")
            response.append(sentence_clean(h_txt) + ".")
            break
        
        else:
            break
    
    return lst, header_vector, response


# In[18]:


def autism_society_screening(soup):
    lst = []
    header_vector = []
    response = []
    
    h_txt = ""
    
    main = soup.find("strong")
    h_txt = main.text.strip()
    h_txt = h_txt.replace("\xa0", " ")
    
    header_vector.append(sentence_clean("What screening tools are there") + ".")
    header_vector.append(sentence_clean("What diagnosis tools are available") + ".")
    header_vector.append(sentence_clean("What diagnostic tools are there") + ".")
    header_vector.append(sentence_clean("What testing tools are available") + ".")
    header_vector.append(sentence_clean("What tests are there") + ".")
    
    lst.append("placeholder.")
    response.append(sentence_clean(h_txt) + ".")
    
    return lst, header_vector, response


# In[19]:


def autism_society_sensory(soup):
    lst = []
    header_vector = []
    response = []
    
    num = 0
    h_txt = ""
    
    main = soup.find_all("div", {'class':'generic-section generic-section--one-column generic-section--h-left header-straight footer-straight padding-top-none padding-bottom-xs'})


    for section in main:
        if num != 2:
            num += 1
            continue
        else:
            h_txt += section.text.strip()
            h_txt = h_txt.replace("\n", " ")
            h_txt = h_txt.strip()
            break
    
    header_vector.append(sentence_clean("Do autistic people feel pain") + ".")
    header_vector.append(sentence_clean("Why do autistic people hate bright lights") + ".")
    header_vector.append(sentence_clean("Why do autistic people hate noise") + ".")
    header_vector.append(sentence_clean("Why do they hate noise") + ".")
    header_vector.append(sentence_clean("Do they hate loud music") + ".")
    header_vector.append(sentence_clean("loud music") + ".")
    header_vector.append(sentence_clean("loud noises") + ".")
    header_vector.append(sentence_clean("being touched") + ".")
    header_vector.append(sentence_clean("itchy") + ".")
    header_vector.append(sentence_clean("bright light") + ".")
    header_vector.append(sentence_clean("bright lights") + ".")
    header_vector.append(sentence_clean("smells") + ".")
    header_vector.append(sentence_clean("smell of") + ".")
    header_vector.append(sentence_clean("feel of") + ".")
    header_vector.append(sentence_clean("sound of") + ".")
    header_vector.append(sentence_clean("colour") + ".")
    header_vector.append(sentence_clean("color") + ".")
    header_vector.append(sentence_clean("feel pain") + ".")
    header_vector.append(sentence_clean("getting hugged") + ".")
    header_vector.append(sentence_clean("hugged") + ".")
    header_vector.append(sentence_clean("hug") + ".")
    header_vector.append(sentence_clean("hearing") + ".")
    header_vector.append(sentence_clean("hears") + ".")
    header_vector.append(sentence_clean("touching") + ".")
    header_vector.append(sentence_clean("touch") + ".")
    header_vector.append(sentence_clean("touches") + ".")
    header_vector.append(sentence_clean("touched") + ".")
    header_vector.append(sentence_clean("kiss") + ".")
    header_vector.append(sentence_clean("kissed") + ".")
    header_vector.append(sentence_clean("taste of") + ".")
    header_vector.append(sentence_clean("taste") + ".")
    
    lst.append("placeholder.")
    response.append(sentence_clean(h_txt) + ".")
    
    return lst, header_vector, response


# In[20]:


def autism_society_addiction(soup):
    h_txt = ""
    
    lst = []
    header_vector = []
    response = []
    
    main = soup.find("div", {'class':'generic-section generic-section--one-column generic-section--h-left header-straight footer-straight padding-top-none padding-bottom-none'})
    h2 = main.find_all("h2")
    p1 = soup.find("div", {'class':'rich-text-editor'})
    p1 = p1.text.strip()
    
    header_vector.append(sentence_clean("What links addiction and autism") + ".")
    header_vector.append(sentence_clean("Do autistic people have addiction") + ".")
    header_vector.append(sentence_clean("Addiction is related to autism") + ".")
    header_vector.append(sentence_clean("Why are autistic people addicted") + ".")
    header_vector.append(sentence_clean("Why are they addicted") + ".")
    header_vector.append(sentence_clean("Why do they have addiction") + ".")
    header_vector.append(sentence_clean("Why are they addicted to") + ".")
    header_vector.append(sentence_clean("drinking so much") + ".")
    header_vector.append(sentence_clean("are they addicts") + ".")
    header_vector.append(sentence_clean("alcohol") + ".")
    header_vector.append(sentence_clean("alcoholic") + ".")
    header_vector.append(sentence_clean("booze") + ".")
    header_vector.append(sentence_clean("drink a lot") + ".")
    header_vector.append(sentence_clean("substance abuse") + ".")
    header_vector.append(sentence_clean("drugs") + ".")
    header_vector.append(sentence_clean("narcotic") + ".")
    header_vector.append(sentence_clean("gambling") + ".")
    
    for i in h2:
        if i.text.strip() != "Why might autistic people develop addictions?":
            continue
        else:
            for sib in i.find_next_siblings():
                if sib.name == "div":
                    break
                else:
                    if sib.name=="ul":
                        bp = sib.findAll("li")
                        for i in bp:
                            h_txt += " "
                            h_txt += i.text.strip() + " "
                    else:
                        h_txt += " "
                        h_txt += sib.text.strip()
    
    h_txt = h_txt.replace("\n", " ")
    h_txt = h_txt.replace("\xa0", " ")
    h_txt = h_txt.replace("\xa0", " ")
    h_txt = p1 + " " + h_txt
    h_txt = h_txt.strip()
    lst.append("placeholder.")
    response.append(sentence_clean(h_txt) + ".")
    
    return lst, header_vector, response


# In[21]:


def autism_society_suicide(soup):
    lst = []
    header_vector = []
    response = []
    
    topic = 0

    while topic != 2:
        if topic == 0:
            h_txt = ""
            p2txt = ""
            p3 = ""
            num = 0
            
            content = soup.find_all("div", {'class':'rich-text-editor'})
            h1 = soup.find("div", {'class':'content-block content-block--vibrant-purple'})
            h2 =  soup.find("div", {'class':'rich-text-editor'})
            p1 = h1.text.strip()
            p2 = h2.find_all("p")
            
            
            header_vector.append(sentence_clean("What links Suicide and Autism") + ".")
            header_vector.append(sentence_clean("Why are autistic people suicidal") + ".")
            header_vector.append(sentence_clean("Why are they suicidal") + ".")
            header_vector.append(sentence_clean("kill themselves") + ".")
            header_vector.append(sentence_clean("kill myself") + ".")
            header_vector.append(sentence_clean("Why do they have Suicidal") + ".")
            header_vector.append(sentence_clean("do they have dark thoughts") + ".")
            header_vector.append(sentence_clean("Suicidal thoughts") + ".")
            header_vector.append(sentence_clean("Dark thoughts") + ".")
            header_vector.append(sentence_clean("suicide") + ".")
            
            for i in p2:
                p2txt += i.text.strip() + " "
            p2 = p2txt.strip()
            
            for i in content:
                if num != 3:
                    num += 1
                    continue
                else:
                    header = i.find_all("h2")
                    for j in header:
                        if j.text.strip() != "Why might you feel suicidal?" and j.text.strip() != "How common is suicide for autistic people?":
                            continue
                        else:
                            for sib in j.find_next_siblings():
                                if sib.name == "h2":
                                    break
                                else:
                                    if sib.name=="ul":
                                        bp = sib.findAll("li")
                                        for i in bp:
                                            p3 += " "
                                            p3 += i.text.strip() + " "
                                    else:
                                        p3 += " "
                                        p3 += sib.text.strip()
                break
            p3 = p3.strip()
            h_txt = p1 + " " + p2 + " " + p3
            h_txt = h_txt.replace("\n", " ")
            h_txt = h_txt.strip()
            lst.append("placeholder.")
            response.append(sentence_clean(h_txt) + ".")
            topic += 1
            continue
                 
        else:
            h_txt = ""
            h3 = soup.find_all("h3")
            
            header_vector.append(sentence_clean("Where can I find autism therapy") + ".")
            header_vector.append(sentence_clean("What therapy is available") + ".")
            header_vector.append(sentence_clean("What therapies are available") + ".")
            header_vector.append(sentence_clean("How do I get therapy") + ".")
            header_vector.append(sentence_clean("Can therapy help") + ".")
            header_vector.append(sentence_clean("Where can I find autism therapist") + ".")
            header_vector.append(sentence_clean("What therapists are available") + ".")
            header_vector.append(sentence_clean("How do I get therapist") + ".")
            header_vector.append(sentence_clean("Can therapist help") + ".")
            
            for i in h3:
                if i.text.strip() != "Therapies":
                    continue
                else:
                    for sib in i.find_next_siblings():
                        if sib.name == "h3":
                            break
                        else:
                            if sib.name=="ul":
                                bp = sib.findAll("li")
                                for i in bp:
                                    h_txt += " "
                                    h_txt += i.text.strip() + " "
                            else:
                                h_txt += " "
                                h_txt += sib.text.strip()
            
            lst.append("placeholder.")
            response.append(sentence_clean(h_txt) + ".")
            topic += 1
            break
    
    return lst, header_vector, response


# In[22]:


def autism_society_anxiety(soup):
    num = 0
    
    lst = []
    header_vector = []
    response = []
    
    h1 = soup.find("div", {'class':'generic-section generic-section--one-column generic-section--h-left header-straight footer-straight padding-top-xs padding-bottom-none'})
    p1 = h1.find("p")
    h2 = soup.find("div", {'class':'content-block content-block--vibrant-purple'})
    p2 = h2.find("p")
    h3 = soup.find_all("div", {'class':'rich-text-editor'})
    
    header_vector.append(sentence_clean("What links Anxiety and Autism") + ".")
    header_vector.append(sentence_clean("Anxiety is related to autism") + ".")
    header_vector.append(sentence_clean("Stress is related to autism") + ".")
    header_vector.append(sentence_clean("Why are autistic people anxious") + ".")
    header_vector.append(sentence_clean("Do autistic people have Anxiety") + ".")
    header_vector.append(sentence_clean("Do they have Anxiety") + ".")
    header_vector.append(sentence_clean("Are they anxious") + ".")
    header_vector.append(sentence_clean("Anxiety") + ".")
    header_vector.append(sentence_clean("What links stress and Autism") + ".")
    header_vector.append(sentence_clean("Why are autistic people stressed") + ".")
    header_vector.append(sentence_clean("Do autistic people have stress") + ".")
    header_vector.append(sentence_clean("Do they have stress") + ".")
    header_vector.append(sentence_clean("Are they stressed") + ".")
    
    for i in h3:
        if num != 4:
            num += 1
            continue
        else:
            txt = i.text.strip()
            p3 = txt.replace("\n", " ")
            break
    
    
    
    txt = p1.text.strip() + " " + p2.text.strip() + " " + p3.strip()
    lst.append("placeholder.")
    response.append(sentence_clean(txt) + ".")
    
    return lst, header_vector, response


# In[23]:


def autism_society_burnout(soup):
    lst = []
    header_vector = []
    response = []
    
    main = soup.find("div", {'class':'col-xs-12 col-sm-12 col-md-8 col-lg-8 guidance__main-content col'})
    header = main.find_all("h2")
    h_txt = ""
    
    header_vector.append(sentence_clean("What is autistic fatigue") + ".")
    header_vector.append(sentence_clean("What does autistic fatigue mean") + ".")
    header_vector.append(sentence_clean("What is autistic burnout") + ".")
    header_vector.append(sentence_clean("What does autistic burnout mean") + ".")
    header_vector.append(sentence_clean("Why are autistic people tired") + ".")
    header_vector.append(sentence_clean("Why do they feel exhausted") + ".")
    header_vector.append(sentence_clean("Why are they fatigued") + ".")
    header_vector.append(sentence_clean("Why are they Burned Out") + ".")
    header_vector.append(sentence_clean("Why are they tired") + ".")
    header_vector.append(sentence_clean("Why are autistic people have headaches") + ".")
    header_vector.append(sentence_clean("Why do they have headaches") + ".")
    header_vector.append(sentence_clean("Fatigue") + ".")
    header_vector.append(sentence_clean("Burnout") + ".")
    header_vector.append(sentence_clean("Exhausted") + ".")
    header_vector.append(sentence_clean("headache") + ".")
    
    for h2 in header:
        if str(h2.get('paraid')) != "2030407110" and str(h2.get('paraid')) != "273466803":
            break
        else:
            for sib in h2.find_next_siblings():
                if sib.name == "h2":
                    break
                else:
                    if sib.name=="ul":
                        bp = sib.findAll("li")
                        for i in bp:
                            h_txt += " "
                            h_txt += i.text.strip() + " "
                    else:
                        h_txt += " "
                        h_txt += sib.text.strip()
                    
            h_txt = h_txt.strip()

    lst.append("placeholder.")
    response.append(sentence_clean(h_txt) + ".")
    
    return lst, header_vector, response


# In[24]:


def change_your_reaction(soup):
    lst = []
    header_vector = []
    response = []
    num = 0
    
    main = soup.find_all("div", {'class':'faqpanel'})
    
    for i in main:
        txt = ""
        
        if num == 4:
            header_vector.append(sentence_clean("Do they look different") + ".")
            header_vector.append(sentence_clean("do autistic people look different") + ".")
            header_vector.append(sentence_clean("What do they look like") + ".")
            header_vector.append(sentence_clean("Do they look any different") + ".")
            header_vector.append(sentence_clean("look like") + ".")
            header_vector.append(sentence_clean("hidden disability") + ".")
            header_vector.append(sentence_clean("look different") + ".")
            txt = i.text.strip()
            txt = txt.replace('\n', ' ')
            
            lst.append("placeholder.")
            response.append(sentence_clean(txt) + ".")
            num += 1
            continue
        
        elif num == 6:
            header_vector.append(sentence_clean("do autistic people lack empathy") + ".")
            header_vector.append(sentence_clean("do they lack emotions") + ".")
            header_vector.append(sentence_clean("do autistic people lack emotions") + ".")
            header_vector.append(sentence_clean("are they emotionless") + ".")
            header_vector.append(sentence_clean("are people with autism emotionless") + ".")
            header_vector.append(sentence_clean("do they have emotions") + ".")
            header_vector.append(sentence_clean("do they have feelings") + ".")
            header_vector.append(sentence_clean("emotionless") + ".")
            header_vector.append(sentence_clean("emotions") + ".")
            header_vector.append(sentence_clean("sympathy") + ".")
            txt = i.text.strip()
            txt = txt.replace('\n', ' ')
            txt = txt.replace('Yes. ', '')
            
            lst.append("placeholder.")
            response.append(sentence_clean(txt) + ".")
            break
        
        else:
            num += 1
            continue
    
    return lst, header_vector, response


# In[25]:


def autism_surrey(soup):
    lst = []
    header_vector = []
    response = []
    h_txt = ""
    num = 0
    
    main = soup.find_all("div", {'class':'wpb_wrapper'})
    
    header_vector.append(sentence_clean("How common is autism") + ".")
    header_vector.append(sentence_clean("What are the rates of autism") + ".")
    header_vector.append(sentence_clean("How many are autistic") + ".")
    header_vector.append(sentence_clean("rates of autism") + ".")
    header_vector.append(sentence_clean("autism rates") + ".")
    
    for i in main:
        if num != 5:
            num += 1
            continue
        else:
            h_txt += i.text.strip()
            break
    
    lst.append("placeholder.")
    response.append(sentence_clean(h_txt) + ".")
    
    return lst, header_vector, response


# In[26]:


def autism_milton(soup):
    lst = []
    header_vector = []
    response = []
    h_txt = ""
    num = 0
    
    main = soup.find("div", {'class':'field field--name-localgov-text field--type-text-long field--label-hidden field__items'})
    p = main.find_all("p")
    
    header_vector.append(sentence_clean("do only children get autism") + ".")
    header_vector.append(sentence_clean("can adults get autism") + ".")
    header_vector.append(sentence_clean("do only kids have autism") + ".")
    header_vector.append(sentence_clean("can adults have autism") + ".")
    
    for i in p:
        if num != 1:
            num += 1
            continue
        else:
            h_txt += i.text.strip()
            break
    
    h_txt += " " + "This means that anybody at any age can be autistic"
    
    lst.append("placeholder.")
    response.append(sentence_clean(h_txt) + ".")
    
    return lst, header_vector, response


# In[27]:


def nhs_bornwithautism(soup):
    lst = []
    header_vector = []
    response = []
    
    main = soup.find("div", {'class':'editor'})
    p = main.find("p")
    
    header_vector.append(sentence_clean("born with autism") + ".")
    header_vector.append(sentence_clean("can you be born with autism") + ".")
    header_vector.append(sentence_clean("autism from birth") + ".")
    header_vector.append(sentence_clean("born with it") + ".")
    header_vector.append(sentence_clean("present from birth") + ".")
    header_vector.append(sentence_clean("are people born with autism") + ".")
    
    txt = p.text.strip()
    
    lst.append("placeholder.")
    response.append(sentence_clean(txt) + ".")
    
    return lst, header_vector, response


# In[28]:


def autism_acceptweek(soup):
    lst = []
    header_vector = []
    response = []
    
    main = soup.find("div", {'class':'fusion-text fusion-text-19'})
    
    header_vector.append(sentence_clean("What is autism acceptance week") + ".")
    header_vector.append(sentence_clean("What is autism acceptance day") + ".")

    txt = main.text.strip()
    txt =  txt.replace("\n", " ")
    
    lst.append("placeholder.")
    response.append(sentence_clean(txt) + ".")
    
    return lst, header_vector, response


# In[29]:


def the_spectrum(soup):
    main = soup.findAll("section", {'class':'content-section content-section--faq-questions content-section--with-anchor'})
    
    buttons = soup.find_all(class_='button')
    for i in buttons:
        i.decompose()
        
    lst = []
    header_vector = []
    response = []
    
    hd_loop_1 = ["Is autism a disability?", "Is autism a learning disability?", "Is autism genetic?", "Can autism run in the family?"]
    hd_loop_2 = ["Why is Asperger’s syndrome not diagnosed anymore?", "Is there an autism diagnosis test online?", "How do you tell someone that you have autism?"]
    hd_loop_4 = ["What is ABA therapy?"]
    hd_loop_5 = ["What date is World Autism Awareness day?", "Why is autism more prevalent today than it was in previous decades?"]
    
    num = 0
    
    for i in main:
        if num == 0:
            header = i.findAll("h3")
            for j in header:
                if j.text.strip() not in hd_loop_1:
                    continue
                elif j.text.strip() == "Is autism a disability?":
                    header_vector.append(sentence_clean(str(j.text.strip())) + ".")
                    header_vector.append(sentence_clean("Are autistic people disabled") + ".")
                    header_vector.append(sentence_clean("Are people with autism disabled") + ".")
                    
                elif j.text.strip() == "Is autism a learning disability?":
                    header_vector.append(sentence_clean(str(j.text.strip())) + ".")
                    header_vector.append(sentence_clean("Are autistic people mentally disabled") + ".")
                    header_vector.append(sentence_clean("Are people with autism mentally disabled") + ".")
                    header_vector.append(sentence_clean("retarded") + ".")
                    header_vector.append(sentence_clean("retard") + ".")
                    header_vector.append(sentence_clean("learning disability") + ".")
                elif j.text.strip() == "Is autism genetic?":
                    header_vector.append(sentence_clean(str(j.text.strip())) + ".")
                elif j.text.strip() == "Can autism run in the family?":
                    header_vector.append(sentence_clean(str(j.text.strip())) + ".")
                    header_vector.append(sentence_clean("Is autism hereditary") + ".")
                else:
                    header_vector.append(sentence_clean(str(j.text.strip())) + ".")
                
                h_txt = j.text.strip() + ": "
                
                for sib in j.find_next_siblings():
                    if sib.name == "h3":
                        break
                    else:
                        h_txt += " "
                        h_txt += sib.text
                
                lst.append("placeholder.")
                h_txt = h_txt.replace("Here is a list of the developmental signs of autism in early childhood", "")
                h_txt = h_txt.replace("Here is a checklist of signs of autism in school years", "")
                response.append(sentence_clean(h_txt) + ".")

        
        elif num == 1:
            header = i.findAll("h3")
            for j in header:
                h_txt = ""
                if j.text.strip() not in hd_loop_2:
                    continue
                elif j.text.strip() == "Why is Asperger’s syndrome not diagnosed anymore?":
                    header_vector.append(sentence_clean(str(j.text.strip())) + ".")
                    header_vector.append(sentence_clean("What is Asperger") + ".")
                    header_vector.append(sentence_clean("What is Aspergers") + ".")
                    header_vector.append(sentence_clean("Asperger") + ".")
                    header_vector.append(sentence_clean("Aspergers") + ".")
                    h_txt += "As this chatbot is designed to increase autism awareness then in the future then please refrain from using the word Asperger, this is because: "
                elif j.text.strip() == "Is there an autism diagnosis test online?":
                    header_vector.append(sentence_clean("get online autism diagnosis") + ".")
                    header_vector.append(sentence_clean("autism diagnosis online") + ".")
                    header_vector.append(sentence_clean("autism assessment online") + ".")
                    header_vector.append(sentence_clean("can get online autism assessment") + ".")
                else:
                    header_vector.append(sentence_clean("How can I tell someone that I have autism") + ".")
                    
                if h_txt == "":
                    h_txt = j.text.strip() + ": "
                
                for sib in j.find_next_siblings():
                    if sib.name == "h3":
                        break
                    else:
                        h_txt += " "
                        h_txt += sib.text
                    
                lst.append("placeholder.")
                h_txt = h_txt.replace("You can find out more about the diagnostic process here", "")
                response.append(sentence_clean(h_txt) + ".")  
                

        elif num == 2:
            num += 1
            continue

        elif num == 3:
            header = i.findAll("h3")
            for j in header:
                if j.text.strip() not in hd_loop_4:
                    continue
                else:
                    header_vector.append(sentence_clean(str(j.text.strip())) + ".")
                    header_vector.append(sentence_clean("What is Applied Behaviour Analysis") + ".")
                    h_txt = j.text.strip() + " "
                    h_txt += "What is Applied Behaviour Analysis: "
                for sib in j.find_next_siblings():
                    if sib.name == "h3":
                        break
                    else:
                        h_txt += " "
                        h_txt += sib.text
                lst.append("placeholder.")
                response.append(sentence_clean(h_txt) + ".")
        
        else:
            header = i.findAll("h3")
            for j in header:
                if j.text.strip() not in hd_loop_5:
                    continue
                elif j.text.strip() == "What date is World Autism Awareness day?":
                    header_vector.append(sentence_clean(str(j.text.strip())) + ".")
                    header_vector.append(sentence_clean("When is World Autism Awareness week?") + ".")
                    h_txt = j.text.strip() + " "
                    h_txt += "When is World Autism Awareness day?: "
                else:
                    header_vector.append(sentence_clean("autism more prevalent today") + ".")
                    header_vector.append(sentence_clean("more cases of autism now") + ".")
                    header_vector.append(sentence_clean("more autistic people today") + ".")
                    h_txt = j.text.strip() + " "

                for sib in j.find_next_siblings():
                    if sib.name == "h3":
                        break
                    else:
                        h_txt += " "
                        h_txt += sib.text

                lst.append("placeholder.")
                response.append(sentence_clean(h_txt) + ".")

        num += 1
        
        
    
    return lst, header_vector, response


# In[30]:


def nhs_high_low(soup):
    lst = []
    header_vector = []
    response = []
    num = 0
    h_txt = ""
    
    main = soup.find("table", {'style':'width: 98.5216%;'})
    td = main.find_all("td", {'style':'width: 63.182%;'})
    
    header_vector.append(sentence_clean("What is high functioning autism") + ".")
    header_vector.append(sentence_clean("What does high functioning mean") + ".")
    header_vector.append(sentence_clean("What is low functioning autism") + ".")
    header_vector.append(sentence_clean("What does low functioning mean") + ".")
    header_vector.append(sentence_clean("high functioning ") + ".")
    header_vector.append(sentence_clean("low functioning ") + ".")
    
    for i in td:
        if num != 4:
            num += 1
            continue
        else:
            h_txt += i.text
            break
    
    lst.append("placeholder.")
    response.append(sentence_clean(h_txt) + ".")
    
    return lst, header_vector, response


# In[31]:


def autism_society_catatonia(soup):
    main = soup.find("div", {'class':'col-xs-12 col-sm-12 col-md-8 col-lg-8 guidance__main-content col'})
    header = main.findAll("h2")
    
    lst = []
    header_vector = []
    response = []
    
    for i in header:
        if str(i.get('paraid')) != "243629785":
            continue
        else:
            header_vector.append(sentence_clean("What is catatonia") + ".")
            header_vector.append(sentence_clean("What does catatonia mean") + ".")
            header_vector.append(sentence_clean("Is catatonia a form of autism") + ".")
            header_vector.append(sentence_clean("catatonia is related to autism") + ".")
            header_vector.append(sentence_clean("What links catatonia and Autism?") + ".")

            h_txt = i.text + ": "
            
            for sib in i.find_next_siblings():
                if sib.name=="h2":
                    break
                else:
                    if sib.name=="ul":
                            bp = sib.findAll("li")
                            for i in bp:
                                h_txt += " "
                                h_txt += i.text + " "
                    else:
                        h_txt += " "
                        h_txt += sib.text
                
            lst.append("placeholder.")
            response.append(sentence_clean(h_txt) + ".")
    
    return lst, header_vector, response


# In[32]:


def autism_society_girl_alt():
    h_txt = ""
    url = "https://www.autism.org.uk/advice-and-guidance/what-is-autism/autistic-women-and-girls"
    link = requests.get(url)
    link.encoding = None
    soup = BeautifulSoup(link.text, "html.parser")
    main = soup.find("div", {'class':'generic-section generic-section--one-column generic-section--h-left header-straight footer-straight padding-top-none padding-bottom-xs'})
    para = main.findAll("p")
    
    for i in para:
        h_txt += sentence_clean(i.text.strip()) + " "
        
    return h_txt


# In[33]:


def autism_society_medi_alt():
    h_txt = ""
    url = "https://www.autism.org.uk/advice-and-guidance/topics/mental-health/suicide"
    link = requests.get(url)
    link.encoding = None
    soup = BeautifulSoup(link.text, "html.parser")

    
    header = soup.findAll("h3")
    
    for i in header:
        if i.text.strip() != "Medication":
            continue
        else:
            for sib in i.find_next_siblings():
                if sib.name == "h3":
                    break
                else:
                    h_txt += sib.text.strip() + " "
    return(sentence_clean(h_txt))


# In[34]:


def nhs_treatment(soup):
    lst = []
    header_vector = []
    response = []
    
    main = soup.find("div", {'class':'nhsuk-main-wrapper nhsuk-u-padding-top-0 nhsuk-u-padding-top-0'})
    
    h1 = soup.find('p',{'data-block-key':'0tqqr'})
    h2 = soup.find('p',{'data-block-key':'c8nor'})
    h3 = soup.find('p',{'data-block-key':'a3gos'})
    p1h3 = soup.find('li',{'data-block-key':'nef0'})
    p2h3 = soup.find('li',{'data-block-key':'5thp7'})
    p3h3 = soup.find('li',{'data-block-key':'fnivl'})
    p4h3 = soup.find('li',{'data-block-key':'7dv7b'})
    p5h3 = soup.find('li',{'data-block-key':'2vll9'})
    p6h3 = soup.find('li',{'data-block-key':'2cfhu'})
    p7h3 = soup.find('li',{'data-block-key':'5qu74'})
    h4 = soup.find('p',{'data-block-key':'fc1mf'})
    p1h4 = soup.find('li',{'data-block-key':'8rvtu'})
    p2h4 = soup.find('li',{'data-block-key':'aihkf'})
    p3h4 = soup.find('li',{'data-block-key':'le8uu'})
    p4h4 = soup.find('li',{'data-block-key':'g1ul7'})
    p5h4 = soup.find('li',{'data-block-key':'jpgjf'})
    p6h4 = soup.find('li',{'data-block-key':'y0tnt'})
    p7h4 = soup.find('li',{'data-block-key':'t8rft'})
    p8h4 = soup.find('li',{'data-block-key':'fqgb2'})
    h5 = "However, in many cases then medication can still be utilised to subside autistic symptoms and other conditions exhaserbated by autism such as anxiety or depression as "
    
    header_vector.append(sentence_clean("GcMAF") + ".")
    header_vector.append(sentence_clean("Naltrexone") + ".")
    header_vector.append(sentence_clean("Secretin") + ".")
    header_vector.append(sentence_clean("bleaching") + ".")
    header_vector.append(sentence_clean("CEASE") + ".")
    header_vector.append(sentence_clean("chelation") + ".")
    header_vector.append(sentence_clean("secretin") + ".")
    header_vector.append(sentence_clean("camel milk") + ".")
    header_vector.append(sentence_clean("raw camel milk") + ".")
    header_vector.append(sentence_clean("vitamins") + ".")
    header_vector.append(sentence_clean("minerals") + ".")
    header_vector.append(sentence_clean("dietary supplements") + ".")
    header_vector.append(sentence_clean("chlorine dioxide") + ".")
    header_vector.append(sentence_clean("What medication is there") + ".")
    header_vector.append(sentence_clean("What medicine is there") + ".")
    header_vector.append(sentence_clean("Can camel milk cure autism") + ".")
    header_vector.append(sentence_clean("What medication can help") + ".")
    header_vector.append(sentence_clean("What treatments are available") + ".")
    header_vector.append(sentence_clean("What treatments are there") + ".")
    
    h_txt = h1.text.strip() + " " + h2.text.strip() + " " + h3.text.strip() + " " + p1h3.text.strip() + " " + p2h3.text.strip() + " " + p3h3.text.strip() + " " + p4h3.text.strip() + " " + p5h3.text.strip() + " " + p6h3.text.strip() + " " + p7h3.text.strip() + " " + h4.text.strip() + " " + p1h4.text.strip() + " " + p2h4.text.strip() + " " + p3h4.text.strip() + " " + p4h4.text.strip() + " " + p5h4.text.strip() + " " + p6h4.text.strip() + " " + p7h4.text.strip() + " " + p8h4.text.strip() + " " + h5 + " " + autism_society_medi_alt()
    h_txt = sentence_clean(h_txt)
    
    lst.append("placeholder.")
    response.append(sentence_clean(h_txt) + ".")
    
    
    return lst, header_vector, response


# In[35]:


def autism_society_find_job(soup):
    main = soup.find("div", {'class':'col-xs-12 col-sm-12 col-md-8 col-lg-8 guidance__main-content col'})
    header = main.findAll("h2")
    
    lst = []
    header_vector = []
    response = []
    
    for i in header:
        if i.text.strip() != "Looking for work":
            continue
        else:
            header_vector.append(sentence_clean("How do autistic people get jobs") + ".")
            header_vector.append(sentence_clean("How do I get work") + ".")
            header_vector.append(sentence_clean("How do I get a job") + ".")
            header_vector.append(sentence_clean("What jobs are available") + ".")
            header_vector.append(sentence_clean("What jobs are there") + ".")
            header_vector.append(sentence_clean("What work is available") + ".")
            header_vector.append(sentence_clean("Find a job") + ".")
            
            h_txt = i.text + ": "
            
            for sib in i.find_next_siblings():
                if sib.name=="h2":
                    break
                else:
                    if sib.name=="ul":
                            bp = sib.findAll("li")
                            for i in bp:
                                h_txt += " "
                                h_txt += i.text + " "
                    else:
                        h_txt += " "
                        h_txt += sib.text
                
            lst.append("placeholder.")
            response.append(sentence_clean(h_txt) + ".")
    
    return lst, header_vector, response


# In[36]:


def autism_society_change(soup):
    main = soup.find("div", {'class':'col-xs-12 col-sm-12 col-md-8 col-lg-8 guidance__main-content col'})
    header = main.findAll("h2")
    
    lst = []
    header_vector = []
    response = []
    
    for i in header:
        if str(i.get('paraid')) != "1892258899":
            continue
        else:
            header_vector.append(sentence_clean("Why do they hate change") + ".")
            header_vector.append(sentence_clean("Why are they fearful of change") + ".")
            header_vector.append(sentence_clean("do they hate change of plans") + ".")
            header_vector.append(sentence_clean("Why do autistic people hate change") + ".")
            header_vector.append(sentence_clean("change of plans") + ".")
            header_vector.append(sentence_clean("change of enviroment") + ".")
            header_vector.append(sentence_clean("why do they hate plans being changed") + ".")
            header_vector.append(sentence_clean("times being changed") + ".")
            header_vector.append(sentence_clean("change") + ".")
            header_vector.append(sentence_clean("What is change like") + ".")
            

            h_txt = i.text + ": "
            
            for sib in i.find_next_siblings():
                if sib.name=="h2":
                    break
                else:
                    if sib.name=="ul":
                            bp = sib.findAll("li")
                            for i in bp:
                                h_txt += " "
                                h_txt += i.text + " "
                    else:
                        h_txt += " "
                        h_txt += sib.text
                
            lst.append("placeholder.")
            response.append(sentence_clean(h_txt) + ".")
    
    return lst, header_vector, response


# In[37]:


def autism_society_distressed(soup):
    main = soup.find("div", {'class':'col-xs-12 col-sm-12 col-md-8 col-lg-8 guidance__main-content col'})
    header = main.findAll("h2")
    
    lst = []
    header_vector = []
    response = []
    
    for i in header:
        if i.text.strip() != "What causes distressed behaviour?":
            continue
        else:
            header_vector.append(sentence_clean(str(i.text)) + ".")
            header_vector.append(sentence_clean("Why do they bite") + ".")
            header_vector.append(sentence_clean("do they bite people") + ".")
            header_vector.append(sentence_clean("What causes them distress") + ".")
            header_vector.append(sentence_clean("Why did they spit") + ".")
            header_vector.append(sentence_clean("Why do they pinch") + ".")
            header_vector.append(sentence_clean("Why do they attack") + ".")
            header_vector.append(sentence_clean("Why did they attack me") + ".")
            header_vector.append(sentence_clean("Why did they hit me") + ".")
            header_vector.append(sentence_clean("Why are they upset") + ".")
            header_vector.append(sentence_clean("upset") + ".")
            header_vector.append(sentence_clean("pinch") + ".")
            header_vector.append(sentence_clean("attack") + ".")
            header_vector.append(sentence_clean("bite") + ".")
            header_vector.append(sentence_clean("spitting") + ".")
            header_vector.append(sentence_clean("Why do they scream") + ".")
            header_vector.append(sentence_clean("scream") + ".")
            h_txt = i.text + ": "
            
            for sib in i.find_next_siblings():
                if sib.name=="h2":
                    break
                else:
                    if sib.name=="ul":
                            bp = sib.findAll("li")
                            for i in bp:
                                h_txt += " "
                                h_txt += i.text + " "
                    else:
                        h_txt += " "
                        h_txt += sib.text
                
            lst.append("placeholder.")
            response.append(sentence_clean(h_txt) + ".")
    
    return lst, header_vector, response


# In[38]:


def autism_society_obsessions(soup):
    main = soup.find("div", {'class':'col-xs-12 col-sm-12 col-md-8 col-lg-8 guidance__main-content col'})
    header = main.findAll("h2")
    
    lst = []
    header_vector = []
    response = []
    
    for i in header:
        if i.text.strip() != "Intense interests" and i.text.strip() != "Repetitive behaviour":
            continue
        else:
            if str(i.get('paraid')) == "946262119":
                header_vector.append(sentence_clean(str(i.text)) + ".")
                header_vector.append(sentence_clean("Why do they have obsessive interests") + ".")
                header_vector.append(sentence_clean("do they have obsessive interests") + ".")
                header_vector.append(sentence_clean("do they so interested in things") + ".")
                header_vector.append(sentence_clean("Why are they fixated on certain topics") + ".")
                header_vector.append(sentence_clean("What obsessions do autisc people have") + ".")
                header_vector.append(sentence_clean("Hobbies") + ".")
                header_vector.append(sentence_clean("Obsession") + ".")
                header_vector.append(sentence_clean("Why are they obsessed with") + ".")
                header_vector.append(sentence_clean("Why are they engrossed with") + ".")

            elif str(i.get('paraid')) == "474478976":
                header_vector.append(sentence_clean(str(i.text)) + ".")
                header_vector.append(sentence_clean("Why do they repeat themselves") + ".")
                header_vector.append(sentence_clean("Why are they repeating me") + ".")
                header_vector.append(sentence_clean("Why do they repeat actions") + ".")
                header_vector.append(sentence_clean("Why do they rock") + ".")
                header_vector.append(sentence_clean("Why do they tap their finger") + ".")
                header_vector.append(sentence_clean("do they repeat") + ".")
                header_vector.append(sentence_clean("Why do they have repetitive movements") + ".")
                header_vector.append(sentence_clean("Why do autistic people have repetitive movements") + ".")
                header_vector.append(sentence_clean("do they have repetitive movements") + ".")
                header_vector.append(sentence_clean("Why do they flap their arms") + ".")
                header_vector.append(sentence_clean("Why do they flap their hands") + ".")
                header_vector.append(sentence_clean("Why do they head bang") + ".")
                header_vector.append(sentence_clean("Why do they finger flick") + ".")
                header_vector.append(sentence_clean("Why do they jump") + ".")
                header_vector.append(sentence_clean("Why do they spin") + ".")
                header_vector.append(sentence_clean("Why do they twirl") + ".")
                header_vector.append(sentence_clean("repetitive movements") + ".")
                header_vector.append(sentence_clean("body movements") + ".")
                header_vector.append(sentence_clean("move their body") + ".")
                header_vector.append(sentence_clean("move their bodies") + ".")
                header_vector.append(sentence_clean("What is repetitive behaviour in autism") + ".")
                
            h_txt = i.text + ": "
            
            for sib in i.find_next_siblings():
                if sib.name=="h2":
                    break
                else:
                    if sib.name=="ul":
                            bp = sib.findAll("li")
                            for i in bp:
                                h_txt += " "
                                h_txt += i.text + " "
                    else:
                        h_txt += " "
                        h_txt += sib.text
                
            lst.append("placeholder.")
            response.append(sentence_clean(h_txt) + ".")
    
    return lst, header_vector, response


# In[39]:


def autism_society_smear(soup):
    main = soup.find("div", {'class':'col-xs-12 col-sm-12 col-md-8 col-lg-8 guidance__main-content col'})
    header = main.findAll("h2")
    
    lst = []
    header_vector = []
    response = []
    
    for i in header:
        if str(i.get('paraid')) != "922552205":
            continue
        else:
            header_vector.append(sentence_clean("What is smearing") + ".")
            header_vector.append(sentence_clean("Why do they smear") + ".")
            header_vector.append(sentence_clean("Why do they smear faeces") + ".")
            header_vector.append(sentence_clean("Why do they rub faeces") + ".")
            header_vector.append(sentence_clean("are they not toilet trained") + ".")
            header_vector.append(sentence_clean("Why are they difficult to potty train") + ".")
            header_vector.append(sentence_clean("Why do they rub poo") + ".")
            header_vector.append(sentence_clean("Why do they smear poop") + ".")
            h_txt = i.text + ": "
            
            for sib in i.find_next_siblings():
                if sib.name=="h2":
                    break
                else:
                    if sib.name=="ul":
                            bp = sib.findAll("li")
                            for i in bp:
                                h_txt += " "
                                h_txt += i.text + " "
                    else:
                        h_txt += " "
                        h_txt += sib.text
                
            lst.append("placeholder.")
            response.append(sentence_clean(h_txt) + ".")
    
    return lst, header_vector, response


# In[40]:


def autism_society_harm(soup):
    main = soup.find("div", {'class':'col-xs-12 col-sm-12 col-md-8 col-lg-8 guidance__main-content col'})
    header = main.findAll("h2")
    comm = main.find("p", {'paraid':'2009906390'})
    
    lst = []
    header_vector = []
    response = []
    
    for i in header:
        if str(i.get('paraid')) != "2097410350":
            continue
        else:
            header_vector.append(sentence_clean("Why are they self destructive") + ".")
            header_vector.append(sentence_clean("Why are they self injurious") + ".")
            header_vector.append(sentence_clean("Why do autistic people hurt themselves") + ".")
            header_vector.append(sentence_clean("do autistic people hurt themselves") + ".")
            header_vector.append(sentence_clean("do they self harm") + ".")
            header_vector.append(sentence_clean("Why do they injure") + ".")
            header_vector.append(sentence_clean("do they hit") + ".")
            header_vector.append(sentence_clean("Why do they punch") + ".")
            header_vector.append(sentence_clean("Why do they bite themselves") + ".")
            h_txt = i.text + ": "
            
        for sib in i.find_next_siblings():
            if sib.name=="h2":
                break
            else:
                if sib.name=="ul":
                    bp = sib.findAll("li")
                    for j in bp:
                        h_txt += " "
                        h_txt += j.text + " "
                else:
                    h_txt += " "
                    h_txt += sib.text
        
        h_txt += " "
        h_txt += comm.text
        lst.append("placeholder.")
        response.append(sentence_clean(h_txt) + ".")
    
    return lst, header_vector, response


# In[41]:


def autism_society_eat(soup):
    main = soup.find("div", {'class':'col-xs-12 col-sm-12 col-md-8 col-lg-8 guidance__main-content col'})
    header = main.findAll("h2")
    
    lst = []
    header_vector = []
    response = []
    
    for i in header:
        if i.text.strip() != "Common food issues and ways to address them":
            continue
        else:
            header_vector.append(sentence_clean(str(i.text)) + ".")
            header_vector.append(sentence_clean("Why do they only like certain food") + ".")
            header_vector.append(sentence_clean("Why are they picky eaters") + ".")
            header_vector.append(sentence_clean("What food do they eat") + ".")
            header_vector.append(sentence_clean("How are their diet different") + ".")
            header_vector.append(sentence_clean("bad eater") + ".")
            header_vector.append(sentence_clean("bad at eating") + ".")
            h_txt = i.text + ": "
            
            for sib in i.find_next_siblings():
                if sib.name=="h2":
                    break
                else:
                    if sib.name=="ul":
                            bp = sib.findAll("li")
                            for i in bp:
                                h_txt += " "
                                h_txt += i.text + " "
                    else:
                        h_txt += " "
                        h_txt += sib.text
                
            lst.append("placeholder.")
            response.append(sentence_clean(h_txt) + ".")
    
    return lst, header_vector, response


# In[42]:


def autism_service(soup):
    main = soup.find("div", {'class':'content general-content__content'})
    header = main.findAll("h2")
    lst = []
    header_vector = []
    response = []
    
    for i in header:
        if i.text == "Common Autism Symptoms" or i.text == "What are the three main symptoms of autism?" or i.text == "What is autism caused by?" or i.text == "What is an autistic person like?" or i.text == "What is autism caused by?":
            continue
            
        if i.text.strip() == "Can you be slightly autistic?":
            header_vector.append(sentence_clean(str(i.text)) + ".")
            header_vector.append(sentence_clean("Can someone be slighty autistic") + ".")
            header_vector.append(sentence_clean("Is everybody autistic") + ".")
            header_vector.append(sentence_clean("Everybody is slightly autistic") + ".")
        elif i.text.strip() == "Can a child with autism lead a normal life?":
            header_vector.append(sentence_clean("Can I live a normal life") + ".")
            header_vector.append(sentence_clean("still get work") + ".")
            header_vector.append(sentence_clean("still get a job") + ".")
            header_vector.append(sentence_clean("normal life") + ".")
        elif i.text.strip() == "Is autism a birth defect?":
            header_vector.append(sentence_clean(str(i.text)) + ".")
            header_vector.append(sentence_clean("Can a difficult birth cause autism") + ".")
            header_vector.append(sentence_clean("Can autism be caused by a birth defect") + ".")
            header_vector.append(sentence_clean("difficult birth") + ".")
            header_vector.append(sentence_clean("birth defect") + ".")
        else:
            header_vector.append(sentence_clean(str(i.text)) + ".")
        
        h_txt = i.text + ": "
  
        for sib in i.find_next_siblings():
            if sib.name == "h2":
                break
            else:
                h_txt += " "
                h_txt += sib.text

        lst.append("placeholder.")
        response.append(sentence_clean(h_txt) + ".")
    
    return lst, header_vector, response


# In[43]:


def beyond_autism(soup):
    main = soup.find("div", {'class':'col-sm-8 order-1 order-md-2'})
    header = main.findAll("h3")
    scrape = beyond_autism_scrape(main, header)
    
    return scrape


# In[44]:


def beyond_autism_diag(soup):
    main = soup.find("div", {'class':'col-md mb-md-0 mb-4'})
    main.find('span', style="font-size: 14pt; color: #0083ba;").decompose()
    header = main.findAll("h4")
    scrape = beyond_autism_scrape(main, header)
    
    return scrape


# In[45]:


def beyond_autism_scrape(main, header):    
    lst = []
    header_vector = []
    response = []
    flag = False
    skip = False
    
    hd_lst = ["What causes autism?", "What is masking?", "Is OCD a form of autism?", "Is there a cure?", "How does a diagnosis happen?", "Do vaccines cause autism?", "Why are autistic children considered naughty?"] 

    for i in header:
        
        if str(i.text.strip()) not in hd_lst:
            continue
        elif str(i.text.strip()) == "What causes autism?":
            header_vector.append(sentence_clean(str(i.text)) + ".")
            header_vector.append(sentence_clean("What is the cause of autism") + ".")
            header_vector.append(sentence_clean("Why are they autistic") + ".")
            header_vector.append(sentence_clean("causes of autism") + ".")
        elif str(i.text.strip()) == "What is masking?":
            header_vector.append(sentence_clean(str(i.text)) + ".")
            header_vector.append(sentence_clean("What does masking mean") + ".")
        elif str(i.text.strip()) == "Is OCD a form of autism?":
            header_vector.append(sentence_clean(str(i.text)) + ".")
            header_vector.append(sentence_clean("OCD is related to autism") + ".")
            header_vector.append(sentence_clean("What links OCD and Autism") + ".")
            header_vector.append(sentence_clean("Do autistic people have OCD") + ".")
            header_vector.append(sentence_clean("Do they have OCD") + ".")
            header_vector.append(sentence_clean("OCD") + ".")
        elif str(i.text.strip()) == "Is there a cure?":
            header_vector.append(sentence_clean(str(i.text)) + ".")
            header_vector.append(sentence_clean("What is the cure of autism") + ".")
            header_vector.append(sentence_clean("What cures autism") + ".")
            header_vector.append(sentence_clean("cure of autism") + ".")
            header_vector.append(sentence_clean("Can autism be cured") + ".")
        elif i.text.strip() == "How does a diagnosis happen?":
            header_vector.append(sentence_clean(str(i.text)) + ".")
            header_vector.append(sentence_clean("How is autism diagnosed") + ".")
            header_vector.append(sentence_clean("How autism diagnosis work") + ".")
        elif i.text.strip() == "Why are autistic children considered naughty?":
            header_vector.append(sentence_clean("Why are they naughty") + ".")
            header_vector.append(sentence_clean("are they naughty") + ".")
            header_vector.append(sentence_clean("naughty behaviour") + ".")
            header_vector.append(sentence_clean("bad behaviour") + ".")
        
        else:
            header_vector.append(sentence_clean("vaccines cause autism") + ".")
            header_vector.append(sentence_clean("thimerosal cause autism") + ".")
        
        h_txt = i.text + ": "
            
        for sib in i.find_next_siblings():
            if sib.name == "h3" or sib.name == "h4":
                break
            elif sib.text == "For more information take a look at our online training courses." or sib.text == "To find out more about diagnosis, take a look at our free online introductory to autism course.":
                flag == True
                break
            else:
                if sib.name == "ul":
                    bp = sib.findAll("li")
                    for i in bp:
                        h_txt += " "
                        h_txt += i.text + " "
                else:
                    h_txt += " "
                    h_txt += sib.text
                
        h_txt = h_txt.replace(u'\xa0', u'')
                
        if skip == False:
            lst.append("placeholder.")
            response.append(sentence_clean(h_txt) + ".")
        
    return lst, header_vector, response


# In[46]:


def autism_society_stim(soup):
    main = soup.find("div", {'class':'col-xs-12 col-sm-12 col-md-8 col-lg-8 guidance__main-content col'})
    header_vector = []
    response = []
    lst = []
    
    header = main.findAll("h2")
    
    for h2 in header:
        if h2.text.strip() == "More from our charity":
            break
        elif h2.text.strip() == "What is stimming?":
            header_vector.append(sentence_clean(str(h2.text)) + ".")
            header_vector.append(sentence_clean("What does stimming mean") + ".")
        elif h2.text.strip() == "Why do some autistic people stim?":
            header_vector.append(sentence_clean(str(h2.text)) + ".")
            header_vector.append(sentence_clean("Why do stimming?") + ".")
        elif h2.text.strip() == "Should you intervene?":
            header_vector.append(sentence_clean("Should I intervene in stimming") + ".")
            header_vector.append(sentence_clean("Should I stop stimming") + ".")
        else:
            break
                 
        h_txt = h2.text + ": "
        
        for sib in h2.find_next_siblings():
            if sib.name=="h2":
                break
            else:
                if sib.name=="ul":
                        bp = sib.findAll("li")
                        for i in bp:
                            h_txt += " "
                            h_txt += i.text + " "
                else:
                    h_txt += " "
                    h_txt += sib.text
                
        lst.append("placeholder.")
        response.append(sentence_clean(h_txt) + ".")
    
    return lst, header_vector, response


# In[47]:


def nhs(soup):
    main = soup.find("main")
    try:
        main.find('div', id="sibling-nav").decompose()
    except:
        expect = "met"

    scrape = data_scrape(main)
    
    return scrape


# In[48]:


def data_scrape(main):
    lst = []
    header_vector = []
    response = []
    header = main.findAll("h2")
    
    try:
         main.find("div", class_="app-brightcove-video").decompose()
    except:
        expect = "met"
    try:
        main.find("p", {'data-block-key':'o23ee'})
    except:
        expect = "met"
        
    for h2 in header:
        if str(h2.get("data-block-key")) != "k4wax":
            h_txt = h2.text + ": "
        else:
            h_txt += " " + h2.text + ": "
        
        
        if h2.text.strip() == "Autistic people may act in a different way to other people" or h2.text.strip() == "top tips" or h2.text.strip() == "Routines" or h2.text.strip() == "Special interests" or h2.text.strip() == "Sensory differences":
            continue
        elif h2.text == "Find out more:" or h2.text == "Find out more about autism" or h2.text == "watch" or str(h2.get("class")) == "['app-related-nav__heading']" or h2.text == "More from our charity" or str(h2.get("paraid")) == "330363173" or h2.text.strip() == "Sensory considerations" or h2.text.strip() == "Autistic people may have other conditions":
            break
            
        
        if h2.text.strip() == "What is a meltdown?":
            header_vector.append(sentence_clean(str(h2.text)) + ".")
            header_vector.append(sentence_clean("What is an autistic meltdown") + ".")
            header_vector.append(sentence_clean("What does meltdown mean") + ".")
            header_vector.append(sentence_clean("Why do autistic people have tantrums") + ".")
            header_vector.append(sentence_clean("do they have tantrum") + ".")
        elif h2.text.strip() == "Autism is not an illness":
            header_vector.append(sentence_clean("Is autism an illness") + ".")
            header_vector.append(sentence_clean("Is autism an a sickness") + ".")
            header_vector.append(sentence_clean("Is autism an infection") + ".")
        elif h2.text.strip() == "Autistic people can live a full life":
            header_vector.append(sentence_clean("Make friends") + ".")
            header_vector.append(sentence_clean("Are they anti social") + ".")
            header_vector.append(sentence_clean("Can they make friends") + ".")
            header_vector.append(sentence_clean("Can they be social") + ".")
            header_vector.append(sentence_clean("get married") + ".")
            header_vector.append(sentence_clean("get relationships") + ".")
            header_vector.append(sentence_clean("girlfriend") + ".")
            header_vector.append(sentence_clean("boyfriend") + ".")
        elif h2.text.strip() == "Autism is different for everyone":
            header_vector.append(sentence_clean("I dont feel autistic") + ".")
            header_vector.append(sentence_clean("are not autistic") + ".")
            header_vector.append(sentence_clean("dont have autism") + ".")
            header_vector.append(sentence_clean("cannot be autistic") + ".")
            header_vector.append(sentence_clean("How is autism different") + ".")
            header_vector.append(sentence_clean("Can autism vary from person to person") + ".")
        elif h2.text.strip() == "Autistic people can have any level of intelligence":
            header_vector.append(sentence_clean("Are autistic people smart") + ".")
            header_vector.append(sentence_clean("Are autistic people stupid") + ".")
            header_vector.append(sentence_clean("high intelligence") + ".")
            header_vector.append(sentence_clean("Do they have high intelligence") + ".")
            header_vector.append(sentence_clean("low intelligence") + ".")
            header_vector.append(sentence_clean("What intelligence are autistic people") + ".")
            header_vector.append(sentence_clean("Do autistic people have intelligence") + ".")
            header_vector.append(sentence_clean("Are autistic people good at numbers") + ".")
            header_vector.append(sentence_clean("Are they intelligent") + ".")
            header_vector.append(sentence_clean("Why are they not intelligent") + ".")
            header_vector.append(sentence_clean("Are they talented") + ".")
            header_vector.append(sentence_clean("intelligent") + ".")
            header_vector.append(sentence_clean("talented") + ".")
            header_vector.append(sentence_clean("good at numbers") + ".")
            header_vector.append(sentence_clean("numbers") + ".")
            header_vector.append(sentence_clean("good at patterns") + ".")
        elif h2.text.strip() == "Some people use other names for autism":
            header_vector.append(sentence_clean("What are other names for autism") + ".")
            header_vector.append(sentence_clean("What are other terms for autism") + ".")
            header_vector.append(sentence_clean("terms for autism") + ".")
        elif h2.text.strip() == "It's not clear what causes autism":
            header_vector.append(sentence_clean("Does bad parenting cause autism") + ".")
            header_vector.append(sentence_clean("Am I a bad parent") + ".")
            header_vector.append(sentence_clean("bad parent") + ".")
            header_vector.append(sentence_clean("bad parenting") + ".")
        elif h2.text.strip() == "Autism in women and men":
            header_vector.append(sentence_clean("Do women get autism") + ".")
            header_vector.append(sentence_clean("Do only boys get autism") + ".")
            header_vector.append(sentence_clean("Can a girl be autistic") + ".")
            header_vector.append(sentence_clean("Do females get autism") + ".")
            header_vector.append(sentence_clean("Are only males autistic") + ".")
            header_vector.append(sentence_clean("women") + ".")
            header_vector.append(sentence_clean("male") + ".")
            header_vector.append(sentence_clean("boy") + ".")
            header_vector.append(sentence_clean("girl") + ".")
            header_vector.append(sentence_clean("female") + ".")
        elif h2.text.strip() == "What to do":
            header_vector.append(sentence_clean("What to do during a meltdown") + ".")
            header_vector.append(sentence_clean("What should I do if a person is having a meltdown") + ".")
            header_vector.append(sentence_clean("How to prevent a meltdown") + ".")
            header_vector.append(sentence_clean("stop a meltdown") + ".")
        elif h2.text.strip() == "Anticipating a meltdown":
            continue
        elif h2.text.strip() == "Identifying the causes":
            continue
        elif h2.text.strip() == "Minimising triggers":
            continue
        elif h2.text.strip() == "Main signs of autism":
            header_vector.append(sentence_clean("What are the signs of autism") + ".")
            header_vector.append(sentence_clean("signs of autism") + ".")
            header_vector.append(sentence_clean("What are the characteristics of autism") + ".")
            header_vector.append(sentence_clean("Why are they rude") + ".")
            header_vector.append(sentence_clean("are they rude") + ".")
        elif h2.text.strip() == "1. Talk to someone for advice":
            header_vector.append(sentence_clean("think I have autism") + ".")
            header_vector.append(sentence_clean("think they are autistic") + ".")
            header_vector.append(sentence_clean("get an autism diagnosis") + ".")
            header_vector.append(sentence_clean("get access to a diagnosis") + ".")
            header_vector.append(sentence_clean("How do I get a diagnosis") + ".")
            header_vector.append(sentence_clean("What should I do if a person has autism") + ".")
        elif h2.text.strip() == "2. Have an autism assessment":
            header_vector.append(sentence_clean(str(h2.text)) + ".")
            header_vector.append(sentence_clean("What is a autism assessment") + ".")
            header_vector.append(sentence_clean("How do I get a assessment") + ".")
            header_vector.append(sentence_clean("autism assessment") + ".")
        elif h2.text.strip() == "How a diagnosis can help":
            header_vector.append(sentence_clean(str(h2.text)) + ".")
            header_vector.append(sentence_clean("What is a autism diagnosis") + ".")
            header_vector.append(sentence_clean("What are the benefits of an autism diagnosis") + ".")
            header_vector.append(sentence_clean("What is the purpose of a diagnosis") + ".")
            header_vector.append(sentence_clean("How can an autism diagnosis help") + ".")
            header_vector.append(sentence_clean("autism diagnosis") + ".")
        elif h2.text.strip() == "If you find it hard to get diagnosed":
            header_vector.append(sentence_clean("finding it hard to get diagnosis") + ".")
            header_vector.append(sentence_clean("finding it hard to get an assessment") + ".")
            header_vector.append(sentence_clean("difficult to get diagnosed") + ".")
            header_vector.append(sentence_clean("difficult to get assessed") + ".")
            header_vector.append(sentence_clean("waiting times") + ".")
        elif h2.text.strip() == "Difficulties with communication":
            header_vector.append(sentence_clean("communication") + ".")
            header_vector.append(sentence_clean("communicational") + ".")
            header_vector.append(sentence_clean("Why do they talk bluntly") + ".")
            header_vector.append(sentence_clean("Why do autistic people talk bluntly") + ".")
            header_vector.append(sentence_clean("do they talk bluntly") + ".")
            header_vector.append(sentence_clean("sarcasm") + ".")
            header_vector.append(sentence_clean("literally") + ".")
            header_vector.append(sentence_clean("joke") + ".")
            header_vector.append(sentence_clean("talking") + ".")
            header_vector.append(sentence_clean("Why do autistic people not understand sarcasm") + ".")
            header_vector.append(sentence_clean("do they not understand jokes") + ".")
            header_vector.append(sentence_clean("why are they not talking") + ".")
            header_vector.append(sentence_clean("are autistic people non verbal") + ".")
            header_vector.append(sentence_clean("Why do they not talk") + ".")
            header_vector.append(sentence_clean("talk to me") + ".")
        elif h2.text.strip() == "Difficulties with socialising and interacting with other people":
            header_vector.append(sentence_clean(str(h2.text)) + ".")
            header_vector.append(sentence_clean("Why are they not social") + ".")
            header_vector.append(sentence_clean("Why are they not interacting") + ".")
        
        elif h2.text.strip() != "Other signs of autism":
            header_vector.append(sentence_clean(str(h2.text)) + ".")

          
        for sib in h2.find_next_siblings():
            if sib.name=="h2" or str(sib.get("class")) == "['nhsuk-inset-text']" or sib.text=="Here are some of the things you might see, in various combinations and from mild to severe, in people who have ASC:":
                break
            else:
                if sib.name=="ul":
                    bp = sib.findAll("li")
                    for i in bp:
                        h_txt += " "
                        h_txt += i.text + " "
                else:
                    h_txt += " "
                    h_txt += sib.text
                        
        if str(h2.get("data-block-key")) != "havm0":
            if h2.text.strip() == "Autism in women and men":
                lst.append("placeholder.")
                response.append(sentence_clean(h_txt) + " " + autism_society_girl_alt() + ".")
            
            elif h2.text.strip() == "Main signs of autism" or h2.text.strip() == "Other signs of autism" or h2.text.strip() == "What is a meltdown?" or h2.text.strip() == "Difficulties with socialising and interacting with other people" or h2.text.strip() == "Difficulties with imagination":
                txt = stop_words(h_txt)
                txt = sentence_clean(txt)
                txt = stop_words(txt) + "."
                lst.append(txt)
                response.append(sentence_clean(h_txt) + ".")
            else:
                lst.append("placeholder.")
                response.append(sentence_clean(h_txt) + ".")
                
        
    return lst, header_vector, response


# In[49]:


def data_scrape_nhs_support(main):
    lst = []
    header_vector = []
    response = []
    h_txt = "Where can I find support: "
    keys = ["73egt", "2phuy", "n363d", "d23cr", "7q6tc", "9c853"]
    sub_key = ["e2mzh", "3zx19"]
    
    header = main.findAll("h2")
    
    header_vector.append(sentence_clean("Where can I find autism support") + ".")
    header_vector.append(sentence_clean("What support is available") + ".")
    header_vector.append(sentence_clean("What support are available") + ".")
    header_vector.append(sentence_clean("What support are there") + ".")
    header_vector.append(sentence_clean("What help is there") + ".")
    header_vector.append(sentence_clean("How do I get support") + ".")
    header_vector.append(sentence_clean("How can I help somebody with autism") + ".")
    
    for h2 in header:
        if str(h2.get("data-block-key")) not in keys:
            continue
        
        h_txt += " "+ h2.text + ": "

        for sib in h2.find_next_siblings():
            if sib.name=="h2" or str(sib.get("data-block-key")) in sub_key:
                break
            else:
                if sib.name=="ul":
                    bp = sib.findAll("li")
                    for i in bp:
                        h_txt += " "
                        h_txt += i.text + " "
                else:
                    h_txt += " "
                    h_txt += sib.text
            
    lst.append("placeholder.")
    response.append(sentence_clean(h_txt) + ".")
    
 
    return lst, header_vector, response


# In[50]:


def autism_society(soup):
    main = soup.find("div", {'class':'col-xs-12 col-sm-12 col-md-8 col-lg-8 guidance__main-content col'}) 
    scrape = data_scrape(main)
    
    return scrape


# In[51]:


def autism_society_anger(soup):
    keys = ["849695660", "255941325"]
    sub_keys_anger = ["447826250", "1619175753", "182969273", "1391313373"]
    sub_keys_anger_sol = ["1807365836", "1497702776", "1277288159"]
    header_vector = []
    response = []
    lst = []
    h_txt = ""
    
    header_vector.append(sentence_clean("Are autistic people angry") + ".")
    header_vector.append(sentence_clean("Why are they aggressive") + ".")
    header_vector.append(sentence_clean("Do autistic people suffer from anger") + ".")
    header_vector.append(sentence_clean("are people with autism aggressive") + ".")
    header_vector.append(sentence_clean("angry") + ".")
    header_vector.append(sentence_clean("anger") + ".")

    for i in keys:
        hd = soup.find("h2", {'paraid':i})
        h_txt += " " + hd.text + " "

        if i == "849695660":
            for j in sub_keys_anger:
                h_txt += soup.find("p", {'paraid':j}).text + " "
        else:
            for k in sub_keys_anger_sol:
                h_txt += soup.find("p", {'paraid':k}).text + " "

    lst.append("placeholder.")
    response.append(sentence_clean(h_txt) + ".")
    
    
    return lst, header_vector, response 


# In[52]:


def stop_words(h_txt):
    txt = ""
    word = h_txt.split()
    stopwords = nltk.corpus.stopwords.words('english')
    stop = ["things", "thing", "does", "my", "take", "son", "autistic", "stop", "doe", "child", "autism", "good", "daughter", "relative", "adult", "getting", "get", "still", "youre", "people", "might", "hard", "much", "different", "person", "way", "has", "ha", "ear", "eg", "are", "is", "ar", "situation", "difficult", "finding", "like", "liking", "point", "keen", "change", "life", "can", "sign", "difficulty", "support", "include", "thinking", "dont", "asc", "family", "friend", "doctor", "noticed", "note", "write", "paper", "pen", "bite", "exchange", "bad", "parent", "works", "altogether", "completely", "condition", "express", "feeling", "understandable", "loss", "loses", "physically", "result", "current", "avoiding", "completely", "condition", "control", "temporarily", "talking", "touch", "smell", "pattern", "touched", "feel"]
    stop_extend = ["0o", "0s", "3a", "3b", "3d", "6b", "6o", "a", "a1", "a2", "a3", "a4", "ab", "able", "about", "above", "abst", "ac", "accordance", "according", "accordingly", "across", "act", "actually", "ad", "added", "adj", "ae", "af", "affected", "affecting", "affects", "after", "afterwards", "ag", "again", "against", "ah", "ain", "ain't", "aj", "al", "all", "allow", "allows", "almost", "alone", "along", "already", "also", "although", "always", "am", "among", "amongst", "amoungst", "amount", "an", "and", "announce", "another", "any", "anybody", "anyhow", "anymore", "anyone", "anything", "anyway", "anyways", "anywhere", "ao", "ap", "apart", "apparently", "appear", "appreciate", "appropriate", "approximately", "ar", "are", "aren", "arent", "aren't", "arise", "around", "as", "a's", "aside", "ask", "asking", "associated", "at", "au", "auth", "av", "available", "aw", "away", "awfully", "ax", "ay", "az", "b", "b1", "b2", "b3", "ba", "back", "bc", "bd", "be", "became", "because", "become", "becomes", "becoming", "been", "before", "beforehand", "begin", "beginning", "beginnings", "begins", "behind", "being", "believe", "below", "beside", "besides", "best", "better", "between", "beyond", "bi", "bill", "biol", "bj", "bk", "bl", "bn", "both", "bottom", "bp", "br", "brief", "briefly", "bs", "bt", "bu", "but", "bx", "by", "c", "c1", "c2", "c3", "ca", "call", "came", "can", "cannot", "cant", "can't", "cause", "causes", "cc", "cd", "ce", "certain", "certainly", "cf", "cg", "ch", "changes", "ci", "cit", "cj", "cl", "clearly", "cm", "c'mon", "cn", "co", "com", "come", "comes", "con", "concerning", "consequently", "consider", "considering", "contain", "containing", "contains", "corresponding", "could", "couldn", "couldnt", "couldn't", "course", "cp", "cq", "cr", "cry", "cs", "c's", "ct", "cu", "currently", "cv", "cx", "cy", "cz", "d", "d2", "da", "date", "dc", "dd", "de", "definitely", "describe", "described", "despite", "detail", "df", "di", "did", "didn", "didn't", "different", "dj", "dk", "dl", "do", "does", "doesn", "doesn't", "doing", "don", "done", "don't", "down", "downwards", "dp", "dr", "ds", "dt", "du", "due", "during", "dx", "dy", "e", "e2", "e3", "ea", "each", "ec", "ed", "edu", "ee", "ef", "effect", "eg", "ei", "eight", "eighty", "either", "ej", "el", "eleven", "else", "elsewhere", "em", "empty", "en", "end", "ending", "enough", "entirely", "eo", "ep", "eq", "er", "es", "especially", "est", "et", "et-al", "etc", "eu", "ev", "even", "ever", "every", "everybody", "everyone", "everything", "everywhere", "ex", "exactly", "example", "except", "ey", "f", "f2", "fa", "far", "fc", "few", "ff", "fi", "fifteen", "fifth", "fify", "fill", "find", "fire", "first", "five", "fix", "fj", "fl", "fn", "fo", "followed", "following", "follows", "for", "former", "formerly", "forth", "forty", "found", "four", "fr", "from", "front", "fs", "ft", "fu", "full", "further", "furthermore", "fy", "g", "ga", "gave", "ge", "get", "gets", "getting", "gi", "give", "given", "gives", "giving", "gj", "gl", "go", "goes", "going", "gone", "got", "gotten", "gr", "greetings", "gs", "gy", "h", "h2", "h3", "had", "hadn", "hadn't", "happens", "hardly", "has", "hasn", "hasnt", "hasn't", "have", "haven", "haven't", "having", "he", "hed", "he'd", "he'll", "hello", "help", "hence", "her", "here", "hereafter", "hereby", "herein", "heres", "here's", "hereupon", "hers", "herself", "hes", "he's", "hh", "hi", "hid", "him", "himself", "his", "hither", "hj", "ho", "home", "hopefully", "how", "howbeit", "however", "how's", "hr", "hs", "http", "hu", "hundred", "hy", "i", "i2", "i3", "i4", "i6", "i7", "i8", "ia", "ib", "ibid", "ic", "id", "i'd", "ie", "if", "ig", "ignored", "ih", "ii", "ij", "il", "i'll", "im", "i'm", "immediate", "immediately", "importance", "important", "in", "inasmuch", "inc", "indeed", "index", "indicate", "indicated", "indicates", "information", "inner", "insofar", "instead", "interest", "into", "invention", "inward", "io", "ip", "iq", "ir", "is", "isn", "isn't", "it", "itd", "it'd", "it'll", "its", "it's", "itself", "iv", "i've", "ix", "iy", "iz", "j", "jj", "jr", "js", "jt", "ju", "just", "k", "ke", "keep", "keeps", "kept", "kg", "kj", "km", "know", "known", "knows", "ko", "l", "l2", "la", "largely", "last", "lately", "later", "latter", "latterly", "lb", "lc", "le", "least", "les", "less", "lest", "let", "lets", "let's", "lf", "like", "liked", "likely", "line", "little", "lj", "ll", "ll", "ln", "lo", "look", "looking", "looks", "los", "lr", "ls", "lt", "ltd", "m", "m2", "ma", "made", "mainly", "make", "makes", "many", "may", "maybe", "me", "mean", "means", "meantime", "meanwhile", "merely", "mg", "might", "mightn", "mightn't", "mill", "million", "mine", "miss", "ml", "mn", "mo", "more", "moreover", "most", "mostly", "move", "mr", "mrs", "ms", "mt", "mu", "much", "mug", "must", "mustn", "mustn't", "my", "myself", "n", "n2", "na", "name", "namely", "nay", "nc", "nd", "ne", "near", "nearly", "necessarily", "necessary", "need", "needn", "needn't", "needs", "neither", "never", "nevertheless", "new", "next", "ng", "ni", "nine", "ninety", "nj", "nl", "nn", "no", "nobody", "non", "none", "nonetheless", "noone", "nor", "normally", "nos", "not", "noted", "nothing", "novel", "now", "nowhere", "nr", "ns", "nt", "ny", "o", "oa", "ob", "obtain", "obtained", "obviously", "oc", "od", "of", "off", "often", "og", "oh", "oi", "oj", "ok", "okay", "ol", "old", "om", "omitted", "on", "once", "one", "ones", "only", "onto", "oo", "op", "oq", "or", "ord", "os", "ot", "other", "others", "otherwise", "ou", "ought", "our", "ours", "ourselves", "out", "outside", "over", "overall", "ow", "owing", "own", "ox", "oz", "p", "p1", "p2", "p3", "page", "pagecount", "pages", "par", "part", "particular", "particularly", "pas", "past", "pc", "pd", "pe", "per", "perhaps", "pf", "ph", "pi", "pj", "pk", "pl", "placed", "please", "plus", "pm", "pn", "po", "poorly", "possible", "possibly", "potentially", "pp", "pq", "pr", "predominantly", "present", "presumably", "previously", "primarily", "probably", "promptly", "proud", "provides", "ps", "pt", "pu", "put", "py", "q", "qj", "qu", "que", "quickly", "quite", "qv", "r", "r2", "ra", "ran", "rather", "rc", "rd", "re", "readily", "really", "reasonably", "recent", "recently", "ref", "refs", "regarding", "regardless", "regards", "related", "relatively", "research", "research-articl", "respectively", "resulted", "resulting", "results", "rf", "rh", "ri", "right", "rj", "rl", "rm", "rn", "ro", "rq", "rr", "rs", "rt", "ru", "run", "rv", "ry", "s", "s2", "sa", "said", "same", "saw", "say", "saying", "says", "sc", "sd", "se", "sec", "second", "secondly", "section", "see", "seeing", "seem", "seemed", "seeming", "seems", "seen", "self", "selves", "sensible", "sent", "serious", "seriously", "seven", "several", "sf", "shall", "shan", "shan't", "she", "shed", "she'd", "she'll", "shes", "she's", "should", "shouldn", "shouldn't", "should've", "show", "showed", "shown", "showns", "shows", "si", "side", "significant", "significantly", "similar", "similarly", "since", "sincere", "six", "sixty", "sj", "sl", "slightly", "sm", "sn", "so", "some", "somebody", "somehow", "someone", "somethan", "something", "sometime", "sometimes", "somewhat", "somewhere", "soon", "sorry", "sp", "specifically", "specified", "specify", "specifying", "sq", "sr", "ss", "st", "still", "stop", "strongly", "sub", "substantially", "successfully", "such", "sufficiently", "suggest", "sup", "sure", "sy", "system", "sz", "t", "t1", "t2", "t3", "take", "taken", "taking", "tb", "tc", "td", "te", "tell", "ten", "tends", "tf", "th", "than", "thank", "thanks", "thanx", "that", "that'll", "thats", "that's", "that've", "the", "their", "theirs", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "thered", "therefore", "therein", "there'll", "thereof", "therere", "theres", "there's", "thereto", "thereupon", "there've", "these", "they", "theyd", "they'd", "they'll", "theyre", "they're", "they've", "thickv", "thin", "think", "third", "this", "thorough", "thoroughly", "those", "thou", "though", "thoughh", "thousand", "three", "throug", "through", "throughout", "thru", "thus", "ti", "til", "tip", "tj", "tl", "tm", "tn", "to", "together", "too", "took", "top", "toward", "towards", "tp", "tq", "tr", "tried", "tries", "truly", "try", "trying", "ts", "t's", "tt", "tv", "twelve", "twenty", "twice", "two", "tx", "u", "u201d", "ue", "ui", "uj", "uk", "um", "un", "under", "unfortunately", "unless", "unlike", "unlikely", "until", "unto", "uo", "up", "upon", "ups", "ur", "us", "use", "used", "useful", "usefully", "usefulness", "uses", "using", "usually", "ut", "v", "va", "value", "various", "vd", "ve", "ve", "very", "via", "viz", "vj", "vo", "vol", "vols", "volumtype", "vq", "vs", "vt", "vu", "w", "wa", "want", "wants", "was", "wasn", "wasnt", "wasn't", "way", "we", "wed", "we'd", "welcome", "well", "we'll", "well-b", "went", "were", "we're", "weren", "werent", "weren't", "we've", "what", "whatever", "what'll", "whats", "what's", "when", "whence", "whenever", "when's", "where", "whereafter", "whereas", "whereby", "wherein", "wheres", "where's", "whereupon", "wherever", "whether", "which", "while", "whim", "whither", "who", "whod", "whoever", "whole", "who'll", "whom", "whomever", "whos", "who's", "whose", "why", "why's", "wi", "widely", "will", "willing", "wish", "with", "within", "without", "wo", "won", "wonder", "wont", "won't", "words", "world", "would", "wouldn", "wouldnt", "wouldn't", "www", "x", "x1", "x2", "x3", "xf", "xi", "xj", "xk", "xl", "xn", "xo", "xs", "xt", "xv", "xx", "y", "y2", "yes", "yet", "yj", "yl", "you", "youd", "you'd", "you'll", "your", "youre", "you're", "yours", "yourself", "yourselves", "you've", "yr", "ys", "yt", "z", "zero", "zi", "zz"]
    stopwords.extend(stop)
    stopwords.extend(stop_extend)
    
    for i in word:
        rmslash = i.lower()
        if i not in stopwords:
            txt += i + " "
        
    return txt 


# In[53]:


def data_separator(scraped_sites):
    data = ""
    for list in scraped_sites:
        for i in list:
            data = data + i + " "
    return data


# In[54]:


def strip(txt):
    num = 0
    for i in txt:
        txt[num] = i.strip()
        num += 1
        
    return txt


# In[55]:


def tokenize(words):
    tokens = nltk.sent_tokenize(words)
    tokens = word_clean(tokens)
    
    return tokens


# In[56]:


def res_tokenize(words):
    tokens = nltk.sent_tokenize(words)
    tokens = res_clean(tokens)
    
    return tokens


# In[57]:


def word_clean(word_sen):
    num = 0
    for i in word_sen:
        word_sen[num] = re.sub(r'[^A-Za-z ]+', '', word_sen[num])
        word_sen[num] = re.sub(' +', ' ', word_sen[num])
        num += 1
        
    return word_sen


# In[58]:


def res_clean(res_sen):
    num = 0
    for i in word_sen:
        res_sen[num] = re.sub(r'[^A-Za-z0-9 ]+', '', res_sen[num])
        res_sen[num] = re.sub(' +', ' ', res_sen[num])
        num += 1
        
    return res_sen


# In[59]:


def create_text_file(data, response):
    if not os.path.isdir('./scraped_intents'):
        try:
            os.mkdir("./scraped_intents")
        except OSError:
            print("Creation of the folder has failed")
        else:
            print("Successfully created folder")
    
    try:
        if os.path.exists("./scraped_intents/intents.txt"):
          os.remove("./scraped_intents/intents.txt")
        else:
            print("File Not Found")
    except:
        print("Error removing old intents file")
    
    try:
        if os.path.exists("./scraped_intents/response.txt"):
          os.remove("./scraped_intents/response.txt")
        else:
            print("File Not Found")
    except:
        print("Error removing old response file")
    
    try:
        with open('./scraped_intents/intents.txt', 'w') as txt:
            txt.write(data)
    except:
        print("Error creating intents file")
    try:
        with open('./scraped_intents/response.txt', 'w') as txt:
            txt.write(response)
    except:
        print("Error creating response file")


# In[60]:


def lemmatization(words):
    lem_words = []

    for lists in words:
        lem = []
        for i in lists:
            lem += [lemmatizer.lemmatize(j.lower()) for j in i.split()]
        lem = sorted(list(set(lem)))
        lem_words.append(lem)
        
    return lem_words


# In[61]:


def lem_stop(lem_words):
    accepted_words = []
    stopwords = nltk.corpus.stopwords.words('english')
    stop = ["things", "thing", "does", "my", "take", "son", "autistic", "stop", "doe", "child", "autism", "good", "daughter", "relative", "adult", "getting", "get", "still", "youre", "people", "might", "hard", "much", "different", "person", "way", "has", "ha", "ear", "eg", "are", "is", "ar", "situation", "difficult", "finding", "like", "liking", "point", "keen", "change", "life", "can", "sign", "difficulty", "support", "include", "thinking", "dont", "asc", "family", "friend", "doctor", "noticed", "note", "write", "paper", "pen", "bite", "exchange", "bad", "parent", "works", "altogether", "completely", "condition", "express", "feeling", "understandable", "loss", "loses", "physically", "result", "current", "avoiding", "completely", "condition", "control", "temporarily", "understand", "talking", "touch", "smell", "pattern", "touched", "feel"]
    stop_extend = ["0o", "0s", "3a", "3b", "3d", "6b", "6o", "a", "a1", "a2", "a3", "a4", "ab", "able", "about", "above", "abst", "ac", "accordance", "according", "accordingly", "across", "act", "actually", "ad", "added", "adj", "ae", "af", "affected", "affecting", "affects", "after", "afterwards", "ag", "again", "against", "ah", "ain", "ain't", "aj", "al", "all", "allow", "allows", "almost", "alone", "along", "already", "also", "although", "always", "am", "among", "amongst", "amoungst", "amount", "an", "and", "announce", "another", "any", "anybody", "anyhow", "anymore", "anyone", "anything", "anyway", "anyways", "anywhere", "ao", "ap", "apart", "apparently", "appear", "appreciate", "appropriate", "approximately", "ar", "are", "aren", "arent", "aren't", "arise", "around", "as", "a's", "aside", "ask", "asking", "associated", "at", "au", "auth", "av", "available", "aw", "away", "awfully", "ax", "ay", "az", "b", "b1", "b2", "b3", "ba", "back", "bc", "bd", "be", "became", "because", "become", "becomes", "becoming", "been", "before", "beforehand", "begin", "beginning", "beginnings", "begins", "behind", "being", "believe", "below", "beside", "besides", "best", "better", "between", "beyond", "bi", "bill", "biol", "bj", "bk", "bl", "bn", "both", "bottom", "bp", "br", "brief", "briefly", "bs", "bt", "bu", "but", "bx", "by", "c", "c1", "c2", "c3", "ca", "call", "came", "can", "cannot", "cant", "can't", "cause", "causes", "cc", "cd", "ce", "certain", "certainly", "cf", "cg", "ch", "changes", "ci", "cit", "cj", "cl", "clearly", "cm", "c'mon", "cn", "co", "com", "come", "comes", "con", "concerning", "consequently", "consider", "considering", "contain", "containing", "contains", "corresponding", "could", "couldn", "couldnt", "couldn't", "course", "cp", "cq", "cr", "cry", "cs", "c's", "ct", "cu", "currently", "cv", "cx", "cy", "cz", "d", "d2", "da", "date", "dc", "dd", "de", "definitely", "describe", "described", "despite", "detail", "df", "di", "did", "didn", "didn't", "different", "dj", "dk", "dl", "do", "does", "doesn", "doesn't", "doing", "don", "done", "don't", "down", "downwards", "dp", "dr", "ds", "dt", "du", "due", "during", "dx", "dy", "e", "e2", "e3", "ea", "each", "ec", "ed", "edu", "ee", "ef", "effect", "eg", "ei", "eight", "eighty", "either", "ej", "el", "eleven", "else", "elsewhere", "em", "empty", "en", "end", "ending", "enough", "entirely", "eo", "ep", "eq", "er", "es", "especially", "est", "et", "et-al", "etc", "eu", "ev", "even", "ever", "every", "everybody", "everyone", "everything", "everywhere", "ex", "exactly", "example", "except", "ey", "f", "f2", "fa", "far", "fc", "few", "ff", "fi", "fifteen", "fifth", "fify", "fill", "find", "fire", "first", "five", "fix", "fj", "fl", "fn", "fo", "followed", "following", "follows", "for", "former", "formerly", "forth", "forty", "found", "four", "fr", "from", "front", "fs", "ft", "fu", "full", "further", "furthermore", "fy", "g", "ga", "gave", "ge", "get", "gets", "getting", "gi", "give", "given", "gives", "giving", "gj", "gl", "go", "goes", "going", "gone", "got", "gotten", "gr", "greetings", "gs", "gy", "h", "h2", "h3", "had", "hadn", "hadn't", "happens", "hardly", "has", "hasn", "hasnt", "hasn't", "have", "haven", "haven't", "having", "he", "hed", "he'd", "he'll", "hello", "help", "hence", "her", "here", "hereafter", "hereby", "herein", "heres", "here's", "hereupon", "hers", "herself", "hes", "he's", "hh", "hi", "hid", "him", "himself", "his", "hither", "hj", "ho", "home", "hopefully", "how", "howbeit", "however", "how's", "hr", "hs", "http", "hu", "hundred", "hy", "i", "i2", "i3", "i4", "i6", "i7", "i8", "ia", "ib", "ibid", "ic", "id", "i'd", "ie", "if", "ig", "ignored", "ih", "ii", "ij", "il", "i'll", "im", "i'm", "immediate", "immediately", "importance", "important", "in", "inasmuch", "inc", "indeed", "index", "indicate", "indicated", "indicates", "information", "inner", "insofar", "instead", "interest", "into", "invention", "inward", "io", "ip", "iq", "ir", "is", "isn", "isn't", "it", "itd", "it'd", "it'll", "its", "it's", "itself", "iv", "i've", "ix", "iy", "iz", "j", "jj", "jr", "js", "jt", "ju", "just", "k", "ke", "keep", "keeps", "kept", "kg", "kj", "km", "know", "known", "knows", "ko", "l", "l2", "la", "largely", "last", "lately", "later", "latter", "latterly", "lb", "lc", "le", "least", "les", "less", "lest", "let", "lets", "let's", "lf", "like", "liked", "likely", "line", "little", "lj", "ll", "ll", "ln", "lo", "look", "looking", "looks", "los", "lr", "ls", "lt", "ltd", "m", "m2", "ma", "made", "mainly", "make", "makes", "many", "may", "maybe", "me", "mean", "means", "meantime", "meanwhile", "merely", "mg", "might", "mightn", "mightn't", "mill", "million", "mine", "miss", "ml", "mn", "mo", "more", "moreover", "most", "mostly", "move", "mr", "mrs", "ms", "mt", "mu", "much", "mug", "must", "mustn", "mustn't", "my", "myself", "n", "n2", "na", "name", "namely", "nay", "nc", "nd", "ne", "near", "nearly", "necessarily", "necessary", "need", "needn", "needn't", "needs", "neither", "never", "nevertheless", "new", "next", "ng", "ni", "nine", "ninety", "nj", "nl", "nn", "no", "nobody", "non", "none", "nonetheless", "noone", "nor", "normally", "nos", "not", "noted", "nothing", "novel", "now", "nowhere", "nr", "ns", "nt", "ny", "o", "oa", "ob", "obtain", "obtained", "obviously", "oc", "od", "of", "off", "often", "og", "oh", "oi", "oj", "ok", "okay", "ol", "old", "om", "omitted", "on", "once", "one", "ones", "only", "onto", "oo", "op", "oq", "or", "ord", "os", "ot", "other", "others", "otherwise", "ou", "ought", "our", "ours", "ourselves", "out", "outside", "over", "overall", "ow", "owing", "own", "ox", "oz", "p", "p1", "p2", "p3", "page", "pagecount", "pages", "par", "part", "particular", "particularly", "pas", "past", "pc", "pd", "pe", "per", "perhaps", "pf", "ph", "pi", "pj", "pk", "pl", "placed", "please", "plus", "pm", "pn", "po", "poorly", "possible", "possibly", "potentially", "pp", "pq", "pr", "predominantly", "present", "presumably", "previously", "primarily", "probably", "promptly", "proud", "provides", "ps", "pt", "pu", "put", "py", "q", "qj", "qu", "que", "quickly", "quite", "qv", "r", "r2", "ra", "ran", "rather", "rc", "rd", "re", "readily", "really", "reasonably", "recent", "recently", "ref", "refs", "regarding", "regardless", "regards", "related", "relatively", "research", "research-articl", "respectively", "resulted", "resulting", "results", "rf", "rh", "ri", "right", "rj", "rl", "rm", "rn", "ro", "rq", "rr", "rs", "rt", "ru", "run", "rv", "ry", "s", "s2", "sa", "said", "same", "saw", "say", "saying", "says", "sc", "sd", "se", "sec", "second", "secondly", "section", "see", "seeing", "seem", "seemed", "seeming", "seems", "seen", "self", "selves", "sensible", "sent", "serious", "seriously", "seven", "several", "sf", "shall", "shan", "shan't", "she", "shed", "she'd", "she'll", "shes", "she's", "should", "shouldn", "shouldn't", "should've", "show", "showed", "shown", "showns", "shows", "si", "side", "significant", "significantly", "similar", "similarly", "since", "sincere", "six", "sixty", "sj", "sl", "slightly", "sm", "sn", "so", "some", "somebody", "somehow", "someone", "somethan", "something", "sometime", "sometimes", "somewhat", "somewhere", "soon", "sorry", "sp", "specifically", "specified", "specify", "specifying", "sq", "sr", "ss", "st", "still", "stop", "strongly", "sub", "substantially", "successfully", "such", "sufficiently", "suggest", "sup", "sure", "sy", "system", "sz", "t", "t1", "t2", "t3", "take", "taken", "taking", "tb", "tc", "td", "te", "tell", "ten", "tends", "tf", "th", "than", "thank", "thanks", "thanx", "that", "that'll", "thats", "that's", "that've", "the", "their", "theirs", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "thered", "therefore", "therein", "there'll", "thereof", "therere", "theres", "there's", "thereto", "thereupon", "there've", "these", "they", "theyd", "they'd", "they'll", "theyre", "they're", "they've", "thickv", "thin", "think", "third", "this", "thorough", "thoroughly", "those", "thou", "though", "thoughh", "thousand", "three", "throug", "through", "throughout", "thru", "thus", "ti", "til", "tip", "tj", "tl", "tm", "tn", "to", "together", "too", "took", "top", "toward", "towards", "tp", "tq", "tr", "tried", "tries", "truly", "try", "trying", "ts", "t's", "tt", "tv", "twelve", "twenty", "twice", "two", "tx", "u", "u201d", "ue", "ui", "uj", "uk", "um", "un", "under", "unfortunately", "unless", "unlike", "unlikely", "until", "unto", "uo", "up", "upon", "ups", "ur", "us", "use", "used", "useful", "usefully", "usefulness", "uses", "using", "usually", "ut", "v", "va", "value", "various", "vd", "ve", "ve", "very", "via", "viz", "vj", "vo", "vol", "vols", "volumtype", "vq", "vs", "vt", "vu", "w", "wa", "want", "wants", "was", "wasn", "wasnt", "wasn't", "way", "we", "wed", "we'd", "welcome", "well", "we'll", "well-b", "went", "were", "we're", "weren", "werent", "weren't", "we've", "what", "whatever", "what'll", "whats", "what's", "when", "whence", "whenever", "when's", "where", "whereafter", "whereas", "whereby", "wherein", "wheres", "where's", "whereupon", "wherever", "whether", "which", "while", "whim", "whither", "who", "whod", "whoever", "whole", "who'll", "whom", "whomever", "whos", "who's", "whose", "why", "why's", "wi", "widely", "will", "willing", "wish", "with", "within", "without", "wo", "won", "wonder", "wont", "won't", "words", "world", "would", "wouldn", "wouldnt", "wouldn't", "www", "x", "x1", "x2", "x3", "xf", "xi", "xj", "xk", "xl", "xn", "xo", "xs", "xt", "xv", "xx", "y", "y2", "yes", "yet", "yj", "yl", "you", "youd", "you'd", "you'll", "your", "youre", "you're", "yours", "yourself", "yourselves", "you've", "yr", "ys", "yt", "z", "zero", "zi", "zz"]
    stopwords.extend(stop)
    stopwords.extend(stop_extend)
    
    for i in lem_words:
        words = []
        for j in i:
            if j not in stopwords:
                words.append(j)
        accepted_words.append(words)
    
    return accepted_words 


# In[62]:


def append_header(lem_words, header):
    num = 0
    lst = ["Where can I find autism support", "What support is available", "What help is there", "What is a meltdown", "Communicate clearly", "Should I intervene in stimming", "What causes autism", "What is the cause of autism", 
        "Is OCD a form of autism", "OCD is related to autism", "Is there a cure", "What is the cure of autism","What cures autism", "What are the signs of autism", "What are the characteristics of autism", "Why are they rude", "signs of autism", "Talk to someone for advice", 
        "think I have autism", "get an autism diagnosis", "Have an autism assessment", "What is a autism assessment", "How a diagnosis can help",  "cure of autism",
        "What is a autism diagnosis", "What are the benefits of an autism diagnosis", "How can an autism diagnosis help", "finding it hard to get diagnosed", "finding it hard to get an assessment", "difficult to get diagnosed",
        "difficult to get assessed", "Can you be slightly autistic", "Can someone be slighty autistic", "Is everybody autistic", "Can I live a normal life", "still get work", "still get a job",
        "Is autism a birth defect", "Can a difficult birth cause autism", "Can autism be caused by a birth defect", "difficult birth", "Common food issues and ways to address them", "Why do they only like certain food", 
        "Why are they picky eaters", "What food do they eat", "How are their diet different", "bad eater", "How does a diagnosis happen", "Why are autistic people angry", "Why are they aggressive", "Do autistic people suffer from anger", "are people with autism aggressive",
        "angry", "What is an autistic meltdown", "What is masking", "What is stimming", "Why do some autistic people stim", "What to do during a meltdown", "What should I do if a person is having a meltdown", "get access to a diagnosis", "Is autism a disability",
        "Is autism a learning disability", "Can autism run in the family", "Why is Aspergers syndrome not diagnosed anymore", "What is Asperger", "Is there an autism diagnosis online", "get online autism diagnosis", "autism diagnosis online",
        "autism assessment online", "What is ABA therapy", "What date is World Autism Awareness day", "Why is autism more prevalent today than it was in previous decades", "autism more prevalent today", "more cases of autism now",
        "Why are they self destructive", "Why are they self injurious", "Why do autistic people hurt themselves", "do they self harm", "Why do they injure", "do they hit", "Why do they punch", "What is smearing", "Why do they smear", "Why do they smear faeces",
        "Why do they rub faeces", "are they not toilet trained", "Why are they difficult to potty train", "Why do they rub poo", "Intense interests", "Why do they have obsessive interests", "do they so interested in things", "Why are they fixated on certain topics",
        "What obsessions do autisc people have", "Hobbies", "Obsession", "Why are they obsessed with", "Repetitive behaviour", "Why do they repeat themselves", "Why are they repeating me", "Why do they repeat actions", "Why do they rock", "Why do they tap their finger",
        "do they repeat", "Why do they have repetitive movements", "Why do they flap their arms", "Why do they flap their hands", "Why do they head bang", "Why do they finger flick", "Why do they jump", "Why do they spin", "Why do they twirl", "repetitive movements",
        "body movements", "move their body", "move their bodies", "What causes distressed behaviour", "Why do they bite", "do they bite people", "What causes them distress", "Why did they spit", "Why do they pinch", "Why do they attack", "pinch", "attack", "bite",
        "spitting", "Why do they scream", "Why do they hate change", "Why are they fearful of change", "change of plans", "change of enviroment", "why do they hate plans being changed", "times being changed", "change", "How do I get a diagnosis", "How do I get a assessment",
        "How do I get support", "How do autistic people get jobs", "How do I get work", "How do I get a job", "What jobs are available", "What work is available", "Is autism an illness", "Is autism an a sickness", "Make friends", "Can they make friends",
        "Can they be social", "get married", "get relationships", "girlfriend", "I dont feel autistic", "are not autistic", "dont have autism", "cannot be autistic", "How is autism different", "Are autistic people smart", "Are autistic people stupid", "high intelligence",
        "low intelligence", "What intelligence are autistic people", "Do autistic people have intelligence", "Are autistic people good at numbers", "good at numbers", "numbers", "What are other names for autism", "What are other terms for autism", "Does bad parenting cause autism",
        "Am I a bad parent", "bad parent", "Do women get autism", "Do only boys get autism", "Can a girl be autistic", "Do females get autism", "Are only males autistic", "women", "male", "boy", "girl", "How to prevent a meltdown", "think they are autistic", 
        "finding it hard to get diagnosis", "Are autistic people angry", "Why did they attack me", "Why did they hit me", "What is catatonia", "What does catatonia mean", "Is catatonia a form of autism", "catatonia is related to autism", "GcMAF", "bleaching", "CEASE", "chelation",
        "secretin", "camel milk", "raw camel milk", "vitamins", "minerals", "dietary supplements", "What medication is there", "What medicine is there", "Can camel milk cure autism", "What medication can help", "Why are they naughty", "naughty behaviour",
        "What is high functioning autism", "What does high functioning mean", "What is low functioning autism", "What does low functioning mean", "high functioning", "What is autism acceptance week", "born with autism", "autism from birth", "born with it", "present from birth",
        "do only children get autism", "can adults get autism", "do only kids have autism", "How common is autism", "What are the rates of autism", "How many are autistic", "rates of autism", "vaccines cause autism", "Naltrexone", "Secretin", "Why do they talk bluntly",
        "do autistic people hurt themselves", "are they naughty", "Do they look different", "do autistic people look different", "What do they look like", "Do they look any different", "look like", "do autistic people lack empathy", "do they lack emotions",
        "do autistic people lack emotions", "are they emotionless", "do they have emotions", "emotionless", "are people with autism emotionless", "emotions", "What is Aspergers", "Asperger", "do they have repetitive movements", "do they have obsessive interests",
        "Do they have high intelligence", "What links OCD and Autism", "Do autistic people have OCD", "Do they have OCD", "Are autistic people disabled", "Are autistic people mentally disabled", "chlorine dioxide", "do they hate change of plans",
        "do they have feelings", "Why do autistic people hate change", "What jobs are there", "What treatments are available", "What support are available", "What support are there", "Are they intelligent", "Are they talented", "intelligent", "talented", "Are they anti social",
        "Why are they autistic", "Why are they upset", "upset", "Why do autistic people have repetitive movements", "Why do autistic people talk bluntly", "communicational", "sarcasm", "literally", "joke", "talking", "joke", "talking", "Why do autistic people not understand sarcasm",
        "do they not understand jokes", "why are they not talking", "are autistic people non verbal", "communication", "Why do they not talk", "What is the purpose of a diagnosis", "do they talk bluntly", "can you be born with autism", "What does meltdown mean",
        "Why do autistic people have tantrums", "What is autistic fatigue", "What does autistic fatigue mean", "What is autistic burnout", "What does autistic burnout mean", "Why are autistic people tired", "Why do they feel exhausted", "Why are they fatigued", "Why are they Burned Out",
        "Why are they tired", "Why are autistic people have headaches", "Why do they have headaches", "Fatigue", "Burnout", "Exhausted", "What links Anxiety and Autism", "Anxiety is related to autism", "Stress is related to autism", "Why are autistic people anxious",
        "Do autistic people have Anxiety", "Do they have Anxiety", "Are they anxious", "Anxiety", "What links stress and Autism", "Why are autistic people stressed", "Do autistic people have stress", "Do they have stress", "What links Suicide and Autism",
        "Why are autistic people suicidal", "Why are they suicidal", "Why do they have Suicidal", "do they have dark thoughts", "Suicidal thoughts", "Dark thoughts", "Where can I find autism therapy", "What therapy is available", "What therapies are available",
        "How do I get therapy", "Can therapy help", "Where can I find autism therapist", "What therapists are available", "How do I get therapist", "What links addiction and autism", "Do autistic people have addiction", "Addiction is related to autism",
        "Why are autistic people addicted", "Why are they addicted", "Why do they have addiction", "Why are they addicted to", "drinking so much", "are they addicts", "alcohol", "alcoholic", "substance abuse", "drugs", "narcotic", "Do autistic people feel pain",
        "Why do autistic people hate bright lights", "Why do autistic people hate noise", "Why do they hate noise", "Do they hate loud music", "loud music", "loud noises", "being touched", "itchy", "bright light", "bright lights", "smells", "smell of",
        "feel of", "sound of", "colour", "color", "feel pain", "getting hugged", "hugged", "hug", "kiss", "kissed", "taste of", "hearing", "hears", "touching", "touch", "touches", "touched", "What screening tools are there", "What diagnosis tools are available",
        "What diagnostic tools are there", "What testing tools are available", "What is DISCO", "What does DISCO mean", "What is the DISCO", "What is ADOS", "What does ADOS mean", "What is the ADOS", "What is ADIR", "What does ADIR mean", "What is the ADIR",
        "kill themselves", "kill myself", "Why are they not intelligent", "Difficulties with socialising and interacting with other people", "Why are they not social", "drink a lot", "booze", "What is Cognitive behavioural therapy", "What does Cognitive behavioural therapy mean",
        "What is CBT", "What does CBT mean", "Cognitive behavioural therapy", "What is Dialectical behaviour therapy", "What does Dialectical behaviour therapy mean", "What is DBT", "What does DBT mean", "Dialectical behaviour therapy", "Are autistic people lonely",
        "What links loneliness and autism", "Loneliness is related to autism", "Do autistic people feel lonely", "Why are they lonely", "Loneliness", "Feel alone", "Feel lonely", "Are people with autism mentally disabled", "Depression is related to autism",
        "What links depression and autism", "Do autistic people have depression", "Why are they depressed", "low mood", "Why are they sad", "Do autistic people depressed", "Depression", "Depressed", "sadness", "hidden disability", "retarded", "retard", "What links ADHD and Autism",
        "ADHD is related to autism", "Do autistic people have ADHD", "Do they have ADHD", "What links Dyslexia and Autism", "Dyslexia is related to autism", "Do autistic people have Dyslexia", "Do they have Dyslexia", "Are they dyslexic", "Are autistic people dyslexic",
        "Dyslexia", "What links Dyspraxia and Autism", "Dyspraxia is related to autism", "Do autistic people have Dyspraxia", "Do they have Dyspraxia", "Are they dyspraxic", "Are autistic people dyspraxic", "Dyspraxia", "What links Epilepsy and Autism", 
        "Epilepsy is related to autism", "Do autistic people have Epilepsy", "Do they have Epilepsy", "Are they Epileptic", "Are autistic people Epileptic", "Epilepsy", "What links bullying and Autism", "bullying is related to autism", "Do autistic people bullied",
        "Bullying", "Bullied", "How is autism diagnosed", "insomnia is related to autism", "Do autistic people have insomnia", "Do they have insomnia", "What links sleep and Autism", "sleep is related to autism", "sleeping", "bad sleep", "What links insomnia and Autism"
        ]

 
    for i in header:
        #print(lem_words[num] , " trying to add: " , i)
        lem_words[num].append(i)
    
        if i in lst:
            continue
        else:
            num += 1
            
    return lem_words


# In[63]:


def remove_placeholder(lem_words):
    accepted_words = []
    plc = ["placeholder"]
    for i in lem_words:
        words = []
        for j in i:
            if j not in plc:
                words.append(j)
        
        accepted_words.append(words)
    return accepted_words


# In[64]:


def create_intent(lem_words, response):
    num = 0
    intents = []
    gr = "greeting"
    gb = "goodbye"
    ty = "gratitude"

    greeting = ["hi", "hi there", "hola", "hello", "hello there", "hya", "hya there", "greetings"]
    greeting_res = ["Hello, thanks for visiting! How can I inform you about autism today?", "Good to see you again! How can I inform you about autism today?", "Hi there, How can I inform you about autism today?"]
    goodbye = ["bye", "see you later", "goodbye", "farewell"]
    goodbye_res = ["See you later", "thanks for visiting", "Have a nice day", "Bye! Come back again soon.", "Thanks for chatting with me. Have a good one!", "It's been a pleasure talking to you. Goodbye!"]
    gratitude = ["thanks", "thank you", "thank you so much"]
    gratitude_res = ["I am so happy that I could inform you about autism", "Happy to help! If you want to learn more about autism then please let me know!", "Great, I am glad that I have helped you today :)"]

    
    greeting_pattern = intent_pattern(greeting)
    greeting_response = intent_pattern(greeting_res)
    intent = {
        "tag": f"response_{gr}",
        "patterns": [f"{greeting_pattern}"],
        "responses": [f"{greeting_response}"]    
    }
    intents.append(intent)
    
    goodbye_pattern = intent_pattern(goodbye)
    goodbye_response = intent_pattern(goodbye_res)
    intent = {
        "tag": f"response_{gb}",
        "patterns": [f"{goodbye_pattern}"],
        "responses": [f"{goodbye_response}"]    
    }
    intents.append(intent)
                    
    gratitude_pattern = intent_pattern(gratitude)
    gratitude_response = intent_pattern(gratitude_res)
    intent = {
        "tag": f"response_{ty}",
        "patterns": [f"{gratitude_pattern}"],
        "responses": [f"{gratitude_response}"]    
    }
    intents.append(intent)
                    
    for tokens in lem_words:
        pattern = intent_pattern(tokens)
              
        intent = {
            "tag": f"response_{num}",
            "patterns": [f"{pattern}"],
            "responses": [f"{response[num]}"]    
        }
        num += 1
        intents.append(intent)
    
    json = {"intents": intents}
    json = str(json)
    json = json.replace("'", '"')
    json = json.replace('""', '"')
    
    return json


# In[65]:


def intent_pattern(i):
    pattern = ""
    for j in range(len(i)):
        if j == (len(i)-1):
            pattern += '"' + i[j] + '"'
        else:
            pattern += '"' + i[j] + '", '
    pattern = pattern.replace("'", "")
    
    return pattern


# In[66]:


def create_json_file(json):
    try:
        if os.path.exists("./scraped_intents/intents.json"):
          os.remove("./scraped_intents/intents.json")
        else:
          print("File Not Found")
    except:
        print("Error removing old intents file")
    
    try:
        with open('./scraped_intents/intents.json', 'w') as txt:
            txt.write(str(json))
    except:
        print("Error creating intents file")
    else:
        print("File successfully created")


# In[67]:


print("\nScraping Websites - 7%               █ o o o o o o o o o o o o o")
data, header, response = get_data()
res = response
print("done")


# In[68]:


print("\nTokenizing sentences - 14%           █ █ o o o o o o o o o o o o")
word_sen = tokenize(data)
print("done")


# In[69]:


print("\nTokenizing responses - 21%           █ █ █ o o o o o o o o o o o")
response = res_tokenize(response)
print("done")


# In[70]:


print("\nStripping sentences - 28%            █ █ █ █ o o o o o o o o o o")
word_sen = strip(word_sen)
print("done")


# In[71]:


print("\nTokenizing headers - 36%             █ █ █ █ █ o o o o o o o o o")
header = tokenize(header)
print("done")


# In[72]:


print("\nStripping intents - 43%              █ █ █ █ █ █ o o o o o o o o")
header = strip(header)
print("done")


# In[73]:


print("\nConverting to .txt - 50%             █ █ █ █ █ █ █ o o o o o o o")
res = stop_words(str(res))
response_txt = ""
for i in response:
    response_txt += str(i) + ". "
create_text_file(res, response_txt)
print("done")


# In[74]:


print("\nTokenizing words - 57%               █ █ █ █ █ █ █ █ o o o o o o")
words = [nltk.word_tokenize(i) for i in word_sen]
print("done")


# In[75]:


print("\nLemmatizing words - 64%              █ █ █ █ █ █ █ █ █ o o o o o")
lem_words = lemmatization(words)
print("done")


# In[76]:


print("\nRemoving stop words - 71%            █ █ █ █ █ █ █ █ █ █ o o o o")
lem_words = lem_stop(lem_words)
print("done")


# In[77]:


print("\nMerging intents - 79%                █ █ █ █ █ █ █ █ █ █ █ o o o")
lem_words = append_header(lem_words, header)
print("done")


# In[78]:


print("\nremoving placeholders - 86%          █ █ █ █ █ █ █ █ █ █ █ █ o o")
lem_words = remove_placeholder(lem_words)
print("done")


# In[79]:


print("\nConverting to JSON format - 94%      █ █ █ █ █ █ █ █ █ █ █ █ █ o")
json = create_intent(lem_words, response)
print("done")


# In[80]:


print("\nCreating JSON file - 99%             █ █ █ █ █ █ █ █ █ █ █ █ █ █")
create_json_file(json)
print("done")


# In[81]:


print("\nTask completed - 100%                ████████████████████████████")


# In[82]:


print("\n\n")
input("Please press ENTER to exit")

