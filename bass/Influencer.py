class Influencer:

    def __init__(self, username, name, bio, posts, total_followers, max_likes, profile_pic_url, paragraph=None):

        self.instagram_url = "https://www.instagram.com/"+username+"/"
        self.profile_pic_url = profile_pic_url
        self.username= username
        self.name= name
        self.bio= bio
        self.posts= posts                   #list of Post objects
        self.total_followers= total_followers
        self.max_likes= max_likes

        if total_followers>0:
            self.engagement_index= max_likes/total_followers
        else:
            self.engagement_index=0
        
        self.paragraph= paragraph            #all posts' info added up into a paragraph

        if paragraph==None:
            self.CreateInfluencerParagraph()    #create paragraph when new influencer is created
        
    def __str__(self):
        return self.username +" " + self.name

    def __repr__(self):
        return "Influencer Object"+ "\nusername: "+self.username+ "\nname: "+ self.name + "\nbio: "+ self.bio + "\ntotal_followers: "+ self.total_followers + "\nmax_likes: "+self.max_likes+ "\engagement_index: "+self.engagement_index
         
    def CreateInfluencerParagraph(self):    #combines all posts' paragraphs into 1 single paragraph

        result_paragraph= ""
        
        for post in self.posts:
            result_paragraph+= post.postTag + " "

        self.paragraph= result_paragraph

    def CreateInfluencerDict(self):
        
        #result={ "instagram_url": self.instagram_url, "username": self.username, "name":self.name, "bio": self.bio, "posts":self.posts,"total_followers": self.total_followers, "max_likes": self.max_likes, "paragraph":self.paragraph,"engagement_index":self.engagement_index}
        result={ "instagram_url": self.instagram_url, "username": self.username, "name":self.name, "bio": self.bio, "total_followers": self.total_followers, "max_likes": self.max_likes, "profile_pic_url": self.profile_pic_url, "paragraph":self.paragraph,"engagement_index":self.engagement_index}
  
        return result
