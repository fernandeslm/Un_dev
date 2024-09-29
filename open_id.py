import wo_maker

wofile  = r'in\wo\RFS-1-12003843920.txt'
name = wo_maker.get_fp_name(wofile)

body_email = f"""Dear {name},

Application registration completed in Azure AD. Please find the details below.
Application Client ID : <<>>
 
Tenant ID : 0f9e35db-544f-4f60-bdcc-5ea416e6dc70
 
Authorization End point :  https://login.microsoftonline.com/0f9e35db-544f-4f60-bdcc-5ea416e6dc70/oauth2/v2.0/authorize
 
Token End point :  https://login.microsoftonline.com/0f9e35db-544f-4f60-bdcc-5ea416e6dc70/oauth2/v2.0/token 
 
Below groups are created and assigned to application. Cloud groups can be managed from https://myapplications.microsoft.com

Best Regards,
Luis Fernandes

"""

print (body_email)