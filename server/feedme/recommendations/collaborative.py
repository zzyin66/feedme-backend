from ..models import Feed, User
from datetime import date, timedelta

def generate_collaborative_recommendations(id):
    try:
        user = User.objects.get(id=id)
        
        today = date.today()
        date_minimum = today - timedelta(days=1)
        feed_history = user.feed_history.all()
        read_feed_ids = [feed.id for feed in feed_history]
        
        keywords = user.keywords
        
        if not keywords:
            # user has no keywords and cannot be grouped with similar users
            return []

        users = User.objects.exclude(id=id)
        
        matches = {}
        user_magnitude = 0
        
        # magnitude of the user's keywords for cosine similarity 
        for keyword in keywords.values():
            user_magnitude += keyword*keyword
        
        for matching_user in users:
            matching_keywords = matching_user.keywords
            match_score = 0
            matching_magnitude = 0
            
            for key, value in matching_keywords.items():
                match_score += value * keywords.get(key, 0.0)
                matching_magnitude = value * value
                
            match_score = match_score / matching_magnitude  
            # cosine similarity has to be greater than 0.5
            if match_score > 0.5:
                matches[matching_user] = match_score

        matches = dict(sorted(matches.items(), key=lambda x: x[1], reverse=True))  
        
          
        # every 10 users is a group
        user_cluster = list(matches.keys())[:9]
        
        recommendations = []
        for matching_user in user_cluster:
            unread_feed = list(matching_user.feed_history.filter(date__gte=date_minimum).exclude(id__in=read_feed_ids))
            recommendations.extend([feed.id for feed in unread_feed])
        return recommendations[:15]
    
    except:
        return []