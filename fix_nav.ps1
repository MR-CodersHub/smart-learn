$files = Get-ChildItem -Path . -Filter *.html
foreach ($file in $files) {
    try {
        $content = Get-Content $file.FullName -Raw
        
        # Regex to find the navbar block
        # Matches <ul class="nav-links"> ... </ul> 
        # Using [s] single-line mode (dot matches newline) equivalent in PS regex?
        # In PS, "." does NOT match newline by default. We need (?s)
        $pattern = '(?s)<ul\s+class=["'']nav-links["''].*?>.*?</ul>'
        
        if ($content -match $pattern) {
            
            # Determine active link based on filename
            $activeLink = ""
            if ($file.Name -eq "index.html") { $activeLink = "Home" }
            elseif ($file.Name -eq "home-digital.html") { $activeLink = "Digital Platform" }
            elseif ($file.Name -eq "about.html") { $activeLink = "About Us" }
            elseif ($file.Name -eq "programs.html") { $activeLink = "Programs" }
            elseif ($file.Name -eq "courses.html") { $activeLink = "Courses" }
            elseif ($file.Name -eq "contact.html") { $activeLink = "Contact" }
            elseif ($file.Name -like "course-*") { $activeLink = "Courses" }
            elseif ($file.Name -in @('digital-business.html', 'design-ux.html', 'ai-data.html', 'elite-mentorship.html', 'expert-instructors.html', 'flexible-learning.html', 'certifications.html')) { $activeLink = "Programs" }
            
            # Construct the new navbar HTML
            # We use `r`n for newlines to be safe on Windows
            $newNav = "                <ul class=""nav-links"">`r`n"
            
            # Helper to create list item
            function Get-Li($href, $text, $target) {
                $cls = ""
                if ($text -eq $target) { $cls = ' class="active"' }
                return "                    <li><a href=""$href""$cls>$text</a></li>`r`n"
            }
            
            $newNav += Get-Li "index.html" "Home" $activeLink
            $newNav += Get-Li "home-digital.html" "Digital Platform" $activeLink
            $newNav += Get-Li "about.html" "About Us" $activeLink
            $newNav += Get-Li "programs.html" "Programs" $activeLink
            $newNav += Get-Li "courses.html" "Courses" $activeLink
            $newNav += Get-Li "contact.html" "Contact" $activeLink
            $newNav += "                </ul>"
            
            # Replace
            $newContent = $content -replace $pattern, $newNav
            
            # Write back
            if ($newContent -ne $content) {
                Set-Content -Path $file.FullName -Value $newContent -Encoding UTF8
                Write-Host "Updated $($file.Name)"
            } else {
                Write-Host "No changes needed for $($file.Name)"
            }
        } else {
            Write-Host "Navbar not found in $($file.Name)"
        }
    } catch {
        Write-Host "Error processing $($file.Name): $_"
    }
}
