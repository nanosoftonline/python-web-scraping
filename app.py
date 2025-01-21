from requests_html import HTMLSession   
from bs4 import BeautifulSoup

def scrape_table_columns(url):
    session = HTMLSession()
    res = session.get(url)
    soup = BeautifulSoup(res.html.html, 'html.parser')

    table = soup.find_all('table')[0]
    rows = table.find_all('tr')
    
    team_points = []
    
    for row in rows[1:]:
        cols = row.find_all('td')
        if len(cols) >= 3: 
            team_data = {
                'team': cols[1].text.strip(),
                'points': int(cols[3].text.strip())
            }
            team_points.append(team_data)
    
    return team_points


url = 'https://all.rugby/tournament/urc/table'
table_data = scrape_table_columns(url)
print(table_data)