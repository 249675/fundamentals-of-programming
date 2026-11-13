#An influencer is a person who can influence other people's behaviour. An influencer communicates with other people using social networking sites. Write a program that checks whether a given person is a good influencer, that is, whether the person has at least two of the following accounts: Facebook, Twitter or Instagram. Use logical type variables: facebook, twitter, instagram, the value of which indicates whether the person has an account on the social networking site. Sample result:

facebook = True
twitter = False
instagram = True
 # You are a good influencer!

if facebook == True and twitter == True and instagram == True:
    print("You are a good influencer!")
elif facebook == True and twitter == True and instagram == False: 
    print("You are a good influencer!")   
elif facebook == True and twitter == False and instagram == True: 
    print("You are a good influencer!")
else:
    print("Try harder with social medias!")       