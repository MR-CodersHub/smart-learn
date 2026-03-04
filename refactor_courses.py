import os
import re

folder = r'c:\Users\dines\OneDrive\Desktop\feb project\EDUC WEBSITE'
files = [f for f in os.listdir(folder) if f.startswith('course-') and f.endswith('.html')]

# We'll skip course-fullstack and course-details since they're mostly done.
skip_files = ['course-fullstack.html', 'course-details.html']

for f in files:
    if f in skip_files:
        continue
    filepath = os.path.join(folder, f)
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Hero section updates
    content = re.sub(
        r'<section style="padding: 160px 0 80px; background: var\(--surface\);\">',
        r'<section class="course-hero-section course-hero">',
        content
    )
    content = re.sub(
        r'<section style="padding: 100px 0; background: var\(--surface\);\">',
        r'<section class="course-hero-section course-hero">',
        content
    )
    # The inner container -> course-hero-container
    content = re.sub(
        r'(<section class="course-hero-section course-hero">)\s*<div class="container">',
        r'\1\n            <div class="course-hero-container">',
        content
    )
    # The back link
    content = re.sub(
        r'<a href="courses\.html"\s*style="display: inline-flex;[^"]*">',
        r'<a href="courses.html" class="course-back-link">',
        content
    )
    
    # The hero grid and content div
    # Replaces `<div style="display: grid; grid-template-columns: 1fr 450px; gap: 4rem; align-items: center;"><div>`
    content = re.sub(
        r'<div style="display: grid; grid-template-columns: 1fr \d{3}px;[^>]*">\s*<div>',
        r'<div class="course-hero-grid">\n                    <div class="course-hero-content">',
        content
    )
    
    # Course Tag
    content = re.sub(
        r'<span class="course-tag"\s*style="background: var\(--primary-light\);[^"]*">',
        r'<span class="course-tag">',
        content
    )
    
    # Hero h1
    content = re.sub(
        r'<h1\s*style="font-size: \d+\.?\d*rem; color: var\(--secondary\); font-weight: 800; [^"]*">',
        r'<h1>',
        content
    )
    
    # Hero p description
    content = re.sub(
        r'<p style="font-size: 1\.2rem; color: var\(--text-muted\); line-height: 1\.8; margin-bottom: 2rem;">',
        r'<p class="course-description">',
        content
    )
    
    # Course stats container
    content = re.sub(
        r'<div style="display: flex; gap: 2rem; flex-wrap: wrap; margin-bottom: 2rem;">',
        r'<div class="course-stats-list">',
        content
    )
    content = re.sub(
        r'<span\s*style="display: flex; align-items: center; gap: 0\.5rem; font-weight: 600; color: var\(--secondary\);">',
        r'<span class="course-stat-item">',
        content
    )
    
    # Price card div
    content = re.sub(
        r'<div\s*style="background: var\(--white\); border-radius: 32px; padding: 2\.5rem; box-shadow: var\(--shadow-lg\); border: 1px solid rgba\(0,0,0,0\.05\);">',
        r'<div class="course-price-card">',
        content
    )
    content = re.sub( # Alternative style matches
        r'<div\s*style="background: white; border-radius: 20px; padding: 3rem; box-shadow: 0 4px 20px rgba\(0,0,0,0\.05\);">',
        r'<div class="course-price-card">',
        content
    )
    
    # Image in price card
    content = re.sub(
        r'<img src="([^"]+)"\s*alt="([^"]+)"\s*style="width: 100%; border-radius: 20px; margin-bottom: 1\.5rem; aspect-ratio: 16/9; object-fit: cover;">',
        r'<img src="\1" alt="\2" class="course-price-card-image">',
        content
    )
    content = re.sub(
        r'<img src="([^"]+)"\s*alt="([^"]+)"\s*style="width: 100%; border-radius: 12px; margin-bottom: 1\.5rem;">',
        r'<img src="\1" alt="\2" class="course-price-card-image">',
        content
    )
    
    # Price display
    content = re.sub(
        r'<div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 2rem;">',
        r'<div class="course-price-display">',
        content
    )
    content = re.sub(
        r'<span style="font-size: 2\.5rem; font-weight: 800; color: var\(--secondary\);\$299</span>',
        r'<span class="course-price-main">$299</span>',
        content
    )
    content = re.sub(
        r'<span style="font-size: \d+\.\d+rem; font-weight: 800; color: var\(--secondary\);">\$(\d+)</span>',
        r'<span class="course-price-main">$\1</span>',
        content
    )
    content = re.sub(
        r'<span\s*style="text-decoration: line-through; color: var\(--text-muted\); font-size: 1\.2rem;">',
        r'<span class="course-price-old">',
        content
    )
    content = re.sub(
        r'<span\s*style="background: #fee2e2; color: #ef4444; padding: 0\.25rem 0\.75rem; border-radius: 50px; font-weight: 700; font-size: 0\.85rem;">',
        r'<span class="course-discount-badge">',
        content
    )
    
    # Enroll button & note
    content = re.sub(
        r'<a href="signup\.html\?course=[a-z-]+" class="btn btn-primary"\s*style="width: 100%; padding: 1\.2rem; display: block; text-align: center; font-size: 1\.1rem;">',
        r'<a href="signup.html?course=\g<0>" class="btn btn-primary course-enroll-btn">',
        content
    ) # regex issue here, let's simplify:
    content = re.sub(
        r'class="btn btn-primary"\s*style="width: 100%; padding: 1\.2rem; display: block; text-align: center; font-size: 1\.1rem;">',
        r'class="btn btn-primary course-enroll-btn">',
        content
    )
    content = re.sub(
        r'<p style="text-align: center; font-size: 0\.9rem; color: var\(--text-muted\); margin-top: 1rem;">',
        r'<p class="course-enroll-note">',
        content
    )

    # Main content wrapper replacements
    content = re.sub(
        r'<section style="padding: 100px 0;">',
        r'<section class="course-content-section">',
        content
    )
    content = re.sub(
        r'(<section class="course-content-section">)\s*<div class="container">',
        r'\1\n            <div class="course-content-wrapper">',
        content
    )
    content = re.sub(
        r'<div style="display: grid; grid-template-columns: 1fr \d{3}px; gap: 5rem;">\s*(<div class="course-details">|<div class="main-content">)',
        r'<div class="course-main-grid">\n                    <div class="course-main-content">',
        content
    )

    # Sidebar
    content = re.sub(
        r'<aside style="position: sticky; top: \d+px; align-self: start;">',
        r'<aside class="course-sidebar sidebar-sticky">',
        content
    )
    content = re.sub(
        r'<div\s*style="background: var\(--secondary\); padding: 2rem; border-radius: 24px; color: white; margin-bottom: 2rem;">',
        r'<div class="sidebar-card sidebar-features">',
        content
    )
    content = re.sub(
        r'<h4 style="margin-bottom: 1\.5rem; font-size: 1\.3rem;">',
        r'<h4>',
        content
    )
    content = re.sub(
        r'<ul style="list-style: none; display: grid; gap: 1rem;">',
        r'<ul>',
        content
    )
    content = re.sub(
        r'<li\s*style="display: flex; align-items: center; gap: 1rem; font-size: 0\.95rem; opacity: 0\.9;">',
        r'<li>',
        content
    )
    
    content = re.sub(
        r'<div\s*style="padding: 2rem; border-radius: 24px; background: var\(--surface\); border: 1px solid #eee;">',
        r'<div class="sidebar-card sidebar-requirements">',
        content
    )
    content = re.sub(
        r'<div\s*style="background: white; border-radius: 20px; padding: 2rem; box-shadow: 0 4px 20px rgba\(0,0,0,0\.05\); margin-bottom: 2rem;">',
        r'<div class="sidebar-card sidebar-features">',
        content
    )
    content = re.sub(
        r'<h4 style="color: var\(--secondary\); margin-bottom: 1rem;">',
        r'<h4>',
        content
    )
    content = re.sub(
        r'<p style="font-size: 0\.9rem; color: var\(--text-muted\); line-height: 1\.6;">',
        r'<p>',
        content
    )
    
    # Typography/section headers
    content = re.sub(
        r'<div style="margin-bottom: 4rem;" data-reveal>',
        r'<div class="course-section" data-reveal>',
        content
    )
    content = re.sub(
        r'<h2\s*style="font-size: 2\.2rem; color: var\(--secondary\); margin-bottom: 1\.5rem; font-weight: 800;">',
        r'<h2>',
        content
    )
    content = re.sub(
        r'<p style="color: var\(--text-muted\); font-size: 1\.1rem; line-height: 1\.9;">',
        r'<p>',
        content
    )
    content = re.sub(
        r'<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1\.5rem;">',
        r'<div class="learning-items-grid">',
        content
    )
    content = re.sub(
        r'<div style="display: flex; gap: 1rem; color: var\(--text-muted\);">',
        r'<div class="learning-item">',
        content
    )
    content = re.sub(
        r'<i class="([^"]+)"\s*style="color: var\(--primary\); margin-top: 0\.25rem;"></i>\s*([^<]+)',
        r'<i class="\1"></i>\n                                    <span class="learning-item-text">\2</span>',
        content
    )
    
    # Curriculum Grid
    content = re.sub(
        r'<div style="display: grid; gap: 1rem;">',
        r'<div class="curriculum-grid">',
        content
    )
    content = re.sub(
        r'<div\s*style="padding: 1\.5rem; background: var\(--surface\); border-radius: 16px; display: flex; justify-content: space-between; align-items: center;">',
        r'<div class="curriculum-item">',
        content
    )
    
    # We will remove the inner wrapper entirely: `<div style="display: flex; align-items: center; gap: 1rem;">` + `</div>` later
    content = re.sub(
        r'<div style="display: flex; align-items: center; gap: 1rem;">\s*<span\s*style="width: 32px; height: 32px; background: var\(--primary\); color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 0\.8rem;">(\d+)</span>\s*<h4 style="color: var\(--secondary\);">([^<]+)</h4>\s*</div>',
        r'<span class="curriculum-number">\1</span>\n                                    <h4 class="curriculum-name">\2</h4>',
        content
    )
    
    content = re.sub(
        r'<span style="color: var\(--text-muted\); font-size: 0\.9rem;">([^<]+)</span>',
        r'<span class="curriculum-sessions">\1</span>',
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(content)
