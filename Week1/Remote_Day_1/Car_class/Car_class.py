class Car(object):
  speed = 0
  def __init__(self, vehicle_type=None,model='GM',name='General'):
    self.vehicle_type= vehicle_type
    self.model = model
    self.name=name
    
    if self.name in ['Porsche', 'Koenigsegg']:
      self.num_of_doors = 2
    else:
      self.num_of_doors = 4
    
    if self.vehicle_type == 'trailer':
      self.num_of_wheels = 8
    else:
      self.num_of_wheels = 4
    
  def is_saloon(self):
    if self.vehicle_type is not 'trailer':
      self.vehicle_type=='saloon'
      return True
      
  def drive_car(self, moving_speed):
    if moving_speed == 3:
      Car.speed = 1000
    elif moving_speed == 7:
      Car.speed = 77
    return self
  
