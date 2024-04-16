from typing import Optional
from bs4 import BeautifulSoup
from realmeye.models import StatusEffect
#import lxml
#import cchardet
def parse_status_effects(html_data: str) -> Optional[StatusEffect]:
    soup = BeautifulSoup(html_data, 'html.parser')
    soup.find('div', class_='wiki-page')
    names = [name.get('name') for name in soup.find_all("a", attrs={"href": None, "name": True})]
    print(len(names))
    descriptions = [description.get_text() for description in soup.find_all('p') if description.em ]
    #for em in soup.find_all('em'):
        #em.decompose()
    #for d, n in zip(descriptions, names):
        #print()
        #print(d)
        #print('---------------------------------------------------------------------')
    print(len(descriptions))
    """Plan:
    1. Scrape all the status effects information at once into arrays
        * so all the names will be its own array, along with icons, and descriptions

    2. Match all status effect names, photos, and descriptions based on the order
    of indices, and make that into a separate StatusEffect List object 
        * caveat: some effects might be mismatched (find a way to fix this)

    3. Put in another argument for the status effect that the specific developer wants,
    see if it's in the array created in 3, and then return that specific effect
    
    Note: I could skip creating the StatusEffect List object"""
    return 