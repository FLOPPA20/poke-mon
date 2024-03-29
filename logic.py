from random import randint
from datetime import datetime,timedelta
import requests
from time import sleep

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.power = randint(5,10)
        self.hp = randint(30,50)
        self.last_feed_time = datetime.now()
        Pokemon.pokemons[pokemon_trainer] = self
        
    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['other']['official-artwork']['front_default'])
        else:
            return "Pikachu"
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"
    def attack(self,enemy):
        if isinstance(enemy,Sprinter): # Проверка на то, что enemy является типом данных Wizard (является экземпляром класса Волшебник)
            chance = randint(1,3)
            if chance == 1:
                return "Покемон увернулся от атаки"
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
        else:
            enemy.hp = 0
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "

    # Метод класса для получения информации
    def info(self):
        return f'''Имя твоего покеомона: {self.name},
Сила покемона {self.power},
Жизнь покемона {self.hp}'''

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img

    def feed(self, feed_interval = 20, hp_increase = 10 ):
        current_time = datetime.now() 
        delta_time = timedelta(seconds=feed_interval)  
        if (current_time - self.last_feed_time) > delta_time:
            self.hp += hp_increase
            self.last_feed_time = current_time
            return f"Здоровье покемона увеличено. Текущее здоровье: {self.hp}"
        else:
            return f"Следующее время кормления покемона: {self.last_feed_time+delta_time}"  

class Sprinter(Pokemon):
    def info(self):
        return  "у тебя покемон спринтер\n"+ super().info()


class Fighter(Pokemon):
    def attack(self, enemy):
        superpower = randint(0,10)
        self.power += superpower
        res = super().attack(enemy)
        self.power -= superpower
        return res +f'\nБоец применил усиленый  удар {superpower}'
    def info(self):
        return "у тебя покемон боец"+ super().info()





flopp = Pokemon('user2311232131245234')
print(flopp.info())
print(flopp.feed())
sleep (20)
print(flopp.feed())
print(flopp.info())
