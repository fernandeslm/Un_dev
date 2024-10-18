class Wo: 
  def __init__(self, fileIn):
    self.FileIn = fileIn

  def entity(self):      
      EntityId = 'Entity Name: '
      
      with open(self.FileIn, 'r') as read:
        for line in read:
          if EntityId in line:
            comment = line.replace(EntityId, '').rstrip('\n')
      return comment.upper() 
  
  def abrv(self):      
      AppAbrv = 'App Abbrev: '
      
      with open(self.FileIn, 'r') as read:
        for line in read:
          if AppAbrv in line:
            comment = line.replace(AppAbrv, '').rstrip('\n')
      return comment.upper() 
  
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


  #def get_fp_name(self):
      Fpmail = 'FP First Name:  '
    
      with open(self.FileIn, 'r') as read:
        for line in read:
          if Fpmail in line:
            comment = (line.replace(Fpmail, '').rstrip('\n'))
          
      return comment[3:]
  
  def owner(self):
      Fpmail = 'FP Email: '
      comment = ''
      with open(self.FileIn, 'r') as read:
        for line in read:
          if Fpmail in line:
           comment =+ (line.replace(Fpmail,'').rstrip('\n'))
      return comment

  def signon(self):
      signon = 'Sign-on URL: '
    
      with open(self.FileIn, 'r') as read:
        for line in read:
          if signon in line:
            comment = line.replace(signon, '').rstrip('\n')
          
      return comment

  def reply(self):
      reply_url = 'Open ID Reply URL: '

      with open(self.FileIn, 'r') as read:
        for line in read:
          if reply_url in line:
            comment = line.replace(reply_url, '').rstrip('\n')

      return comment
  
  def logout(self):
      logout_url = 'OpenID Logout URL: '

      with open(self.FileIn, 'r') as read:
        for line in read:
          if logout_url in line:
            comment = line.replace(logout_url, '').rstrip('\n')

      return comment     
    
  def close(self):
     app = self.entity() + '-' + self.abrv() + '-' + self.env()
     owner = self.owner()
     signon = self.signon()
     reply = self.reply()
     logout = self.logout()
     #group = self.group()
     
     body = f"""
Please name application: 
{app}

Owners:
{owner}

Sign-on URL: 
{signon}

Protocol_urls:
{reply}
{logout}

Groups: 
{app}-MEMBERS-ASGM

"""
     print (body)

