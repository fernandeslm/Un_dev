
def get_app(fileIn):
    print('Please name application:')
    filterLn = ""
    EntityId = 'Entity Name: '
    AppAbrv ='App Abbrev: '
    env = 'Environment (Other): '
    
    with open(fileIn, 'r') as read:
      for line in read:
        if AppAbrv in line:
          comment = line.replace(AppAbrv, '').rstrip('\n') + '-'
        if EntityId in line:
          comment += line.replace(EntityId, '').rstrip('\n') + '-'
        if env in line:
          comment += line.replace(env, '').rstrip('\n')
        
    return comment.upper() 

def get_owner(fileIn):
    print('Owners:')
    filterLn = ""
    Fpmail = 'FP Email: '
  
    with open(fileIn, 'r') as read:
      for line in read:
        if Fpmail in line:
          print (line.replace(Fpmail, '').rstrip('\n'))
        
    return 

def signon(fileIn):
    print('signon:')
    filterLn = ""
    signon = 'Sign-on URL: '
  
    with open(fileIn, 'r') as read:
      for line in read:
        if signon in line:
          print (line.replace(signon, '').rstrip('\n'))
        
    return 

def get_protocol(fileIn):
    print('protocol_urls:')
    filterLn = ""
    reply_url = 'Open ID Reply URL: '
    logout_url = 'OpenID Logout URL: '

    with open(fileIn, 'r') as read:
      for line in read:
        if reply_url in line:
          print ('reply: ' + line.replace(reply_url, '').rstrip('\n'))
        if logout_url in line:
          print ('logout: ' + line.replace(logout_url, '').rstrip('\n'))
    return 

def get_group(fileIn):
    print('Groups:  ')
    filterLn = ""
    EntityId = 'Entity Name: '
    AppAbrv ='App Abbrev: '
    env = 'Environment (Other): '
    guests = '-GUESTS-ASGM'
    members = '-MEMBERS-ASGM'
    
    with open(fileIn, 'r') as read:
      for line in read:
        if AppAbrv in line:
          comment = line.replace(AppAbrv, '').rstrip('\n') + '-'
        if EntityId in line:
          comment += line.replace(EntityId, '').rstrip('\n') + '-'
        if env in line:
          comment += line.replace(env, '').rstrip('\n')
        
    return comment.upper() + guests + ('\n') +  comment.upper() + members