


def get_app(fileIn):
    print('Please name application:')
    filterLn = ""
    EntityId = 'Entity Name: '
    AppAbrv ='App Abbrev: '
    env = 'Environment (Other): '
    
    with open(fileIn, 'r') as read:
      for line in read:
        if AppAbrv in line:
          AppAbrv = line.replace(AppAbrv, '').rstrip('\n')
        if EntityId in line:
          EntityId = line.replace(EntityId, '').rstrip('\n')
        if env in line:
          env = line.replace(env, '').rstrip('\n')
        
      comment = EntityId + '-' + AppAbrv + '-' + env
    return comment.upper()



