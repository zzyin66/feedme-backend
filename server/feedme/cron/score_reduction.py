from ..models import User

def score_reduction():
    users = User.objects.all()
    
    for user in users:
        user_keywords = user.keywords
        for key in user_keywords.keys():
            reduction_value = float(user_keywords[key]) * 0.8
            user_keywords[key] = reduction_value
        user.keywords = user_keywords
        user.save()
            