class Wo: 
  def __init__(self, fileIn):
    self.FileIn = fileIn

  '''Entity Name'''
  def entity(self):      
      filterLn = ""
      EntityId = 'Entity Name: '
      
      with open(self.FileIn, 'r') as read:
        for line in read:
          if EntityId in line:
            comment = line.replace(EntityId, '').rstrip('\n')
      return comment.upper() 
  
  '''App Abbrev'''
  def abrv(self):      
      filterLn = ""
      AppAbrv = 'App Abbrev: '
      
      with open(self.FileIn, 'r') as read:
        for line in read:
          if AppAbrv in line:
            comment = line.replace(AppAbrv, '').rstrip('\n')
      return comment.upper() 
  
  '''Environment'''
  def env(self):
      #env = 'Environment (Other): '
      env2 = 'Environment: '
      
      with open(self.FileIn, 'r') as read:
        for line in read:
         # if env in line:
          #  comment += line.replace(env, '').rstrip('\n')
          if env2 in line:
            comment = line.replace(env2, '').rstrip('\n')
      return comment.upper() 

  '''Owner Email'''
  def get_owner(self):
      print('Owners:')
      filterLn = ""
      Fpmail = 'FP Email: '
    
      with open(self.FileIn, 'r') as read:
        for line in read:
          if Fpmail in line:
            print (line.replace(Fpmail, '').rstrip('\n'))
          
      return 

  '''Sign-on URL'''
  def signon(self):
      print('signon:')
      filterLn = ""
      signon = 'Sign-on URL: '
    
      with open(self.FileIn, 'r') as read:
        for line in read:
          if signon in line:
            print (line.replace(signon, '').rstrip('\n'))
          
      return 

  '''Open Id URL'''
  def get_protocol(self):
      print('protocol_urls:')
      filterLn = ""
      reply_url = 'Open ID Reply URL: '
      logout_url = 'OpenID Logout URL: '

      with open(self.FileIn, 'r') as read:
        for line in read:
          if reply_url in line:
            print ('reply: ' + line.replace(reply_url, '').rstrip('\n'))
          if logout_url in line:
            print ('logout: ' + line.replace(logout_url, '').rstrip('\n'))
      return 

  '''Groups'''
  def get_group(self):
      members = '-MEMBERS-ASGM'
      
      comment = self.entity() + '-' + self.abrv() + '-' + self.env()
      print('Groups:  ' + '\n' + comment +  members)

  '''Create App Name'''
  def get_appname(self):

      comment = self.entity() + '-' + self.abrv() + '+' + self.env()
      print('Please name application: ' + '\n' + comment) 

  #def get_fp_name(self):
      filterLn = ""
      Fpmail = 'FP First Name:  '
    
      with open(self.FileIn, 'r') as read:
        for line in read:
          if Fpmail in line:
            comment = (line.replace(Fpmail, '').rstrip('\n'))
          
      return comment[3:]


