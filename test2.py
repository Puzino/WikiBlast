
from bs4 import BeautifulSoup
import mechanicalsoup

url = 'https://ru.wikipedia.org/wiki/Служебная:RandomInCategory'
for _ in range(10):
    br = mechanicalsoup.StatefulBrowser()
    br.open(url)
    submit = br.page.find('input', {'name': 'wpcategory'})
    submit['value'] = "Информационная безопасность"
    button = br.page.find('button', {'class': 'oo-ui-inputWidget-input oo-ui-buttonElement-button'})
    form = br.select_form()
    form.choose_submit(button)
    br.submit_selected()
    bs = BeautifulSoup(str(br.page), 'lxml')
    print(bs.find('span', {'class':'mw-page-title-main'}))