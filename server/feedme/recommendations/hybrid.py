from .content import generate_content_recommendations
from .collaborative import generate_collaborative_recommendations
from ..models import User
import random

def hybrid_recommendations(id):
    content_recommendations = generate_content_recommendations(id)
    collborative_recommendations = generate_collaborative_recommendations(id)
    
    common_recommendations = [x for x in content_recommendations if x in collborative_recommendations]
    
    recommendations = []
    if common_recommendations:
        recommendations.extend(common_recommendations)
        recommendations.extend(content_recommendations[:7])
        recommendations.extend(collborative_recommendations[:7])
        recommendations = list(set(recommendations))
    else:
        recommendations.extend(content_recommendations[:10])
        recommendations.extend(collborative_recommendations[:5])
        
    random.shuffle(recommendations)
    
    try:
        user = User.objects.get(id=id)
        user.recommendations.clear()
        user.recommendations.add(*recommendations)
        user.save()
    except:
        pass