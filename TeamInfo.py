class TeamInfo():
    ''' Represents a single team '''
    def __init__(self, init_dict):
        self._raw_dict = init_dict
        self. address = init_dict['address']
        self.city = init_dict['city']
        self.country = init_dict['country']
        self.gmaps_place_id = init_dict['gmaps_place_id']
        self.gmaps_url = init_dict['gmaps_url']
        self.home_championship = init_dict['home_championship']
        self.key = init_dict['key']
        self.lat = init_dict['lat']
        self.lng = init_dict['lng']
        self.location_name = init_dict['location_name']
        self.motto = init_dict['motto']
        self.name = init_dict['name']
        self.nickname = init_dict['nickname']
        self.postal_code = init_dict['postal_code']
        self.rookie_year = init_dict['rookie_year']
        self.state_prov = init_dict['state_prov']
        self.team_number = init_dict['team_number']
        self.website = init_dict['website']
    def __repr__(self):
        string_representation = "\n**********TEAM**********\n"
        if self.team_number:
            string_representation += "Team Number: {team_number}\n".format(team_number = self.team_number)
        if self.name:
            string_representation += "Name: {name}\n".format(name = self.name)
        if self.address:
            string_representation += "Address: {address}\n".format(address = self.address)
        if self.city:
            string_representation += "City: {city}\n".format(city = self.city)
        if self.country:
            string_representation += "Country: {city}\n".format(city = self.city)
        if self.home_championship:
            string_representation += "Home Championship(s): {home_championship}\n".format(home_championship = self.home_championship)
        if self.location_name:
            string_representation += "Location Name: {location_name}\n".format(location_name = self.location_name)
        if self.motto:
            string_representation += "Motto: {motto}\n".format(motto = self.motto)
        if self.nickname:
            string_representation += "Nickname: {nickname}\n".format(nickname = self.nickname)
        if self.postal_code:
            string_representation += "Postal Code: {postal_code}\n".format(postal_code = self.postal_code)
        if self.rookie_year:
            string_representation += "Rookie Year: {rookie_year}\n".format(rookie_year = self.rookie_year)
        if self.state_prov:
            string_representation += "State/Province: {state_prov}\n".format(state_prov = self.state_prov)
        if self.website:
            string_representation += "Website: {website}\n".format(website = self.website)
        string_representation += "\n"
        return string_representation

    def __str__(self):
        return "Team {team_number}: {nickname}. From {city} {state_prov}".format(
            team_number = self.team_number, 
            nickname = self.nickname, 
            city = self.city, 
            state_prov = self.state_prov)
    
    def queryEvents(self, year = None):
        '''Perform a TBA query for all events this team has competed in. Optional filter based on year.'''
        pass