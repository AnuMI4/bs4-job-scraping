import requests
from bs4 import BeautifulSoup
import time

def job_scrape():
    html_text = requests.get('https://laborx.com/?utm_source=google&utm_medium=UK_IR&utm_campaign=uk_ir&utm_term=best%20job%20posting%20sites&gad_source=1&gclid=CjwKCAjwgdayBhBQEiwAXhMxtoM1bzBm36MyHfKwiSch536o4a_Hx_uWezGEfRPBDVzd5YwpE-DZPRoCPkIQAvD_BwE').text

    soup = BeautifulSoup(html_text, 'lxml')

    job_cards = soup.find_all(class_='card-content')

    for index, job_card in enumerate(job_cards):
        # Get all 'a' tags with class 'name-link'
        links = job_card.find_all('a', class_='name-link')

        # Extract the texts using indices
        job_name = links[0].text.strip()
        company_name = links[1].text.strip()
        job_info = job_card.find(class_='info').text.strip()
        job_time = job_card.find(class_='time').text.strip()
        skills_wrapper = job_card.find('div', class_='skills-wrapper')
        skills = skills_wrapper.find('a', class_='tag clickable')

        with open(f'posts/{index}.txt', 'w',  encoding="utf-8") as f:
            # print(f'''
            # Job Name: {job_name}
            # Company Name: {company_name}
            # Job Type: {job_info}
            # Posted: {job_time}
            # Skills: {skills}
            # ''')
            f.write(f'Job Name: {job_name} \n')
            f.write(f'Company Name: {company_name} \n')
            f.write(f'Job Type: {job_info} \n')
            f.write(f'Posted: {job_time}')
        print(f'File saved {index}')

if __name__ == '__main__':
    while True:
        job_scrape()
        time_wait = 10
        print(f'waiting {time_wait} seconds')
        time.sleep(time_wait)