const fs = require('fs');
const path = require('path');

const folder = __dirname;
let files = fs.readdirSync(folder).filter(f => f.endsWith('.html'));

for (const file of files) {
    if (file === 'course-fullstack.html' || file === 'course-details.html') continue;

    const filepath = path.join(folder, file);
    let content = fs.readFileSync(filepath, 'utf8');

    // Fix remaining grid-template-columns: 1fr 400px in programs
    if (content.includes('grid-template-columns: 1fr 400px')) {
        content = content.replace(/<div style="display: grid; grid-template-columns: 1fr 400px;[^>]*">\s*<div class="detail-content">/, '<div class="course-main-grid">\n                    <div class="course-main-content">');

        // Also update the sidebar aside for these program pages
        content = content.replace(/<aside style="position: sticky; top: [\d]+px; align-self: start;">/, '<aside class="course-sidebar sidebar-sticky">');

        // And the hero section container might be missing styling or padding, but the main issue is the grid sideways scroll.
        fs.writeFileSync(filepath, content, 'utf8');
    }
}
console.log('Programs Refactored');
