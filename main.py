from fasthtml.common import *
from monsterui.all import *

# Choose a clean theme for Notion-like appearance
hdrs = Theme.neutral.headers()

# Create your app with the theme
app, rt = fast_app(hdrs=hdrs)

@rt
def index():
    socials = [('github', 'https://github.com/vinayakathavale/aihumorproject')]
    
    return Div(
        # Title section
        H1("AIHUMORPROJECT", cls="text-3xl font-bold mb-6"),
        
        # Main heading
        H2("Can AI Be Funny?", cls="text-2xl font-bold mb-4"),
        P("We're exploring if Artificial Intelligence can understand and generate humor. It's a tough challenge, pushing the limits of AI creativity and language understanding.", 
          cls="mb-6"),
        
        Hr(cls="my-6"),
        
        # Goal section
        H3("Our Goal 🎯", cls="text-xl font-bold mb-2"),
        P("Train AI to recognize, create, and maybe even appreciate a good joke. We analyze humor patterns and experiment with generating original comedic content.",
          cls="mb-6"),
          
        Hr(cls="my-6"),
        
        # Why section
        H3("Why? 🤔", cls="text-xl font-bold mb-2"),
        P("Humor is complex! Tackling it helps us understand both AI limitations and human intelligence better. Plus, who doesn't want funnier robots?",
          cls="mb-6"),
          
        Hr(cls="my-6"),
        
        # AI Attempt section
        H3("An AI Attempt... 😂", cls="text-xl font-bold mb-2"),
        Blockquote("Why did the AI cross the road? To optimize its pathfinding algorithm. (Work in progress!)",
                  cls="italic pl-4 border-l-4 border-gray-300 mb-6"),
        
        # Footer with social links
        DivLAligned(*[UkIconLink(icon, href=url, cls="mr-2") for icon, url in socials],
                   cls="mt-8 pt-4 border-t border-gray-200"),
        cls="notion-container max-w-3xl mx-auto p-8"
    )

serve()
