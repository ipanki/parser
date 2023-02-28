import asyncio

import httpx
from bs4 import BeautifulSoup
from fastapi import HTTPException
from starlette import status
from src.config.config import lamoda_config


class ParserLamoda:
    def __init__(self):
        self.url = lamoda_config.url
        self.price = lamoda_config.price
        self.discount_price = lamoda_config.discount_price
        self.pages = lamoda_config.pages

    async def parse_clothes(self):
        man_clothes = []
        for page in range(1, self.pages + 1):
            async with httpx.AsyncClient(timeout=None) as client:
                lamoda_url = f'{self.url}?page={page}'
                response = await client.get(lamoda_url)

                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    all_data = soup.find_all('div', class_='x-product-card__card')
                    thing_category = soup.h1.text.strip()

                    for data in all_data:
                        thing_brand = data.find('div', class_='x-product-card-description__brand-name').text
                        thing_model = data.find('div', class_='x-product-card-description__product-name').text

                        if data.find('div', class_='x-product-card-description__microdata-wrap').find(
                                'span', class_=self.discount_price):
                            thing_price = data.find('div', class_='x-product-card-description__microdata-wrap').find(
                                'span', class_=self.discount_price).text
                        else:
                            thing_price = data.find('div', class_='x-product-card-description__microdata-wrap').find(
                                'span', class_=self.price).text
                        int_price = thing_price.replace(" ", "").replace("р.", "")
                        thing_data = dict(
                            brand=thing_brand,
                            model=thing_model,
                            category=thing_category,
                            price=int_price
                        )
                        man_clothes.append(thing_data)

                else:
                    raise HTTPException(status.HTTP_400_BAD_REQUEST, detail='Parsing raised error')
        return man_clothes



