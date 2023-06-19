from django.contrib import admin


from .models import User, Champion_rate, Champions,Champion_story, champion_tip, Champion_counter, champion_skill_name, champion_skill_img_text, Review

admin.site.register(User)
admin.site.register(Champions)
admin.site.register(Champion_rate)
admin.site.register(Champion_story)
admin.site.register(champion_tip)
admin.site.register(Champion_counter)
admin.site.register(champion_skill_name)
admin.site.register(champion_skill_img_text)
admin.site.register(Review)

# Register your models here.
