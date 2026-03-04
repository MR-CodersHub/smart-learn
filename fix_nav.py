import os
import re

directory = r'c:\Users\dines\OneDrive\Desktop\EDUC WEBSITE'

# Standard items: (href, text)
nav_items = [
    ('index.html', 'Home'),
    ('home-digital.html', 'Digital Platform'),
    ('about.html', 'About Us'),
    ('programs.html', 'Programs'),
    ('courses.html', 'Courses'),
    ('contact.html', 'Contact')
]

updated_count = 0

for filename in os.listdir(directory):
    if filename.endswith('.html'):
        filepath = os.path.join(directory, filename)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Find the nav-links block
            # Matches <ul class="nav-links"> ... </ul> handling potential attributes spacing
            nav_regex = re.compile(r'<ul\s+class=["\']nav-links["\'][^>]*>[\s\S]*?</ul>', re.IGNORECASE)
            match = nav_regex.search(content)
            
            if match:
                old_block = match.group(0)
                
                # Determine active link
                active_href = None
                
                # 1. Explicit filename rules (Strongest signal)
                if filename == 'index.html': active_href = 'index.html'
                elif filename == 'home-digital.html': active_href = 'home-digital.html'
                elif filename == 'about.html': active_href = 'about.html'
                elif filename == 'programs.html': active_href = 'programs.html'
                elif filename == 'courses.html': active_href = 'courses.html'
                elif filename == 'contact.html': active_href = 'contact.html'
                
                # 2. Heuristics for sub-pages based on filename pattern
                elif filename.startswith('course-'): active_href = 'courses.html'
                
                # 3. Fallback: Check for existing active class/style in the OLD block
                if not active_href:
                    # Look for class="active"
                    active_match = re.search(r'<a\s+href=["\']([^"\']+)["\'][^>]*class=["\'][^"\']*active', old_block)
                    if active_match:
                        active_href = active_match.group(1)
                    else:
                        # Look for style="color: var(--primary)" or similar
                        style_match = re.search(r'<a\s+href=["\']([^"\']+)["\'][^>]*style=["\'][^"\']*color', old_block)
                        if style_match:
                            active_href = style_match.group(1)

                # Special cases for known sub-pages if heuristics failed
                if not active_href:
                     if filename in ['digital-business.html', 'design-ux.html', 'ai-data.html', 'elite-mentorship.html', 'expert-instructors.html', 'flexible-learning.html', 'certifications.html']:
                         active_href = 'programs.html'
                     elif filename in ['login.html', 'signup.html', 'reset-password.html', '404.html', 'privacy-policy.html', 'faq.html', 'support.html']:
                         active_href = None # No active link for auth/utility pages usually, or maybe 'Home'? Let's set None to be safe.

                # Rebuild block
                new_list_items = []
                for href, text in nav_items:
                    is_active = (href == active_href)
                    attr = ' class="active"' if is_active else ''
                    new_list_items.append(f'                    <li><a href="{href}"{attr}>{text}</a></li>')
                
                new_block = '<ul class="nav-links">\n' + '\n'.join(new_list_items) + '\n                </ul>'
                
                # Normalizing whitespace for comparison could be good, but strict replacement is safer if we match formatting
                if new_block.strip() != old_block.strip():
                    new_content = content.replace(old_block, new_block)
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated {filename}")
                    updated_count += 1
                else:
                    print(f"Skipped {filename} (already correct)")
            else:
                print(f"No navbar found in {filename}")
                
        except Exception as e:
            print(f"Error processing {filename}: {e}")

print(f"Total files updated: {updated_count}")
