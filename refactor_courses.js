const fs = require('fs');
const path = require('path');

const folder = __dirname;
const files = fs.readdirSync(folder).filter(f => f.startsWith('course-') && f.endsWith('.html') && !['course-fullstack.html', 'course-details.html'].includes(f));

for (const file of files) {
    const filepath = path.join(folder, file);
    let content = fs.readFileSync(filepath, 'utf8');

    // Hero section
    content = content.replace(/<section style="padding: 160px 0 80px; background: var\(--surface\);">/g, '<section class="course-hero-section course-hero">');
    content = content.replace(/<section style="padding: 100px 0; background: var\(--surface\);">/g, '<section class="course-hero-section course-hero">');

    // Container to course-hero-container
    content = content.replace(/(<section class="course-hero-section course-hero">\s*)<div class="container">/, '$1<div class="course-hero-container">');

    // Back link
    content = content.replace(/<a href="courses\.html"\s*style="display: inline-flex;[^"]*">/, '<a href="courses.html" class="course-back-link">');

    // Hero Grid
    content = content.replace(/<div style="display: grid; grid-template-columns: 1fr \d{3}px;[^>]*">\s*<div>/, '<div class="course-hero-grid">\n                    <div class="course-hero-content">');

    // Course Tag
    content = content.replace(/<span class="course-tag"\s*style="background: var\(--primary-light\);[^"]*">/, '<span class="course-tag">');

    // Hero h1
    content = content.replace(/<h1\s*style="font-size: [^"]*">/, '<h1>');

    // Hero description
    content = content.replace(/<p style="font-size: 1\.2rem; color: var\(--text-muted\); line-height: 1\.8; margin-bottom: 2rem;">/, '<p class="course-description">');

    // Stats
    content = content.replace(/<div style="display: flex; gap: 2rem; flex-wrap: wrap; margin-bottom: 2rem;">/, '<div class="course-stats-list">');
    content = content.replace(/<span\s*style="display: flex; align-items: center; gap: 0\.5rem; font-weight: 600; color: var\(--secondary\);">/g, '<span class="course-stat-item">');

    // Price Card Outer Div
    content = content.replace(/<div\s*style="background: var\(--white\); border-radius: 32px; padding: 2\.5rem;[^\"]*">/, '<div class="course-price-card">');
    content = content.replace(/<div\s*style="background: white; border-radius: 20px; padding: 3rem;[^\"]*">/, '<div class="course-price-card">');
    content = content.replace(/<div\s*style="background: white; border-radius: 20px; padding: 2\.5rem;[^\"]*">/, '<div class="course-price-card">');
    content = content.replace(/<div\s*style="background: var\(--white\); padding: 3rem; border-radius: 30px;[^\"]*">/, '<div class="course-price-card">');

    // Image
    content = content.replace(/<img src="([^"]+)"\s*alt="([^"]+)"\s*style="width: 100%; border-radius: [^"]+">/, '<img src="$1" alt="$2" class="course-price-card-image">');

    // Price Display
    content = content.replace(/<div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 2rem;">/, '<div class="course-price-display">');
    content = content.replace(/<span style="font-size: [^"]+">\$(\d+)<\/span>/, '<span class="course-price-main">$$$1</span>');
    content = content.replace(/<span\s*style="text-decoration: line-through;[^"]*">/, '<span class="course-price-old">');
    content = content.replace(/<span\s*style="background: #fee2e2;[^"]*">/, '<span class="course-discount-badge">');

    // Enroll Button
    content = content.replace(/class="btn btn-primary"\s*style="width: 100%;[^"]*">/, 'class="btn btn-primary course-enroll-btn">');
    content = content.replace(/<p style="text-align: center; font-size: 0\.9rem; color: var\(--text-muted\); margin-top: 1rem;">/, '<p class="course-enroll-note">');

    // Main Content
    content = content.replace(/<section style="padding: 100px 0;">/, '<section class="course-content-section">');
    content = content.replace(/(<section class="course-content-section">\s*)<div class="container">/, '$1<div class="course-content-wrapper">');
    content = content.replace(/<div style="display: grid; grid-template-columns: 1fr \d{3}px; gap: 5rem;">\s*(<div class="course-details">|<div class="main-content">)/, '<div class="course-main-grid">\n                    <div class="course-main-content">');

    // Sidebar
    content = content.replace(/<aside style="position: sticky; top: \d+px; align-self: start;">/, '<aside class="course-sidebar sidebar-sticky">');
    content = content.replace(/<div\s*style="background: var\(--secondary\);[^"]*">/, '<div class="sidebar-card sidebar-features">');
    content = content.replace(/<h4 style="margin-bottom: 1\.5rem; font-size: 1\.3rem;">/, '<h4>');
    content = content.replace(/<ul style="list-style: none; display: grid; gap: 1rem;">/, '<ul>');
    content = content.replace(/<li\s*style="display: flex; align-items: center; gap: 1rem; font-size: 0\.95rem; opacity: 0\.9;">/g, '<li>');

    content = content.replace(/<div\s*style="padding: 2rem; border-radius: 24px; background: var\(--surface\);[^"]*">/, '<div class="sidebar-card sidebar-requirements">');

    // Fix alternative sidebar card styling (like cybersecurity)
    content = content.replace(/<div\s*style="background: white; border-radius: 20px; padding: 2rem; box-shadow:[^"]+margin-bottom: 2rem;">/, '<div class="sidebar-card sidebar-features">');

    content = content.replace(/<h4 style="color: var\(--secondary\); margin-bottom: 1rem;">/, '<h4>');
    content = content.replace(/<p style="font-size: 0\.9rem; color: var\(--text-muted\); line-height: 1\.6;">/, '<p>');

    // Section Content
    content = content.replace(/<div style="margin-bottom: 4rem;" data-reveal>/g, '<div class="course-section" data-reveal>');
    content = content.replace(/<h2\s*style="font-size: 2\.2rem; color: var\(--secondary\)[^"]*">/g, '<h2>');
    content = content.replace(/<p style="color: var\(--text-muted\); font-size: 1\.1rem; line-height: 1\.9;">/g, '<p>');

    // Learning list grid
    content = content.replace(/<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1\.5rem;">/g, '<div class="learning-items-grid">');
    content = content.replace(/<div style="display: flex; gap: 1rem; color: var\(--text-muted\);">/g, '<div class="learning-item">');
    content = content.replace(/<i class="([^"]+)"\s*style="color: var\(--primary\); margin-top: 0\.25rem;"><\/i>\s*([^<]+)/g, '<i class="$1"></i>\n                                    <span class="learning-item-text">$2</span>');

    // Curriculum
    content = content.replace(/<div style="display: grid; gap: 1rem;">/g, '<div class="curriculum-grid">');
    content = content.replace(/<div\s*style="padding: 1\.5rem; background: var\(--surface\); border-radius: 16px; display: flex; justify-content: space-between; align-items: center;">/g, '<div class="curriculum-item">');
    content = content.replace(/<div style="display: flex; align-items: center; gap: 1rem;">\s*<span\s*style="width: 32px; height: 32px; background: var\(--primary\); color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 0\.8rem;">(\d+)<\/span>\s*<h4 style="color: var\(--secondary\);">([^<]+)<\/h4>\s*<\/div>/g, '<span class="curriculum-number">$1</span>\n                                    <h4 class="curriculum-name">$2</h4>');
    content = content.replace(/<span style="color: var\(--text-muted\); font-size: 0\.9rem;">([^<]+)<\/span>/g, '<span class="curriculum-sessions">$1</span>');

    fs.writeFileSync(filepath, content, 'utf8');
}
console.log('Complete');
