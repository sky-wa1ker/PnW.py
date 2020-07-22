import requests


f = open('key.txt', 'r')
api_key = f.readline()
f.close()



class Nation:

    def __init__(self, nation_id):
        
        nation_dict = requests.get(f'https://politicsandwar.com/api/nation/id={nation_id}&key={api_key}').json()
        if 'error' in nation_dict:
            print(nation_dict.get('error'))
            exit()

        elif 'general_message' in nation_dict:
            print(nation_dict.get('general_message'))
            exit()

        else:
            self.name = nation_dict.get('name')
            self.leader = nation_dict.get('leadername')
            self.id = nation_dict.get('nationid')
            self.continent = nation_dict.get('continent')
            self.last_active = str(nation_dict.get('minutessinceactive')) + ' minutes ago.'
            self.war_policy = nation_dict.get('war_policy')
            self.founded = nation_dict.get('founded')
            self.color = nation_dict.get('color')
            self.domestic_policy = nation_dict.get('domestic_policy')
            self.daysold = nation_dict.get('daysold')
            self.alliance = nation_dict.get('alliance')
            self.alliance_id = nation_dict.get('allianceid')
            self.flag = nation_dict.get('flagurl')
            self.score = nation_dict.get('score')
            self.city_count = nation_dict.get('totalinfrastructure')
            self.avg_infra = round(nation_dict.get('totalinfrastructure') / nation_dict.get('cities'))
            self.land_area = nation_dict.get('landarea')
            self.soldiers = nation_dict.get('soldiers')
            self.tanks = nation_dict.get('tanks')
            self.ships = nation_dict.get('ships')
            self.missiles = nation_dict.get('missiles')
            self.nukes = nation_dict.get('nukes')
            self.offensive_wars = nation_dict.get('offenisvewars')
            self.defensive_wars = nation_dict.get('defensivewars')



nation1 = Nation('176311')

print(nation1.avg_infra)