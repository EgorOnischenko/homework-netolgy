#!/usr/bin/env python
# coding: utf-8

# In[97]:


# Task 1


# In[98]:


class Goose:
    
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    
    def feed(self, food):
        self.weight += food
        
    def collect_eggs(self, quantity):
        self.weight -= quantity * 0.144
        
    def sound(self):
        print('Honk!')
        
class Cow:
    
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        
    def feed(self, food):
        self.weight += food
    
    def milk(self, litres):
        self.weight -= litres
    
    def sound(self):
        print('Moooo!')
        
class Sheep:
    
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        
    def feed(self, food):
        self.weight += food
        
    def shear(self, kg):
        self.weight -= kg
    
    def sound(self):
        print('Baaa!')
    
class Chicken:
    
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        
    def feed(self, food):
        self.weight += food
        
    def collect_eggs(self, quantity):
        self.weight -= quantity * 0.06
        
    def sound(self):
        print('Clucking!')
    
class Goat:
    
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        
    def feed(self, food):
        self.weight += food
        
    def milk(self, litres):
        self.weight -= litres
        
    def sound(self):
        print('Bleat!')

class Duck:
    
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        
    def feed(self, food):
        self.weight += food
        
    def collect_eggs(self, quantity):
        self.weight -= quantity * 0.07
        
    def sound(self):
        print('Quack!')
    


# In[99]:


farm = []
grey = Goose('Grey', 5.45)
farm.append(grey)

white = Goose('White', 5.45)
farm.append(white)

manka = Cow('Manka', 545)
farm.append(manka)

rammy = Sheep('Rammy', 100)
farm.append(rammy)

curly = Sheep('Curly', 100)
farm.append(curly)

co_co = Chicken('Co-Co', 3)
farm.append(co_co)

cock_a_doodle_doo = Chicken('Cock-A-Doodle-Doo', 3)
farm.append(cock_a_doodle_doo)

horns = Goat('Horns', 25)
farm.append(horns)

hooves = Goat('Hooves', 25)
farm.append(hooves)

quacky = Duck('Quacky', 2.9)
farm.append(quacky)


# In[100]:


for animal in farm:
    
    if isinstance(animal, Goose):
        animal.feed(1)
        animal.collect_eggs(3)
    
    elif isinstance(animal, Cow):
        animal.feed(15)
        animal.milk(10)
        
    elif isinstance(animal, Sheep):
        animal.feed(5)
        animal.shear(2)
        
    elif isinstance(animal, Chicken):
        animal.feed(0.5)
        animal.collect_eggs(5)
        
    elif isinstance(animal, Goat):
        animal.feed(3)
        animal.milk(2)
        
    elif isinstance(animal, Duck):
        animal.feed(1.5)
        animal.collect_eggs(4)
    
    print(animal.weight)


# In[101]:


total_weight = 0
max_weight = 0
leader_id = 0

for id, animal in enumerate(farm):
  
    total_weight += animal.weight
    
    if animal.weight > max_weight:
        max_weight = animal.weight
        leader_id = id
    else:
        pass

print(farm[leader_id].name)
print(total_weight)  


# In[102]:


# Task 2


# In[103]:


class Track:
    
    def __init__(self, name, duration):
        self.name = name
        self.duration = int(duration)
        
    def show(self):
        print(f'<{self.name}-{self.duration}>')
        


# In[104]:


atlas = Track('Atlas', 6)


# In[105]:


atlas.show()


# In[130]:


class Album:
    
    def __init__(self, name, band):
        self.a_name = name
        self.band = band
        self.tracks = []
        
        
    def get_tracks(self):
        for track in self.tracks:
            Track.show(track)

        
    def add_track(self, name, duration, track):
        self.name = name
        self.duration = int(duration)
        self.track = track
        
        self.track = Track(self.name, self.duration)
        self.tracks.append(self.track)
        
    def get_duration(self):
        duration = 0
        for track in self.tracks:
            duration += track.duration
            
        return duration


# In[131]:


fallen_light = Album('Fallen Light', 'Phaeleh')
tides = Album('Tides', 'Phaeleh')


# In[132]:


# Adding tracks to the first album
fallen_light.add_track('Afterglow', 4, 'track_1')
fallen_light.add_track('Losing You', 6, 'track_2')
fallen_light.add_track('Lament', 5, 'track_3')

# Adding tracks to the second album
tides.add_track('Journey',5, 'track_1' )
tides.add_track('Storm',5, 'track_2' )
tides.add_track('Tokoi',3, 'track_3' )

# while True:
#     x = input('To add a new track to "Fallen Light" - press 1, to add a new track to "Tides" - press 2. To exit - press "e" ')
#     if x == '1':
#         fallen_light.add_track()
#     elif x == '2':
#         tides.add_track()
#     elif x == 'e':
#         break


# In[133]:


fallen_light.get_tracks()


# In[134]:


tides.get_tracks()


# In[135]:


fallen_light.get_duration()


# In[136]:


tides.get_duration()


# In[ ]:





# In[ ]:




